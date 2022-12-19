from rest_framework import serializers
from .models import *

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    
    Taken from Django REST Framework Documentation
    https://www.django-rest-framework.org/api-guide/serializers/#example
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        # Don't pass the 'exclude' arg up to the superclass
        exclude = kwargs.pop('exclude', None)
        
        '''
        Note: The exclude mode works well only if you have
              set all the fields to be included in serializer
              otherwise this may break!
              (Untested)
        '''
        if exclude is None:
            exclude = False
        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None and exclude is False:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        elif fields is not None and exclude is True:
            disallowed = [fields]
            for field_name in disallowed:
                self.fields.pop(field_name)

class AlzheimerSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Alzheimer
        fields = '__all__'

class AmyotrophicSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Amyotrophic_Lateral_Sclerosis
        fields = '__all__'

class MeningiomaSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Meningioma
        fields = '__all__'

class GliomaSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Glioma
        fields = '__all__'

class GlioblastomaSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Glioblastoma
        fields = '__all__'

class MedulloblastomaSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Medulloblastoma
        fields = '__all__'

class PituitaryAdenomaSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Pituitary_Adenoma
        fields = '__all__'

class ParkinsonSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Parkinson
        fields = '__all__'

class HuntingtonSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Huntington
        fields = '__all__'

class MultipleSclerosisSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Multiple_Sclerosis
        fields = '__all__'

class FrontotemporalSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Frontotemporal
        fields = '__all__'

