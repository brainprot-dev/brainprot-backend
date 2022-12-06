from django.contrib import admin
from .models_meningiomas import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# # # # # # # # # # # # # # # # # # # 
# Meningioma 1
# # # # # # # # # # # # # # # # # # # 

class Meningioma_1_PXD007073_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Meningioma_1_PXD007073
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Meningioma_1_PXD007073_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Meningioma_1_PXD007073_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Meningioma_1_PXD007073_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Meningioma_1_PXD007073_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI', 'groupII', 'groupIII', 'groupIV',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('sampleId', 'sampleName')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Meningioma_1_PXD007073_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Meningioma_1_PXD007073_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupII')
    list_filter = ('gender', 'groupI', 'groupII', 'groupIII', 'groupIV')
    search_fields = ['sampleId', 'sampleName']


# # # # # # # # # # # # # # # # # # # 
# Meningioma 2
# # # # # # # # # # # # # # # # # # # 

class Meningioma_2_PXD014852_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Meningioma_2_PXD014852
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Meningioma_2_PXD014852_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Meningioma_2_PXD014852_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Meningioma_2_PXD014852_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Meningioma_2_PXD014852_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI', 'groupII',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('sampleId', 'sampleName')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Meningioma_2_PXD014852_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Meningioma_2_PXD014852_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupII')
    list_filter = ('gender', 'groupI', 'groupII',)
    search_fields = ['sampleId', 'sampleName']