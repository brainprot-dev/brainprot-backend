import time
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *
from rdkit import Chem


from chembl_webresource_client.new_client import new_client
# from chembl_webresource_client.settings import Settings
# Settings.Instance().NEW_CLIENT_TIMEOUT = 10

import re
import requests
import pandas as pd
import math
import numpy as np
import json
import xmltodict
import ast

# Added a timeout to API call
# Reference :- https://towardsdatascience.com/adding-timeouts-to-functions-using-wrapt-timeout-decorator-21790890a49b

disease_ID_list = [
    "D000544",
    "D000690",
    "D057174",
    "D005909",
    "D005910",
    "D006816",
    "D008527",
    "D008579",
    "D009103",
    "D010300",
    "D049912",
]

disease_mapping = {
    "D000544": "Alzheimer's Disease",
    "D000690": "Amyotrophic Lateral Sclerosis",
    "D057174": "Frontotemporal Lobar Degeneration",
    "D005909": "Glioblastoma",
    "D005910": "Glioma",
    "D006816": "Huntington's Disease",
    "D008527": "Medulloblastoma",
    "D008579": "Meningioma",
    "D009103": "Multiple Sclerosis",
    "D010300": "Parkinson's Disease",
    "D049912": "Pituitary Adenoma",
}

def TTD_union(x,y):
  try: 
    if(np.isnan(x)):
      return y
  except:
    return x

def bindingdb_clean(b):
  try:
    return float(b)
  except:
    return float(b[1:])

def same_smiles(smiles_1, smiles_2):
    try:
        a = Chem.CanonSmiles(smiles_1)
        b = Chem.CanonSmiles(smiles_2)
        return a==b
    except:
        return False

def clue_mapping(clue_df, database_df):
    database_df["Clue_Clinical_Phase"] = np.nan
    database_df["CLUE_MOA"] = np.nan
    if clue_df.shape[0]!=0:
        for database_index in range(database_df.shape[0]):
            Clinical_Phase = []
            MOA = []
            for clue_index in range(clue_df.shape[0]):
                if same_smiles(clue_df.iloc[clue_index]["Smiles_ID"], database_df.iloc[database_index]["Smiles_ID"]):
                    Clinical_Phase.append(clue_df.iloc[clue_index]["Clinical_Phase"])
                    MOA.append(clue_df.iloc[clue_index]["MOA"])
            database_df.at[database_index, "Clue_Clinical_Phase"] = str(Clinical_Phase)
            database_df.at[database_index, "CLUE_MOA"] = str(MOA)
        database_df.dropna(subset=["Clue_Clinical_Phase", "Smiles_ID"], inplace=True)
        return database_df
    else:
        database_df.dropna(subset=["CLUE_MOA", "Smiles_ID"], inplace=True)
        return database_df

# Function to map Smiles ID to ChEMBL IDs
def smiles_to_chembl(smiles_id):
    try:
        response = requests.get("https://www.ebi.ac.uk/chembl/api/data/substructure/" + smiles_id) # API Request
        data_dict = xmltodict.parse(response.text)
        chembl_id = data_dict['response']['molecules']['molecule'][0]['molecule_chembl_id']
        return chembl_id
    except:
        return None

# Function to map ChEMBL ID to Smiles IDs
def chembl_to_smiles(chembl_id):
    try:
        response = requests.get("https://www.ebi.ac.uk/chembl/api/data/molecule/" + chembl_id) # API Request
        data_dict = xmltodict.parse(response.text) # Convert XML response to JSON
        smiles_id = data_dict['molecule']['molecule_structures']['canonical_smiles'] # Extract smiles_id
        return smiles_id
    except:
        return None
    
# Function to get Overall Status from NCT ID
def get_overall_status(nct_id):
    # Clinical Trials API supports v2 endpoints currently
    status_api = f"https://clinicaltrials.gov/api/v2/studies/{nct_id}?fields=OverallStatus&format=json"
    status_response = requests.get(status_api)
    status_json = json.loads(status_response.text)
    overall_status = status_json['protocolSection']['statusModule']['overallStatus']
    return overall_status

# Function to get Common Drug Names for the given ChEMBL ID
def get_drug_name(chemblID):
    drug_api = f"https://www.ebi.ac.uk/chembl/api/data/molecule/{chemblID}.json"
    drug_response = requests.get(drug_api)
    drug_data = drug_response.text
    drug_json = json.loads(drug_data)
    drug_name = drug_json['pref_name']
    return drug_name

def get_drug_name_smiles(smilesID):
    try:
        Drug_Object = Drug_Names_Smiles.objects.filter(Smiles_ID=smilesID)
    except:
       return None
    
    Drug_list = []
    for i in Drug_Object:
        Drug_list.append(Drug_Serializer(i, 
                                        fields=('Smiles_ID'), 
                                        exclude=True).data)
    if len(Drug_list)==0:
        return None
    else:
        return Drug_list
    
#     drug_api = f"https://www.ebi.ac.uk/chembl/api/data/molecule/{smilesID}"
#     drug_response = requests.get(drug_api)
#     try:
#         drug_data = xmltodict.parse(drug_response.text)
#         drug_df = pd.DataFrame(drug_data['molecule_synonyms'])
#         FDA_ATC_Drugs = drug_df[drug_df['syn_type'] == 'FDA' or drug_df['syn_type'] == 'ATC']
#         drug_name = FDA_ATC_Drugs['molecule_synonym'].tolist()[0]
#         return drug_name
#     except:
#         return "NA"
    
# Function to get Toxicity Classes from given Chembl ID
def OpenTargets_chembl_api(ChemblId):
    query_string = """
        query drugannotation($chemblId: String!){
            drug(chemblId: $chemblId) {
            id
            
            drugWarnings {
            
            
            toxicityClass
            
            }
        }
        }
    """

    # Setting variables object of arguments to be passed to endpoint
    variables = {"chemblId": ChemblId}

    # Setting base URL of GraphQL API endpoint
    base_url = "https://api.platform.opentargets.org/api/v4/graphql"

    try:
        # Performing POST request and check status code of response
        r = requests.post(base_url, json={"query": query_string, "variables": variables})

        # Transforming API response into JSON 
        api_response_as_json = json.loads(r.text)

        # Printing API response to terminal
        if api_response_as_json['data']['drug']:
            x=api_response_as_json['data']['drug']['drugWarnings']
            y=api_response_as_json['data']['drug']['id']

        ToxicityClasses=[]
        for tox in x:
            if(tox['toxicityClass'] is not None):
                ToxicityClasses.append(tox['toxicityClass'])
        data = dict({"id": y, "toxscore": ToxicityClasses})
        return data
    except:
        return None

# Function to get Toxicity Classes from given Smiles ID 
def OpenTargets_smiles_api(SmilesID):
    response = smiles_to_chembl(SmilesID)
    chembl_id = ""
    if response is None:
        return None
    else:
        chembl_id = response
    
    query_string = """
        query drugannotation($chemblId: String!){
            drug(chemblId: $chemblId) {
            id
            
            drugWarnings {
            
            
            toxicityClass
            
            }
        }
        }
    """

    # Setting variables object of arguments to be passed to endpoint
    variables = {"chemblId": chembl_id}

    # Setting base URL of GraphQL API endpoint
    base_url = "https://api.platform.opentargets.org/api/v4/graphql"

    try:
        # Performing POST request and check status code of response
        r = requests.post(base_url, json={"query": query_string, "variables": variables})

        # Transforming API response into JSON 
        api_response_as_json = json.loads(r.text)

        # Printing API response to terminal
        if api_response_as_json['data']['drug']:
            x=api_response_as_json['data']['drug']['drugWarnings']
            y=api_response_as_json['data']['drug']['id']

        ToxicityClasses=[]
        for tox in x:
            if(tox['toxicityClass'] is not None):
                ToxicityClasses.append(tox['toxicityClass'])
        data = dict({"Chembl id": y, "toxscore": ToxicityClasses})
        return data
    except:
        return None

# Function to make the API Call to ChEMBL database
def chembl_api(uniprotId):
    try: 
        # Step 1: Targets API
        targets_api = new_client.target
        targets = targets_api.get(target_components__accession=uniprotId).only("target_chembl_id", "organism", "pref_name", "target_type") 
        targets = pd.DataFrame.from_records(targets)
        targets = targets.iloc[0]
        chembl_id = targets.target_chembl_id
        print("Completed Step 1")

        # Step 2 : Bioactivities API
        bioactivities_api = new_client.activity
        bioactivities = bioactivities_api.filter(target_chembl_id=chembl_id,
                                                type="IC50", relation="=",
                                                assay_type="B").only(
                                                                    "activity_id",
                                                                    "assay_chembl_id",
                                                                    "assay_description",
                                                                    "assay_type",
                                                                    "molecule_chembl_id",
                                                                    "type",
                                                                    "standard_units",
                                                                    "relation",
                                                                    "standard_value",
                                                                    "target_chembl_id",
                                                                    "target_organism",
                                                                    ).order_by("standard_value")
        if len(bioactivities)>=100:
            bioactivities = bioactivities[:100]
        bioactivities_df = pd.DataFrame.from_records(bioactivities)
        bioactivities_df.drop(["units", "value"], axis=1, inplace=True)
        bioactivities_df = bioactivities_df.astype({"standard_value": "float64"})
        bioactivities_df.dropna(axis=0, how="any", inplace=True)
        bioactivities_df = bioactivities_df[bioactivities_df["standard_units"] == "nM"]
        bioactivities_df.drop_duplicates("molecule_chembl_id", keep="first", inplace=True)
        bioactivities_df.reset_index(drop=True, inplace=True)
        bioactivities_df.rename(
            columns={"standard_value": "IC50", "standard_units": "units"}, inplace=True
        )
        print("Completed Step 2")

        # Step 3 : Compounds API
        compounds_api = new_client.molecule
        compounds_provider = compounds_api.filter(
                                                molecule_chembl_id__in=list(bioactivities_df["molecule_chembl_id"]), limits=100
                                                ).only(
                                                    "molecule_chembl_id", 
                                                    "molecule_structures"
                                                )
        if len(compounds_provider)>=100:
            compounds_provider = compounds_provider[:100]
        compounds = list(compounds_provider)
        compounds_df = pd.DataFrame.from_records(compounds)
        compounds_df.dropna(axis=0, how="any", inplace=True)
        compounds_df.drop_duplicates("molecule_chembl_id", keep="first", inplace=True)

        canonical_smiles = []

        for i, compounds in compounds_df.iterrows():
            try:
                canonical_smiles.append(compounds["molecule_structures"]["canonical_smiles"])
            except KeyError:
                canonical_smiles.append(None)

        compounds_df["smiles"] = canonical_smiles
        compounds_df.drop("molecule_structures", axis=1, inplace=True)
        compounds_df.dropna(axis=0, how="any", inplace=True)

        # Step 4 : Merge
        output_df = pd.merge(
            bioactivities_df[["molecule_chembl_id", "IC50", "units"]],
            compounds_df,
            on="molecule_chembl_id",
        )
        
        output_df.reset_index(drop=True, inplace=True)
        output_df = output_df[output_df["IC50"]!=0]
        output_df['IC50log10'] = np.log10(output_df['IC50'])
        output_df.dropna(inplace=True)
        output_df["pIC50"] = 9-output_df['IC50log10']
        output_df.sort_values(by="pIC50", ascending=False, inplace=True)
        output_df.drop(['IC50log10', 'IC50', 'units'], axis=1, inplace=True)
        output_df['drug'] = output_df.apply(lambda row: get_drug_name_smiles(row.smiles), axis = 1)
        # output_df['Toxicity'] = output_df.apply(lambda row: OpenTargets_chembl_api(row.molecule_chembl_id), axis = 1) # Add Toxicity Class from Open Targets
        output_dict = output_df.to_dict('records')
        return output_dict
    except:
        return None

# Function to make API Call to BindingDB Database
def BindingDB_api(uniprotId):
    response = requests.get(f"https://bindingdb.org/axis2/services/BDBService/getLigandsByUniprot?uniprot={uniprotId}")
    data = []
    if response.status_code==200:
        data_dict = xmltodict.parse(response.text)
        if data_dict['bdb:getLigandsByUniprotResponse']['bdb:hit']=='1':
            if(data_dict['bdb:getLigandsByUniprotResponse']['bdb:affinities']['bdb:affinity_type']=="IC50"):
                output_dict = {}
                output_dict["MonomerID"] = data_dict['bdb:getLigandsByUniprotResponse']['bdb:affinities']['bdb:monomerid']
                output_dict["Smiles_ID"] =  data_dict['bdb:getLigandsByUniprotResponse']['bdb:affinities']['bdb:smiles']
                if bindingdb_clean(data_dict['bdb:getLigandsByUniprotResponse']['bdb:affinities']['bdb:affinity']) != 0: 
                    output_dict["pIC50"] = 9-np.log10(bindingdb_clean(data_dict['bdb:getLigandsByUniprotResponse']['bdb:affinities']['bdb:affinity']))
                else:
                    output_dict["pIC50"] = 0
                output_dict["Drug"] = get_drug_name_smiles(data_dict['bdb:getLigandsByUniprotResponse']['bdb:affinities']['bdb:smiles'])
                # output_dict["Toxicity"] = OpenTargets_smiles_api(data_dict['bdb:getLigandsByUniprotResponse']['bdb:affinities']['bdb:smiles']) # Add Toxicity Class from Open Targets
                data.append(output_dict)
        else:
            for i in data_dict['bdb:getLigandsByUniprotResponse']['bdb:affinities']:
                if(i['bdb:affinity_type']=="IC50"):
                    output_dict = {}
                    output_dict["MonomerID"] = i['bdb:monomerid']
                    output_dict["Smiles_ID"] = i['bdb:smiles']
                    if bindingdb_clean(i['bdb:affinity'])!=0:
                        output_dict["pIC50"] = 9-np.log10(bindingdb_clean(i['bdb:affinity']))
                    else:
                        output_dict["pIC50"] = 0
                    output_dict["Drug"] = get_drug_name_smiles(i['bdb:smiles'])
                    # output_dict["Toxicity"] = OpenTargets_smiles_api(i['bdb:smiles']) # Add Toxicity Class from Open Targets
                    data.append(output_dict)
    if len(data)==0:
        return None
    else:
        return data
    
# Function to make API Call to TTD Database
def TTD_api(uniprotId):
    # Get MOA and Highest Status
    try:
        TTD_MOA_Status_object = TTD_MOA_Status.objects.filter(UniprotID=uniprotId)
    except:
        return None
    
    # Get IC50 values
    try:
        TTD_IC50_object = TTD_IC50.objects.filter(UniprotID=uniprotId)
    except:
        return None

    MOA_Status_list = []
    for i in TTD_MOA_Status_object:
        MOA_Status_list.append(TTD_MOA_Status_Serializer(i).data)
    MOA_Status_df = None
    if len(MOA_Status_list)==0:
        MOA_Status_df = pd.DataFrame(columns = ['id', 'TargetID', 'DrugID', 'Highest_Status', 'MOA', 'Smiles_ID', 'UniprotID'])
    else:
        MOA_Status_df = pd.DataFrame(MOA_Status_list)
    
    IC50_list = []
    for i in TTD_IC50_object:
        IC50_list.append(TTD_IC50_Serializer(i).data)
    IC50_df = None
    if len(IC50_list)==0:
        IC50_df = pd.DataFrame(columns = ['id', 'TargetID', 'DrugID', 'UniprotID', 'Smiles_ID', 'Activity_IC50'])
    else:
        IC50_df = pd.DataFrame(IC50_list)

    try:
        df = IC50_df.merge(MOA_Status_df, how='outer', on=['Smiles_ID', 'UniprotID'])
        df['TargetID'] = df.apply(lambda x: TTD_union(x['TargetID_y'],x['TargetID_x']), axis=1)
        df['DrugID'] = df.apply(lambda x: TTD_union(x['DrugID_y'],x['DrugID_x']), axis=1)
        df.drop(['TargetID_x','TargetID_y','DrugID_x','DrugID_y','UniprotID','id_x','id_y'], axis=1, inplace=True)
        df['drug'] = df.apply(lambda row: get_drug_name_smiles(row.Smiles_ID), axis = 1)
        df['Highest_Status'] = df['Highest_Status'].fillna("")
        df['MOA'] = df['MOA'].fillna("")
        df['Activity_IC50'] = df['Activity_IC50'].fillna("")
        # df['Toxicity'] = df.apply(lambda row: OpenTargets_smiles_api(row.Smiles_ID), axis = 1) # Add Toxicity Class from Open Targets
        output_dict = df.to_dict('records')
        return output_dict
    except:
        return None
    
# Function to make API Call to CLUE Database
def CLUE_api(uniprotId):
    try:
        CLUE_object = CLUE.objects.filter(UniprotID=uniprotId)
    except:
       return None
    
    CLUE_list = []
    for i in CLUE_object:
        CLUE_list.append(CLUE_Serializer(i, 
                                        fields=('UniprotID'), 
                                        exclude=True).data)
    if len(CLUE_list)==0:
        return None
    else:
        # Add Toxicity classes from Open Targets
        # for i in CLUE_list:
        #     i["Toxicity"] = OpenTargets_chembl_api(i["Chembl_ID"])
        return CLUE_list

# Function to make API Call to Stitch Database
def Stitch_API(uniprotId):
    Stitch_object = 0
    Stitch_list = []
    
    try:
        Stitch_object = Stitch.objects.filter(UniprotID=uniprotId)
        for i in Stitch_object:
            Stitch_list.append(Stitch_Serializer(i, 
                                            fields=('UniprotID'), 
                                            exclude=True).data)
    except:
        return None
    
    if len(Stitch_list)==0:
        return None
    else:
        for i in Stitch_list:
            i["Drug"] = get_drug_name_smiles(i["Smiles_ID"])
        return Stitch_list

# Serialized Data for Top 25 Uniprot IDs for each disease
def get_all_uniprots(diseaseID):
    if diseaseID == "D000544":
        try:
            dataset = D000544.objects.all()
        except:
            dataset = None
        serialized_dataset = D000544Serializer(dataset, many=True)
        return serialized_dataset.data

    elif diseaseID == "D000690":
        try:
            dataset = D000690.objects.all()
        except:
            dataset = None
        serialized_dataset = D000690Serializer(dataset, many=True)
        return serialized_dataset.data

    elif diseaseID == "D057174":
        try:
            dataset = D057174.objects.all()
        except:
            dataset = None
        serialized_dataset = D057174Serializer(dataset, many=True)
        return serialized_dataset.data

    elif diseaseID == "D005909":
        try:
            dataset = D005909.objects.all()
        except:
            dataset = None
        serialized_dataset = D005909Serializer(dataset, many=True)
        return serialized_dataset.data

    elif diseaseID == "D005910":
        try:
            dataset = D005910.objects.all()
        except:
            dataset = None
        serialized_dataset = D005910Serializer(dataset, many=True)
        return serialized_dataset.data

    elif diseaseID == "D006816":
        try:
            dataset = D006816.objects.all()
        except:
            dataset = None
        serialized_dataset = D006816Serializer(dataset, many=True)
        return serialized_dataset.data

    elif diseaseID == "D008527":
        try:
            dataset = D008527.objects.all()
        except:
            dataset = None
        serialized_dataset = D008527Serializer(dataset, many=True)
        return serialized_dataset.data

    elif diseaseID == "D008579":
        try:
            dataset = D008579.objects.all()
        except:
            dataset = None
        serialized_dataset = D008579Serializer(dataset, many=True)
        return serialized_dataset.data

    elif diseaseID == "D009103":
        try:
            dataset = D009103.objects.all()
        except:
            dataset = None
        serialized_dataset = D009103Serializer(dataset, many=True)
        return serialized_dataset.data

    elif diseaseID == "D010300":
        try:
            dataset = D010300.objects.all()
        except:
            dataset = None
        serialized_dataset = D010300Serializer(dataset, many=True)
        return serialized_dataset.data

    elif diseaseID == "D049912":
        try:
            dataset = D049912.objects.all()
        except:
            dataset = None
        serialized_dataset = D049912Serializer(dataset, many=True)
        return serialized_dataset.data
     
# Django REST API Function for fetching data from ChEMBL Database
@api_view(['GET'])
def chembl_Django_API(request, uniprotId):
    try:
        response = Chembl.objects.filter(UniprotID=uniprotId)
    except:
        response = chembl_api(uniprotId)
    Chembl_list = []
    for i in response:
        Chembl_list.append(Chembl_Serializer(i, 
                                        fields=('UniprotID'), 
                                        exclude=True).data)
    if response is None or len(Chembl_list)==0:
        return JsonResponse({'message': f'The Uniprot ID: "{uniprotId}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'})
    else:
        return JsonResponse({'UniprotID': uniprotId, "Source" : "CHEMBL", "data" : Chembl_list})
    
# Django REST API Function for fetching data from BindingDB Database
@api_view(['GET'])
def BindingDB_Django_API(request, uniprotId):
    response = BindingDB_api(uniprotId)
    if response is None:
        return JsonResponse({'message': f'The Uniprot ID: "{uniprotId}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'})
    else:
        return JsonResponse({'UniprotID': uniprotId, "Source" : "BindingDB", "data" : response})
    
# Django REST API Function for fetching data from TTD Database
@api_view(['GET'])
def TTD_Django_API(request, uniprotId):
    response = TTD_api(uniprotId)
    if response is None:
        return JsonResponse({'message': f'The Uniprot ID: "{uniprotId}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'})
    else:
        return JsonResponse({'UniprotID': uniprotId, "Source" : "TTD", "data" : response})
    
# Django REST API Function for fetching data from CLUE Database
@api_view(['GET'])
def CLUE_Django_API(request, uniprotId):
    response = CLUE_api(uniprotId)
    if response is None:
        return JsonResponse({'message': f'The Uniprot ID: "{uniprotId}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'})
    else:
        return JsonResponse({'UniprotID': uniprotId, "Source" : "CLUE", "data" : response})
    
# Django REST API Function for fetching data from Stitch Database
@api_view(['GET'])
def Stitch_Django_API(request, uniprotId):
    response = Stitch_API(uniprotId)
    if response is None:
        return JsonResponse({'message': f'The Uniprot ID: "{uniprotId}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'})
    else:
        return JsonResponse({'UniprotID': uniprotId, "Source" : "Stitch", "data" : response})
    
# Django REST API Function for fetching toxicity class from Open Targets Database using ChEMBL IDs
@api_view(['GET'])
def OpenTargets_Chembl_Django_API(request, chembl_id):
    response = OpenTargets_chembl_api(chembl_id)
    if response is None:
        return JsonResponse({'message': f'The ChEMBL ID: "{chembl_id}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'})
    else:
        return JsonResponse({'ChEMBL': chembl_id, "data" : response})
    
# Django REST API Function for fetching toxicity class from Open Targets Database using Smiles IDs
@api_view(['GET'])
def OpenTargets_Smiles_Django_API(request, smiles_id):
    response = OpenTargets_smiles_api(smiles_id)
    if response is None:
        return JsonResponse({'message': f'The Smiles ID: "{smiles_id}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'})
    else:
        return JsonResponse({'Smiles': smiles_id, "data" : response})
    
@api_view(['GET'])
def All_Database_Django_API(request, uniprotId):
    # ChEMBL API
    is_dynamic = 0
    Chembl_response = None
    try:
        Chembl_response = Chembl.objects.filter(UniprotID=uniprotId)
    except:
        is_dynamic = 1
    if is_dynamic==1 or len(Chembl_response)==0:
        Chembl_list = chembl_api(uniprotId)
        if Chembl_list is None:
            Chembl_list = []
    else:
        Chembl_list = []
        for i in Chembl_response:
            Chembl_list.append(Chembl_Serializer(i, 
                                            fields=('UniprotID'), 
                                            exclude=True).data)
        if len(Chembl_list)==0:
            Chembl_list = []
    print("Chembl Completed")

    # BindingDB API
    BindingDB_response = BindingDB_api(uniprotId)
    if BindingDB_response is None:
        BindingDB_response = {}
    print("BindingDb Completed")

    # Stitch API
    Stitch_response = Stitch_API(uniprotId)
    if Stitch_response is None:
        Stitch_response = {}
    print("Stitch Completed")

    # TTD API
    TTD_response = TTD_api(uniprotId)
    if TTD_response is None:
        TTD_response = {}
    print("TTD Completed")

    # CLUE API
    Clue_response = CLUE_api(uniprotId)
    if Clue_response is None:
        Clue_response = {}
    print("CLUE Completed")

    return JsonResponse({'UniprotID': uniprotId, "Chembl" : Chembl_list, "BindingDB" : BindingDB_response, "Stitch" : Stitch_response, "TTD" : TTD_response, "Clue" : Clue_response})     
    # return JsonResponse({'UniprotID': uniprotId, "BindingDB" : BindingDB_response, "Stitch" : Stitch_response, "TTD" : TTD_response, "Clue" : Clue_response})

# Django REST API Function to fetch data for Disease Tab
# Data for Top 25 Uniprot IDs for each disease
@api_view(["GET"])
def single_disease_all_data(request, diseaseID):
    diseaseID = diseaseID.upper()
    if diseaseID in disease_ID_list:
        data = get_all_uniprots(diseaseID=diseaseID)
        disease = disease_mapping[diseaseID]
        return JsonResponse({"disease": disease, "uniprotList": data})
    else:
        return JsonResponse(
            {
                "message": f'The diseaseID: "{diseaseID}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'
            },
            status=status.HTTP_404_NOT_FOUND,
        )

# Formats disease names to replace whitespace with + and replaces other special characters with %
def format_disease_name(diseaseName, isReplaceSpecialChars):
    pattern = r"[^a-zA-Z\s]+" if isReplaceSpecialChars else r"\s+"
    replacement = "%" if isReplaceSpecialChars else "+"
    return re.sub(pattern, replacement, diseaseName)

# Fetch chembl data
@api_view(['GET'])
def chembl_disease(request, diseaseId):
    diseaseId = diseaseId.upper()
    # Check if disease exists in BDDF
    try:
        disease_object = BDDF_Disease.objects.get(MESHID=diseaseId)
    except:
        disease_object = None
        return JsonResponse({'message': f'The disease ID: "{diseaseId}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)

    drug_indication = new_client.drug_indication
    disease_ind = drug_indication.filter(efo_term__icontains=disease_object.diseaseName)
    formatted_disease_name = format_disease_name(disease_object.diseaseName, True)
    
    output = []
    for entry in disease_ind:
        ref_type = entry["indication_refs"][0]["ref_type"]
        if ref_type == 'ClinicalTrials':
            ref_id = entry["indication_refs"][0]["ref_id"]
            nct_id = ref_id.split(',')[0]
            clinical_trial_url = f"https://clinicaltrials.gov/ct2/show/{nct_id}?cond={formatted_disease_name}"
            chembl_id = entry["molecule_chembl_id"]
            output.append({'drugind_id' : entry["drugind_id"], 'ref_url' : entry["indication_refs"][0]["ref_url"], 'nct_id': nct_id, 'clinical_trial_url': clinical_trial_url, 'max_phase_for_ind' : entry["max_phase_for_ind"], 'molecule_chembl_id' : chembl_id})

    return JsonResponse({'Disease Name': disease_object.diseaseName, 'data': output}, safe=False)

# Helper function to extract fields from Clinical trials response study
def extract_study_info(study):
    protocol_section = study.get('protocolSection', {})
    
    nct_id = protocol_section.get('identificationModule', {}).get('nctId', "")
    overall_status = protocol_section.get('statusModule', {}).get('overallStatus', "")
    
    # Extract first condition if available, otherwise empty string
    conditions = protocol_section.get('conditionsModule', {}).get('conditions', [])
    condition = conditions[0] if conditions else ""
    
    # Extract first intervention name if available, otherwise empty string
    interventions = protocol_section.get('armsInterventionsModule', {}).get('interventions', [])
    intervention_name = interventions[0].get('name', "") if interventions else ""
    
    return {
        "NCTId": nct_id,
        "Condition": condition,
        "InterventionName": intervention_name,
        "OverallStatus": overall_status
    }

# Fetches clinical trial information for a particular disease
@api_view(['GET'])
def get_clinical_trial_info(request, diseaseId):
    diseaseId = diseaseId.upper()
    # Check if disease exists in BDDF
    try:
        disease_object = BDDF_Disease.objects.get(MESHID=diseaseId)
    except:
        disease_object = None
        return JsonResponse({'message': f'The disease ID: "{diseaseId}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)
    disease_name = format_disease_name(disease_object.diseaseName, False)
    url = f"https://clinicaltrials.gov/api/v2/studies?query.cond={disease_name}&fields=NCTId%7CCondition%7CInterventionName%7COverallStatus&pageSize=1000"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, timeout=5) 
        response.raise_for_status() 
        json_data = response.json()

    except requests.exceptions.Timeout:
        return JsonResponse({"error": "Request timed out. The server took too long to respond."}, status=504)
    
    except requests.exceptions.ConnectionError:
        return JsonResponse({"error": "Failed to connect to clinicaltrials.gov. Please check your internet connection."}, status=503)

    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({"error": f"HTTP error occurred: {http_err}"}, status=response.status_code)

    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Request failed: {e}"}, status=500)

    except ValueError:
        return JsonResponse({"error": "Got invalid JSON response"}, status=502)
    
    clinical_trial_info = [extract_study_info(study) for study in json_data.get('studies', [])]
    return JsonResponse({'Disease Name': disease_object.diseaseName, 'data': clinical_trial_info}, safe=False)
