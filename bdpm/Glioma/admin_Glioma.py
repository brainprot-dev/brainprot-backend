from django.contrib import admin
from .models_Glioma import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# # # # # # # # # # # # # # # # # # # 
# Glioma 1
# # # # # # # # # # # # # # # # # # # 

class Glioma_1_PXD010247_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Glioma_1_PXD010247
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', )
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Glioma_1_PXD010247_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Glioma_1_PXD010247_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

# class Glioma_1_PXD010247_Unprocessed_Resource(resources.ModelResource):
#     #geneProt = fields.Field(
#     #    column_name='geneProt',
#     #    attribute='geneProt',
#     #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

#     class Meta:
#         # Controls which Model this resource is for
#         model = Glioma_1_PXD010247_Unprocessed
#         # Fields useful for import and export
#         fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25',)
#         # Fields which will be useful for object identification during import
#         import_id_fields = ('proteinId',)
#         # This will allow to skip unchanged entries
#         skip_unchanged = True
#         # This will report the skipped rows in Admin integration Preview page
#         report_skipped = True

# class Glioma_1_PXD010247_Unprocessed_Admin(ImportExportMixin, admin.ModelAdmin):
#     # For ImportExportMixin Interface, we set what resource class it deals with
#     resource_class = Glioma_1_PXD010247_Unprocessed_Resource

#     list_display = ('proteinId',)
#     search_fields = ['proteinId']
#     #prepopulated_fields = {'slug': ('peptideSequence',)}

class Glioma_1_PXD010247_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Glioma_1_PXD010247_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI', 'groupII')
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Glioma_1_PXD010247_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Glioma_1_PXD010247_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupII')
    list_filter = ('gender', 'groupI', 'groupII')
    search_fields = ['sampleId', 'sourceName']


# # # # # # # # # # # # # # # # # # # 
# Glioma 2
# # # # # # # # # # # # # # # # # # # 

class Glioma_2_PXD014606_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Glioma_2_PXD014606
        # Fields useful for import and export
        #fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29','S1_Raw','S2_Raw','S3_Raw','S4_Raw','S5_Raw','S6_Raw','S7_Raw','S8_Raw','S9_Raw','S10_Raw','S11_Raw','S12_Raw','S13_Raw','S14_Raw','S15_Raw','S16_Raw','S17_Raw','S18_Raw','S19_Raw','S20_Raw','S21_Raw','S22_Raw','S23_Raw','S24_Raw','S25_Raw','S26_Raw','S27_Raw','S28_Raw','S29_Raw')
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29','S30','S31','S32','S33','S34','S35','S36','S37','S38','S39','S40','S41','S42','S43','S44','S45','S46','S47','S48')
        
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Glioma_2_PXD014606_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Glioma_2_PXD014606_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

# class Glioma_2_PXD014606_Unprocessed_Resource(resources.ModelResource):
#     #geneProt = fields.Field(
#     #    column_name='geneProt',
#     #    attribute='geneProt',
#     #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

#     class Meta:
#         # Controls which Model this resource is for
#         model = Glioma_2_PXD014606_Unprocessed
#         # Fields useful for import and export
#         fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25', 'S26', 'S27', 'S28', 'S29',)
#         # Fields which will be useful for object identification during import
#         import_id_fields = ('proteinId',)
#         # This will allow to skip unchanged entries
#         skip_unchanged = True
#         # This will report the skipped rows in Admin integration Preview page
#         report_skipped = True

# class Glioma_2_PXD014606_Unprocessed_Admin(ImportExportMixin, admin.ModelAdmin):
#     # For ImportExportMixin Interface, we set what resource class it deals with
#     resource_class = Glioma_2_PXD014606_Unprocessed_Resource

#     list_display = ('proteinId',)
#     search_fields = ['proteinId']
#     #prepopulated_fields = {'slug': ('peptideSequence',)}

class Glioma_2_PXD014606_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Glioma_2_PXD014606_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI', 'groupII')
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Glioma_2_PXD014606_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Glioma_2_PXD014606_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender','groupI', 'groupII')
    list_filter = ('gender', 'groupI', 'groupII',)
    search_fields = ['sampleId', 'sourceName']


# # # # # # # # # # # # # # # # # # # 
# Glioma 3
# # # # # # # # # # # # # # # # # # # 

class Glioma_3_PXD028931_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Glioma_3_PXD028931
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25','S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35','S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43')
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Glioma_3_PXD028931_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Glioma_3_PXD028931_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

# class Glioma_3_PXD028931_Unprocessed_Resource(resources.ModelResource):
#     #geneProt = fields.Field(
#     #    column_name='geneProt',
#     #    attribute='geneProt',
#     #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

#     class Meta:
#         # Controls which Model this resource is for
#         model = Glioma_3_PXD028931_Unprocessed
#         # Fields useful for import and export
#         fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25','S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35','S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45','S46', 'S47', 'S48', 'S49', 'S50', 'S51', 'S52', 'S53', 'S54', 'S55','S56', 'S57', 'S58', 'S59', 'S60', 'S61', 'S62', 'S63', 'S64', 'S65')
#         # Fields which will be useful for object identification during import
#         import_id_fields = ('proteinId',)
#         # This will allow to skip unchanged entries
#         skip_unchanged = True
#         # This will report the skipped rows in Admin integration Preview page
#         report_skipped = True

# class Glioma_3_PXD028931_Unprocessed_Admin(ImportExportMixin, admin.ModelAdmin):
#     # For ImportExportMixin Interface, we set what resource class it deals with
#     resource_class = Glioma_1_PXD010247_Unprocessed_Resource

#     list_display = ('proteinId',)
#     search_fields = ['proteinId']
#     #prepopulated_fields = {'slug': ('peptideSequence',)}

class Glioma_3_PXD028931_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Glioma_3_PXD028931_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI')
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Glioma_3_PXD028931_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Glioma_3_PXD028931_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['sampleId', 'sourceName']