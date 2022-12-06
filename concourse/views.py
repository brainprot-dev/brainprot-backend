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
def search(request, query):
    if request.method == 'GET':
        search_response = requests.get(f'https://{env("SERVER_IP")}:{env("SERVER_PORT")}/{env("INDEX")}/select?q={query}', verify=False, auth=(env('USER'), env('PASS')))
        response_dict = json.loads(search_response.text)
        print(response_dict)
        return JsonResponse(response_dict)
