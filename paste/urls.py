from django.urls import path
from . import views
urlpatterns = [
    path('yourdata', views.Data, name='data'),
    path('publicpastes', views.public, name='datalist'),
]