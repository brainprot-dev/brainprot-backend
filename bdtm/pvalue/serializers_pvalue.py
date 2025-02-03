from rest_framework import serializers
from .models_pvalue import *

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

class P_Value_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = P_Value
        fields = '__all__'