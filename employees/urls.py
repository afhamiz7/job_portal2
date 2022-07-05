from django.urls import path
from . import views

urlpatterns=[

    path('login',views.user_login),
    path('home',views.user_home),
    
    
    ]


