from django.contrib import admin
from .models_Alzhiemer_s import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 1
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_1_PXD009199_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_1_PXD009199
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10')
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_1_PXD009199_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_1_PXD009199_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']

class Alzhiemer_s_1_PXD009199_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_1_PXD009199_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'gender', 'age', 'groupI',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_1_PXD009199_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_1_PXD009199_Metadata_Resource

    list_display = ('sourceName','sampleId',  'gender', 'groupI')
    list_filter = ('gender', 'groupI')
    search_fields = ['sampleId']


# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 2
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_2_PXD014376_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_2_PXD014376
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', )
        
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_2_PXD014376_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_2_PXD014376_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Alzhiemer_s_2_PXD014376_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_2_PXD014376_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI', )
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_2_PXD014376_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_2_PXD014376_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupI')
    list_filter = ('gender', 'groupI',)
    search_fields = ['sourceName', 'sampleId']


# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 3
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_3_PXD037133_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_3_PXD037133
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16')
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_3_PXD037133_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_3_PXD037133_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}
class Alzhiemer_s_3_PXD037133_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_3_PXD037133_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_3_PXD037133_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_3_PXD037133_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupI')
    list_filter = ('gender', 'groupI', )
    search_fields = ['sampleId', 'sourceName']

# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 4
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_4_PXD005319_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_4_PXD005319
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', )
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_4_PXD005319_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_4_PXD005319_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Alzhiemer_s_4_PXD005319_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_4_PXD005319_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_4_PXD005319_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_4_PXD005319_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupI')
    list_filter = ('gender', 'groupI', )
    search_fields = ['sampleId', 'sourceName']

# # # # # # # # # # # # # # # # # # #
# Alzhiemer_s 5
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_5_PXD005321_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_5_PXD005321
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16','S17','S18' )
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_5_PXD005321_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_5_PXD005321_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Alzhiemer_s_5_PXD005321_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_5_PXD005321_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_5_PXD005321_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_5_PXD005321_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupI')
    list_filter = ('gender', 'groupI', )
    search_fields = ['sampleId', 'sourceName']



# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 6
# # # # # # # # # # # # # # # # # # # 

""" class Alzhiemer_s_6_PXD021645_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_6_PXD021645
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', )
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_6_PXD021645_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_6_PXD021645_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Alzhiemer_s_6_PXD021645_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_6_PXD021645_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_6_PXD021645_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_6_PXD021645_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupI')
    list_filter = ('gender', 'groupI', )
    search_fields = ['sampleId', 'sourceName']

 """


# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 7
# # # # # # # # # # # # # # # # # # # 

class Alzhiemer_s_7_PXD023199_Resource(resources.ModelResource):
    #geneProt = fields.Field(
    #    column_name='geneProt',
    #    attribute='geneProt',
    #    widget=widgets.ForeignKeyWidget(GeneProt, 'geneName'))

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_7_PXD023199
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25','S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_7_PXD023199_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_7_PXD023199_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']
    #prepopulated_fields = {'slug': ('peptideSequence',)}

class Alzhiemer_s_7_PXD023199_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_7_PXD023199_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_7_PXD023199_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_7_PXD023199_Metadata_Resource

    list_display = ('sourceName','sampleId', 'sampleName', 'gender', 'groupI')
    list_filter = ('gender', 'groupI', )
    search_fields = ['sampleId', 'sourceName']



# # # # # # # # # # # # # # # # # # # 
# Alzhiemer_s 8
# # # # # # # # # # # # # # # # # # # 



class Alzhiemer_s_8_PXD027173_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_8_PXD027173
        # Fields useful for import and export
        fields = ('proteinId', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22', 'S23', 'S24', 'S25','S26', 'S27', 'S28', 'S29', 'S30', 'S31', 'S32', 'S33', 'S34', 'S35','S36', 'S37', 'S38', 'S39', 'S40', 'S41', 'S42', 'S43', 'S44', 'S45','S46', 'S47', 'S48', 'S49', 'S50', 'S51', 'S52', 'S53', 'S54', 'S55','S56', 'S57', 'S58',)
        # Fields which will be useful for object identification during import
        import_id_fields = ('proteinId',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_8_PXD027173_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_8_PXD027173_Resource

    list_display = ('proteinId',)
    search_fields = ['proteinId']




class Alzhiemer_s_8_PXD027173_Metadata_Resource(resources.ModelResource):

    class Meta:
        # Controls which Model this resource is for
        model = Alzhiemer_s_8_PXD027173_Metadata
        # Fields useful for import and export
        fields = ('sourceName', 'sampleId', 'sampleName', 'gender', 'age', 'groupI','groupII')
        # Fields which will be useful for object identification during import
        import_id_fields = ('sourceName', )
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzhiemer_s_8_PXD027173_Metadata_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzhiemer_s_8_PXD027173_Metadata_Resource

    list_display = ('sourceName','sampleId','sampleName','gender', 'groupI','groupII')
    list_filter = ('gender', 'groupI','groupII' )
    search_fields = ['sampleId', 'sourceName']