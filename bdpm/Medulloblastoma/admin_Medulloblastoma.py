from django.contrib import admin
from .models_Medulloblastoma import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# # # # # # # # # # # # # # # # # # # 
# Medulloblastoma 1
# # # # # # # # # # # # # # # # # # # 

class Medulloblastoma_1_PXD014950_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Medulloblastoma_1_PXD014950
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', )
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Medulloblastoma_1_PXD014950_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Medulloblastoma_1_PXD014950_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']

class Medulloblastoma_1_PXD014950_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Medulloblastoma_1_PXD014950_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Medulloblastoma_1_PXD014950_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Medulloblastoma_1_PXD014950_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['sampleId', 'sourceName']
