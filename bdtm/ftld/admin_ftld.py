from .models_ftld import *
from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Register your models here.

# # # # # # # # # # # # # # # # # # # 
# FTLD
# # # # # # # # # # # # # # # # # # # 

class FTLD_1_GSE13162_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = FTLD_1_GSE13162
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45', 'S46', 'S47', 'S48', 'S49', 'S50', 'S51', 'S52', 'S53', 'S54', 'S55', 'S56',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class FTLD_1_GSE13162_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = FTLD_1_GSE13162_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class FTLD_1_GSE13162_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = FTLD_1_GSE13162_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class FTLD_1_GSE13162_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = FTLD_1_GSE13162_Metadata_Resource

    list_display = ('accession','sampleId', 'groupI')
    list_filter = ('groupI',)
    search_fields = ['accession']