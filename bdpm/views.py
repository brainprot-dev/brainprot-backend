from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

# All Models
from .meningioma.models_meningiomas import *
from .Amyotrophic_Lateral_Sclerosis.models_Amyotrophic_Lateral_Sclerosis import *
from .Alzhiemer_s.models_Alzhiemer_s import *
from .Medulloblastoma.models_Medulloblastoma import *
from .Parkinson.models_Parkinson import *
from .Glioma.models_Glioma import *

# All serializers
from .meningioma.serializers_meningiomas import *
from .Amyotrophic_Lateral_Sclerosis.serializers_Amyotrophic_Lateral_Sclerosis import *
from .Alzhiemer_s.serializers_Alzhiemer_s import *
from .Medulloblastoma.serializers_Medulloblastoma import *
from .Parkinson.serializers_Parkinson import *
from .Glioma.serializers_Glioma import *

#For Faster Concatenating of Lists
from itertools import chain 

# Global Variables
disease_list = [
    'als',
    'alzheimer',
    'glioma',
    'medulloblastoma',
    'meningioma',
    'parkinson'
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
        try:
            dataset_4 = Meningioma_4_PXD015979.objects.get(proteinId=proteinId)
        except:
            dataset_4 = None

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
        serialized_dataset_4 = Meningioma_4_PXD015979_Serializer(dataset_4,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )

        return (4,[
                    {'studyId': 'PXD007073', 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014852', 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD012923', 'data': serialized_dataset_3.data},
                    {'studyId': 'PXD015979', 'data': serialized_dataset_4.data},
                    ]
                )
    elif disease == 'alzheimer':
        try:
            dataset_1 = Alzhiemer_s_1_PXD009199.objects.get(proteinId=proteinId)
        except:
            dataset_1 = None
        try:
            dataset_2 = Alzhiemer_s_2_PXD014376.objects.get(proteinId=proteinId)
        except:
            dataset_2 = None
        try:
            dataset_3 = Alzhiemer_s_3_PXD037133.objects.get(proteinId=proteinId)
        except:
            dataset_3 = None
        try:
            dataset_4 = Alzhiemer_s_4_PXD005319.objects.get(proteinId=proteinId)
        except:
            dataset_4 = None
        try:
            dataset_5 = Alzhiemer_s_5_PXD005321.objects.get(proteinId=proteinId)
        except:
            dataset_5 = None
        #try:
        #    dataset_6 = Alzhiemer_s_6_PXD021645.objects.get(proteinId=proteinId)
        #except:
        #    dataset_6 = None
        try:
            dataset_7 = Alzhiemer_s_7_PXD023199.objects.get(proteinId=proteinId)
        except:
            dataset_7 = None
        try:
            dataset_8 = Alzhiemer_s_8_PXD027173.objects.get(proteinId=proteinId)
        except:
            dataset_8 = None


        serialized_dataset_1 = Alzhiemer_s_1_PXD009199_Serializer(dataset_1,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_2 = Alzhiemer_s_2_PXD014376_Serializer(dataset_2,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )


        serialized_dataset_3 = Alzhiemer_s_3_PXD037133_Serializer(dataset_3,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_4 = Alzhiemer_s_4_PXD005319_Serializer(dataset_4,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_5 = Alzhiemer_s_5_PXD005321_Serializer(dataset_5,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        """ serialized_dataset_6 = Alzhiemer_s_6_PXD021645_Serializer(dataset_6,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        ) """
        serialized_dataset_7 = Alzhiemer_s_7_PXD023199_Serializer(dataset_7,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_8 = Alzhiemer_s_8_PXD027173_Serializer(dataset_8,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )


        return (7,[
                    {'studyId': 'PXD009199', 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014376', 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD037133', 'data': serialized_dataset_3.data},
                    {'studyId': 'PXD005319', 'data': serialized_dataset_4.data},
                    {'studyId': 'PXD005321', 'data': serialized_dataset_5.data},
                    #{'studyId': 'PXD021645', 'data': serialized_dataset_6.data},
                    {'studyId': 'PXD023199', 'data': serialized_dataset_7.data},
                    {'studyId': 'PXD027173', 'data': serialized_dataset_8.data},

                    ]
                )


    elif disease == 'als':
        try:
            dataset_1 = Amyotrophic_Lateral_Sclerosis_1_PXD021630.objects.get(proteinId=proteinId)
        except:
            dataset_1 = None


        serialized_dataset_1 = Amyotrophic_Lateral_Sclerosis_1_PXD021630_Serializer(dataset_1,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
 

        return (1,[
                    {'studyId': 'PXD021630', 'data': serialized_dataset_1.data},

                    ]
                )



    elif disease == 'glioma':
        try:
            dataset_1 = Glioma_1_PXD010247.objects.get(proteinId=proteinId)
        except:
            dataset_1 = None

        try:
            dataset_2 = Glioma_2_PXD014606.objects.get(proteinId=proteinId)
        except:
            dataset_2 = None
        try:
            dataset_3 = Glioma_3_PXD028931.objects.get(proteinId=proteinId)
        except:
            dataset_3 = None


        serialized_dataset_1 = Glioma_1_PXD010247_Serializer(dataset_1,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_2 = Glioma_2_PXD014606_Serializer(dataset_2,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_3 = Glioma_3_PXD028931_Serializer(dataset_3,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )

        return (3,[
                    {'studyId': 'PXD010247', 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014606', 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD028931', 'data': serialized_dataset_3.data},

                    ]
                )


    elif disease == 'medulloblastoma':
        try:
            dataset_1 = Medulloblastoma_1_PXD014950.objects.get(proteinId=proteinId)
        except:
            dataset_1 = None


        serialized_dataset_1 = Medulloblastoma_1_PXD014950_Serializer(dataset_1,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
 

        return (1,[
                    {'studyId': 'PXD014950', 'data': serialized_dataset_1.data},

                    ]
                )

    elif disease == 'parkinson':
        try:
            dataset_1 = Parkinson_1_PXD008036.objects.get(proteinId=proteinId)
        except:
            dataset_1 = None
        try:
            dataset_2 = Parkinson_2_PXD022092.objects.get(proteinId=proteinId)
        except:
            dataset_2 = None
        try:
            dataset_3 = Parkinson_3_PXD024998.objects.get(proteinId=proteinId)
        except:
            dataset_3 = None


        serialized_dataset_1 = Parkinson_1_PXD008036_Serializer(dataset_1,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_2 = Parkinson_2_PXD022092_Serializer(dataset_2,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_3 = Parkinson_3_PXD024998_Serializer(dataset_3,
                                                        fields=(
                                                                'proteinId',
                                                                ),
                                                        exclude=True
                                                        )

        return (3,[
                    {'studyId': 'PXD008036', 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD022092', 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD024998', 'data': serialized_dataset_3.data}
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
        try:
            dataset_4 = Meningioma_4_PXD015979_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_4 = None

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
        serialized_dataset_4 = Meningioma_4_PXD015979_Metadata_Serializer(dataset_4,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True )
        
        groupII_choices = ['Control', 'Grade 1', 'Grade 2','Grade 3']
        groupIIIchoices_PXD007073 = [
        'Anaplastic',
        'Atypical',
        'Fibroplastic',
        'Meningothelial',
        'Transitional'
        ]

        groupIIIchoices_PXD012923 = [
        (0, 'Primary'),
        (1, 'Recurrence 1st'),
        (2, 'Recurrence 2nd')
        ]

        groupIVchoices_PXD012923 = [
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
        groupIIIchoices_PXD015979 = [
        (0, 'Primary'),
        (1, 'Recurrence 1st'),
        (2, 'Recurrence 2nd')
        ]

        return (4,[
                    {'studyId': 'PXD007073','numGroups': 4, 'groupChoices': [groupIchoices, groupII_choices, groupIIIchoices_PXD007073, groupIVchoices_PXD007073], 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014852','numGroups': 2, 'groupChoices': [groupIchoices, groupII_choices], 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD012923','numGroups': 3, 'groupChoices': [groupIchoices, groupII_choices, groupIIIchoices_PXD012923, groupIVchoices_PXD012923], 'data': serialized_dataset_3.data},
                    {'studyId': 'PXD015979','numGroups': 2, 'groupChoices': [groupIchoices, groupII_choices, groupIIIchoices_PXD015979], 'data': serialized_dataset_3.data},
                    ]
                )
    elif disease == 'alzheimer':
        try:
            dataset_1 = Alzhiemer_s_1_PXD009199_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_1 = None
        try:
            dataset_2 = Alzhiemer_s_2_PXD014376_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_2 = None
        try:
            dataset_3 = Alzhiemer_s_3_PXD037133_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_3 = None
        try:
            dataset_4 = Alzhiemer_s_4_PXD005319_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_4 = None
        try:
            dataset_5 = Alzhiemer_s_5_PXD005321_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_5 = None
        """ try:
            dataset_6 = Alzhiemer_s_6_PXD021645_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_6 = None """
        try:
            dataset_7 = Alzhiemer_s_7_PXD023199_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_7 = None
        try:
            dataset_8 = Alzhiemer_s_8_PXD027173_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_8 = None

        serialized_dataset_1 = Alzhiemer_s_1_PXD009199_Metadata_Serializer(dataset_1,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_2 = Alzhiemer_s_2_PXD014376_Metadata_Serializer(dataset_2,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_3 = Alzhiemer_s_3_PXD037133_Metadata_Serializer(dataset_3,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_4 = Alzhiemer_s_4_PXD005319_Metadata_Serializer(dataset_4,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_5 = Alzhiemer_s_5_PXD005321_Metadata_Serializer(dataset_5,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        """ serialized_dataset_6 = Alzhiemer_s_6_PXD021645_Metadata_Serializer(dataset_6,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        ) """
        serialized_dataset_7 = Alzhiemer_s_7_PXD023199_Metadata_Serializer(dataset_7,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_8 = Alzhiemer_s_8_PXD027173_Metadata_Serializer(dataset_8,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )

        groupIIchoices = ['Control', 'Grade 1', 'Grade 2','Grade 3']
      
        return (8,[
                    {'studyId': 'PXD009199','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014376','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD037133','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_3.data},
                    {'studyId': 'PXD005319','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_4.data},
                    {'studyId': 'PXD005321','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_5.data},
                    #{'studyId': 'PXD021645','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_6.data},
                    {'studyId': 'PXD023199','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_7.data},
                    {'studyId': 'PXD027173','numGroups': 2, 'groupChoices': [groupIchoices,groupIIchoices], 'data': serialized_dataset_8.data},
                    ]
                )


    elif disease == 'als':
        try:
            dataset_1 = Amyotrophic_Lateral_Sclerosis_1_PXD021630_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_1 = None

        serialized_dataset_1 = Amyotrophic_Lateral_Sclerosis_1_PXD021630_Metadata_Serializer(dataset_1,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )


        groupIIchoices = ['Control', 'Grade 1', 'Grade 2','Grade 3']
      
        return (1,[
                    {'studyId': 'PXD021630','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data},

                    ]
                )

    elif disease == 'glioma':
        try:
            dataset_1 = Glioma_1_PXD010247_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_1 = None
        try:
            dataset_2 = Glioma_2_PXD014606_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_2 = None
        try:
            dataset_3 = Glioma_3_PXD028931_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_3 = None


        serialized_dataset_1 = Glioma_1_PXD010247_Metadata_Serializer(dataset_1,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_2 = Glioma_2_PXD014606_Metadata_Serializer(dataset_2,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_3 = Glioma_3_PXD028931_Metadata_Serializer(dataset_3,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )

        groupIIchoices = ['Control', 'Grade 1', 'Grade 2','Grade 3']
      
        return (1,[
                    {'studyId': 'PXD010247','numGroups': 2, 'groupChoices': [groupIchoices,groupIIchoices], 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD014606','numGroups': 2, 'groupChoices': [groupIchoices,groupIIchoices], 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD028931','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_3.data},
                    ]
                )


    elif disease == 'medulloblastoma':
        try:
            dataset_1 = Medulloblastoma_1_PXD014950_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_1 = None

        serialized_dataset_1 = Medulloblastoma_1_PXD014950_Metadata_Serializer(dataset_1,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )


        groupIIchoices = ['Control', 'Grade 1', 'Grade 2','Grade 3']
      
        return (1,[
                    {'studyId': 'PXD014950','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data},

                    ]
                )

    elif disease == 'parkinson':
        try:
            dataset_1 = Parkinson_1_PXD008036_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_1 = None
        try:
            dataset_2 = Parkinson_2_PXD022092_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_2 = None
        try:
            dataset_3 = Parkinson_3_PXD024998_Metadata.objects.all().order_by('sampleId')
        except:
            dataset_3 = None


        serialized_dataset_1 = Parkinson_1_PXD008036_Metadata_Serializer(dataset_1,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_2 = Parkinson_2_PXD022092_Metadata_Serializer(dataset_2,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )
        serialized_dataset_3 = Parkinson_3_PXD024998_Metadata_Serializer(dataset_3,
                                                        fields=(
                                                                ),
                                                        many=True,
                                                        exclude=True
                                                        )

        groupIIchoices = ['Control', 'Grade 1', 'Grade 2','Grade 3']
      
        return (1,[
                    {'studyId': 'PXD008036','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data},
                    {'studyId': 'PXD022092','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_2.data},
                    {'studyId': 'PXD024998','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_3.data},
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
    #unprocessed_data_list = []
    proteinId = proteinId.upper()
    for disease in disease_list:
        metadata_length, metadata = get_metadata_objects(disease)
        data_length, data = get_objects(disease=disease, proteinId=proteinId)


        # reading data from models and split in to raw and pocessed
        
        data_list.append({'disease': disease, 'diseaseData': data, 'diseaseMetadata':metadata})


    return JsonResponse({'proteinId': proteinId, 'data': data_list})
