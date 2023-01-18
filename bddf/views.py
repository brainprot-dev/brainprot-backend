from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from hbda.models import Disease
from rest_framework import status

from chembl_webresource_client.new_client import new_client

import requests
import pandas as pd
from tqdm.auto import tqdm
import math
import numpy as np
import json

# Added a timeout to API call
# Reference :- https://towardsdatascience.com/adding-timeouts-to-functions-using-wrapt-timeout-decorator-21790890a49b
from wrapt_timeout_decorator import *

@timeout(30)
def chembl_uniprot(uniprotId):
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
                                                                )
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
                                              molecule_chembl_id__in=list(bioactivities_df["molecule_chembl_id"])
                                            ).only(
                                                "molecule_chembl_id", 
                                                "molecule_structures"
                                            )
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
    output_df['IC50log10'] = np.log10(output_df['IC50'])
    output_df.dropna(inplace=True)
    output_df["pIC50"] = 9-output_df['IC50log10']
    output_df.sort_values(by="pIC50", ascending=False, inplace=True)
    output_df.drop(['IC50log10'], axis=1, inplace=True)
    output_dict = output_df.to_dict('records')
    return JsonResponse({'uniprotId': uniprotId, 'data': output_dict})

@api_view(['GET'])
def get_protein_data(request, uniprotId):
    try: 
        return chembl_uniprot(uniprotId)
    except:
        return JsonResponse({'message': f'The Uniprot ID: "{uniprotId}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def chembl_disease(request, diseaseId):
    try:
        disease_object = Disease.objects.get(DisGeNetDiseaseId=diseaseId)
    except:
        disease_object = None
        return JsonResponse({'message': f'The disease ID: "{diseaseId}" does not exist in BDDF Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)

    drug_indication = new_client.drug_indication
    molecules = new_client.molecule
    disease_ind = drug_indication.filter(efo_term__icontains=disease_object.diseaseName)
    disease_mols = molecules.filter(molecule_chembl_id__in=[x['molecule_chembl_id'] for x in disease_ind])
    output = []
    for drug_entry in range(len(disease_ind)):
        output.append({'drugind_id' : disease_ind[drug_entry]["drugind_id"], 'ref_url' : disease_ind[drug_entry]["indication_refs"][0]["ref_url"], 'max_phase_for_ind' : disease_ind[drug_entry]["max_phase_for_ind"], 'molecule_chembl_id' : disease_ind[drug_entry]["molecule_chembl_id"]})
    #output_df = pd.DataFrame.from_records(disease_mols)
    #output_dict = output_df.to_json()
    return JsonResponse({'Disease Name': diseaseId, 'data': output}, safe=False)