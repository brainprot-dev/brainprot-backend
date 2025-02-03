from django.shortcuts import render
from django.http import HttpResponse
from sklearn.preprocessing import MinMaxScaler
from hbda.models import Disease
from hbda.serializers import DiseaseSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.conf import settings

import requests
import environ
import urllib.parse
import time
import requests
import json
import os, shutil
import pandas as pd



# Create your views here.
# Initialise environment and global variables 
env = environ.Env()
environ.Env.read_env()

@api_view(['GET'])
def get_disease_table(request):
    all_disease_objects = Disease.objects.all().order_by('diseaseName')

    serialized_disease_objects = DiseaseSerializer(all_disease_objects,
                                                    fields=(),
                                                    exclude=True,
                                                    many=True
                                                    )

    return JsonResponse({'diseaseTableData': serialized_disease_objects.data})
                                                
