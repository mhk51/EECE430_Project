from django.urls import path
from .views import loginPage,registerPage

urlpatterns = [
    path('',loginPage,name='login'),
    path('register/',registerPage,name='register'),
]
