from .models_sclerosis import Multiple_Sclerosis_1_GSE38010, Multiple_Sclerosis_1_GSE38010_Metadata, Multiple_Sclerosis_2_GSE52139, Multiple_Sclerosis_2_GSE52139_Metadata, Multiple_Sclerosis_3_GSE83670, Multiple_Sclerosis_3_GSE83670_Metadata
from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Register your models here.

# # # # # # # # # # # # # # # # # # # 
# Multiple Sclerosis 1
# # # # # # # # # # # # # # # # # # # 

class Multiple_Sclerosis_1_GSE38010_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Multiple_Sclerosis_1_GSE38010
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Multiple_Sclerosis_1_GSE38010_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Multiple_Sclerosis_1_GSE38010_Resource

    list_display = ('probeId','geneName')
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Multiple_Sclerosis_1_GSE38010_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Multiple_Sclerosis_1_GSE38010_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Multiple_Sclerosis_1_GSE38010_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Multiple_Sclerosis_1_GSE38010_Metadata_Resource

    list_display = ('accession','sampleId', 'groupI')
    list_filter = ('groupI',)
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # # 
# Multiple Sclerosis 2
# # # # # # # # # # # # # # # # # # # 

class Multiple_Sclerosis_2_GSE52139_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Multiple_Sclerosis_2_GSE52139
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Multiple_Sclerosis_2_GSE52139_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Multiple_Sclerosis_2_GSE52139_Resource

    list_display = ('probeId','geneName')
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Multiple_Sclerosis_2_GSE52139_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Multiple_Sclerosis_2_GSE52139_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Multiple_Sclerosis_2_GSE52139_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Multiple_Sclerosis_2_GSE52139_Metadata_Resource

    list_display = ('accession','sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # # 
# Multiple Sclerosis 3
# # # # # # # # # # # # # # # # # # # 

class Multiple_Sclerosis_3_GSE83670_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Multiple_Sclerosis_3_GSE83670
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Multiple_Sclerosis_3_GSE83670_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Multiple_Sclerosis_3_GSE83670_Resource

    list_display = ('probeId','geneName')
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Multiple_Sclerosis_3_GSE83670_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Multiple_Sclerosis_3_GSE83670_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Multiple_Sclerosis_3_GSE83670_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Multiple_Sclerosis_3_GSE83670_Metadata_Resource

    list_display = ('accession','sampleId', 'groupI')
    list_filter = ('groupI',)
    search_fields = ['accession']