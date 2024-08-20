from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutPage, name = "logout"),
    path('register/', views.registerPage, name = "register"),

    path('', views.profiles, name = "profiles"),
    path('profile/<str:pk>/', views.userprofile, name = "user-profile"),
    path('account/', views.userAccount, name = "account"),
    path('editAccount/', views.editAccount, name = "edit-account"),
    path('addSkill/', views.addSkill, name= "add-skill"),
    path('updateSkill/<str:pk>/', views.updateSkill, name = "update-skill"),
    path('deleteSkill/<str:pk>/', views.deleteSkill, name = "delete-skill"),
]
