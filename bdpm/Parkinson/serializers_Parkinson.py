from rest_framework import serializers
from .models_Parkinson import *
from ibpm.serializers import DynamicFieldsModelSerializer

class Parkinson_1_PXD008036_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_1_PXD008036
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', )

class Parkinson_1_PXD008036_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Parkinson_1_PXD008036_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')

class Parkinson_2_PXD022092_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_2_PXD022092
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',)

class Parkinson_2_PXD022092_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_2_PXD022092_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')


class Parkinson_3_PXD024998_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_3_PXD024998
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', )

class Parkinson_3_PXD024998_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Parkinson_3_PXD024998_Metadata
        fields = ('sourceName', 'sampleId', 'gender', 'age', 'groupInformation')
