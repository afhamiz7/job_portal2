from nturl2path import url2pathname
from django.urls import path
from . import views
app_name='jbskr'

urlpatterns=[

    path('login',views.user_login),
    path('jobsearch',views.search_job),
    path('jobdetails',views.details_job,name='jobdetails'),
    
    ]

