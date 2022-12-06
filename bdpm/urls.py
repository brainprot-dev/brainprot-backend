from django.urls import path, re_path

from bdpm import views

app_name = 'bdpm'

urlpatterns = [
    #path('', views.index, name='index'),

    # Single Entity, Paticular Disease, all data
    path('api/bdpm/proteins/<str:proteinId>/disease/<str:disease>', views.single_protein_single_disease, name='single_protein_single_disease'),
    
    # Single Entity, All Data + Metadata
    path('api/bdpm/proteins/<str:proteinId>', views.single_protein_all_data, name='single_protein_all_data'),

    # Single Disease All Metadata
    path('api/bdpm/metadata/<str:disease>', views.disease_metadata, name='disease_metadata'),

]