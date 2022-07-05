from django.urls import path
from . import views

urlpatterns=[
   path('login',views.user_login,name='user'),
    path('view',views.view_emp,name='view_employees'),
   

]
