from django.urls import path, re_path

from . import views

app_name = 'bddf'

urlpatterns = [
     # Single Protein, BindingDB Data
    path('api/bddf/protein/bindingdb/<str:uniprotId>', views.BindingDB_Django_API, name='BindingDB API'),

    # Single Protein, ChemBl Data
    path('api/bddf/protein/chembl/<str:uniprotId>', views.chembl_Django_API, name='ChEMBL API'),

    # Single Protein, TTD Data
    path('api/bddf/protein/ttd/<str:uniprotId>', views.TTD_Django_API, name='TTD_API'),

    # Single Protein, CLUE Data
    path('api/bddf/protein/clue/<str:uniprotId>', views.CLUE_Django_API, name='CLUE_api'),

    # Single Protein, Stitch Data
    path('api/bddf/protein/stitch/<str:uniprotId>', views.Stitch_Django_API, name='Stitch API'),

    # Single Protein, All Data
    path('api/bddf/protein/all/<str:uniprotId>', views.All_Database_Django_API, name='All Data'),

    # ChEMBL ID, Open Targets Data
    path('api/bddf/opentargets/chembl/<str:ChemblId>', views.OpenTargets_Chembl_Django_API, name='Open Targets Chembl API'),

     # Smiles ID, Open Targets Data
    path('api/bddf/opentargets/smiles/<str:SmilesID>', views.OpenTargets_Smiles_Django_API, name='Open Targets Smiles API'),

    # Single Disease, All Data
    path('api/bddf/disease/<str:diseaseID>', views.single_disease_all_data, name='Static Disease Sheet API'),

    # Single Disease, ChemBl Data
    path('api/bddf/compound/<str:diseaseId>', views.chembl_disease, name='chembl_disease'),

     # Single Disease, Clinical Trial Data
    path('api/bddf/clinical/<str:diseaseId>', views.get_clinical_trial_info, name='Clinical Trial'),
]
