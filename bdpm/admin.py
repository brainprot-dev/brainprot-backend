from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Meningioma Admin
from .meningioma.models_meningiomas import *
from .meningioma.admin_meningiomas import  *

from .Alzhiemer_s.models_Alzhiemer_s import *
from .Alzhiemer_s.admin_Alzhiemer_s import *


from .Amyotrophic_Lateral_Sclerosis.models_Amyotrophic_Lateral_Sclerosis import *
from .Amyotrophic_Lateral_Sclerosis.admin_Amyotrophic_Lateral_Sclerosis import *


from .Glioma.models_Glioma import *
from .Glioma.admin_Glioma import *

from .Medulloblastoma.models_Medulloblastoma import *
from .Medulloblastoma.admin_Medulloblastoma import *

from .Parkinson.models_Parkinson import *
from .Parkinson.admin_Parkinson import *

admin.site.register(Meningioma_1_PXD007073, Meningioma_1_PXD007073_Admin)
admin.site.register(Meningioma_1_PXD007073_Metadata, Meningioma_1_PXD007073_Metadata_Admin)

admin.site.register(Meningioma_2_PXD014852, Meningioma_2_PXD014852_Admin)
admin.site.register(Meningioma_2_PXD014852_Metadata, Meningioma_2_PXD014852_Metadata_Admin)

admin.site.register(Meningioma_3_PXD012923, Meningioma_3_PXD012923_Admin)
admin.site.register(Meningioma_3_PXD012923_Metadata, Meningioma_3_PXD012923_Metadata_Admin)

admin.site.register(Meningioma_4_PXD015979, Meningioma_4_PXD015979_Admin)
admin.site.register(Meningioma_4_PXD015979_Metadata, Meningioma_4_PXD015979_Metadata_Admin)

# Register your models here.


#Alzhiemer_s
admin.site.register(Alzhiemer_s_1_PXD009199, Alzhiemer_s_1_PXD009199_Admin)
admin.site.register(Alzhiemer_s_1_PXD009199_Metadata, Alzhiemer_s_1_PXD009199_Metadata_Admin)

admin.site.register(Alzhiemer_s_2_PXD014376, Alzhiemer_s_2_PXD014376_Admin)
admin.site.register(Alzhiemer_s_2_PXD014376_Metadata, Alzhiemer_s_2_PXD014376_Metadata_Admin)


admin.site.register(Alzhiemer_s_3_PXD037133, Alzhiemer_s_3_PXD037133_Admin)
admin.site.register(Alzhiemer_s_3_PXD037133_Metadata, Alzhiemer_s_3_PXD037133_Metadata_Admin)

admin.site.register(Alzhiemer_s_4_PXD005319, Alzhiemer_s_4_PXD005319_Admin)
admin.site.register(Alzhiemer_s_4_PXD005319_Metadata, Alzhiemer_s_4_PXD005319_Metadata_Admin)

admin.site.register(Alzhiemer_s_5_PXD005321, Alzhiemer_s_5_PXD005321_Admin)
admin.site.register(Alzhiemer_s_5_PXD005321_Metadata, Alzhiemer_s_5_PXD005321_Metadata_Admin)

#admin.site.register(Alzhiemer_s_6_PXD021645, Alzhiemer_s_6_PXD021645_Admin)
#admin.site.register(Alzhiemer_s_6_PXD021645_Metadata, Alzhiemer_s_6_PXD021645_Metadata_Admin)

admin.site.register(Alzhiemer_s_7_PXD023199, Alzhiemer_s_7_PXD023199_Admin)
admin.site.register(Alzhiemer_s_7_PXD023199_Metadata, Alzhiemer_s_7_PXD023199_Metadata_Admin)


admin.site.register(Alzhiemer_s_8_PXD027173, Alzhiemer_s_8_PXD027173_Admin)
admin.site.register(Alzhiemer_s_8_PXD027173_Metadata, Alzhiemer_s_8_PXD027173_Metadata_Admin)

#ALS
admin.site.register(Amyotrophic_Lateral_Sclerosis_1_PXD021630, Amyotrophic_Lateral_Sclerosis_1_PXD021630_Admin)
admin.site.register(Amyotrophic_Lateral_Sclerosis_1_PXD021630_Metadata, Amyotrophic_Lateral_Sclerosis_1_PXD021630_Metadata_Admin)




#Glioma
admin.site.register(Glioma_1_PXD010247, Glioma_1_PXD010247_Admin)
admin.site.register(Glioma_1_PXD010247_Metadata, Glioma_1_PXD010247_Metadata_Admin)

admin.site.register(Glioma_2_PXD014606, Glioma_2_PXD014606_Admin)
admin.site.register(Glioma_2_PXD014606_Metadata, Glioma_2_PXD014606_Metadata_Admin)


admin.site.register(Glioma_3_PXD028931, Glioma_3_PXD028931_Admin)
admin.site.register(Glioma_3_PXD028931_Metadata, Glioma_3_PXD028931_Metadata_Admin)



#Medulloblastoma
admin.site.register(Medulloblastoma_1_PXD014950, Medulloblastoma_1_PXD014950_Admin)
admin.site.register(Medulloblastoma_1_PXD014950_Metadata, Medulloblastoma_1_PXD014950_Metadata_Admin)


#parkinson
admin.site.register(Parkinson_1_PXD008036, Parkinson_1_PXD008036_Admin)
admin.site.register(Parkinson_1_PXD008036_Metadata, Parkinson_1_PXD008036_Metadata_Admin)

admin.site.register(Parkinson_2_PXD022092, Parkinson_2_PXD022092_Admin)
admin.site.register(Parkinson_2_PXD022092_Metadata, Parkinson_2_PXD022092_Metadata_Admin)

admin.site.register(Parkinson_3_PXD024998, Parkinson_3_PXD024998_Admin)
admin.site.register(Parkinson_3_PXD024998_Metadata, Parkinson_3_PXD024998_Metadata_Admin)