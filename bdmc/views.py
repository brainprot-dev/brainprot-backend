from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .models import *
from .serializers import *
# Create your views here.

database = [
    'Bionda',
    'Harmonizome',
    'Pubpular',
    'Disgenet'
]

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

def get_objects(disease, geneName):
    if disease == 'als':
        try:
            dataset = Amyotrophic_Lateral_Sclerosis.objects.get(geneName=geneName)
        except:
            dataset = None
       
        serialized_dataset = AmyotrophicSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                    )

        return (
                    {'Scores': serialized_dataset.data},
                )

    elif disease == 'alzheimer':
        try:
            dataset = Alzheimer.objects.get(geneName=geneName)
        except:
            dataset = None

        serialized_dataset = AlzheimerSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                        )

        return (
                    {'Scores': serialized_dataset.data},
                )
    elif disease == 'ftld':
        try:
            dataset = Frontotemporal.objects.get(geneName=geneName)
        except:
            dataset = None

        serialized_dataset = FrontotemporalSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                        )

        return (
                    {'Scores': serialized_dataset.data},
                )
    elif disease == 'glioblastoma':
        try:
            dataset = Glioblastoma.objects.get(geneName=geneName)
        except:
            dataset = None

        serialized_dataset = GlioblastomaSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                        )

        return (
                    {'Scores': serialized_dataset.data},
                )
    elif disease == 'glioma':
        try:
            dataset = Glioma.objects.get(geneName=geneName)
        except:
            dataset = None

        serialized_dataset = GliomaSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                        )

        return (
                    {'Scores': serialized_dataset.data},
                )
    elif disease == 'huntington':
        try:
            dataset = Huntington.objects.get(geneName=geneName)
        except:
            dataset = None

        serialized_dataset = HuntingtonSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                        )

        return (
                    {'Scores': serialized_dataset.data},
                )
    elif disease == 'medulloblastoma':
        try:
            dataset = Medulloblastoma.objects.get(geneName=geneName)
        except:
            dataset = None

        serialized_dataset = MedulloblastomaSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                        )

        return (
                    {'Scores': serialized_dataset.data},
                )
    elif disease == 'meningioma':
        try:
            dataset = Meningioma.objects.get(geneName=geneName)
        except:
            dataset = None

        serialized_dataset = MeningiomaSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                        )

        return (
                    {'Scores': serialized_dataset.data},
                )
    elif disease == 'multiple_sclerosis':
        try:
            dataset = Multiple_Sclerosis.objects.get(geneName=geneName)
        except:
            dataset = None

        serialized_dataset = MultipleSclerosisSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                        )

        return (
                    {'Scores': serialized_dataset.data},
                )
    elif disease == 'parkinson':
        try:
            dataset = Parkinson.objects.get(geneName=geneName)
        except:
            dataset = None

        serialized_dataset = ParkinsonSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                        )

        return (
                    {'Scores': serialized_dataset.data},
                )
    elif disease == 'pituitary_adenoma':
        try:
            dataset = Pituitary_Adenoma.objects.get(geneName=geneName)
        except:
            dataset = None

        serialized_dataset = PituitaryAdenomaSerializer(dataset,
                                                        fields=(
                                                                'geneName'
                                                                ),
                                                        exclude=True,
                                                        )

        return (
                    {'Scores': serialized_dataset.data},
                )
    
@api_view(['GET'])
def single_gene_single_disease(request, geneName, disease):
    geneName = geneName.upper()
    disease = disease.lower()
    if disease in disease_list:
        data = get_objects(disease=disease, geneName=geneName)
        return JsonResponse({'geneName': geneName, 'disease': disease, 'data': data})
    else:
        return JsonResponse({'message': f'The disease: "{disease}" does not exist in BDMC Database or the query is malformed. Please refer to https://brainprot.org/api for help.'},
                            status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def single_gene_all_data(request, geneName):
    data_list = []
    geneName = geneName.upper()
    for disease in disease_list:
        data = get_objects(disease=disease, geneName=geneName)
        data_list.append({'disease': disease, 'diseaseData': data})
    
    return JsonResponse({'geneName': geneName, 'data': data_list})