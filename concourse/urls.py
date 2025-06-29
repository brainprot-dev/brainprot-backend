from django.urls import path, re_path
from . import views

# For Testing Purposes of API
# CSRF Exempt excluses CSRF Checking for particular views. 
# Do not use it in Production!
from django.views.decorators.csrf import csrf_exempt 

app_name = 'concourse'

urlpatterns = [
    # Index
    path('', views.index, name='index'),
    # Deals with all team-members
    path('api/team-members', views.team_member_list, name='team_member_list'), 
    # Get a particular team member details with <pk> id 
    re_path(r'^api/team-members/(?P<pk>[0-9]+)', views.team_member_detail, name='team_member_detail'),
    
    # Deals with all posts
    path('api/posts', csrf_exempt(views.post_list), name='post_list'), 
    # Get a particular team member details with <pk> id 
    re_path(r'^api/posts/(?P<pk>[0-9]+)/', views.post_detail, name='post_detail'),
    # Get all published posts (posts with status published)
    path('api/posts/published', views.post_published_list, name='post_published_list'),
    # Get all draft posts (posts with status published)
    path('api/posts/drafts', views.post_drafts_list, name='post_drafts_list'),

    # Search
    # Unified search endpoints
    path('search/', views.unified_search, name='unified-search'),
    path('search/simple/', views.simple_unified_search, name='simple-unified-search'),
    
    # Legacy support
    path('search/<str:query>/', views.search, name='search-with-param'),

    #Debug
    # path('debug-search/', views.debug_search, name='debug-search'),
    # path('debug-search/<str:query>/', views.debug_search, name='debug-search-with-param'),
    # path('test-db/', views.test_basic_queries, name='test-db'),
]
