from rest_framework import serializers
from .models_pituitary import *
from ibpm.serializers import DynamicFieldsModelSerializer

class Pituitary_1_GSE36314_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Pituitary_1_GSE36314
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',)

class Pituitary_1_GSE36314_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Pituitary_1_GSE36314_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')
