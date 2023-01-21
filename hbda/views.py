from django.shortcuts import render
from django.http import HttpResponse
from sklearn.preprocessing import MinMaxScaler
from hbda.models import Disease
from hbda.serializers import DiseaseSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.conf import settings

import requests
import environ
import urllib.parse
import time
import requests
import json
import os, shutil
import pandas as pd



# Create your views here.
# Initialise environment and global variables 
env = environ.Env()
environ.Env.read_env()

HBDA_CACHE_DIR = os.path.join(settings.BASE_DIR, "hbda/cache")


def getDisgenetData(disease_object):
    #Build a dict with the following format, change the value of the two keys your DisGeNET account credentials, if you don't have an account you can create one here https://www.disgenet.org/signup/ 
    start = time.perf_counter()
    api_host = "https://www.disgenet.org/api"

    disgenet_api_key = env("DISGENET_API_KEY")

    harmonizome_query_term = disease_object.HarmonizomeQueryTerm

    harmonizome_url_string = 'https://maayanlab.cloud/Harmonizome/api/1.0/gene_set/' + urllib.parse.quote_plus(harmonizome_query_term) + '/DISEASES+Text-mining+Gene-Disease+Assocation+Evidence+Scores'
    disgenet_url_string = api_host + f'/gda/disease/{disease_object.DisGeNETDiseaseId}'
    if disgenet_api_key and disease_object:
        #Get Harmonizome Data
        harmonizome_response = requests.get(harmonizome_url_string)
        harmonizome_response_dict = json.loads(harmonizome_response.text)
        
        print("Got Harmonizome response in ",time.perf_counter()-start, "s")
        start = time.perf_counter()
        #Add the api key to the requests headers of the requests Session object in order to use the restricted endpoints.
        #Lets get all the diseases associated to a gene eg. APP (EntrezID 351) and restricted by a source.
        disgenet_response = requests.get(disgenet_url_string, headers={"Authorization": f"Bearer {disgenet_api_key}"})
        disgenet_response_dict = json.loads(disgenet_response.text)
        print("Got Disgenet response in ",time.perf_counter()-start, "s")

    disgenet_score_list = []
    harmonizome_score_list = []
    disgenet_gene_list = []
    harmonizome_gene_list = []

    for entry in disgenet_response_dict:
        disgenet_score_list.append([entry['gene_symbol'], entry['score']])
        disgenet_gene_list.append(entry['gene_symbol'])
    
    for entry in harmonizome_response_dict['associations']:
        harmonizome_score_list.append([entry['gene']['symbol'], entry['standardizedValue']])
        harmonizome_gene_list.append(entry['gene']['symbol'])

    common_gene_list = [gene for gene in disgenet_gene_list if gene in harmonizome_gene_list]

    disgenet_df = pd.DataFrame(disgenet_score_list, columns =['geneName', 'score'])
    harmonizome_df = pd.DataFrame(harmonizome_score_list, columns =['geneName', 'standardizedValue'])

    disgenet_scores_array = disgenet_df[['score']].to_numpy()
    harmonizome_scores_array = harmonizome_df[['standardizedValue']].to_numpy()

    disgenet_scaler = MinMaxScaler()
    disgenet_scaler.fit(disgenet_scores_array)
    normalized_disgenet_scores = disgenet_scaler.transform(disgenet_scores_array)

    normalized_disgenet_scores_df = pd.DataFrame(normalized_disgenet_scores, columns=["normalizedScore"])
    normalized_disgenet_df = pd.concat([disgenet_df, normalized_disgenet_scores_df], axis=1)

    harmonizome_scaler = MinMaxScaler()
    harmonizome_scaler.fit(harmonizome_scores_array)
    normalized_harmonizome_scores = harmonizome_scaler.transform(harmonizome_scores_array)

    normalized_harmonizome_scores_df = pd.DataFrame(normalized_harmonizome_scores, columns=["normalizedStandardizedValue"])
    normalized_harmonizome_df = pd.concat([harmonizome_df, normalized_harmonizome_scores_df], axis=1)

    common_gene_data = []
    for gene in common_gene_list:
        normalized_disgenet_score = normalized_disgenet_df[normalized_disgenet_df['geneName'] == gene]['normalizedScore'].values[0]
        normalized_harmonizome_score = normalized_harmonizome_df[normalized_harmonizome_df['geneName'] == gene]['normalizedStandardizedValue'].values[0]
        common_gene_data.append([gene, normalized_disgenet_score, normalized_harmonizome_score])

    normalized_common_df = pd.DataFrame(common_gene_data, columns=['geneName', 'normalizedGDAScore', 'normalizedHarmonizomeScore'])
    
    normalized_disgenet_df.to_csv(HBDA_CACHE_DIR + "/" + f'{disease_object.DisGeNETDiseaseId}_disgenet.csv', index=False)
    normalized_harmonizome_df.to_csv(HBDA_CACHE_DIR + "/" + f'{disease_object.DisGeNETDiseaseId}_harmonizome.csv', index=False)
    normalized_common_df.to_csv(HBDA_CACHE_DIR + "/" + f'{disease_object.DisGeNETDiseaseId}_common.csv', index=False)





@api_view(['GET'])
def get_disease_data(request, diseaseId):
    try:
        disease_object = Disease.objects.get(DisGeNETDiseaseId=diseaseId)
    except:
        disease_object = None
        return JsonResponse({'message': f'The disease ID: "{diseaseId}" does not exist in HBDA Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)
    if (not disease_object.includeInBDDF):
        return JsonResponse({'message': f'The disease ID: "{diseaseId}" does not exist in HBDA Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        pass
    try:
        harmonizome_disease_processed_dataset = pd.read_csv(HBDA_CACHE_DIR + "/" + f'{diseaseId}_harmonizome.csv')
        disgenet_disease_processed_dataset = pd.read_csv(HBDA_CACHE_DIR + "/" + f'{diseaseId}_disgenet.csv')
        common_disease_processed_dataset = pd.read_csv(HBDA_CACHE_DIR + "/" + f'{diseaseId}_common.csv')
    except:
        getDisgenetData(disease_object)
        harmonizome_disease_processed_dataset = pd.read_csv(HBDA_CACHE_DIR + "/" + f'{diseaseId}_harmonizome.csv')
        disgenet_disease_processed_dataset = pd.read_csv(HBDA_CACHE_DIR + "/" + f'{diseaseId}_disgenet.csv')
        common_disease_processed_dataset = pd.read_csv(HBDA_CACHE_DIR + "/" + f'{diseaseId}_common.csv')

    common_data = common_disease_processed_dataset.to_dict('records')
    disgenet_data = disgenet_disease_processed_dataset.to_dict('records')
    harmonizome_data = harmonizome_disease_processed_dataset.to_dict('records')

    return JsonResponse({'diseaseName': disease_object.diseaseName, 'diseaseId': disease_object.DisGeNETDiseaseId, 'data': {'disgenetData': disgenet_data, 'harmonizomeData': harmonizome_data, 'commonData': common_data}})

    
@api_view(['GET'])
def delete_hbda_cache(request):
    for filename in os.listdir(HBDA_CACHE_DIR):
        file_path = os.path.join(HBDA_CACHE_DIR, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    return JsonResponse({'message': f'Cache has been cleared'})

@api_view(['GET'])
def get_disease_table(request):
    all_disease_objects = Disease.objects.filter(includeInBDDF=True).order_by('diseaseName')

    serialized_disease_objects = DiseaseSerializer(all_disease_objects,
                                                    fields=(),
                                                    exclude=True,
                                                    many=True
                                                    )

    return JsonResponse({'diseaseTableData': serialized_disease_objects.data})
                                                
