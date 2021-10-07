from django.urls import path
from . import views

app_name = 'carusel'
urlpatterns = [
    path('', views.index,name='index'),
]
