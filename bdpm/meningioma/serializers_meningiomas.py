from rest_framework import serializers
from .models_meningiomas import *
from ibpm.serializers import DynamicFieldsModelSerializer

class Meningioma_1_PXD007073_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Meningioma_1_PXD007073
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25',)

class Meningioma_1_PXD007073_Metadata_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Meningioma_1_PXD007073_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI', 'groupII', 'groupIII', 'groupIV',)

class Meningioma_2_PXD014852_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Meningioma_2_PXD014852
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29',)

class Meningioma_2_PXD014852_Metadata_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Meningioma_2_PXD014852_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI', 'groupII',)
