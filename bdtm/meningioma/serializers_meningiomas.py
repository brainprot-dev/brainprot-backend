from rest_framework import serializers
from .models_meningiomas import *
from ibpm.serializers import DynamicFieldsModelSerializer

class Meningioma_1_GSE43290_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Meningioma_1_GSE43290
        fields = '__all__' #Shortcut to add all fields

class Meningioma_1_GSE43290_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display(), obj.get_groupII_display()]
        return groupInformation

    class Meta:
        model = Meningioma_1_GSE43290_Metadata
        fields = '__all__' #Shortcut to add all fields

class Meningioma_2_GSE54934_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Meningioma_2_GSE54934
        fields = '__all__' #Shortcut to add all fields

class Meningioma_2_GSE54934_Metadata_Serializer(DynamicFieldsModelSerializer):
    groupInformation = serializers.SerializerMethodField()

    def get_groupInformation(self, obj):
        # Database only stores the integer
        # We get its label
        groupInformation = [obj.get_groupI_display(), obj.get_groupII_display()]
        return groupInformation

    class Meta:
        model = Meningioma_2_GSE54934_Metadata
        fields = '__all__' #Shortcut to add all fields
