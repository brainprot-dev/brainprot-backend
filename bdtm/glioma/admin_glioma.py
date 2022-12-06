from .models_glioma import *
from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# # # # # # # # # # # # # # # # # # # 
# Glioma
# # # # # # # # # # # # # # # # # # # 

class Glioma_1_GSE12657_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Glioma_1_GSE12657
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Glioma_1_GSE12657_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Glioma_1_GSE12657_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Glioma_1_GSE12657_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Glioma_1_GSE12657_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Glioma_1_GSE12657_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Glioma_1_GSE12657_Metadata_Resource

    list_display = ('accession','sampleId', 'groupI')
    list_filter = ('groupI',)
    search_fields = ['accession']