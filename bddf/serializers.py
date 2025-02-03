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

# MOA Status from TTD Database
class TTD_MOA_Status_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TTD_MOA_Status
        fields = '__all__'

# IC50 Values from TTD Database
class TTD_IC50_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TTD_IC50
        fields = '__all__'

# Clue Database	
class CLUE_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CLUE
        fields = '__all__'
	
# Stitch Database
class Stitch_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Stitch
        fields = '__all__'
	
# Chembl Database
class Chembl_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Chembl
        fields = '__all__'

# Drug Names Database
class Drug_Serializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Drug_Names_Smiles
        fields = '__all__'
	
# BDDF Disease
class BDDF_Disease_Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = BDDF_Disease
		fields = '__all__'

# Alzheimer's Disease
class D000544Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D000544
		fields = '__all__'

# Amyotrophic Lateral Sclerosis
class D000690Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D000690
		fields = '__all__'

# Frontotemporal Lobar Degeneration
class D057174Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D057174
		fields = '__all__'

# Glioblastoma
class D005909Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D005909
		fields = '__all__'

# Glioma
class D005910Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D005910
		fields = '__all__'

# Huntington's Disease
class D006816Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D006816
		fields = '__all__'

# Medulloblastoma
class D008527Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D008527
		fields = '__all__'

# Meningioma
class D008579Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D008579
		fields = '__all__'

# Multiple Sclerosis
class D009103Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D009103
		fields = '__all__'

# Parkinson's Disease
class D010300Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D010300
		fields = '__all__'

# Pituitary Adenoma
class D049912Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D049912
		fields = '__all__'