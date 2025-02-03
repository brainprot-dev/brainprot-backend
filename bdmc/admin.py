from django.contrib import admin
from .models import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Register your models here.

# Alzheimer's Disease
class D000544_Resource(resources.ModelResource):
	class Meta:
		model = D000544
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D000544_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D000544_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Amyotrophic Lateral Sclerosis
class D000690_Resource(resources.ModelResource):
	class Meta:
		model = D000690
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D000690_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D000690_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Angelman Syndrome
class D017204_Resource(resources.ModelResource):
	class Meta:
		model = D017204
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D017204_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D017204_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Anxiety Disorder
class D001008_Resource(resources.ModelResource):
	class Meta:
		model = D001008
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D001008_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D001008_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Aphasia
class D001037_Resource(resources.ModelResource):
	class Meta:
		model = D001037
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D001037_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D001037_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Ataxia Telangiectasia
class D001260_Resource(resources.ModelResource):
	class Meta:
		model = D001260
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D001260_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D001260_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Attention deficit hyperactivity disorder
class D001289_Resource(resources.ModelResource):
	class Meta:
		model = D001289
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D001289_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D001289_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Autism Spectrum Disorder
class D000067877_Resource(resources.ModelResource):
	class Meta:
		model = D000067877
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D000067877_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D000067877_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Bipolar Disorder
class D001714_Resource(resources.ModelResource):
	class Meta:
		model = D001714
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D001714_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D001714_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Cerebral Infarction
class D002544_Resource(resources.ModelResource):
	class Meta:
		model = D002544
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D002544_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D002544_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Cerebral Ischemia/Transient Cerebral Ischemia
class D002545_Resource(resources.ModelResource):
	class Meta:
		model = D002545
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D002545_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D002545_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Cerebral Palsy
class D002547_Resource(resources.ModelResource):
	class Meta:
		model = D002547
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D002547_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D002547_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Creutzfeldt Jakob Disease
class D007562_Resource(resources.ModelResource):
	class Meta:
		model = D007562
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D007562_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D007562_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Dementia (Non-Alzheimer)
class D003704_Resource(resources.ModelResource):
	class Meta:
		model = D003704
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D003704_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D003704_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Down Syndrome
class D004314_Resource(resources.ModelResource):
	class Meta:
		model = D004314
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D004314_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D004314_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Dyslexia
class D004410_Resource(resources.ModelResource):
	class Meta:
		model = D004410
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D004410_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D004410_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Dystonia
class D004421_Resource(resources.ModelResource):
	class Meta:
		model = D004421
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D004421_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D004421_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Encephalitis
class D004660_Resource(resources.ModelResource):
	class Meta:
		model = D004660
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D004660_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D004660_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Encephalomyelitis
class D004679_Resource(resources.ModelResource):
	class Meta:
		model = D004679
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D004679_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D004679_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Epilepsy
class D004827_Resource(resources.ModelResource):
	class Meta:
		model = D004827
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D004827_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D004827_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Essential Tremor
class D020329_Resource(resources.ModelResource):
	class Meta:
		model = D020329
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D020329_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D020329_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Fragile X Syndrome
class D005600_Resource(resources.ModelResource):
	class Meta:
		model = D005600
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D005600_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D005600_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Friedreich Ataxia
class D005621_Resource(resources.ModelResource):
	class Meta:
		model = D005621
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D005621_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D005621_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Frontotemporal Dementia
class D057180_Resource(resources.ModelResource):
	class Meta:
		model = D057180
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D057180_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D057180_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Frontotemporal Lobar Degeneration
class D057174_Resource(resources.ModelResource):
	class Meta:
		model = D057174
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D057174_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D057174_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Gaucher Disease
class D005776_Resource(resources.ModelResource):
	class Meta:
		model = D005776
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D005776_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D005776_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Gilles De La Tourette Syndrome
class D005879_Resource(resources.ModelResource):
	class Meta:
		model = D005879
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D005879_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D005879_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Glioblastoma
class D005909_Resource(resources.ModelResource):
	class Meta:
		model = D005909
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D005909_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D005909_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Glioma
class D005910_Resource(resources.ModelResource):
	class Meta:
		model = D005910
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D005910_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D005910_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Huntington's Disease
class D006816_Resource(resources.ModelResource):
	class Meta:
		model = D006816
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D006816_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D006816_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Hydrocephalus
class D006849_Resource(resources.ModelResource):
	class Meta:
		model = D006849
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D006849_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D006849_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Intellectual Disability
class D008607_Resource(resources.ModelResource):
	class Meta:
		model = D008607
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D008607_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D008607_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Intracranial Aneurysm
class D002532_Resource(resources.ModelResource):
	class Meta:
		model = D002532
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D002532_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D002532_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Medulloblastoma
class D008527_Resource(resources.ModelResource):
	class Meta:
		model = D008527
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D008527_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D008527_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Meningitis
class D008581_Resource(resources.ModelResource):
	class Meta:
		model = D008581
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D008581_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D008581_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Meningioma
class D008579_Resource(resources.ModelResource):
	class Meta:
		model = D008579
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score','BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D008579_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D008579_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Motor Neurone Disease
class D016472_Resource(resources.ModelResource):
	class Meta:
		model = D016472
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D016472_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D016472_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Multiple Sclerosis
class D009103_Resource(resources.ModelResource):
	class Meta:
		model = D009103
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D009103_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D009103_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Muscular Dystrophy
class D009136_Resource(resources.ModelResource):
	class Meta:
		model = D009136
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D009136_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D009136_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# narcolepsy
class D009290_Resource(resources.ModelResource):
	class Meta:
		model = D009290
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D009290_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D009290_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Neurilemmoma
class D009442_Resource(resources.ModelResource):
	class Meta:
		model = D009442
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D009442_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D009442_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Neuroblastoma
class D009447_Resource(resources.ModelResource):
	class Meta:
		model = D009447
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D009447_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D009447_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Neuroendocrine Tumor
class D018358_Resource(resources.ModelResource):
	class Meta:
		model = D018358
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D018358_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D018358_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Neurofibromatosis
class D017253_Resource(resources.ModelResource):
	class Meta:
		model = D017253
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D017253_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D017253_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Panic Disorder
class D016584_Resource(resources.ModelResource):
	class Meta:
		model = D016584
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D016584_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D016584_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Paraganglioma
class D010235_Resource(resources.ModelResource):
	class Meta:
		model = D010235
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D010235_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D010235_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Parkinson's Disease
class D010300_Resource(resources.ModelResource):
	class Meta:
		model = D010300
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D010300_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D010300_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Pituitary Adenoma
class D049912_Resource(resources.ModelResource):
	class Meta:
		model = D049912
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D049912_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D049912_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Plexiform Neurofibroma
class D018318_Resource(resources.ModelResource):
	class Meta:
		model = D018318
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D018318_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D018318_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Post-traumatic Stress Disorder
class D013313_Resource(resources.ModelResource):
	class Meta:
		model = D013313
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D013313_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D013313_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Prader-Willi Syndrome
class D011218_Resource(resources.ModelResource):
	class Meta:
		model = D011218
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D011218_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D011218_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Prion Disease
class D017096_Resource(resources.ModelResource):
	class Meta:
		model = D017096
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D017096_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D017096_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Rett Syndrome
class D015518_Resource(resources.ModelResource):
	class Meta:
		model = D015518
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D015518_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D015518_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Schizophrenia
class D012559_Resource(resources.ModelResource):
	class Meta:
		model = D012559
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D012559_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D012559_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Tay-Sachs Disease
class D013661_Resource(resources.ModelResource):
	class Meta:
		model = D013661
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D013661_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D013661_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']


# Tuberous Sclerosis
class D014402_Resource(resources.ModelResource):
	class Meta:
		model = D014402
		fields = ('SwissProt_Accessions', 'geneName', 'DISGENET_Score', 'Harmonizome_Score', 'Pubpular_Score', 'CTD_Score', 'D2_Score', 'DH_Score', 'DP_Score', 'DC_Score', 'HP_Score', 'HC_Score', 'PC_Score', 'D2D_Score', 'D2H_Score', 'D2P_Score', 'D2C_Score', 'BDMC_Score', 'Frequency', 'CTD_Marker', 'eDGAR_Marker', 'BIONDA_Marker', 'Dis_2_Marker')
		import_id_fields = ('geneName',)
		skip_unchanged = True
		report_skipped = True

class D014402_Admin(ImportExportMixin, admin.ModelAdmin):
	resource_class = D014402_Resource
	list_display = ('geneName',)
	search_fields = ['geneName']

admin.site.register(D000544, D000544_Admin)
admin.site.register(D000690, D000690_Admin)
admin.site.register(D017204, D017204_Admin)
admin.site.register(D001008, D001008_Admin)
admin.site.register(D001037, D001037_Admin)
admin.site.register(D001260, D001260_Admin)
admin.site.register(D001289, D001289_Admin)
admin.site.register(D000067877, D000067877_Admin)
admin.site.register(D001714, D001714_Admin)
admin.site.register(D002544, D002544_Admin)
admin.site.register(D002545, D002545_Admin)
admin.site.register(D002547, D002547_Admin)
admin.site.register(D007562, D007562_Admin)
admin.site.register(D003704, D003704_Admin)
admin.site.register(D004314, D004314_Admin)
admin.site.register(D004410, D004410_Admin)
admin.site.register(D004421, D004421_Admin)
admin.site.register(D004660, D004660_Admin)
admin.site.register(D004679, D004679_Admin)
admin.site.register(D004827, D004827_Admin)
admin.site.register(D020329, D020329_Admin)
admin.site.register(D005600, D005600_Admin)
admin.site.register(D005621, D005621_Admin)
admin.site.register(D057180, D057180_Admin)
admin.site.register(D057174, D057174_Admin)
admin.site.register(D005776, D005776_Admin)
admin.site.register(D005879, D005879_Admin)
admin.site.register(D005909, D005909_Admin)
admin.site.register(D005910, D005910_Admin)
admin.site.register(D006816, D006816_Admin)
admin.site.register(D006849, D006849_Admin)
admin.site.register(D008607, D008607_Admin)
admin.site.register(D002532, D002532_Admin)
admin.site.register(D008527, D008527_Admin)
admin.site.register(D008581, D008581_Admin)
admin.site.register(D008579, D008579_Admin)
admin.site.register(D016472, D016472_Admin)
admin.site.register(D009103, D009103_Admin)
admin.site.register(D009136, D009136_Admin)
admin.site.register(D009290, D009290_Admin)
admin.site.register(D009442, D009442_Admin)
admin.site.register(D009447, D009447_Admin)
admin.site.register(D018358, D018358_Admin)
admin.site.register(D017253, D017253_Admin)
admin.site.register(D016584, D016584_Admin)
admin.site.register(D010235, D010235_Admin)
admin.site.register(D010300, D010300_Admin)
admin.site.register(D049912, D049912_Admin)
admin.site.register(D018318, D018318_Admin)
admin.site.register(D013313, D013313_Admin)
admin.site.register(D011218, D011218_Admin)
admin.site.register(D017096, D017096_Admin)
admin.site.register(D015518, D015518_Admin)
admin.site.register(D012559, D012559_Admin)
admin.site.register(D013661, D013661_Admin)
admin.site.register(D014402, D014402_Admin)

