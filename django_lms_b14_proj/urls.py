"""
URL configuration for django_lms_b14_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Use include() to add paths from the catalog application
    # This is to Create an URL Path - which if accessed will open the URL File in APP DIRECTORY
    path('library/', include('lms_app.urls'))
]

    # Adding URL Maps to redirect to MAIN URL - whenever the server is accessed
from django.views.generic import RedirectView

urlpatterns += [
    path('',RedirectView.as_view(url='library/', permanent = False)),
]
