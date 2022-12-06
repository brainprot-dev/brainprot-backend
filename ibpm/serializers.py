from dataclasses import fields
from rest_framework import serializers
from ibpm.models import GeneProt, Protein, Peptide, PhosphoPeptide

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
            disallowed = set(fields)
            for field_name in disallowed:
                self.fields.pop(field_name)


# Create your Serializers here
class GeneProtSerializer(DynamicFieldsModelSerializer):
    full_chromosome = serializers.SerializerMethodField()
    #protein_peptide_serialized_data = serializers.SerializerMethodField()
    class Meta:
        model = GeneProt
        fields = '__all__' #Shortcut to add all fields

    def get_full_chromosome(self, obj):
        if obj.chromosome == 'M':
            return 'Mitochondrion'
        elif obj.chromosome == 'NA':
            return 'Not Applicable'
        elif obj.chromosome == '0':
            return 'Unplaced'
        else:
            return f'Chromosome {obj.chromosome}'
    
    def get_protein_peptide_serialized_data(self,obj):
        pass

class ProteinSerializer(DynamicFieldsModelSerializer):
    gene = serializers.SerializerMethodField()
    proteinNames = serializers.SerializerMethodField()
    proteinLength = serializers.SerializerMethodField()
    proteinMass = serializers.SerializerMethodField()
    chromosome = serializers.SerializerMethodField()

    class Meta:
        model = Protein
        fields = '__all__' #Shortcut to add all fields

    def get_gene(self, obj):
        # Database only stores the primary key of the foreign key model 
        # we try to get its attributes using the object itself
        # The thing is - while serializing, only primary key is searialized
        # but django stores the entire model object
        geneName = getattr(obj.geneProt, 'geneName')
        return geneName
    
    def get_proteinNames(self, obj):
        # Database only stores the primary key of the foreign key model 
        # we try to get its attributes using the object itself
        # The thing is - while serializing, only primary key is searialized
        # but django stores the entire model object
        proteinNames = getattr(obj.geneProt, 'geneProtFullNames')
        return proteinNames

    def get_proteinLength(self, obj):
        # Database only stores the primary key of the foreign key model 
        # we try to get its attributes using the object itself
        # The thing is - while serializing, only primary key is searialized
        # but django stores the entire model object
        proteinLength = getattr(obj.geneProt, 'protMass')
        return proteinLength

    def get_proteinMass(self, obj):
        # Database only stores the primary key of the foreign key model 
        # we try to get its attributes using the object itself
        # The thing is - while serializing, only primary key is searialized
        # but django stores the entire model object
        proteinMass = getattr(obj.geneProt, 'protLength')
        return proteinMass

    def get_chromosome(self, obj):
        # Database only stores the primary key of the foreign key model 
        # we try to get its attributes using the object itself
        # The thing is - while serializing, only primary key is searialized
        # but django stores the entire model object
        proteinMass = getattr(obj.geneProt, 'chromosome')
        return proteinMass

class PeptideSerializer(DynamicFieldsModelSerializer):
    gene = serializers.SerializerMethodField()
    protein = serializers.SerializerMethodField()

    class Meta:
        model = Peptide
        fields = '__all__' #Shortcut to add all fields

    def get_gene(self, obj):
        # Database only stores the primary key of the foreign key model 
        # we try to get its attributes using the object itself
        # The thing is - while serializing, only primary key is searialized
        # but django stores the entire model object
        geneName = getattr(obj.geneProt, 'geneName')
        return geneName

    def get_protein(self, obj):
        # Database only stores the primary key of the foreign key model 
        # we try to get its attributes using the object itself
        # The thing is - while serializing, only primary key is searialized
        # but django stores the entire model object
        protName = getattr(obj.geneProt, 'protName')
        return protName

class PhosphoPeptideSerializer(DynamicFieldsModelSerializer):
    gene = serializers.SerializerMethodField()
    protein = serializers.SerializerMethodField()

    class Meta:
        model = PhosphoPeptide
        fields = '__all__' #Shortcut to add all fields

    def get_gene(self, obj):
        # Database only stores the primary key of the foreign key model 
        # we try to get its attributes using the object itself
        # The thing is - while serializing, only primary key is searialized
        # but django stores the entire model object
        geneName = getattr(obj.geneProt, 'geneName')
        return geneName

    def get_protein(self, obj):
        # Database only stores the primary key of the foreign key model 
        # we try to get its attributes using the object itself
        # The thing is - while serializing, only primary key is searialized
        # but django stores the entire model object
        protName = getattr(obj.geneProt, 'protName')
        return protName

