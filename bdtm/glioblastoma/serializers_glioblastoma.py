from rest_framework import serializers
from .models_glioblastoma import *
from ibpm.serializers import DynamicFieldsModelSerializer

class Glioblastoma_1_GSE13276_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Glioblastoma_1_GSE13276
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15',)

class Glioblastoma_1_GSE13276_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display(), obj.get_groupII_display()]
        return groupInformation

    class Meta:
        model = Glioblastoma_1_GSE13276_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupInformation')
