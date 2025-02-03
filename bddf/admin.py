from django.contrib import admin
from .models import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Register your models here.

class TTD_MOA_Status_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = TTD_MOA_Status
        # Fields useful for import and export
        fields = ('TargetID', 'DrugID', 'Highest_Status', 'MOA', 'Smiles_ID', 'UniprotID')

        # Fields which will be useful for object identification during import
        import_id_fields = ('UniprotID', 'DrugID')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class TTD_MOA_Status_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = TTD_MOA_Status_Resource
    list_display = ('UniprotID','DrugID')
    search_fields = ['UniprotID', 'DrugID']

class TTD_IC50_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = TTD_IC50
        # Fields useful for import and export
        fields = ('TargetID', 'DrugID', 'UniprotID', 'Smiles_ID', 'Activity_IC50')

        # Fields which will be useful for object identification during import
        import_id_fields = ('UniprotID', 'DrugID')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class TTD_IC50_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = TTD_IC50_Resource
    list_display = ('UniprotID','DrugID')
    search_fields = ['UniprotID', 'DrugID']

class CLUE_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = CLUE
        # Fields useful for import and export
        fields = ('Chembl_ID', 'Smiles_ID', 'Drug_Name', 'Clinical_Phase', 'MOA', "UniprotID")

        # Fields which will be useful for object identification during import
        import_id_fields = ('UniprotID', 'Drug_Name')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class CLUE_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = CLUE_Resource
    list_display = ('UniprotID','Drug_Name')
    search_fields = ['UniprotID', 'Drug_Name']

class Stitch_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Stitch
        # Fields useful for import and export
        fields = ('Chemical_ID', 'Protein_ID', 'Combined_Score', 'Smiles_ID', 'UniprotID')

        # Fields which will be useful for object identification during import
        import_id_fields = ('UniprotID', 'Smiles_ID')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Stitch_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Stitch_Resource
    list_display = ('UniprotID','Smiles_ID')
    search_fields = ['UniprotID', 'Smiles_ID']
    
class Chembl_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Chembl
        # Fields useful for import and export
        fields = ('Chembl_ID', 'UniprotID', 'Smiles_ID', 'Investigation', 'MOA', 'Toxicity', 'pIC50', 'Clue_MOA', 'Clinical_Phase')

        # Fields which will be useful for object identification during import
        import_id_fields = ('UniprotID', 'Chembl_ID')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Chembl_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Chembl_Resource
    list_display = ('UniprotID','Chembl_ID')
    search_fields = ['UniprotID', 'Chembl_ID']
    
class Drug_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Drug_Names_Smiles
        # Fields useful for import and export
        fields = ('Drug_Name', 'CNS', 'Smiles_ID')

        # Fields which will be useful for object identification during import
        import_id_fields = ('Drug_Name', 'Smiles_ID')
        # This will allow to skip unchanged entries
        skip_unchanged = True 
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Drug_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Drug_Resource
    list_display = ('Drug_Name', 'Smiles_ID')
    search_fields = ['Drug_Name', 'Smiles_ID']
    
class BDDF_Disease_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = BDDF_Disease
        # Fields useful for import and export
        fields = ('diseaseName', 'MESHID')

        # Fields which will be useful for object identification during import
        import_id_fields = ('diseaseName', 'MESHID')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class BDDF_Disease_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = BDDF_Disease_Resource
    list_display = ('diseaseName', 'MESHID')
    search_fields = ['diseaseName', 'MESHID']

# Alzheimer's Disease
class D000544_Resource(resources.ModelResource):
	class Meta:
		model = D000544
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		skip_unchanged = True
		report_skipped = True

class D000544_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D000544_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


# Amyotrophic Lateral Sclerosis
class D000690_Resource(resources.ModelResource):
	class Meta:
		model = D000690
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		# import_id_fields = ('ID')
		skip_unchanged = True
		report_skipped = True

class D000690_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D000690_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


# Frontotemporal Lobar Degeneration
class D057174_Resource(resources.ModelResource):
	class Meta:
		model = D057174
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		# import_id_fields = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source')
		skip_unchanged = True
		report_skipped = True

class D057174_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D057174_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


# Glioblastoma
class D005909_Resource(resources.ModelResource):
	class Meta:
		model = D005909
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		# import_id_fields = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source')
		skip_unchanged = True
		report_skipped = True

class D005909_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D005909_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


# Glioma
class D005910_Resource(resources.ModelResource):
	class Meta:
		model = D005910
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		# import_id_fields = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source')
		skip_unchanged = True
		report_skipped = True

class D005910_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D005910_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


# Huntington's Disease
class D006816_Resource(resources.ModelResource):
	class Meta:
		model = D006816
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		# import_id_fields = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source')
		skip_unchanged = True
		report_skipped = True

class D006816_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D006816_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


# Medulloblastoma
class D008527_Resource(resources.ModelResource):
	class Meta:
		model = D008527
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		# import_id_fields = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source')
		skip_unchanged = True
		report_skipped = True

class D008527_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D008527_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


# Meningioma
class D008579_Resource(resources.ModelResource):
	class Meta:
		model = D008579
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		# import_id_fields = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source')
		skip_unchanged = True
		report_skipped = True

class D008579_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D008579_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


# Multiple Sclerosis
class D009103_Resource(resources.ModelResource):
	class Meta:
		model = D009103
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		# import_id_fields = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source')
		skip_unchanged = True
		report_skipped = True

class D009103_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D009103_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


# Parkinson's Disease
class D010300_Resource(resources.ModelResource):
	class Meta:
		model = D010300
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		# import_id_fields = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source')
		skip_unchanged = True
		report_skipped = True

class D010300_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D010300_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


# Pituitary Adenoma
class D049912_Resource(resources.ModelResource):
	class Meta:
		model = D049912
		fields = ('id', 'Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
		# import_id_fields = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source')
		skip_unchanged = True
		report_skipped = True

class D049912_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D049912_Resource
	list_display = ('Uniprot', 'Smiles', 'Score', 'MOA', 'Investigation', 'ChemblID', 'Toxicity', 'Drug_Name', 'clue_moa', 'clinical_phase', 'Source', 'pref_name', 'Gene_Name')
	search_fields = ['Uniprot', 'ChemblID', 'Source']


admin.site.register(D000544, D000544_Admin)
admin.site.register(D000690, D000690_Admin)
admin.site.register(D057174, D057174_Admin)
admin.site.register(D005909, D005909_Admin)
admin.site.register(D005910, D005910_Admin)
admin.site.register(D006816, D006816_Admin)
admin.site.register(D008527, D008527_Admin)
admin.site.register(D008579, D008579_Admin)
admin.site.register(D009103, D009103_Admin)
admin.site.register(D010300, D010300_Admin)
admin.site.register(D049912, D049912_Admin)
admin.site.register(TTD_MOA_Status, TTD_MOA_Status_Admin)
admin.site.register(TTD_IC50, TTD_IC50_Admin)
admin.site.register(CLUE, CLUE_Admin)
admin.site.register(Stitch, Stitch_Admin)
admin.site.register(Chembl, Chembl_Admin)
admin.site.register(Drug_Names_Smiles, Drug_Admin)
admin.site.register(BDDF_Disease, BDDF_Disease_Admin)