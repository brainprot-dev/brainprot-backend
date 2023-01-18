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
        try:
            dataset_3 = Meningioma_3_PXD012923.objects.get(proteinId=proteinId)
        except:
            dataset_3 = None

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
        serialized_dataset_3 = Meningioma_3_PXD012923_Serializer(dataset_3,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )

        return (3,[
                    {'studyId': 'PXD007073', 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014852', 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD012923', 'data': serialized_dataset_3.data},
                    ]
                )
    else:
        raise Exception("Wrong Disease Token!")


# Helper Functions

# # # # get_objects
# This will return all objects of a disease, across all its models
# We can then put any manager class methods(like .all, .get, .get) 
# (Refer to Django Documentation on QuerySets for more information)
# This assumes that the argument is a valid, verified disease name identifier,
# (which means it belongs to the list above)
# returns a tuple of all dataset objects, which has the number of datasets as the first value
# and a list of objects as second value

def get_unprocessed_objects(disease, proteinId):
    if disease == 'meningioma':
        try:
            dataset_1 = Meningioma_1_PXD007073_Unprocessed.objects.get(proteinId=proteinId)
        except:
            dataset_1 = None
        try:
            dataset_2 = Meningioma_2_PXD014852_Unprocessed.objects.get(proteinId=proteinId)
        except:
            dataset_2 = None
        try:
            dataset_3 = Meningioma_3_PXD012923_Unprocessed.objects.get(proteinId=proteinId)
        except:
            dataset_3 = None

        serialized_dataset_1 = Meningioma_1_PXD007073_Unprocessed_Serializer(dataset_1,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_2 = Meningioma_2_PXD014852_Unprocessed_Serializer(dataset_2,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_3 = Meningioma_3_PXD012923_Unprocessed_Serializer(dataset_3,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )

        return (3,[
                    {'studyId': 'PXD007073', 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014852', 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD012923', 'data': serialized_dataset_3.data},
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
    groupIchoices = ["Control", "Disease"]

    if disease == 'meningioma':
        try:
            dataset_1 = Meningioma_1_PXD007073_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_1 = None
        try:
            dataset_2 = Meningioma_2_PXD014852_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_2 = None
        try:
            dataset_3 = Meningioma_3_PXD012923_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_3 = None

        serialized_dataset_1 = Meningioma_1_PXD007073_Metadata_Serializer(dataset_1,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_2 = Meningioma_2_PXD014852_Metadata_Serializer(dataset_2,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_3 = Meningioma_3_PXD012923_Metadata_Serializer(dataset_3,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        groupIIchoices = ['Control', 'Grade 1', 'Grade 2','Grade 3']
        groupIIIchoices_PXD007073 = [
        'Anaplastic',
        'Atypical',
        'Fibroplastic',
        'Meningothelial',
        'Transitional'
        ]
        groupIIIchoices_PXD012923 = [
            'Skull Base',
            'Convexity',
            'Other'
        ]
        groupIVchoices_PXD007073 = [
        'Brain Stem',
        'Frontal',
        'Lateral posterior fossa',
        'Occipital',
        'Olfactory groove',
        'Parafalcine',
        'Parasagittal',
        'Parietal',
        'Sphenoid wing'
        ]
        return (3,[
                    {'studyId': 'PXD007073','numGroups': 4, 'groupChoices': [groupIchoices, groupIIchoices, groupIIIchoices_PXD007073, groupIVchoices_PXD007073], 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014852','numGroups': 2, 'groupChoices': [groupIchoices, groupIIchoices], 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD012923','numGroups': 3, 'groupChoices': [groupIchoices, groupIIchoices, groupIIIchoices_PXD012923], 'data': serialized_dataset_3.data},
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
        unprocessed_data_length, unprocessed_data = get_unprocessed_objects(disease=disease, proteinId=proteinId)
        return JsonResponse({'proteinId': proteinId, 'disease': disease, 'data': data, 'metadata':metadata, 'unprocessedData': unprocessed_data})
    else:
        return JsonResponse({'message': f'The disease: "{disease}" does not exist in BDTM Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def single_protein_all_data(request, proteinId):
    data_list = []
    #unprocessed_data_list = []
    proteinId = proteinId.upper()
    for disease in disease_list:
        metadata_length, metadata = get_metadata_objects(disease)
        data_length, data = get_objects(disease=disease, proteinId=proteinId)
        #unprocessed_data_length, unprocessed_data = get_unprocessed_objects(disease=disease, proteinId=proteinId)
        data_list.append({'disease': disease, 'diseaseData': data, 'diseaseMetadata':metadata})
        #unprocessed_data_list.append({'disease': disease, 'diseaseData': unprocessed_data, 'diseaseMetadata':metadata})
    
    return JsonResponse({'proteinId': proteinId, 'data': data_list})
