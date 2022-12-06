from rest_framework import serializers
from .models_als import *
from ibpm.serializers import DynamicFieldsModelSerializer

class ALS_1_GSE19332_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ALS_1_GSE19332
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',)  

class ALS_1_GSE19332_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = ALS_1_GSE19332_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupInformation')

class ALS_2_GSE20589_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ALS_2_GSE20589
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',)

class ALS_2_GSE20589_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = ALS_2_GSE20589_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupInformation')

class ALS_3_GSE68605_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ALS_3_GSE68605
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11',)

class ALS_3_GSE68605_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = ALS_3_GSE68605_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupInformation')