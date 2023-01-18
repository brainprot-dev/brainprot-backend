from django.contrib import admin
from .models import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# # # # # # # # # # # # # # # # # # # 
# Meningioma 1
# # # # # # # # # # # # # # # # # # # 

class Disease_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Disease
        # Fields useful for import and export
        fields = ('diseaseName', 'DisGeNetDiseaseId', 'numGeneDisGeNet', 'numGeneHarmonizome',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('DisGeNetDiseaseId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Disease_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Disease_Resource

    list_display = ('diseaseName',)
    search_fields = ['diseaseName', 'DisGeNetDiseaseId']
    #prepopulated_fields = {'diseaseSlug': ('diseaseName',)}


admin.site.register(Disease, Disease_Admin)
