from django.conf.urls import url
from django.urls import path
from .views import add_book, add_category, success, index, contact, Book_List, Book_Delete
#from . import views
urlpatterns = [
#    path('', views.index, name='index'),
     url('success/', success),
     url('success/index', index),
     url('Book_Delete/success/index', index),
     url('Book_Delete/Book_Delete', success),
     url('Book_Delete/Book_List', Book_List.as_view()),
     url('Book_Delete/Book_List/index', index),
     url('Book_Delete/index.html', index),
     #url('^$', add_book)
     url(r'^$', index),
     url(r'^index', index),
     url(r'^add_book', add_book),
     url(r'^add_category', add_category),
     url(r'^contact', contact),
     url(r'^Book_List', Book_List.as_view()),
     #url(r'^Book_Delete', Book_Delete),
     path('Book_Delete/<int:pk>', Book_Delete),
     path('Book_Delete/<int:pk>/Book_Delete/Book_List', Book_List),
     path('Book_Delete/<int:pk>/Book_List', Book_Delete),
     #path('<int:id>/Book_Delete/', Book_Delete)
     #path('Book_Delete', Book_Delete),
]