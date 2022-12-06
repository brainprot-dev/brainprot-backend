from django.contrib import admin

# Meningioma Admin
from .meningioma.models_meningiomas import *
from .meningioma.admin_meningiomas import Meningioma_1_PXD007073_Admin, Meningioma_1_PXD007073_Metadata_Admin, Meningioma_2_PXD014852_Admin, Meningioma_2_PXD014852_Metadata_Admin

admin.site.register(Meningioma_1_PXD007073, Meningioma_1_PXD007073_Admin)
admin.site.register(Meningioma_1_PXD007073_Metadata, Meningioma_1_PXD007073_Metadata_Admin)
admin.site.register(Meningioma_2_PXD014852, Meningioma_2_PXD014852_Admin)
admin.site.register(Meningioma_2_PXD014852_Metadata, Meningioma_2_PXD014852_Metadata_Admin)

# Register your models here.
