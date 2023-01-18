from rest_framework import serializers
from .models import *
from ibpm.serializers import DynamicFieldsModelSerializer

class DiseaseSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Disease
        fields = ('diseaseName', 'DisGeNetDiseaseId', 'numGeneDisGeNet', 'numGeneHarmonizome',)