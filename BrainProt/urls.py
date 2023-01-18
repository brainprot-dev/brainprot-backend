"""BrainProt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

admin.site.site_header = "BrainProt Admin"
admin.site.site_title = "BrainProt Admin Portal"
admin.site.index_title = "Welcome to BrainProt Admin Panel"

# The name space thing really helps with templates
# We can use the {% url %} tag
# Read more in documentation

# Check if using re_path (RegEx Path) is better
urlpatterns = [
    # Main Paths
    path('',include(('concourse.urls', 'concourse'), namespace='concourse')),
    path('bp-admin/', admin.site.urls),


    # Individual Portal Paths
    path('',include(('ibpm.urls', 'ibpm'), namespace='ibpm')),
    path('',include(('bdtm.urls', 'bdtm'), namespace='bdtm')),
    path('',include(('bdpm.urls', 'bdpm'), namespace='bdpm')),
    path('',include(('bdmc.urls', 'bdmc'), namespace='bdmc')),
    path('',include(('bddf.urls', 'bddf'), namespace='bddf')),
    path('',include(('hbda.urls', 'hbda'), namespace='hbda')),
]
