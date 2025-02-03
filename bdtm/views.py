from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

# All Models
from .als.models_als import *
from .alzheimer.models_alzheimer import *
from .ftld.models_ftld import *
from .glioblastoma.models_glioblastoma import *
from .glioma.models_glioma import *
from .huntington.models_huntington import *
from .medulloblastoma.models_medulloblastoma import *
from .meningioma.models_meningiomas import *
from .multiple_sclerosis.models_sclerosis import *
from .parkinson.models_parkinson import *
from .pituitary_adenoma.models_pituitary import *
from .pvalue.models_pvalue import *

# All Serializers
from .als.serializers_als import *
from .alzheimer.serializers_alzheimer import *
from .ftld.serializers_ftld import *
from .glioblastoma.serializers_glioblastoma import *
from .glioma.serializers_glioma import *
from .huntington.serializers_huntington import *
from .medulloblastoma.serializers_medulloblastoma import *
from .meningioma.serializers_meningiomas import *
from .multiple_sclerosis.serializers_sclerosis import *
from .parkinson.serializers_parkinson import *
from .pituitary_adenoma.serializers_pituitary import *
from .pvalue.serializers_pvalue import *

#For Faster Concatenating of Lists
from itertools import chain 

# Global Variables
disease_list = [
    'als',
    'alzheimer',
    'ftld',
    'glioblastoma',
    'glioma',
    'huntington',
    'medulloblastoma',
    'meningioma',
    'multiple_sclerosis',
    'parkinson',
    'pituitary_adenoma'
]



# Helper Functions

# # # # get_objects_from_disease
# This will return all objects of a disease, across all its models
# We can then put any manager class methods(like .all, .get, .get) 
# (Refer to Django Documentation on QuerySets for more information)
# This assumes that the argument is a valid, verified disease name identifier,
# (which means it belongs to the list above)
# returns a tuple of all dataset objects, which has the number of datasets as the first value
# and a list of objects as second value

def get_objects(disease, geneName):
    if disease == 'als':
        try:
            dataset_1 = ALS_1_GSE19332.objects.get(geneName=geneName)
        except:
            dataset_1 = None
        try:
            dataset_2 = ALS_2_GSE20589.objects.get(geneName=geneName)
        except:
            dataset_2 = None
        try:
            dataset_3 = ALS_3_GSE68605.objects.get(geneName=geneName)
        except:
            dataset_3 = None

        serialized_dataset_1 = ALS_1_GSE19332_Serializer(dataset_1,
                                                        fields=(
                                                                'probeId',
                                                                'geneName'
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_2 = ALS_2_GSE20589_Serializer(dataset_2,
                                                        fields=(
                                                                'probeId',
                                                                'geneName'
                                                                ),
                                                        exclude=True
                                                        )
        serialized_dataset_3 = ALS_3_GSE68605_Serializer(dataset_3,
                                                        fields=(
                                                                'probeId',
                                                                'geneName'
                                                                ),
                                                        exclude=True
                                                        )

        return (3,[
                    {'studyId': 'GSE19332', 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE20589', 'data': serialized_dataset_2.data},
                    {'studyId': 'GSE68605', 'data': serialized_dataset_3.data}
                    ]
                )
    elif disease == 'alzheimer':
        try:
            dataset_1 = Alzheimer_1_GSE12685.objects.get(geneName=geneName)
        except:
            dataset_1 = None
        try:
            dataset_2 = Alzheimer_2_GSE1297.objects.get(geneName=geneName)
        except:
            dataset_2 = None
        try:
            dataset_3 = Alzheimer_3_GSE28146.objects.get(geneName=geneName)
        except:
            dataset_3 = None
        try:
            dataset_4 = Alzheimer_4_GSE4757.objects.get(geneName=geneName)
        except:
            dataset_4 = None
        try:
            dataset_5 = Alzheimer_5_GSE16759.objects.get(geneName=geneName)
        except:
            dataset_5 = None
        try:
            dataset_6 = Alzheimer_6_GSE5281.objects.get(geneName=geneName)
        except:
            dataset_6 = None
        try:
            dataset_7 = Alzheimer_7_GSE48350.objects.get(geneName=geneName)
        except:
            dataset_7 = None

        serialized_dataset_1 = Alzheimer_1_GSE12685_Serializer(dataset_1,
                                                                fields=(
                                                                        
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_2 = Alzheimer_2_GSE1297_Serializer(dataset_2,
                                                            fields=(
                                                                    'probeId',
                                                                    'geneName'
                                                                    ),
                                                            exclude=True
                                                            )
        serialized_dataset_3 = Alzheimer_3_GSE28146_Serializer(dataset_3,
                                                            fields=(                   
                                                                    'probeId',
                                                                    'geneName'
                                                                    ),
                                                            exclude=True
                                                            )
        serialized_dataset_4 = Alzheimer_4_GSE4757_Serializer(dataset_4,
                                                            fields=(
                                                                    'probeId',
                                                                    'geneName'
                                                                    ),
                                                            exclude=True
                                                            )
        serialized_dataset_5 = Alzheimer_5_GSE16759_Serializer(dataset_5,
                                                            fields=(
                                                                    'probeId',
                                                                    'geneName'
                                                                    ),
                                                            exclude=True
                                                            )
        serialized_dataset_6 = Alzheimer_6_GSE5281_Serializer(dataset_6,
                                                            fields=(
                                                                    'probeId',
                                                                    'geneName'
                                                                    ),
                                                            exclude=True
                                                            )
        serialized_dataset_7 = Alzheimer_7_GSE48350_Serializer(dataset_7,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )

        return (7,[
                    {'studyId': 'GSE12685', 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE1297', 'data': serialized_dataset_2.data},
                    {'studyId': 'GSE28146', 'data': serialized_dataset_3.data},
                    {'studyId': 'GSE4757', 'data': serialized_dataset_4.data},
                    {'studyId': 'GSE16759', 'data': serialized_dataset_5.data},
                    {'studyId': 'GSE5281', 'data': serialized_dataset_6.data},
                    {'studyId': 'GSE48350', 'data': serialized_dataset_7.data}
                    ]
                )
    elif disease == 'ftld':
        try:
            dataset_1 = FTLD_1_GSE13162.objects.get(geneName=geneName)
        except:
            dataset_1 = None

        serialized_dataset_1 = FTLD_1_GSE13162_Serializer(dataset_1,
                                                        fields=(
                                                                'probeId',
                                                                'geneName'
                                                                ),
                                                        exclude=True
                                                        )

        return (1,[
                    {'studyId': 'GSE13162', 'data': serialized_dataset_1.data}
                    ]
                )
    elif disease == 'glioblastoma':
        try:
            dataset_1 = Glioblastoma_1_GSE13276.objects.get(geneName=geneName)
        except:
            dataset_1 = None

        serialized_dataset_1 = Glioblastoma_1_GSE13276_Serializer(dataset_1,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                ) 

        return (1,[
                    {'studyId': 'GSE13276', 'data': serialized_dataset_1.data}
                    ]
                )
    elif disease == 'glioma':
        try:
            dataset_1 = Glioma_1_GSE12657.objects.get(geneName=geneName)
        except:
            dataset_1 = None

        serialized_dataset_1 = Glioma_1_GSE12657_Serializer(dataset_1,
                                                            fields=(
                                                                    'probeId',
                                                                    'geneName'
                                                                    ),
                                                            exclude=True
                                                            )

        return (1,[
                    {'studyId': 'GSE12657', 'data': serialized_dataset_1.data}
                    ]
                )
    elif disease == 'huntington':
        try:
            dataset_1 = Huntington_1_GSE3790_U133A.objects.get(geneName=geneName)
        except:
            dataset_1 = None
        try:
            dataset_2 = Huntington_2_GSE3790_U133B.objects.get(geneName=geneName)
        except:
            dataset_2 = None

        serialized_dataset_1 = Huntington_1_GSE3790_U133A_Serializer(dataset_1,
                                                                    fields=(
                                                                            'probeId',
                                                                            'geneName'
                                                                            ),
                                                                    exclude=True
                                                                    )
        serialized_dataset_2 = Huntington_2_GSE3790_U133B_Serializer(dataset_2,
                                                                    fields=(
                                                                            'probeId',
                                                                            'geneName'
                                                                            ),
                                                                    exclude=True
                                                                    )

        return (2,[
                    {'studyId': 'GSE3790_U133A', 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE3790_U133B', 'data': serialized_dataset_2.data}
                    ]
                )
    elif disease == 'medulloblastoma':
        try:
            dataset_1 = Medulloblastoma_1_GSE62600.objects.get(geneName=geneName)
        except:
            dataset_1 = None

        serialized_dataset_1 = Medulloblastoma_1_GSE62600_Serializer(dataset_1,
                                                                    fields=(
                                                                            'probeId',
                                                                            'geneName'
                                                                            ),
                                                                    exclude=True
                                                                    )

        return (1,[
                    {'studyId': 'GSE62600', 'data': serialized_dataset_1.data}
                    ]
                )
    elif disease == 'meningioma':
        try:
            dataset_1 = Meningioma_1_GSE43290.objects.get(geneName=geneName)
        except:
            dataset_1 = None
        try:
            dataset_2 = Meningioma_2_GSE54934.objects.get(geneName=geneName)
        except:
            dataset_2 = None

        serialized_dataset_1 = Meningioma_1_GSE43290_Serializer(dataset_1,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_2 = Meningioma_2_GSE54934_Serializer(dataset_2,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )

        return (2,[
                    {'studyId': 'GSE43290', 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE54934', 'data': serialized_dataset_2.data}
                    ]
                )
    elif disease == 'multiple_sclerosis':
        try:
            dataset_1 = Multiple_Sclerosis_1_GSE38010.objects.get(geneName=geneName)
        except:
            dataset_1 = None
        try:
            dataset_2 = Multiple_Sclerosis_2_GSE52139.objects.get(geneName=geneName)
        except:
            dataset_2 = None
        try:
            dataset_3 = Multiple_Sclerosis_3_GSE83670.objects.get(geneName=geneName)
        except:
            dataset_3 = None

        serialized_dataset_1 = Multiple_Sclerosis_1_GSE38010_Serializer(dataset_1,
                                                                        fields=(
                                                                                'probeId',
                                                                                'geneName'
                                                                                ),
                                                                        exclude=True
                                                                        )
        serialized_dataset_2 = Multiple_Sclerosis_2_GSE52139_Serializer(dataset_2,
                                                                        fields=(
                                                                                'probeId',
                                                                                'geneName'
                                                                                ),
                                                                        exclude=True
                                                                        )
        serialized_dataset_3 = Multiple_Sclerosis_3_GSE83670_Serializer(dataset_3,
                                                                        fields=(
                                                                                'probeId',
                                                                                'geneName'
                                                                                ),
                                                                        exclude=True
                                                                        )

        return (3,[
                    {'studyId': 'GSE38010', 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE52139', 'data': serialized_dataset_2.data},
                    {'studyId': 'GSE83670', 'data': serialized_dataset_3.data}
                    ]
                )
    elif disease == 'parkinson':
        try:
            dataset_1 = Parkinson_1_GSE7621.objects.get(geneName=geneName)
        except:
            dataset_1 = None
        try:
            dataset_2 = Parkinson_2_GSE8397_U133A.objects.get(geneName=geneName)
        except:
            dataset_2= None
        try:
            dataset_3 = Parkinson_3_GSE8397_U133B.objects.get(geneName=geneName)
        except:
            dataset_3 = None
        try:
            dataset_4 = Parkinson_4_GSE19587.objects.get(geneName=geneName)
        except:
            dataset_4 = None
        try:
            dataset_5 = Parkinson_5_GSE20141.objects.get(geneName=geneName)
        except:
            dataset_5 = None
        try:
            dataset_6 = Parkinson_6_GSE20146.objects.get(geneName=geneName)
        except:
            dataset_6 = None
        try:
            dataset_7 = Parkinson_7_GSE20163.objects.get(geneName=geneName)
        except:
            dataset_7 = None
        try:
            dataset_8 = Parkinson_8_GSE20164.objects.get(geneName=geneName)
        except:
            dataset_8 = None
        try:
            dataset_9 = Parkinson_9_GSE20168.objects.get(geneName=geneName)
        except:
            dataset_9 = None
        try:
            dataset_10 = Parkinson_10_GSE20291.objects.get(geneName=geneName)
        except:
            dataset_10 = None
        try:
            dataset_11 = Parkinson_11_GSE20292.objects.get(geneName=geneName)
        except:
            dataset_11 = None
        try:
            dataset_12 = Parkinson_12_GSE20314.objects.get(geneName=geneName)
        except:
            dataset_12 = None
        try:
            dataset_13 = Parkinson_13_GSE20333.objects.get(geneName=geneName)
        except:
            dataset_13 = None
        try:
            dataset_14 = Parkinson_14_GSE24378.objects.get(geneName=geneName)
        except:
            dataset_14 = None

        serialized_dataset_1 = Parkinson_1_GSE7621_Serializer(dataset_1,
                                                            fields=(
                                                                    'probeId',
                                                                    'geneName'
                                                                    ),
                                                            exclude=True
                                                            )
        serialized_dataset_2 = Parkinson_2_GSE8397_U133A_Serializer(dataset_2,
                                                            fields=(
                                                                    'probeId',
                                                                    'geneName'
                                                                    ),
                                                            exclude=True
                                                            )
        serialized_dataset_3 = Parkinson_3_GSE8397_U133B_Serializer(dataset_3,
                                                            fields=(
                                                                    'probeId',
                                                                    'geneName'
                                                                    ),
                                                            exclude=True
                                                            )
        serialized_dataset_4 = Parkinson_4_GSE19587_Serializer(dataset_4,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_5 = Parkinson_5_GSE20141_Serializer(dataset_5,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_6 = Parkinson_6_GSE20146_Serializer(dataset_6,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_7 = Parkinson_7_GSE20163_Serializer(dataset_7,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_8 = Parkinson_8_GSE20164_Serializer(dataset_8,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_9 = Parkinson_9_GSE20168_Serializer(dataset_9,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_10 = Parkinson_10_GSE20291_Serializer(dataset_10,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_11 = Parkinson_11_GSE20292_Serializer(dataset_11,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_12 = Parkinson_12_GSE20314_Serializer(dataset_12,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_13 = Parkinson_13_GSE20333_Serializer(dataset_13,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        serialized_dataset_14 = Parkinson_14_GSE24378_Serializer(dataset_14,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )

        return (14,[
                    {'studyId': 'GSE7621', 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE8397_U133A', 'data': serialized_dataset_2.data},
                    {'studyId': 'GSE8397_U133B', 'data': serialized_dataset_3.data},
                    {'studyId': 'GSE19587', 'data': serialized_dataset_4.data},
                    {'studyId': 'GSE20141', 'data': serialized_dataset_5.data},
                    {'studyId': 'GSE20146', 'data': serialized_dataset_6.data},
                    {'studyId': 'GSE20163', 'data': serialized_dataset_7.data},
                    {'studyId': 'GSE20164', 'data': serialized_dataset_8.data},
                    {'studyId': 'GSE20168', 'data': serialized_dataset_9.data},
                    {'studyId': 'GSE20291', 'data': serialized_dataset_10.data},
                    {'studyId': 'GSE20292', 'data': serialized_dataset_11.data},
                    {'studyId': 'GSE20314', 'data': serialized_dataset_12.data},
                    {'studyId': 'GSE20333', 'data': serialized_dataset_13.data},
                    {'studyId': 'GSE24378', 'data': serialized_dataset_14.data}
                    ]
                )
    elif disease == 'pituitary_adenoma':
        try:
            dataset_1 = Pituitary_1_GSE36314.objects.get(geneName=geneName)
        except:
            dataset_1 = None

        serialized_dataset_1 = Pituitary_1_GSE36314_Serializer(dataset_1,
                                                                fields=(
                                                                        'probeId',
                                                                        'geneName'
                                                                        ),
                                                                exclude=True
                                                                )
        return (1,[
                    {'studyId': 'GSE36314', 'data': serialized_dataset_1.data}
                    ]
                )
    else:
        raise Exception("Wrong Disease Token!")

    
# # # # get_metadata_objects_from_disease
# This will return all objects of a disease, across all its models
# We can then put any manager class methods(like .all, .get, .get) 
# (Refer to Django Documentation on QuerySets for more information)
# This assumes that the argument is a valid, verified disease name identifier,
# (which means it belongs to the list above)
# returns a tuple of all dataset objects, which has the number of datasets as the first value

def get_metadata_objects(disease):
    groupIchoices = ["Control", "Disease"]

    if disease == 'als':
        dataset_1 = ALS_1_GSE19332_Metadata.objects.all().order_by('sampleId')
        dataset_2 = ALS_2_GSE20589_Metadata.objects.all().order_by('sampleId')
        dataset_3 = ALS_3_GSE68605_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = ALS_1_GSE19332_Metadata_Serializer(dataset_1,
                                                                fields=(
                                                                        
                                                                        ),
                                                                many=True,
                                                                exclude=True
                                                                )
        serialized_dataset_2 = ALS_2_GSE20589_Metadata_Serializer(dataset_2,
                                                                fields=(
                                                                        
                                                                        ),
                                                                many=True,
                                                                exclude=True
                                                                )
        serialized_dataset_3 = ALS_3_GSE68605_Metadata_Serializer(dataset_3,
                                                                fields=(
                                                                        
                                                                        ),
                                                                many=True,
                                                                exclude=True
                                                                )

        return (3,[
                    {'studyId': 'GSE19332','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE20589','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_2.data},
                    {'studyId': 'GSE68605','numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_3.data}
                    ]
                )
    elif disease == 'alzheimer':
        dataset_1 = Alzheimer_1_GSE12685_Metadata.objects.all().order_by('sampleId')
        dataset_2 = Alzheimer_2_GSE1297_Metadata.objects.all().order_by('sampleId')
        dataset_3 = Alzheimer_3_GSE28146_Metadata.objects.all().order_by('sampleId')
        dataset_4 = Alzheimer_4_GSE4757_Metadata.objects.all().order_by('sampleId')
        dataset_5 = Alzheimer_5_GSE16759_Metadata.objects.all().order_by('sampleId')
        dataset_6 = Alzheimer_6_GSE5281_Metadata.objects.all().order_by('sampleId')
        dataset_7 = Alzheimer_7_GSE48350_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = Alzheimer_1_GSE12685_Metadata_Serializer(dataset_1,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_2 = Alzheimer_2_GSE1297_Metadata_Serializer(dataset_2,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_3 = Alzheimer_3_GSE28146_Metadata_Serializer(dataset_3,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_4 = Alzheimer_4_GSE4757_Metadata_Serializer(dataset_4,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_5 = Alzheimer_5_GSE16759_Metadata_Serializer(dataset_5,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_6 = Alzheimer_6_GSE5281_Metadata_Serializer(dataset_6,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_7 = Alzheimer_7_GSE48350_Metadata_Serializer(dataset_7,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        groupIIchoices = ['Control', 'Grade 1', 'Grade 2','Grade 3']

        return (7,[
                    {'studyId': 'GSE12685', 'numGroups': 2, 'groupChoices': [groupIchoices, groupIIchoices], 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE1297', 'numGroups': 2, 'groupChoices': [groupIchoices, groupIIchoices], 'data': serialized_dataset_2.data},
                    {'studyId': 'GSE28146', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_3.data},
                    {'studyId': 'GSE4757', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_4.data},
                    {'studyId': 'GSE16759', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_5.data},
                    {'studyId': 'GSE5281', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_6.data},
                    {'studyId': 'GSE48350', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_7.data}
                    ]
                )
    elif disease == 'ftld':
        dataset_1 = FTLD_1_GSE13162_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = FTLD_1_GSE13162_Metadata_Serializer(dataset_1,
                                                                    fields=(
                                                                            
                                                                            ),
                                                                    many=True,
                                                                    exclude=True
                                                                    )

        return (1,[
                    {'studyId': 'GSE13162', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data}
                    ]
                )
    elif disease == 'glioblastoma':
        dataset_1 = Glioblastoma_1_GSE13276_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = Glioblastoma_1_GSE13276_Metadata_Serializer(dataset_1,
                                                                            fields=(
                                                                                    
                                                                                    ),
                                                                            many=True,
                                                                            exclude=True
                                                                            )
        groupIIchoices = ['Control', 'Grade 1', 'Grade 2','Grade 3', 'Grade 4']

        return (1,[
                    {'studyId': 'GSE13276', 'numGroups': 2, 'groupChoices': [groupIchoices, groupIIchoices], 'data': serialized_dataset_1.data}
                    ]
                )
    elif disease == 'glioma':
        dataset_1 = Glioma_1_GSE12657_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = Glioma_1_GSE12657_Metadata_Serializer(dataset_1,
                                                                    fields=(
                                                                            
                                                                            ),
                                                                    many=True,
                                                                    exclude=True
                                                                    )

        return (1,[
                    {'studyId': 'GSE12657', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data}
                    ]
                )
    elif disease == 'huntington':
        dataset_1 = Huntington_1_GSE3790_U133A_Metadata.objects.all().order_by('sampleId')
        dataset_2 = Huntington_2_GSE3790_U133B_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = Huntington_1_GSE3790_U133A_Metadata_Serializer(dataset_1,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_2 = Huntington_2_GSE3790_U133B_Metadata_Serializer(dataset_2,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        groupIIchoices = ['Control', 'Grade 1', 'Grade 2','Grade 3', 'Grade 4']

        return (2,[
                    {'studyId': 'GSE3790_U133A', 'numGroups': 2, 'groupChoices': [groupIchoices, groupIIchoices], 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE3790_U133B', 'numGroups': 2, 'groupChoices': [groupIchoices, groupIIchoices], 'data': serialized_dataset_2.data}
                    ]
                )
    elif disease == 'medulloblastoma':
        dataset_1 = Medulloblastoma_1_GSE62600_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = Medulloblastoma_1_GSE62600_Metadata_Serializer(dataset_1,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )

        return (1,[
                    {'studyId': 'GSE62600', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data}
                    ]
                )
    elif disease == 'meningioma':
        dataset_1 = Meningioma_1_GSE43290_Metadata.objects.all().order_by('sampleId')
        dataset_2 = Meningioma_2_GSE54934_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = Meningioma_1_GSE43290_Metadata_Serializer(dataset_1,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_2 = Meningioma_2_GSE54934_Metadata_Serializer(dataset_2,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )

        groupIIchoices = ['Control', 'Grade 1', 'Grade 2','Grade 3']
    
        return (2,[
                    {'studyId': 'GSE43290', 'numGroups': 2, 'groupChoices': [groupIchoices, groupIIchoices], 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE54934', 'numGroups': 2, 'groupChoices': [groupIchoices, groupIIchoices], 'data': serialized_dataset_2.data}
                    ]
                )
    elif disease == 'multiple_sclerosis':
        dataset_1 = Multiple_Sclerosis_1_GSE38010_Metadata.objects.all().order_by('sampleId')
        dataset_2 = Multiple_Sclerosis_2_GSE52139_Metadata.objects.all().order_by('sampleId')
        dataset_3 = Multiple_Sclerosis_3_GSE83670_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = Multiple_Sclerosis_1_GSE38010_Metadata_Serializer(dataset_1,
                                                                                fields=(
                                                                                        
                                                                                        ),
                                                                                many=True,
                                                                                exclude=True
                                                                                )
        serialized_dataset_2 = Multiple_Sclerosis_2_GSE52139_Metadata_Serializer(dataset_2,
                                                                                fields=(
                                                                                        
                                                                                        ),
                                                                                many=True,
                                                                                exclude=True
                                                                                )
        serialized_dataset_3 = Multiple_Sclerosis_3_GSE83670_Metadata_Serializer(dataset_3,
                                                                                fields=(
                                                                                        
                                                                                        ),
                                                                                many=True,
                                                                                exclude=True
                                                                                )

        return (3,[
                    {'studyId': 'GSE38010', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE52139', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_2.data},
                    {'studyId': 'GSE83670', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_3.data}
                    ]
                )
    elif disease == 'parkinson':
        dataset_1 = Parkinson_1_GSE7621_Metadata.objects.all().order_by('sampleId')
        dataset_2 = Parkinson_2_GSE8397_U133A_Metadata.objects.all().order_by('sampleId')
        dataset_3 = Parkinson_3_GSE8397_U133B_Metadata.objects.all().order_by('sampleId')
        dataset_4 = Parkinson_4_GSE19587_Metadata.objects.all().order_by('sampleId')
        dataset_5 = Parkinson_5_GSE20141_Metadata.objects.all().order_by('sampleId')
        dataset_6 = Parkinson_6_GSE20146_Metadata.objects.all().order_by('sampleId')
        dataset_7 = Parkinson_7_GSE20163_Metadata.objects.all().order_by('sampleId')
        dataset_8 = Parkinson_8_GSE20164_Metadata.objects.all().order_by('sampleId')
        dataset_9 = Parkinson_9_GSE20168_Metadata.objects.all().order_by('sampleId')
        dataset_10 = Parkinson_10_GSE20291_Metadata.objects.all().order_by('sampleId')
        dataset_11 = Parkinson_11_GSE20292_Metadata.objects.all().order_by('sampleId')
        dataset_12 = Parkinson_12_GSE20314_Metadata.objects.all().order_by('sampleId')
        dataset_13 = Parkinson_13_GSE20333_Metadata.objects.all().order_by('sampleId')
        dataset_14 = Parkinson_14_GSE24378_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = Parkinson_1_GSE7621_Metadata_Serializer(dataset_1,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_2 = Parkinson_2_GSE8397_U133A_Metadata_Serializer(dataset_2,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_3 = Parkinson_3_GSE8397_U133B_Metadata_Serializer(dataset_3,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_4 = Parkinson_4_GSE19587_Metadata_Serializer(dataset_4,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_5 = Parkinson_5_GSE20141_Metadata_Serializer(dataset_5,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_6 = Parkinson_6_GSE20146_Metadata_Serializer(dataset_6,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_7 = Parkinson_7_GSE20163_Metadata_Serializer(dataset_7,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_8 = Parkinson_8_GSE20164_Metadata_Serializer(dataset_8,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_9 = Parkinson_9_GSE20168_Metadata_Serializer(dataset_9,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_10 = Parkinson_10_GSE20291_Metadata_Serializer(dataset_10,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_11 = Parkinson_11_GSE20292_Metadata_Serializer(dataset_11,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_12 = Parkinson_12_GSE20314_Metadata_Serializer(dataset_12,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_13 = Parkinson_13_GSE20333_Metadata_Serializer(dataset_13,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        serialized_dataset_14 = Parkinson_14_GSE24378_Metadata_Serializer(dataset_14,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )

        return (14,[
                    {'studyId': 'GSE7621', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data},
                    {'studyId': 'GSE8397_U133A', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_2.data},
                    {'studyId': 'GSE8397_U133B', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_3.data},
                    {'studyId': 'GSE19587', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_4.data},
                    {'studyId': 'GSE20141', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_5.data},
                    {'studyId': 'GSE20146', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_6.data},
                    {'studyId': 'GSE20163', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_7.data},
                    {'studyId': 'GSE20164', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_8.data},
                    {'studyId': 'GSE20168', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_9.data},
                    {'studyId': 'GSE20291', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_10.data},
                    {'studyId': 'GSE20292', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_11.data},
                    {'studyId': 'GSE20314', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_12.data},
                    {'studyId': 'GSE20333', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_13.data},
                    {'studyId': 'GSE24378', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_14.data}
                    ]
                )
    elif disease == 'pituitary_adenoma':
        dataset_1 = Pituitary_1_GSE36314_Metadata.objects.all().order_by('sampleId')

        serialized_dataset_1 = Pituitary_1_GSE36314_Metadata_Serializer(dataset_1,
                                                                        fields=(
                                                                                
                                                                                ),
                                                                        many=True,
                                                                        exclude=True
                                                                        )
        return (1,[
                    {'studyId': 'GSE36314', 'numGroups': 1, 'groupChoices': [groupIchoices], 'data': serialized_dataset_1.data},
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
def single_protein_single_disease(request, geneName, disease):
    geneName = geneName.upper()
    disease = disease.lower()
    if disease in disease_list:
        metadata_length, metadata = get_metadata_objects(disease)
        data_length, data = get_objects(disease=disease, geneName=geneName)
        return JsonResponse({'geneName': geneName, 'disease': disease, 'data': data, 'metadata':metadata})
    else:
        return JsonResponse({'message': f'The disease: "{disease}" does not exist in BDTM Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def single_protein_all_data(request, geneName):
    data_list = []
    geneName = geneName.upper()
    for disease in disease_list:
        metadata_length, metadata = get_metadata_objects(disease)
        data_length, data = get_objects(disease=disease, geneName=geneName)
        data_list.append({'disease': disease, 'diseaseData': data, 'diseaseMetadata':metadata})
    
    return JsonResponse({'geneName': geneName, 'data': data_list})


@api_view(['GET'])
def single_gene_pvalue(request, geneName):
    geneName = geneName.upper()
    try:
        dataset = P_Value.objects.filter(geneName=geneName)
    except:
        dataset = None
    serialized_dataset = P_Value_Serializer(dataset, many=True)
    return JsonResponse({'geneName': geneName, 'data': serialized_dataset.data})

