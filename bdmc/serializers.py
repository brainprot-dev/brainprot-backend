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

# Angelman Syndrome
class D017204Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D017204
		fields = '__all__'

# Anxiety Disorder
class D001008Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D001008
		fields = '__all__'

# Aphasia
class D001037Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D001037
		fields = '__all__'

# Ataxia Telangiectasia
class D001260Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D001260
		fields = '__all__'

# Attention deficit hyperactivity disorder
class D001289Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D001289
		fields = '__all__'

# Autism Spectrum Disorder
class D000067877Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D000067877
		fields = '__all__'

# Bipolar Disorder
class D001714Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D001714
		fields = '__all__'

# Cerebral Infarction
class D002544Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D002544
		fields = '__all__'

# Cerebral Ischemia/Transient Cerebral Ischemia
class D002545Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D002545
		fields = '__all__'

# Cerebral Palsy
class D002547Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D002547
		fields = '__all__'

# Creutzfeldt Jakob Disease
class D007562Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D007562
		fields = '__all__'

# Dementia (Non-Alzheimer)
class D003704Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D003704
		fields = '__all__'

# Down Syndrome
class D004314Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D004314
		fields = '__all__'

# Dyslexia
class D004410Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D004410
		fields = '__all__'

# Dystonia
class D004421Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D004421
		fields = '__all__'

# Encephalitis
class D004660Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D004660
		fields = '__all__'

# Encephalomyelitis
class D004679Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D004679
		fields = '__all__'

# Epilepsy
class D004827Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D004827
		fields = '__all__'

# Essential Tremor
class D020329Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D020329
		fields = '__all__'

# Fragile X Syndrome
class D005600Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D005600
		fields = '__all__'

# Friedreich Ataxia
class D005621Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D005621
		fields = '__all__'

# Frontotemporal Dementia
class D057180Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D057180
		fields = '__all__'

# Frontotemporal Lobar Degeneration
class D057174Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D057174
		fields = '__all__'

# Gaucher Disease
class D005776Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D005776
		fields = '__all__'

# Gilles De La Tourette Syndrome
class D005879Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D005879
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

# Hydrocephalus
class D006849Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D006849
		fields = '__all__'

# Intellectual Disability
class D008607Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D008607
		fields = '__all__'

# Intracranial Aneurysm
class D002532Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D002532
		fields = '__all__'

# Medulloblastoma
class D008527Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D008527
		fields = '__all__'

# Meningitis
class D008581Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D008581
		fields = '__all__'

# Meningioma
class D008579Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D008579
		fields = '__all__'

# Motor Neurone Disease
class D016472Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D016472
		fields = '__all__'

# Multiple Sclerosis
class D009103Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D009103
		fields = '__all__'

# Muscular Dystrophy
class D009136Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D009136
		fields = '__all__'

# narcolepsy
class D009290Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D009290
		fields = '__all__'

# Neurilemmoma
class D009442Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D009442
		fields = '__all__'

# Neuroblastoma
class D009447Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D009447
		fields = '__all__'

# Neuroendocrine Tumor
class D018358Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D018358
		fields = '__all__'

# Neurofibromatosis
class D017253Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D017253
		fields = '__all__'

# Panic Disorder
class D016584Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D016584
		fields = '__all__'

# Paraganglioma
class D010235Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D010235
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

# Plexiform Neurofibroma
class D018318Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D018318
		fields = '__all__'

# Post-traumatic Stress Disorder
class D013313Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D013313
		fields = '__all__'

# Prader-Willi Syndrome
class D011218Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D011218
		fields = '__all__'

# Prion Disease
class D017096Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D017096
		fields = '__all__'

# Rett Syndrome
class D015518Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D015518
		fields = '__all__'

# Schizophrenia
class D012559Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D012559
		fields = '__all__'

# Tay-Sachs Disease
class D013661Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D013661
		fields = '__all__'

# Tuberous Sclerosis
class D014402Serializer(DynamicFieldsModelSerializer):
	class Meta:
		model = D014402
		fields = '__all__'
