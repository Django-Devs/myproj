from django.urls import path
from . import views

urlpatterns=[
    path('',views.iregister,name='register'),
    path('login',views.ilogin, name='login'),
]