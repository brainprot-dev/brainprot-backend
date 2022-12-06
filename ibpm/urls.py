from django.urls import path, re_path
from . import views

app_name = 'ibpm'


### TODO: Phospho Single Gene Data okay?

urlpatterns = [
    ####### NO PHOSPHO #######
    ### ONLY METADATA ###
    # Deals with all genes, gives meta information
    path('api/ibpm/genes/list-all', views.gene_list, name='gene_list'),
    # Deals with all proteins, gives meta information
    path('api/ibpm/proteins/list-all', views.protein_list, name='protein_list'),
    # Deals with all peptides, gives meta information
    path('api/ibpm/peptides/list-all', views.peptide_list, name='peptide_list'),
   
    ### ALL ENTITY ALL DATA ###
    # Deals with all genes, gives all ibpm information, no phospho data
    # path('api/ibpm', views.ibpm_data, name='ibpm_data'),
    # Deals with all proteins, gives all ibpm information, no phospho data
    path('api/ibpm/proteins', views.protein_data, name='protein_data'),
    # Deals with all peptides, gives all ibpm information, no phospho data
    path('api/ibpm/peptides', views.peptide_data, name='peptide_data'),

    ### SINGLE ENTITY ALL DATA ###
    # Deals with single gene, gives all ibpm information, no phospho data
    path('api/ibpm/genes/<str:geneName>', views.single_gene_data, name='single_gene_data'),
    # Deals with single protein, gives all ibpm information, no phospho data
    path('api/ibpm/proteins/<str:proteinName>', views.single_protein_data, name='single_protein_data'),
    # Deals with single peptide, gives all ibpm information, no phospho data
    path('api/ibpm/peptides/<str:peptideSequence>', views.single_peptide_data, name='single_peptide_data'),

    ### SINGLE ENTITY REGIONAL DATA ###
    # Deals with single gene, gives single region information, no phospho data
    path('api/ibpm/genes/<str:geneName>/region/<str:region>', views.single_gene_region_data, name='single_gene_region_data'),
    # Deals with single protein, gives single region information, no phospho data
    path('api/ibpm/proteins/<str:proteinName>/region/<str:region>', views.single_protein_region_data, name='single_protein_region_data'),
    

    ####### PHOSPHO ONLY #######
    ### ONLY METADATA ###
    # Deals with all genes, gives meta information
    path('api/ibpm/phosphomap/genes/list-all', views.phospho_gene_list, name='phospho_gene_list'),
    # Deals with all proteins, gives meta information
    path('api/ibpm/phosphomap/proteins/list-all', views.phospho_protein_list, name='phospho_protein_list'),
    # Deals with all peptides, gives meta information
    path('api/ibpm/phosphomap/peptides/list-all', views.phospho_peptide_list, name='phospho_peptide_list'),
   
    ### ALL ENTITY ALL DATA ###
    # Deals with all genes, gives all ibpm phospho information
    # path('api/ibpm/genes', views.phospho_gene_data, name='phospho_gene_data'),
    # Deals with all proteins, gives all ibpm phospho information
    # path('api/ibpm/proteins', views.phospho_protein_data, name='phospho_protein_data'),
    # Deals with all peptides, gives all ibpm phospho information
    path('api/ibpm/phosphomap', views.phospho_peptide_data, name='phospho_peptide_data'),

    ### SINGLE ENTITY ALL DATA ###
    # Deals with single gene, gives all ibpm phospho information
    #path('api/ibpm/phosphomap/genes/<str:geneName>', views.phospho_single_gene_data, name='phospho_single_gene_data'),
    # Deals with single protein, gives all ibpm phospho information
    path('api/ibpm/phosphomap/proteins/<str:proteinName>', views.phospho_single_protein_data, name='phospho_single_protein_data'),
    # Deals with single peptide, gives all ibpm phospho information
    path('api/ibpm/phosphomap/peptides/<str:peptideSequence>', views.phospho_single_peptide_data, name='phospho_single_peptide_data'),

    ### SINGLE ENTITY REGIONAL DATA ###
    # Deals with single gene, gives all ibpm phospho information
    path('api/ibpm/phosphomap/genes/<str:geneName>/region/<str:region>', views.phospho_single_gene_region_data, name='phospho_single_region_gene_data'),
    # Deals with single protein, gives all ibpm phospho information
    path('api/ibpm/phosphomap/proteins/<str:proteinName>/region/<str:region>', views.phospho_single_protein_region_data, name='phospho_single_protein_region_data'),
    # Deals with single peptide, gives region ibpm phospho information
    path('api/ibpm/phosphomap/peptides/<str:peptideSequence>/region/<str:region>', views.phospho_single_peptide_region_data, name='phospho_single_peptide_region_data'),

]
