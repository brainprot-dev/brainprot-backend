from re import template
from django.shortcuts import render
from django.http import JsonResponse
from yaml import serialize
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from ibpm.models import *
from ibpm.serializers import *
from rest_framework.decorators import api_view

#For Faster Concatenating of Lists
from itertools import chain 

# Setting the API HTML Template to be (not) visible
#class CustomPagination(PageNumberPagination):
#    template = None

'''
TO DO:

Fix the issue of incosistent filter and no filter -> Only filter

'''



# Creating a Paginator
paginator = PageNumberPagination()
paginator.page_size = 100

# Global Variables
protein_regions = [
    'AMY',
    'BS',
    'CING',
    'CN',
    'CV',
    'DG',
    'FCM',
    'FWM',
    'HIP',
    'LE',
    'LI',
    'OB',
    'OC',
    'PC',
    'PONS',
    'PUT',
    'SN',
    'TC',
    'THAL'
]
phospho_regions = [
    'AMY',
    'BS',
    'CN',
    'CV',
    'CING',
    'DG',
    'FC',
    'HIP',
    'MC',
    'SN',
    'SC',
    'THAL',
]
# Create your views here.

### ONLY METADATA ###
# Deals with all genes, gives meta information
@api_view(['GET'])
def gene_list(request):
    all_ibpm_prots = Protein.objects.all().order_by('id')
    page = paginator.paginate_queryset(all_ibpm_prots, request)
    serialized_page = ProteinSerializer(page,
                                         fields=(
                                                 'proteinId',
                                                 #'geneProt',
                                                 'gene',
                                                 'proteinNames',
                                                 ),
                                         many=True)
    paginated_response = paginator.get_paginated_response(serialized_page.data)
    return paginated_response


# Deals with all proteins, gives meta information
@api_view(['GET'])
def protein_list(request):
    all_ibpm_prots = Protein.objects.all().order_by('id')
    page = paginator.paginate_queryset(all_ibpm_prots, request)
    serialized_page = ProteinSerializer(page,
                                         fields=(
                                                 'proteinId',
                                                 #'geneProt',
                                                 'gene',
                                                 'proteinNames',
                                                 'proteinLength',
                                                 'proteinMass',
                                                 ),
                                         many=True)
    paginated_response = paginator.get_paginated_response(serialized_page.data)
    return paginated_response

# Deals with all peptides, gives meta information
@api_view(['GET'])
def peptide_list(request):
    all_ibpm_peps = Peptide.objects.all().order_by('id')
    page = paginator.paginate_queryset(all_ibpm_peps, request)
    serialized_page = PeptideSerializer(page,
                                         fields=(
                                                 'peptideSequence',
                                                 #'geneProt',
                                                 'gene',
                                                 'protein',
                                                 ),
                                         many=True)
    paginated_response = paginator.get_paginated_response(serialized_page.data)
    return paginated_response 

### ALL ENTITY ALL DATA ###
# Deals with all genes, gives all ibpm information, no phospho data
'''
This crashes the server because too much data
@api_view(['GET'])
def ibpm_data(request):
    all_ibpm_prots = Protein.objects.all().order_by('id')
    all_ibpm_peps = Peptide.objects.all().order_by('id')

    serialized_prots = ProteinSerializer(all_ibpm_prots,
                                        fields=(
                                                'id',
                                                'geneProt',
                                                'proteinNames',
                                                'proteinLength',
                                                'proteinMass',
                                                ),
                                        exclude=True,
                                        many=True)
    serialized_peps = PeptideSerializer(all_ibpm_peps,
                                        fields=(
                                                'id',
                                                'geneProt',
                                               ),
                                        exclude = True,
                                        many=True)

    return JsonResponse({'proteinData':serialized_prots.data, 'peptideData':serialized_peps.data},safe=False)
'''

# Deals with all proteins, gives all ibpm information, no phospho data
@api_view(['GET'])
def protein_data(request):
    all_ibpm_prots = Protein.objects.all().order_by('id')
    page = paginator.paginate_queryset(all_ibpm_prots, request)
    serialized_page = ProteinSerializer(page,
                                        fields=(
                                                'id',
                                                'geneProt',
                                                'proteinNames',
                                                'proteinLength',
                                                'proteinMass',
                                                ),
                                        exclude=True,
                                        many=True)
    paginated_response = paginator.get_paginated_response(serialized_page.data)
    return paginated_response


# Deals with all peptides, gives all ibpm information, no phospho data
@api_view(['GET'])
def peptide_data(request):
    all_ibpm_peps = Peptide.objects.all().order_by('id')
    page = paginator.paginate_queryset(all_ibpm_peps, request)
    serialized_page = PeptideSerializer(page,
                                        fields=(
                                                'id',
                                                'geneProt',
                                               ),
                                        exclude = True,
                                        many=True)
    paginated_response = paginator.get_paginated_response(serialized_page.data)
    return paginated_response

### SINGLE ENTITY ALL DATA ###
# Deals with single gene, gives all ibpm information, no phospho data
@api_view(['GET'])
def single_gene_data(request, geneName):
    geneName = geneName.upper()
    geneProt_obj_list = GeneProt.objects.filter(geneName=geneName)
    geneData = []
    '''
    Remark: Using filter always returns a queryset, which is a list
    However, using get can return a list or a queryset

    Since proteinId/protName is unique, in latter functions we are allowing
    the use of get, instead of filter.

    While filter can be used, it adds the hassle of being a list and would
    uneccsarily complicate the json structure

    # PROBLEM: Multiple Peptides Found!
    FIX THE CODE THEN FIX FRONT CODE!!!!

    # TODO: 
    '''
    if len(geneProt_obj_list) > 0:
        for geneProt_obj in geneProt_obj_list:
            protein_obj = Protein.objects.filter(geneProt=geneProt_obj)
            peptide_obj_list = Peptide.objects.filter(geneProt=geneProt_obj)
            serialized_peptides = PeptideSerializer(peptide_obj_list,
                                                    fields=(
                                                    'peptideSequence',
                                                    'missedCleavages',
                                                    'length',
                                                    ),
                                                    exclude = False,
                                                    many=True)
            serialized_protein = ProteinSerializer(protein_obj,
                                            fields=(
                                                    'id',
                                                    'proteinNames',
                                                    'geneProt',
                                                    'gene'
                                                    ),
                                            exclude=True,
                                            many=True)
            geneData.append({"proteinData": serialized_protein.data, "peptideData": serialized_peptides.data}) 
    else:
        return JsonResponse({'message': 'The gene does not exist in IBPM Database'},
                            status=status.HTTP_404_NOT_FOUND)
    return JsonResponse({"geneName": geneName, "data": geneData}, safe=False)


 
# Deals with single protein, gives all ibpm information, no phospho data
@api_view(['GET'])
def single_protein_data(request, proteinName):
    proteinName = proteinName.upper()
    try:
        geneProt_obj = GeneProt.objects.get(protName=proteinName) 
        protein_obj = Protein.objects.get(proteinId=proteinName)
        peptide_obj_list = Peptide.objects.filter(geneProt=geneProt_obj)
        # To make sure API format is consistent
        # if peptide_object_list is not a list
        # then we make it into a list
        try:
            temp = len(peptide_obj_list)
        except:
            peptide_obj_list = [peptide_obj_list]
        serialized_peptides = PeptideSerializer(peptide_obj_list,
                                                fields=(
                                                'peptideSequence',
                                                'missedCleavages',
                                                'length',
                                                ),
                                                exclude = False,
                                                many=True)
        serialized_protein = ProteinSerializer(protein_obj,
                                           fields=(
                                                   'id',
                                                   'proteinNames',
                                                   'proteinLength',
                                                   'proteinMass',
                                                   'geneProt',
                                                   'proteinId',
                                                   ),
                                           exclude=True,) 
    except Exception: 
        return JsonResponse({'message': 'The protein does not exist in IBPM Database'},
                            status=status.HTTP_404_NOT_FOUND)
    return JsonResponse({"proteinName": proteinName, "proteinData": serialized_protein.data, "peptideData": serialized_peptides.data}, safe=False)


# Deals with single peptide, gives all ibpm information, no phospho data
@api_view(['GET'])
def single_peptide_data(request, peptideSequence):
    peptideSeq = peptideSequence.upper()
    try: 
        pep_obj = Peptide.objects.filter(peptideSequence=peptideSeq)
        serialized_peptide = PeptideSerializer(pep_obj,
                                           fields=(
                                                   'id',
                                                   'geneProt',
                                                   'peptideSequence'
                                                   ),
                                           exclude=True,
                                           many=True) 
    except Exception: 
        return JsonResponse({'message': 'The peptide does not exist in IBPM Database'},
                            status=status.HTTP_404_NOT_FOUND)
    return JsonResponse({'peptideSequence':peptideSeq,'data': serialized_peptide.data}, safe=False) 


### SINGLE ENTITY REGIONAL DATA ###
# Deals with single gene, gives single region information, no phospho data
@api_view(['GET'])
def single_gene_region_data(request, geneName, region):
    regionName = region.upper()
    if regionName in protein_regions:
        geneName = geneName.upper()
        geneProt_obj_list = GeneProt.objects.filter(geneName=geneName)
        geneData = []
        if len(geneProt_obj_list) > 0:
            for geneProt_obj in geneProt_obj_list:
                protein_obj = Protein.objects.filter(geneProt=geneProt_obj)
                serialized_protein = ProteinSerializer(protein_obj,
                                                fields=(
                                                        'gene',
                                                        f'{regionName}_L_Med',
                                                        f'{regionName}_R_Med',
                                                        f'{regionName}_Med',
                                                        ),
                                                exclude=False,
                                                many=True)
        else:
            return JsonResponse({'message': 'The gene does not exist in IBPM Database'},
                                status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'message': 'The region code does not exist or is incorrect. Please check the region code once or refer API Documentation.'},
                            status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'proteinName':geneName, 'region':regionName, 'data': serialized_protein.data}, safe=False)

# Deals with single protein, gives single region information, no phospho data
@api_view(['GET'])
def single_protein_region_data(request, proteinName, region):
    regionName = region.upper()
    if regionName in protein_regions:
        proteinName = proteinName.upper()
        try: 
            protein_obj = Protein.objects.filter(proteinId=proteinName) 
        except Exception: 
            return JsonResponse({'message': 'The protein does not exist in IBPM Database'},
                                status=status.HTTP_404_NOT_FOUND)
        
        
        serialized_protein = ProteinSerializer(protein_obj,
                                        fields=(
                                                #'proteinId',
                                                'gene',
                                                f'{regionName}_L_Med',
                                                f'{regionName}_R_Med',
                                                f'{regionName}_Med',
                                                ),
                                        exclude=False,
                                        many=True)
    else:
        return JsonResponse({'message': 'The region code does not exist or is incorrect. Please check the region code once or refer API Documentation.'},
                            status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'proteinName':proteinName, 'region':regionName, 'data': serialized_protein.data}, safe=False)


####### PHOSPHO ONLY #######
### ONLY METADATA ###
# Deals with all genes, gives meta information
@api_view(['GET'])
def phospho_gene_list(request):
    all_phospho_peps = PhosphoPeptide.objects.all().order_by('id')
    page = paginator.paginate_queryset(all_phospho_peps, request)
    serialized_page = PhosphoPeptideSerializer(page,
                                         fields=(
                                                 #'peptideSequence',
                                                 #'geneProt',
                                                 'gene',
                                                 #'protein',
                                                 ),
                                         many=True)
    paginated_response = paginator.get_paginated_response(serialized_page.data)
    return paginated_response 
# Deals with all proteins, gives meta information
@api_view(['GET'])
def phospho_protein_list(request):
    all_phospho_peps = PhosphoPeptide.objects.all().order_by('id')
    page = paginator.paginate_queryset(all_phospho_peps, request)
    serialized_page = PhosphoPeptideSerializer(page,
                                         fields=(
                                                 #'peptideSequence',
                                                 #'geneProt',
                                                 #'gene',
                                                 'protein',
                                                 ),
                                         many=True)
    paginated_response = paginator.get_paginated_response(serialized_page.data)
    return paginated_response 
# Deals with all peptides, gives meta information
@api_view(['GET'])
def phospho_peptide_list(request):
    all_phospho_peps = PhosphoPeptide.objects.all().order_by('id')
    page = paginator.paginate_queryset(all_phospho_peps, request)
    serialized_page = PhosphoPeptideSerializer(page,
                                         fields=(
                                                 'peptideSequence',
                                                 #'geneProt',
                                                 'gene',
                                                 'protein',
                                                 ),
                                         many=True)
    paginated_response = paginator.get_paginated_response(serialized_page.data)
    return paginated_response 

### ALL ENTITY ALL DATA ###
# Deals with all genes, gives all ibpm phospho information
#@api_view(['GET'])
#def phospho_gene_data(request):
#    return JsonResponse({"message": "Not yet Implemented"}) 

# Deals with all peptides, gives all ibpm phospho information
#@api_view(['GET'])
#def phospho_protein_data(request):
#    return JsonResponse({"message": "Not yet Implemented"}) 

# Deals with all peptides, gives all ibpm phospho information
@api_view(['GET'])
def phospho_peptide_data(request):
    all_phospho_peps = PhosphoPeptide.objects.all().order_by('id')
    page = paginator.paginate_queryset(all_phospho_peps, request)
    serialized_page = PhosphoPeptideSerializer(page,
                                        fields=(
                                                'id',
                                                'geneProt',
                                               ),
                                        exclude = True,
                                        many=True)
    paginated_response = paginator.get_paginated_response(serialized_page.data)
    return paginated_response 

### SINGLE ENTITY ALL DATA ###
# Deals with single gene, gives all ibpm phospho information
@api_view(['GET'])
def phospho_single_gene_data(request, geneName):
    geneName = geneName.upper()
    try: 
        geneProt_obj = GeneProt.objects.get(geneName=geneName)
    except Exception: 
        return JsonResponse({'message': 'The gene does not exist in IBPM PhosphoProteome Database'},
                            status=status.HTTP_404_NOT_FOUND)
    phospho_obj_list =PhosphoPeptide.objects.filter(geneProt=geneProt_obj)
    if len(phospho_obj_list) == 0:
        return JsonResponse({'message': 'The gene does not exist in IBPM PhosphoProteome Database'},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        serialized_geneprot = GeneProtSerializer(geneProt_obj,
                                                 fields=(
                                                    'geneName',
                                                    'proteinName'
                                                    'proteinLength',
                                                    'proteinMass',
                                                    'chromosome'
                                                    ),
                                                 exclude=False,
                                                 many=True)
        serialized_phospho_list = PhosphoPeptideSerializer(phospho_obj_list,
                                                           fields=(
                                                                    'id',
                                                                    'geneProt',
                                                                    ),
                                                           exclude=True,
                                                           many=True)
    return JsonResponse({'geneData': serialized_geneprot.data, 'phosphoData': serialized_phospho_list.data}, safe=False) 

# Deals with single protein, gives all ibpm phospho information
@api_view(['GET'])
def phospho_single_protein_data(request, proteinName):
    proteinName = proteinName.upper()
    try: 
        geneProt_obj = GeneProt.objects.get(protName=proteinName)
    except Exception: 
        return JsonResponse({'message': 'The protein does not exist in IBPM PhosphoProteome Database'},
                            status=status.HTTP_404_NOT_FOUND)
    phospho_obj_list =PhosphoPeptide.objects.filter(geneProt=geneProt_obj)
    if len(phospho_obj_list) == 0:
        return JsonResponse({'message': 'The protein does not exist in IBPM PhosphoProteome Database'},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        serialized_geneprot = GeneProtSerializer(geneProt_obj,
                                                 fields=(
                                                    'geneName',
                                                    'protName',
                                                    'protLength',
                                                    'protMass',
                                                    'chromosome'
                                                    ),
                                                 exclude=False,
                                                 )
        serialized_phospho_list = PhosphoPeptideSerializer(phospho_obj_list,
                                                           fields=(
                                                                    'id',
                                                                    'geneProt',
                                                                    ),
                                                           exclude=True,
                                                           many=True)
    return JsonResponse({'proteinData':serialized_geneprot.data, 'phosphoData': serialized_phospho_list.data}, safe=False) 

# Deals with single peptide, gives all ibpm phospho information
@api_view(['GET'])
def phospho_single_peptide_data(request, peptideSequence):
    peptideSeq = peptideSequence.upper()
    try: 
        pep_obj = PhosphoPeptide.objects.filter(peptideSequence=peptideSeq)
        serialized_pep = PhosphoPeptideSerializer(pep_obj,
                                           fields=(
                                                   'id',
                                                   'geneProt',
                                                   'peptideSequence'
                                                   ),
                                           exclude=True,
                                           many=True) 
    except Exception: 
        return JsonResponse({'message': 'The peptide does not exist in IBPM Database'},
                            status=status.HTTP_404_NOT_FOUND)
    return JsonResponse({'peptideSequence':peptideSeq, 'phosphoData': serialized_pep.data}, safe=False)



### SINGLE ENTITY REGIONAL DATA ###
@api_view(['GET'])
def phospho_single_gene_region_data(request, geneName, region):
    regionName = region.upper()
    if regionName in phospho_regions:
        geneName = geneName.upper()
        try: 
            geneProt_obj_list = GeneProt.objects.filter(geneName=geneName)
        except Exception: 
            return JsonResponse({'message': 'The gene does not exist in IBPM PhosphoProteome Database'},
                                status=status.HTTP_404_NOT_FOUND)
        phosphoData = []
        for geneProt_obj in geneProt_obj_list:
            phospho_obj_list =PhosphoPeptide.objects.filter(geneProt=geneProt_obj)
            if len(phospho_obj_list) == 0:
                return JsonResponse({'message': 'The gene does not exist in IBPM PhosphoProteome Database'},
                                    status=status.HTTP_404_NOT_FOUND)
            else:
                serialized_phospho_list = PhosphoPeptideSerializer(phospho_obj_list,
                                                fields=(
                                                        'peptideSequence',
                                                        'protein',
                                                        f'{regionName}_L_Phos',
                                                        f'{regionName}_R_Phos',
                                                        'Phospho_LH_Average',
                                                        'Phospho_RH_Average',
                                                        ),
                                                exclude=False,
                                                many=True)
                phosphoData.append(serialized_phospho_list.data)
    else:
        return JsonResponse({'message': 'The region code does not exist or is incorrect. Please check the region code once or refer API Documentation.'},
                            status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'geneName':geneName, 'region':regionName, 'phosphoData': phosphoData}, safe=False)


@api_view(['GET'])
def phospho_single_protein_region_data(request, proteinName, region):
    regionName = region.upper()
    if regionName in phospho_regions:
        proteinName = proteinName.upper()
        try: 
            geneProt_obj = GeneProt.objects.get(protName=proteinName)
        except Exception: 
            return JsonResponse({'message': 'The protein does not exist in IBPM PhosphoProteome Database'},
                                status=status.HTTP_404_NOT_FOUND)
            
        phospho_obj_list =PhosphoPeptide.objects.filter(geneProt=geneProt_obj)
        if len(phospho_obj_list) == 0:
            return JsonResponse({'message': 'The protein does not exist in IBPM PhosphoProteome Database'},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            serialized_phospho_list = PhosphoPeptideSerializer(phospho_obj_list,
                                            fields=(
                                                    'peptideSequence',
                                                    'gene',
                                                    f'{regionName}_L_Phos',
                                                    f'{regionName}_R_Phos',
                                                    'Phospho_LH_Average',
                                                    'Phospho_RH_Average',
                                                    ),
                                            exclude=False,
                                            many=True)
    else:
        return JsonResponse({'message': 'The region code does not exist or is incorrect. Please check the region code once or refer API Documentation.'},
                            status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'proteinName':proteinName, 'region':regionName, 'phosphoData': serialized_phospho_list.data}, safe=False)

@api_view(['GET'])
def phospho_single_peptide_region_data(request, peptideSequence, region):
    regionName = region.upper()
    if regionName in phospho_regions:
        peptideSeq = peptideSequence.upper()
        try: 
            pep_obj = PhosphoPeptide.objects.filter(peptideSequence=peptideSeq) 
        except Exception: 
            return JsonResponse({'message': 'The peptide does not exist in IBPM PhosphoProteome Database'},
                                status=status.HTTP_404_NOT_FOUND)
        
        serialized_pep = PhosphoPeptideSerializer(pep_obj,
                                        fields=(
                                                'gene',
                                                'protein',
                                                f'{regionName}_L_Phos',
                                                f'{regionName}_R_Phos',
                                                'Phospho_LH_Average',
                                                'Phospho_RH_Average',
                                                ),
                                        exclude=False,
                                        many=True)

    else:
        return JsonResponse({'message': 'The region code does not exist or is incorrect. Please check the region code once or refer API Documentation.'},
                            status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'peptideSequence':peptideSeq, 'region':regionName, 'phosphoData': serialized_pep.data}, safe=False) 
