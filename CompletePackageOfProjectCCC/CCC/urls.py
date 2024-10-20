from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('jobrole/', views.jobrole, name='jobrole'),
    path('location/', views.location, name='location'),
    path('description/', views.description, name='description'),
    path('loginToReg/', views.LoginToReg, name='loginToReg'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.user_logout, name='logout'),  # Add this route
]
