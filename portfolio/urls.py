from django.urls import path, include
from . import views

app_name='portfolio'

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name="logout"),
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills')
]