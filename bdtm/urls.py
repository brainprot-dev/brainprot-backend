from django.urls import path, re_path

from . import views

app_name = 'bdtm'

urlpatterns = [
    #path('', views.index, name='index'),

    # Single Entity, Paticular Disease, all data
    path('api/bdtm/genes/<str:geneName>/disease/<str:disease>', views.single_protein_single_disease, name='single_protein_single_disease'),
    
    # Single Entity, All Data + Metadata
    path('api/bdtm/genes/<str:geneName>', views.single_protein_all_data, name='single_protein_all_data'),

    # Single Disease All Metadata
    path('api/bdtm/metadata/<str:disease>', views.disease_metadata, name='disease_metadata'),

]
