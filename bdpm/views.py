from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

# All Models
from .meningioma.models_meningiomas import *

# All serializers
from .meningioma.serializers_meningiomas import *

#For Faster Concatenating of Lists
from itertools import chain 

# Global Variables
disease_list = [
    'meningioma'
]



# Helper Functions

# # # # get_objects
# This will return all objects of a disease, across all its models
# We can then put any manager class methods(like .all, .get, .get) 
# (Refer to Django Documentation on QuerySets for more information)
# This assumes that the argument is a valid, verified disease name identifier,
# (which means it belongs to the list above)
# returns a tuple of all dataset objects, which has the number of datasets as the first value
# and a list of objects as second value

def get_objects(disease, proteinId):
    if disease == 'meningioma':
        try:
            dataset_1 = Meningioma_1_PXD007073.objects.get(proteinId=proteinId)
        except:
            dataset_1 = None
        try:
            dataset_2 = Meningioma_2_PXD014852.objects.get(proteinId=proteinId)
        except:
            dataset_2 = None

        serialized_dataset_1 = Meningioma_1_PXD007073_Serializer(dataset_1,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_2 = Meningioma_2_PXD014852_Serializer(dataset_2,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )

        return (2,[
                    {'studyId': 'PXD007073', 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014852', 'data': serialized_dataset_2.data},
                    ]
                )
    else:
        raise Exception("Wrong Disease Token!")

# # # # get_metadata_objects
# This will return all objects of a disease, across all its models
# We can then put any manager class methods(like .all, .get, .get) 
# (Refer to Django Documentation on QuerySets for more information)
# This assumes that the argument is a valid, verified disease name identifier,
# (which means it belongs to the list above)
# returns a tuple of all dataset objects, which has the number of datasets as the first value
# and a list of objects as second value

def get_metadata_objects(disease):
    if disease == 'meningioma':
        try:
            dataset_1 = Meningioma_1_PXD007073_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_1 = None
        try:
            dataset_2 = Meningioma_2_PXD014852_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_2 = None

        serialized_dataset_1 = Meningioma_1_PXD007073_Metadata_Serializer(dataset_1,
                                                        fields=(
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_2 = Meningioma_2_PXD014852_Metadata_Serializer(dataset_2,
                                                        fields=(
                                                                ),
                                                        exclude=True
                                                        )

        return (2,[
                    {'studyId': 'PXD007073', 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014852', 'data': serialized_dataset_2.data},
                    ]
                )
    else:
        raise Exception("Wrong Disease Token!")

# Create your views here.
@api_view(['GET'])
def disease_metadata(request, disease):
    disease = disease.lower()
    if disease in disease_list:
        metadata_length, metadata = get_metadata_objects(disease)
        return JsonResponse({'disease': disease, 'data': metadata})
    else:
        return JsonResponse({'message': f'The disease: "{disease}" does not exist in BDTM Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def single_protein_single_disease(request, proteinId, disease):
    proteinId = proteinId.upper()
    disease = disease.lower()
    if disease in disease_list:
        metadata_length, metadata = get_metadata_objects(disease)
        data_length, data = get_objects(disease=disease, proteinId=proteinId)
        return JsonResponse({'proteinId': proteinId, 'disease': disease, 'data': data, 'metadata':metadata})
    else:
        return JsonResponse({'message': f'The disease: "{disease}" does not exist in BDTM Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def single_protein_all_data(request, proteinId):
    data_list = []
    proteinId = proteinId.upper()
    for disease in disease_list:
        metadata_length, metadata = get_metadata_objects(disease)
        data_length, data = get_objects(disease=disease, proteinId=proteinId)
        data_list.append({'disease': disease, 'diseaseData': data, 'diseaseMetadata':metadata})
    
    return JsonResponse({'proteinId': proteinId, 'data': data_list})
