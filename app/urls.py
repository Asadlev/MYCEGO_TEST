from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('download/<path:path>/', views.download_file, name='download_file'),
]
