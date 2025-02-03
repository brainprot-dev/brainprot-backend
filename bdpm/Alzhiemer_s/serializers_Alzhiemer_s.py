from rest_framework import serializers
from .models_Alzhiemer_s import *
from ibpm.serializers import DynamicFieldsModelSerializer

class Alzhiemer_s_1_PXD009199_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Alzhiemer_s_1_PXD009199
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10')

class Alzhiemer_s_1_PXD009199_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Alzhiemer_s_1_PXD009199_Metadata
        fields = ('sourceName', 'sampleId', 'gender', 'age', 'groupInformation')



class Alzhiemer_s_2_PXD014376_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Alzhiemer_s_2_PXD014376
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18')

class Alzhiemer_s_2_PXD014376_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Alzhiemer_s_2_PXD014376_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')




class Alzhiemer_s_3_PXD037133_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Alzhiemer_s_3_PXD037133
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16')

class Alzhiemer_s_3_PXD037133_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Alzhiemer_s_3_PXD037133_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')

class Alzhiemer_s_4_PXD005319_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Alzhiemer_s_4_PXD005319
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', )

class Alzhiemer_s_4_PXD005319_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Alzhiemer_s_4_PXD005319_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')



class Alzhiemer_s_5_PXD005321_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Alzhiemer_s_5_PXD005321
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', )

class Alzhiemer_s_5_PXD005321_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:

        model = Alzhiemer_s_5_PXD005321_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')



""" class Alzhiemer_s_6_PXD021645_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Alzhiemer_s_6_PXD021645
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15',)

class Alzhiemer_s_6_PXD021645_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Alzhiemer_s_6_PXD021645_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')

 """

class Alzhiemer_s_7_PXD023199_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Alzhiemer_s_7_PXD023199
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18','S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25','S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35',)

# class Alzhiemer_s_3_PXD037133_Unprocessed_Serializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Alzhiemer_s_3_PXD037133_Unprocessed
#         fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25','S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35','S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45','S46', 'S47', 'S48', 'S49', 'S50', 'S51', 'S52', 'S53', 'S54', 'S55','S56', 'S57', 'S58', 'S59', 'S60', 'S61', 'S62', 'S63', 'S64', 'S65',)

class Alzhiemer_s_7_PXD023199_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Alzhiemer_s_7_PXD023199_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')





class Alzhiemer_s_8_PXD027173_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Alzhiemer_s_8_PXD027173
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25','S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35','S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45','S46', 'S47', 'S48', 'S49', 'S50', 'S51', 'S52', 'S53', 'S54', 'S55','S56', 'S57', 'S58',)

# class Alzhiemer_s_3_PXD037133_Unprocessed_Serializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = Alzhiemer_s_3_PXD037133_Unprocessed
#         fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25','S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35','S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45','S46', 'S47', 'S48', 'S49', 'S50', 'S51', 'S52', 'S53', 'S54', 'S55','S56', 'S57', 'S58', 'S59', 'S60', 'S61', 'S62', 'S63', 'S64', 'S65',)

class Alzhiemer_s_8_PXD027173_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation

    class Meta:
        model = Alzhiemer_s_8_PXD027173_Metadata
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupInformation')