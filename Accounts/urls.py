from django.urls import path
from .views import loginPage,User_registerPage,loginPage_L,activate#,Librarian_index,User_index

urlpatterns = [
    path('Librarian_login/',loginPage_L,name='Librarian_login'),
    path('',loginPage,name='User_login'),
    path('register/',User_registerPage,name='register'),
    path('activate/<int:token>',activate,name = 'Activate')
    #path('Librarian_index/', Librarian_index, name='Librarian_index'),
    #path('User_index/', User_index, name='User_index'),
]
