from django.urls import path
from . import views


urlpatterns = [
    path('project/<str:pk>/', views.project, name = "project")
]

