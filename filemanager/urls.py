# urls.py in filemanager
from django.urls import path
from . import views

urlpatterns = [
    path('files/', views.file_list, name='file_list'),  # Aufruf der richtigen View-Funktion
]
