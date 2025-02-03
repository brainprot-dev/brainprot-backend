from django.urls import path, re_path

from . import views

app_name = 'bdmc'

urlpatterns = [

    # Single Entity, Paticular Disease, all data
    path('api/bdmc/genes/<str:geneName>/disease/<str:diseaseID>', views.single_gene_single_disease, name='single_protein_single_disease'),
    
    # Single Entity, All Data 
    path('api/bdmc/genes/<str:geneName>', views.single_gene_all_data, name='single_protein_all_data'),

    # Single disease, all gene
    path('api/bdmc/disease/<str:diseaseID>', views.single_disease_all_gene, name='single_disease_all_gene'),
]
