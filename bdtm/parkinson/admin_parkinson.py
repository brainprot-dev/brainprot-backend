from django.contrib import admin
from .models_parkinson import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Register your models here.

# # # # # # # # # # # # # # # # # # #
# Parkinson 1
# # # # # # # # # # # # # # # # # # #


class Parkinson_1_GSE7621_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_1_GSE7621
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11',
                  'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_1_GSE7621_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_1_GSE7621_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_1_GSE7621_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_1_GSE7621_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_1_GSE7621_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_1_GSE7621_Metadata_Resource

    list_display = ('accession', 'sampleId', 'groupI')
    list_filter = ('groupI',)
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 2
# # # # # # # # # # # # # # # # # # #


class Parkinson_2_GSE8397_U133A_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_2_GSE8397_U133A
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22',
                  'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45', 'S46', 'S47')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_2_GSE8397_U133A_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_2_GSE8397_U133A_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_2_GSE8397_U133A_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_2_GSE8397_U133A_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'gender', 'groupI',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_2_GSE8397_U133A_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_2_GSE8397_U133A_Metadata_Resource

    list_display = ('accession', 'sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 3
# # # # # # # # # # # # # # # # # # #


class Parkinson_3_GSE8397_U133B_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_3_GSE8397_U133B
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22',
                  'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35', 'S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45', 'S46', 'S47')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_3_GSE8397_U133B_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_3_GSE8397_U133B_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_3_GSE8397_U133B_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_3_GSE8397_U133B_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_3_GSE8397_U133B_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_3_GSE8397_U133B_Metadata_Resource

    list_display = ('accession', 'sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 4
# # # # # # # # # # # # # # # # # # #


class Parkinson_4_GSE19587_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_4_GSE19587
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10',
                  'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_4_GSE19587_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_4_GSE19587_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_4_GSE19587_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_4_GSE19587_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_4_GSE19587_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_4_GSE19587_Metadata_Resource

    list_display = ('accession', 'sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 5
# # # # # # # # # # # # # # # # # # #


class Parkinson_5_GSE20141_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_5_GSE20141
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',
                  'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_5_GSE20141_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_5_GSE20141_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_5_GSE20141_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_5_GSE20141_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_5_GSE20141_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_5_GSE20141_Metadata_Resource

    list_display = ('accession', 'sampleId', 'groupI')
    list_filter = ('groupI',)
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 6
# # # # # # # # # # # # # # # # # # #


class Parkinson_6_GSE20146_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_6_GSE20146
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8',
                  'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_6_GSE20146_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_6_GSE20146_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_6_GSE20146_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_6_GSE20146_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_6_GSE20146_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_6_GSE20146_Metadata_Resource

    list_display = ('accession', 'sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 7
# # # # # # # # # # # # # # # # # # #


class Parkinson_7_GSE20163_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_7_GSE20163
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',
                  'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_7_GSE20163_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_7_GSE20163_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_7_GSE20163_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_7_GSE20163_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'age', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_7_GSE20163_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_7_GSE20163_Metadata_Resource

    list_display = ('accession', 'sampleId', 'groupI')
    list_filter = ('groupI',)
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 8
# # # # # # # # # # # # # # # # # # #


class Parkinson_8_GSE20164_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_8_GSE20164
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4',
                  'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_8_GSE20164_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_8_GSE20164_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_8_GSE20164_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_8_GSE20164_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_8_GSE20164_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_8_GSE20164_Metadata_Resource

    list_display = ('accession', 'sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 9
# # # # # # # # # # # # # # # # # # #


class Parkinson_9_GSE20168_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_9_GSE20168
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13',
                  'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_9_GSE20168_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_9_GSE20168_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_9_GSE20168_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_9_GSE20168_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_9_GSE20168_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_9_GSE20168_Metadata_Resource

    list_display = ('accession', 'sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 10
# # # # # # # # # # # # # # # # # # #


class Parkinson_10_GSE20291_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_10_GSE20291
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16',
                  'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_10_GSE20291_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_10_GSE20291_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_10_GSE20291_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_10_GSE20291_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_10_GSE20291_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_10_GSE20291_Metadata_Resource

    list_display = ('accession', 'sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 11
# # # # # # # # # # # # # # # # # # #


class Parkinson_11_GSE20292_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_11_GSE20292
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13',
                  'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_11_GSE20292_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_11_GSE20292_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_11_GSE20292_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_11_GSE20292_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_11_GSE20292_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_11_GSE20292_Metadata_Resource

    list_display = ('accession', 'sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 12
# # # # # # # # # # # # # # # # # # #


class Parkinson_12_GSE20314_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_12_GSE20314
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2',
                  'S3', 'S4', 'S5', 'S6', 'S7', 'S8')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_12_GSE20314_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_12_GSE20314_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_12_GSE20314_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_12_GSE20314_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_12_GSE20314_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_12_GSE20314_Metadata_Resource

    list_display = ('accession', 'sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 13
# # # # # # # # # # # # # # # # # # #


class Parkinson_13_GSE20333_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_13_GSE20333
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4',
                  'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_13_GSE20333_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_13_GSE20333_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_13_GSE20333_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_13_GSE20333_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title',
                  'sourceName', 'gender', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_13_GSE20333_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_13_GSE20333_Metadata_Resource

    list_display = ('accession', 'sampleId', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['accession']

# # # # # # # # # # # # # # # # # # #
# Parkinson 14
# # # # # # # # # # # # # # # # # # #


class Parkinson_14_GSE24378_Resource(resources.ModelResource):
    # geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_14_GSE24378
        # Fields useful for import and export
        fields = ('probeId', 'geneName', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',
                  'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17')
        # Fields which will be useful for object identification during import
        import_id_fields = ('probeId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_14_GSE24378_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_14_GSE24378_Resource

    list_display = ('geneName',)
    search_fields = ['geneName']
    #prepopulated_fields = {'slug': ('peptideSequence',)}


class Parkinson_14_GSE24378_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Parkinson_14_GSE24378_Metadata
        # Fields useful for import and export
        fields = ('accession', 'sampleId', 'title', 'sourceName', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('accession', 'sampleId')
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True


class Parkinson_14_GSE24378_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_14_GSE24378_Metadata_Resource

    list_display = ('accession', 'sampleId', 'groupI')
    list_filter = ('groupI',)
    search_fields = ['accession']
