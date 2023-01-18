from django.urls import path, re_path

from . import views

app_name = 'bddf'

urlpatterns = [
    #path('api/bddf/bindingdb/<str:uniprotID>', views.bindingdb, name='bindingdb'),

    # Single Protein, ChemBl Data
    path('api/bddf/protein/<str:uniprotId>', views.get_protein_data, name='get_protein_data'),

    # Single Disease, ChemBl Data
    path('api/bddf/disease/<str:diseaseId>', views.chembl_disease, name='chembl_disease'),
]
