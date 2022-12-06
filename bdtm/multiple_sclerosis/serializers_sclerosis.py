from rest_framework import serializers
from .models_sclerosis import *
from ibpm.serializers import DynamicFieldsModelSerializer

class Multiple_Sclerosis_1_GSE38010_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Multiple_Sclerosis_1_GSE38010
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',)

class Multiple_Sclerosis_1_GSE38010_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Multiple_Sclerosis_1_GSE38010_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupInformation')

class Multiple_Sclerosis_2_GSE52139_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Multiple_Sclerosis_2_GSE52139
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16',)

class Multiple_Sclerosis_2_GSE52139_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Multiple_Sclerosis_2_GSE52139_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Multiple_Sclerosis_3_GSE83670_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Multiple_Sclerosis_3_GSE83670
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',)

class Multiple_Sclerosis_3_GSE83670_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Multiple_Sclerosis_3_GSE83670_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupInformation')
