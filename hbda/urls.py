from django.urls import path, re_path

from . import views

app_name = 'hbda'

urlpatterns = [
    #path('', views.index, name='index'),

    # Single Disease
    path('api/hbda/disease/<str:diseaseId>', views.get_disease_data, name='get_disease_data'),

    # Cache Delete
    path('hbda/delete_cache', views.delete_hbda_cache, name='delete_hbda_cache'),

    # All Disease Metadata
    path('api/hbda/disease_table', views.get_disease_table, name='get_disease_table')
]
