from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start-camera/', views.start_camera, name='start_camera'),
    path('stop-camera/', views.stop_camera, name='stop_camera'),
    path('download-excel/', views.download_excel, name='download_excel'),
    path('HOG.py', views.process_image, name='process_image'),
]
