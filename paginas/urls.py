from django.urls import path
from . import views

urlpatterns = [
    path('memento', views.memento, name='memento'),
]