from django.contrib import admin
from .models_meningiomas import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Register your models here.

# # # # # # # # # # # # # # # # # # # 
# Meningioma 1
# # # # # # # # # # # # # # # # # # # 

class Meningioma_1_GSE43290_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Meningioma_1_GSE43290
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45', 'S46', 'S47', 'S48', 'S49', 'S50', 'S51',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Meningioma_1_GSE43290_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Meningioma_1_GSE43290_Resource

    list_display = ('probeId','geneName')
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Meningioma_1_GSE43290_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Meningioma_1_GSE43290_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupI', 'groupII')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Meningioma_1_GSE43290_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Meningioma_1_GSE43290_Metadata_Resource

    list_display = ('accession','sampleId', 'gender', 'groupI', 'groupII')
    list_filter = ('gender', 'groupI', 'groupII')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # # 
# Meningioma 2
# # # # # # # # # # # # # # # # # # # 

class Meningioma_2_GSE54934_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Meningioma_2_GSE54934
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = False
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Meningioma_2_GSE54934_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Meningioma_2_GSE54934_Resource

    list_display = ('probeId','geneName')
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Meningioma_2_GSE54934_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Meningioma_2_GSE54934_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupI', 'groupII')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = False
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Meningioma_2_GSE54934_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Meningioma_2_GSE54934_Metadata_Resource

    list_display = ('accession','sampleId', 'gender', 'groupI', 'groupII')
    list_filter = ('gender', 'groupI', 'groupII')
    search_fields = ['accession']

