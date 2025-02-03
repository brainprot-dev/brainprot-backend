from django.urls import path, re_path

from . import views

app_name = 'hbda'

urlpatterns = [
    #path('', views.index, name='index'),

    # All Disease Metadata
    path('api/hbda/disease_table', views.get_disease_table, name='get_disease_table')
]
