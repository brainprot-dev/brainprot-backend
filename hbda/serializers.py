from rest_framework import serializers
from .models import *
from ibpm.serializers import DynamicFieldsModelSerializer

class DiseaseSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Disease
        fields =('diseaseName', 'MESHID', 'umlsId', 'diseaseOntology', 'NCI', 'GARD', 'KEGG', 'HPO', 'monarchInitiative', 'MedGenUID', 'orphanet', 'OMIM', 'description')