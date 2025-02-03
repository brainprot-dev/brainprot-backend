from rest_framework import serializers
from .models_Amyotrophic_Lateral_Sclerosis import *
from ibpm.serializers import DynamicFieldsModelSerializer

class Amyotrophic_Lateral_Sclerosis_1_PXD021630_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Amyotrophic_Lateral_Sclerosis_1_PXD021630
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20',)

# class Amyotrophic_Lateral_Sclerosis_1_PXD021630_Unprocessed_Serializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Amyotrophic_Lateral_Sclerosis_1_PXD021630_Unprocessed
#         fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25',)

class Amyotrophic_Lateral_Sclerosis_1_PXD021630_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display(),]
        return groupInformation

    class Meta:
        model = Amyotrophic_Lateral_Sclerosis_1_PXD021630_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')

# class Amyotrophic_Lateral_Sclerosis_2_PXD014852_Serializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Amyotrophic_Lateral_Sclerosis_2_PXD014852
#         fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29',)
        #fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29','S1_Raw','S2_Raw','S3_Raw','S4_Raw','S5_Raw','S6_Raw','S7_Raw','S8_Raw','S9_Raw','S10_Raw','S11_Raw','S12_Raw','S13_Raw','S14_Raw','S15_Raw','S16_Raw','S17_Raw','S18_Raw','S19_Raw','S20_Raw','S21_Raw','S22_Raw','S23_Raw','S24_Raw','S25_Raw','S26_Raw','S27_Raw','S28_Raw','S29_Raw')

# class Amyotrophic_Lateral_Sclerosis_2_PXD014852_Unprocessed_Serializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Amyotrophic_Lateral_Sclerosis_2_PXD014852_Unprocessed
#         fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29',)

# class Amyotrophic_Lateral_Sclerosis_2_PXD014852_Metadata_Serializer(DynamicFieldsModelSerializer):
#     groupInformation = serializers.SerializerMethodField()

#     def get_groupInformation(self, obj):
#         # Database only stores the integer
#         # We get its label
#         groupInformation = [obj.get_groupI_display(), obj.get_groupII_display()]
#         return groupInformation
        
#     class Meta:
#         model = Amyotrophic_Lateral_Sclerosis_2_PXD014852_Metadata
#         fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')


# class Amyotrophic_Lateral_Sclerosis_3_PXD012923_Serializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Amyotrophic_Lateral_Sclerosis_3_PXD012923
#         fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25','S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35','S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45','S46', 'S47', 'S48', 'S49', 'S50', 'S51', 'S52', 'S53', 'S54', 'S55','S56', 'S57', 'S58', 'S59', 'S60', 'S61', 'S62', 'S63', 'S64', 'S65',)

# class Amyotrophic_Lateral_Sclerosis_3_PXD012923_Unprocessed_Serializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Amyotrophic_Lateral_Sclerosis_3_PXD012923_Unprocessed
#         fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25','S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35','S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45','S46', 'S47', 'S48', 'S49', 'S50', 'S51', 'S52', 'S53', 'S54', 'S55','S56', 'S57', 'S58', 'S59', 'S60', 'S61', 'S62', 'S63', 'S64', 'S65',)

# class Amyotrophic_Lateral_Sclerosis_3_PXD012923_Metadata_Serializer(DynamicFieldsModelSerializer):
#     groupInformation = serializers.SerializerMethodField()

#     def get_groupInformation(self, obj):
#         # Database only stores the integer
#         # We get its label
#         groupInformation = [obj.get_groupI_display(), obj.get_groupII_display(), obj.get_groupIII_display()]
#         return groupInformation

#     class Meta:
#         model = Amyotrophic_Lateral_Sclerosis_3_PXD012923_Metadata
#         fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')