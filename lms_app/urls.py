from django.urls import path
from . import views

urlpatterns = [

    # When a URL is accessed, the Function in the View.py file will be accessed and run
    path('', views.index, name='index'), # Route is Main URL: /library/
    path('about-us/', views.about_us, name='about_us') # Route is: /library/about-us/
]