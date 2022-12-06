from rest_framework import serializers
from .models_medulloblastoma import *
from ibpm.serializers import DynamicFieldsModelSerializer

class Medulloblastoma_1_GSE62600_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Medulloblastoma_1_GSE62600
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28',)

class Medulloblastoma_1_GSE62600_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Medulloblastoma_1_GSE62600_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')
