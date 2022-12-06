from .models_pituitary import *
from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Register your models here.

# # # # # # # # # # # # # # # # # # # 
# Pituitary Adenoma
# # # # # # # # # # # # # # # # # # # 

class Pituitary_1_GSE36314_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Pituitary_1_GSE36314
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Pituitary_1_GSE36314_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Pituitary_1_GSE36314_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Pituitary_1_GSE36314_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Pituitary_1_GSE36314_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Pituitary_1_GSE36314_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Pituitary_1_GSE36314_Metadata_Resource

    list_display = ('accession','sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']