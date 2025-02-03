from django.contrib import admin
from .models_pvalue import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Register your models here.

class P_Value_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = P_Value
        # Fields useful for import and export
        fields = ('geneName', 'GSE43290', 'GSE54934', 'GSE62600', 'GSE12657', 'GSE13276', 'GSE36314', 'GSE13162', 'GSE83790_U133A', 'GSE83790_U133B', 'GSE20589', 'GSE19332', 'GSE68605', 'GSE52139', 'GSE83670', 'GSE38010', 'GSE5281', 'GSE48350', 'GSE1297', 'GSE4757', 'GSE12685', 'GSE16759', 'GSE28146', 'GSE8397_U133A', 'GSE8397_U133B', 'GSE7621', 'GSE19587', 'GSE20163', 'GSE20164', 'GSE20291', 'GSE20292', 'GSE20314', 'GSE20333', 'GSE24378', 'GSE20146', 'GSE20168', 'GSE20141')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class P_Value_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = P_Value_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']