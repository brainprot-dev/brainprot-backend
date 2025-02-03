from django.contrib import admin
from .models_Parkinson import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# # # # # # # # # # # # # # # # # # # 
# Parkinson 1
# # # # # # # # # # # # # # # # # # # 

class Parkinson_1_PXD008036_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_1_PXD008036
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', )
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Parkinson_1_PXD008036_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_1_PXD008036_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Parkinson_1_PXD008036_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_1_PXD008036_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Parkinson_1_PXD008036_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_1_PXD008036_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['sampleId', 'sourceName']


# # # # # # # # # # # # # # # # # # # 
# Parkinson 2
# # # # # # # # # # # # # # # # # # # 

class Parkinson_2_PXD022092_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_2_PXD022092
        # Fields useful for import and export
        #fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29','S1_Raw','S2_Raw','S3_Raw','S4_Raw','S5_Raw','S6_Raw','S7_Raw','S8_Raw','S9_Raw','S10_Raw','S11_Raw','S12_Raw','S13_Raw','S14_Raw','S15_Raw','S16_Raw','S17_Raw','S18_Raw','S19_Raw','S20_Raw','S21_Raw','S22_Raw','S23_Raw','S24_Raw','S25_Raw','S26_Raw','S27_Raw','S28_Raw','S29_Raw')
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',)
        
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Parkinson_2_PXD022092_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_2_PXD022092_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']

class Parkinson_2_PXD022092_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_2_PXD022092_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Parkinson_2_PXD022092_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_2_PXD022092_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['sampleId', 'sourceName']


# # # # # # # # # # # # # # # # # # # 
# Parkinson 3
# # # # # # # # # # # # # # # # # # # 

class Parkinson_3_PXD024998_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_3_PXD024998
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Parkinson_3_PXD024998_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_3_PXD024998_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']

class Parkinson_3_PXD024998_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_3_PXD024998_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'gender', 'age', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Parkinson_3_PXD024998_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_3_PXD024998_Metadata_Resource

    list_display = ('sourceName','sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['sampleId', 'sourceName']
