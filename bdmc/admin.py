from django.contrib import admin
from .models import *
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin

# Register your models here.

class ALS_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Amyotrophic_Lateral_Sclerosis
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class ALS_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = ALS_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

class Alzheimer_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Alzheimer
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Alzheimer_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Alzheimer_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

class Meningioma_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Meningioma
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Meningioma_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Meningioma_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

class Glioma_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Glioma
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Glioma_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Glioma_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

class Glioblastoma_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Glioblastoma
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Glioblastoma_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Glioblastoma_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

class Medulloblastoma_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Medulloblastoma
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Medulloblastoma_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Medulloblastoma_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

class Pituitary_Adenoma_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Pituitary_Adenoma
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Pituitary_Adenoma_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Pituitary_Adenoma_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

class Parkinson_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Parkinson
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Parkinson_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Parkinson_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

class Huntington_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Huntington
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Huntington_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Huntington_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

class Multiple_Sclerosis_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Multiple_Sclerosis
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Multiple_Sclerosis_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Multiple_Sclerosis_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

class Frontotemporal_Resource(resources.ModelResource):
    class Meta:
        # Controls which Model this resource is for
        model = Frontotemporal
        # Fields useful for import and export
        fields = ('geneName', 'DISGENET_Score', 'Pubpular_Score', 'Harmonizome_Score', 'Bionda_Score', 'Unscaled_DISGENET_Score', 'Unscaled_Pubpular_Score', 'Unscaled_Harmonizome_Score', 'Unscaled_Bionda_Score')
        # Fields which will be useful for object identification during import
        import_id_fields = ('geneName',)
        # This will allow to skip unchanged entries
        skip_unchanged = True
        # This will report the skipped rows in Admin integration Preview page
        report_skipped = True

class Frontotemporal_Admin(ImportExportMixin, admin.ModelAdmin):
    # For ImportExportMixin Interface, we set what resource class it deals with
    resource_class = Frontotemporal_Resource
    list_display = ('geneName',)
    search_fields = ['geneName']

admin.site.register(Amyotrophic_Lateral_Sclerosis, ALS_Admin)
admin.site.register(Alzheimer, Alzheimer_Admin)
admin.site.register(Meningioma, Meningioma_Admin)
admin.site.register(Glioma, Glioma_Admin)
admin.site.register(Glioblastoma, Glioblastoma_Admin)
admin.site.register(Medulloblastoma, Medulloblastoma_Admin)
admin.site.register(Pituitary_Adenoma, Pituitary_Adenoma_Admin)
admin.site.register(Parkinson, Parkinson_Admin)
admin.site.register(Huntington, Huntington_Admin)
admin.site.register(Multiple_Sclerosis, Multiple_Sclerosis_Admin)
admin.site.register(Frontotemporal, Frontotemporal_Admin)