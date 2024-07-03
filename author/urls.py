from django.urls import path, include
from . import views

urlpatterns = [
    path('Add_Musicians/', views.add_musicians, name='add_musicians'),
]
