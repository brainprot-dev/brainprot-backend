import requests
import json
import environ

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from concourse.models import Post, TeamMember
from concourse.serializers import PostSerializer, TeamMemberSerializer
from rest_framework.decorators import api_view


# New Search Stuff Imports
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q, F, Case, When, IntegerField, FloatField
from django.db.models.functions import Greatest, Length
from ibpm.models import GeneProt
from ibpm.serializers import GeneProtSerializer
from rest_framework.response import Response
import re

# Initialise environment variables 
env = environ.Env()
environ.Env.read_env()

def index(request):
    return HttpResponse("API Index Page. Please check API Help to understand how to use the API.")

@api_view(['GET', 'POST', 'DELETE'])
def post_list(request):
    # GET list of posts, POST a new post, DELETE all posts
    if request.method == 'GET':
        posts = Post.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            posts = posts.filter(title__icontains=title)
        
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Post.objects.all().delete()
        return JsonResponse({f'message': '{count[0]} Posts were deleted successfully!'},
                             status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    # find post by pk (id)
    try: 
        post = Post.objects.get(pk=pk) 
    except Post.DoesNotExist: 
        return JsonResponse({'message': 'The post does not exist'},
                            status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE 
    if request.method == 'GET': 
        post_serializer = PostSerializer(post) 
        return JsonResponse(post_serializer.data)

    elif request.method == 'DELETE': 
        post.delete() 
        return JsonResponse({'message': 'The post was deleted successfully!'},
                             status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        post_data = JSONParser().parse(request) 
        post_serializer = PostSerializer(post, data=post_data) 
        if post_serializer.is_valid(): 
            post_serializer.save() 
            return JsonResponse(post_serializer.data) 
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

        
@api_view(['GET'])
def post_published_list(request):
    # GET all published posts
    posts = Post.objects.filter(status=1)
        
    if request.method == 'GET': 
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)

@api_view(['GET'])
def post_drafts_list(request):
    # GET all draft posts
    posts = Post.objects.filter(status=0)
        
    if request.method == 'GET': 
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)

### TEAM MEMBERS ###
@api_view(['GET', 'POST', 'DELETE'])
def team_member_list(request):
    # GET list of team-members, POST a new team-member, DELETE all team-members
    if request.method == 'GET':
        members = TeamMember.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            members = members.filter(name__icontains=name)
        
        members_serializer = TeamMemberSerializer(members, many=True)
        return JsonResponse(members_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        member_data = JSONParser().parse(request)
        member_serializer = TeamMemberSerializer(data=member_data)
        if member_serializer.is_valid():
            member_serializer.save()
            return JsonResponse(member_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = TeamMember.objects.all().delete()
        return JsonResponse({f'message': '{count[0]} Team members were deleted successfully!'},
                             status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def team_member_detail(request, pk):
    # find teammember by pk (id)
    try: 
        member = TeamMember.objects.get(pk=pk) 
    except TeamMember.DoesNotExist: 
        return JsonResponse({'message': 'The team member does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE 
    if request.method == 'GET': 
        member_serializer = TeamMemberSerializer(member) 
        return JsonResponse(member_serializer.data)

    elif request.method == 'DELETE': 
        member.delete() 
        return JsonResponse({'message': 'The team member was deleted successfully!'},
                             status=status.HTTP_204_NO_CONTENT) 

    elif request.method == 'PUT': 
        member_data = JSONParser().parse(request) 
        member_serializer = PostSerializer(member, data=member_data) 
        if member_serializer.is_valid(): 
            member_serializer.save() 
            return JsonResponse(member_serializer.data) 
        return JsonResponse(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

@api_view(['GET'])
def unified_search(request):
    """
    Unified search that combines exact, partial, full-text, and similarity matching
    with intelligent ranking and deduplication
    """
    query = request.GET.get('q', '').strip()
    
    if not query:
        return Response({
            'results': [],
            'total_count': 0,
            'query': '',
            'message': 'Query parameter "q" is required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    limit = int(request.GET.get('limit', 50))
    min_similarity = float(request.GET.get('min_similarity', 0.1))
    
    try:
        # Clean query for similarity matching
        clean_query = re.sub(r'[^\w\s-]', '', query)
        
        # Create search vector for full-text search
        search_vector = SearchVector(
            'geneName', weight='A'
        ) + SearchVector(
            'protName', weight='A'
        ) + SearchVector(
            'entryName', weight='B'
        ) + SearchVector(
            'altGeneNames', weight='B'
        ) + SearchVector(
            'geneProtFullNames', weight='C'
        )
        
        search_query = SearchQuery(query)
        
        # Build the unified query with multiple ranking factors
        results = GeneProt.objects.annotate(
            # 1. Exact match scoring (highest priority)
            exact_match_score=Case(
                When(Q(geneName__iexact=query), then=100),
                When(Q(protName__iexact=query), then=95),
                When(Q(entryName__iexact=query), then=90),
                When(Q(altGeneNames__iexact=query), then=85),
                When(Q(geneProtFullNames__iexact=query), then=80),
                default=0,
                output_field=IntegerField()
            ),
            
            # 2. Starts with scoring (high priority)
            starts_with_score=Case(
                When(Q(geneName__istartswith=query), then=75),
                When(Q(protName__istartswith=query), then=70),
                When(Q(entryName__istartswith=query), then=65),
                When(Q(altGeneNames__istartswith=query), then=60),
                default=0,
                output_field=IntegerField()
            ),
            
            # 3. Contains scoring (medium priority)
            contains_score=Case(
                When(Q(geneName__icontains=query), then=50),
                When(Q(protName__icontains=query), then=45),
                When(Q(entryName__icontains=query), then=40),
                When(Q(altGeneNames__icontains=query), then=35),
                When(Q(geneProtFullNames__icontains=query), then=30),
                default=0,
                output_field=IntegerField()
            ),
            
            # 4. Full-text search ranking
            search_vector_field=search_vector,
            fulltext_rank=SearchRank(search_vector, search_query),
            
            # 5. Trigram similarity scoring
            trigram_similarity=Greatest(
                TrigramSimilarity('geneName', clean_query),
                TrigramSimilarity('protName', clean_query),
                TrigramSimilarity('entryName', clean_query),
                TrigramSimilarity('altGeneNames', clean_query),
                TrigramSimilarity('geneProtFullNames', clean_query)
            ),
            
            # 6. Length-based scoring (shorter matches are often more relevant)
            # Handle empty geneName field gracefully
            length_score=Case(
                When(Q(geneName__icontains=query) & ~Q(geneName=''), 
                     then=100.0 / (Length('geneName') + 1)),
                When(Q(protName__icontains=query), 
                     then=90.0 / (Length('protName') + 1)),
                default=0,
                output_field=FloatField()
            ),
            
            # 7. Combined final score
            final_score=(
                F('exact_match_score') +
                F('starts_with_score') +
                F('contains_score') +
                (F('fulltext_rank') * 25) +  # Scale full-text rank
                (F('trigram_similarity') * 40) +  # Scale similarity
                F('length_score')
            )
        ).filter(
            # Include results that match any of these criteria
            # Handle empty geneName gracefully in filters
            Q(exact_match_score__gt=0) |
            Q(starts_with_score__gt=0) |
            Q(contains_score__gt=0) |
            Q(fulltext_rank__gt=0.01) |
            Q(trigram_similarity__gt=min_similarity) |
            Q(search_vector_field=search_query)
        ).order_by(
            '-final_score',  # Primary sort by combined score
            '-exact_match_score',  # Secondary sort by exact matches
            '-starts_with_score',  # Tertiary sort
            'protName'  # Final sort by protein name for consistency
        ).distinct()[:limit]
        
        # Serialize results
        serializer = GeneProtSerializer(results, many=True)
        
        # Add scoring information to each result for debugging/transparency
        enhanced_results = []
        for i, result in enumerate(results):
            result_data = serializer.data[i]
            result_data['match_info'] = {
                'final_score': float(result.final_score or 0),
                'exact_match_score': result.exact_match_score,
                'starts_with_score': result.starts_with_score,
                'contains_score': result.contains_score,
                'fulltext_rank': float(result.fulltext_rank or 0),
                'trigram_similarity': float(result.trigram_similarity or 0),
                'length_score': float(result.length_score or 0)
            }
            enhanced_results.append(result_data)
        
        return Response({
            'results': enhanced_results,
            'total_count': len(enhanced_results),
            'query': query,
            'search_strategy': 'unified',
            'parameters': {
                'limit': limit,
                'min_similarity': min_similarity
            }
        })
        
    except Exception as e:
        return Response({
            'error': f'Search failed: {str(e)}',
            'results': [],
            'total_count': 0,
            'query': query
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def simple_unified_search(request):
    """
    Simplified version of unified search without detailed scoring
    """
    query = request.GET.get('q', '').strip()
    
    if not query:
        return Response({
            'results': [],
            'total_count': 0,
            'query': '',
            'message': 'Query parameter "q" is required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    limit = int(request.GET.get('limit', 50))
    
    try:
        # Clean query
        clean_query = re.sub(r'[^\w\s-]', '', query)
        
        # Create search components
        search_vector = SearchVector('geneName', 'protName', 'entryName', 'altGeneNames', 'geneProtFullNames')
        search_query = SearchQuery(query)
        
        # Unified query with simplified scoring
        results = GeneProt.objects.annotate(
            # Simple combined score
            combined_score=Case(
                # Exact matches (highest priority)
                When(Q(geneName__iexact=query) | Q(protName__iexact=query), then=100),
                When(Q(entryName__iexact=query) | Q(altGeneNames__iexact=query), then=90),
                
                # Starts with matches
                When(Q(geneName__istartswith=query) | Q(protName__istartswith=query), then=80),
                
                # Contains matches
                When(Q(geneName__icontains=query) | Q(protName__icontains=query), then=70),
                When(Q(entryName__icontains=query) | Q(altGeneNames__icontains=query), then=60),
                When(Q(geneProtFullNames__icontains=query), then=50),
                
                # Full-text and similarity fallback
                default=40,
                output_field=IntegerField()
            ),
            
            # Add full-text ranking
            fulltext_rank=SearchRank(search_vector, search_query),
            
            # Add trigram similarity
            similarity=Greatest(
                TrigramSimilarity('geneName', clean_query),
                TrigramSimilarity('protName', clean_query),
                TrigramSimilarity('entryName', clean_query),
                TrigramSimilarity('altGeneNames', clean_query),
                TrigramSimilarity('geneProtFullNames', clean_query)
            )
        ).filter(
            Q(geneName__icontains=query) |
            Q(protName__icontains=query) |
            Q(entryName__icontains=query) |
            Q(altGeneNames__icontains=query) |
            Q(geneProtFullNames__icontains=query) |
            Q(search_vector=search_query) |
            Q(similarity__gt=0.1)
        ).order_by(
            '-combined_score',
            '-fulltext_rank',
            '-similarity',
            'protName'  # Sort by protName since it's unique
        ).distinct()[:limit]
        
        serializer = GeneProtSerializer(results, many=True)
        
        return Response({
            'results': serializer.data,
            'total_count': len(serializer.data),
            'query': query,
            'search_strategy': 'simple_unified'
        })
        
    except Exception as e:
        return Response({
            'error': f'Search failed: {str(e)}',
            'results': [],
            'total_count': 0,
            'query': query
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Legacy endpoint for backward compatibility
@api_view(['GET'])
def search(request, query=None):
    """
    Legacy search endpoint - redirects to unified search
    """
    # Extract the query parameter
    if query:
        # Query is from URL path parameter
        search_query = query
    else:
        # Query is from GET parameter
        search_query = request.GET.get('q', '').strip()
    
    if not search_query:
        return Response({
            'results': [],
            'total_count': 0,
            'query': '',
            'message': 'Query parameter required'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Get other parameters
    limit = int(request.GET.get('limit', 50))
    
    try:
        # Build search with intelligent ranking using basic Django ORM
        results = GeneProt.objects.annotate(
            # Simple ranking system
            relevance_score=Case(
                # Exact matches get highest scores
                When(Q(geneName__iexact=search_query) & ~Q(geneName=''), then=100),
                When(Q(protName__iexact=search_query), then=95),
                When(Q(entryName__iexact=search_query), then=90),
                
                # Starts with matches get high scores
                When(Q(geneName__istartswith=search_query) & ~Q(geneName=''), then=80),
                When(Q(protName__istartswith=search_query), then=75),
                When(Q(entryName__istartswith=search_query), then=70),
                
                # Contains matches get medium scores
                When(Q(geneName__icontains=search_query) & ~Q(geneName=''), then=60),
                When(Q(protName__icontains=search_query), then=55),
                When(Q(entryName__icontains=search_query), then=50),
                When(Q(altGeneNames__icontains=search_query), then=45),
                When(Q(geneProtFullNames__icontains=search_query), then=40),
                
                # Default score for other matches
                default=30,
                output_field=IntegerField()
            )
        ).filter(
            # Search across all text fields, handling empty geneName
            Q(geneName__icontains=search_query, geneName__gt='') |
            Q(protName__icontains=search_query) |
            Q(entryName__icontains=search_query) |
            Q(altGeneNames__icontains=search_query) |
            Q(geneProtFullNames__icontains=search_query)
        ).order_by(
            '-relevance_score',  # Best matches first
            'protName'  # Consistent secondary sort
        )[:limit]
        
        # Serialize results
        serializer = GeneProtSerializer(results, many=True)
        
        return Response({
            'results': serializer.data,
            'total_count': len(serializer.data),
            'query': search_query,
            'search_type': 'legacy_unified'
        })
        
    except Exception as e:
        return Response({
            'error': f'Search failed: {str(e)}',
            'results': [],
            'total_count': 0,
            'query': search_query
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['GET'])
# def debug_search(request, query=None):
#     """
#     Debug search with detailed logging to help troubleshoot
#     """
#     # Get query from URL parameter or GET parameter
#     if query:
#         search_query = query.strip()
#     else:
#         search_query = request.GET.get('q', '').strip()
    
#     if not search_query:
#         return Response({
#             'results': [],
#             'total_count': 0,
#             'query': '',
#             'message': 'Query parameter required'
#         }, status=status.HTTP_400_BAD_REQUEST)
    
#     # Clean the query (remove trailing slashes, etc.)
#     clean_query = search_query.rstrip('/')
    
#     limit = int(request.GET.get('limit', 50))
    
#     try:
#         # Debug info
#         debug_info = {
#             'original_query': search_query,
#             'cleaned_query': clean_query,
#             'total_records': GeneProt.objects.count()
#         }
        
#         # Test different search strategies individually
#         exact_protName = GeneProt.objects.filter(protName__iexact=clean_query)
#         exact_geneName = GeneProt.objects.filter(geneName__iexact=clean_query, geneName__gt='')
#         exact_entryName = GeneProt.objects.filter(entryName__iexact=clean_query)
        
#         contains_protName = GeneProt.objects.filter(protName__icontains=clean_query)
#         contains_geneName = GeneProt.objects.filter(geneName__icontains=clean_query, geneName__gt='')
#         contains_entryName = GeneProt.objects.filter(entryName__icontains=clean_query)
#         contains_altNames = GeneProt.objects.filter(altGeneNames__icontains=clean_query)
#         contains_fullNames = GeneProt.objects.filter(geneProtFullNames__icontains=clean_query)
        
#         debug_info.update({
#             'exact_matches': {
#                 'protName': exact_protName.count(),
#                 'geneName': exact_geneName.count(),
#                 'entryName': exact_entryName.count()
#             },
#             'contains_matches': {
#                 'protName': contains_protName.count(),
#                 'geneName': contains_geneName.count(),
#                 'entryName': contains_entryName.count(),
#                 'altGeneNames': contains_altNames.count(),
#                 'geneProtFullNames': contains_fullNames.count()
#             }
#         })
        
#         # Get sample matches for debugging
#         if exact_protName.exists():
#             debug_info['sample_exact_protName'] = {
#                 'protName': exact_protName.first().protName,
#                 'geneName': exact_protName.first().geneName,
#                 'entryName': exact_protName.first().entryName,
#                 'geneProtFullNames': exact_protName.first().geneProtFullNames[:100] + '...' if len(exact_protName.first().geneProtFullNames) > 100 else exact_protName.first().geneProtFullNames
#             }
        
#         # Main search query
#         results = GeneProt.objects.annotate(
#             relevance_score=Case(
#                 # Exact matches get highest scores
#                 When(Q(geneName__iexact=clean_query) & ~Q(geneName=''), then=100),
#                 When(Q(protName__iexact=clean_query), then=95),
#                 When(Q(entryName__iexact=clean_query), then=90),
                
#                 # Starts with matches get high scores  
#                 When(Q(geneName__istartswith=clean_query) & ~Q(geneName=''), then=80),
#                 When(Q(protName__istartswith=clean_query), then=75),
#                 When(Q(entryName__istartswith=clean_query), then=70),
                
#                 # Contains matches get medium scores
#                 When(Q(geneName__icontains=clean_query) & ~Q(geneName=''), then=60),
#                 When(Q(protName__icontains=clean_query), then=55),
#                 When(Q(entryName__icontains=clean_query), then=50),
#                 When(Q(altGeneNames__icontains=clean_query), then=45),
#                 When(Q(geneProtFullNames__icontains=clean_query), then=40),
                
#                 default=30,
#                 output_field=IntegerField()
#             )
#         ).filter(
#             # Search across all fields
#             Q(geneName__icontains=clean_query, geneName__gt='') |
#             Q(protName__icontains=clean_query) |
#             Q(entryName__icontains=clean_query) |
#             Q(altGeneNames__icontains=clean_query) |
#             Q(geneProtFullNames__icontains=clean_query)
#         ).order_by(
#             '-relevance_score',
#             'protName'
#         )[:limit]
        
#         serializer = GeneProtSerializer(results, many=True)
        
#         return Response({
#             'results': serializer.data,
#             'total_count': len(serializer.data),
#             'query': search_query,
#             'cleaned_query': clean_query,
#             'search_type': 'debug',
#             'debug_info': debug_info
#         })
        
#     except Exception as e:
#         return Response({
#             'error': f'Search failed: {str(e)}',
#             'results': [],
#             'total_count': 0,
#             'query': search_query,
#             'debug_info': debug_info if 'debug_info' in locals() else {}
#         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['GET'])
# def test_basic_queries(request):
#     """
#     Test basic database queries to verify data is loaded
#     """
#     try:
#         total_count = GeneProt.objects.count()
        
#         # Get some sample records
#         sample_records = GeneProt.objects.all()[:5]
#         samples = []
#         for record in sample_records:
#             samples.append({
#                 'protName': record.protName,
#                 'geneName': record.geneName,
#                 'entryName': record.entryName,
#                 'geneProtFullNames': record.geneProtFullNames[:100] + '...' if len(record.geneProtFullNames) > 100 else record.geneProtFullNames
#             })
        
#         # Test specific queries
#         p_proteins = GeneProt.objects.filter(protName__startswith='P').count()
#         a_proteins = GeneProt.objects.filter(protName__startswith='A').count()
        
#         # Test for P04745 specifically
#         p04745_exact = GeneProt.objects.filter(protName='P04745')
#         p04745_data = None
#         if p04745_exact.exists():
#             record = p04745_exact.first()
#             p04745_data = {
#                 'protName': record.protName,
#                 'geneName': record.geneName,
#                 'entryName': record.entryName,
#                 'geneProtFullNames': record.geneProtFullNames
#             }
        
#         return Response({
#             'database_status': 'connected',
#             'total_records': total_count,
#             'sample_records': samples,
#             'statistics': {
#                 'proteins_starting_with_P': p_proteins,
#                 'proteins_starting_with_A': a_proteins
#             },
#             'p04745_search': {
#                 'found': p04745_exact.exists(),
#                 'data': p04745_data
#             }
#         })
        
#     except Exception as e:
#         return Response({
#             'error': f'Database test failed: {str(e)}',
#             'database_status': 'error'
#         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)