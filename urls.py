from django.urls import path
from . import views


urlpatterns = [
    path('add', views.addTask, name="addTask"),
    path('view', views.viewTask, name="viewTask"),
    path('delete', views.deleteTask, name="deleteTask")
]