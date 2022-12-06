from rest_framework import serializers
from .models_parkinson import *
from ibpm.serializers import DynamicFieldsModelSerializer

class Parkinson_1_GSE7621_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_1_GSE7621
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25',)

class Parkinson_1_GSE7621_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_1_GSE7621_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupInformation')

class Parkinson_2_GSE8397_U133A_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_2_GSE8397_U133A
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45', 'S46', 'S47')

class Parkinson_2_GSE8397_U133A_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_2_GSE8397_U133A_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Parkinson_3_GSE8397_U133B_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_3_GSE8397_U133B
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45', 'S46', 'S47')

class Parkinson_3_GSE8397_U133B_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_3_GSE8397_U133B_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Parkinson_4_GSE19587_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_4_GSE19587
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22',)

class Parkinson_4_GSE19587_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_4_GSE19587_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Parkinson_5_GSE20141_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_5_GSE20141
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18')

class Parkinson_5_GSE20141_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_5_GSE20141_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupInformation')

class Parkinson_6_GSE20146_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_6_GSE20146
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20')

class Parkinson_6_GSE20146_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_6_GSE20146_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Parkinson_7_GSE20163_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_7_GSE20163
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17')

class Parkinson_7_GSE20163_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_7_GSE20163_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'age', 'groupInformation')

class Parkinson_8_GSE20164_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_8_GSE20164
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11')

class Parkinson_8_GSE20164_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_8_GSE20164_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Parkinson_9_GSE20168_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_9_GSE20168
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29')

class Parkinson_9_GSE20168_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_9_GSE20168_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Parkinson_10_GSE20291_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_10_GSE20291
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35')

class Parkinson_10_GSE20291_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_10_GSE20291_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Parkinson_11_GSE20292_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_11_GSE20292
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29')

class Parkinson_11_GSE20292_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_11_GSE20292_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Parkinson_12_GSE20314_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_12_GSE20314
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8')

class Parkinson_12_GSE20314_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_12_GSE20314_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Parkinson_13_GSE20333_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_13_GSE20333
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12')

class Parkinson_13_GSE20333_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_13_GSE20333_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupInformation')

class Parkinson_14_GSE24378_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson_14_GSE24378
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17')

class Parkinson_14_GSE24378_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display()]
        return groupInformation
        
    class Meta:
        model = Parkinson_14_GSE24378_Metadata
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupInformation')
