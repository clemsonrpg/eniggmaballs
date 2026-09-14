from django.urls import path
from . import views

urlpatterns = [
    path('memento', views.memento, name='memento'),
    path('origem', views.origem, name='origem'),
    path("download-memento/",views.download_memento,name="download_memento"),
]