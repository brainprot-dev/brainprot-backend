from django.contrib import admin
from .models_medulloblastoma import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Register your models here.

# # # # # # # # # # # # # # # # # # # 
# Medulloblastoma
# # # # # # # # # # # # # # # # # # # 

class Medulloblastoma_1_GSE62600_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Medulloblastoma_1_GSE62600
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Medulloblastoma_1_GSE62600_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Medulloblastoma_1_GSE62600_Resource

    list_display = ('probeId','geneName')
    search_fields = ['geneName']

class Medulloblastoma_1_GSE62600_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Medulloblastoma_1_GSE62600_Metadata
        # Fields useful for import and export
        # TODO : Age not necessary?
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Medulloblastoma_1_GSE62600_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Medulloblastoma_1_GSE62600_Metadata_Resource

    list_display = ('accession','sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']