from django.urls import path
from . import views

app_name = 'paste'
urlpatterns = [
    path('yourdata', views.Data, name='data'),
    path('thanks', views.Complete, name='done'),
    path('detailed/<str:str>',views.detailed, name='detailed'),
]