from django.urls import path
from . import views

app_name = 'paste'
urlpatterns = [
    path('yourdata', views.Data, name='data'),
    path('publicpastes', views.public, name='datalist'),
    path('thanks', views.Complete, name='done'),
]