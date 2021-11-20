from django.conf.urls import url
from django.urls import path
from .views import add_book, add_category, success, index, contact, Book_List, Book_Delete,bookList,search_book
#from . import views


urlpatterns = [
    path('', index, name='index'),
    path('success/',success, name= "success"),
    path('Book_List/',bookList,name ="Book_List"),
    path('search/',search_book,name ="search"),
    #  url('Book_Delete/Book_Delete', success),
    #  url('Book_Delete/Book_List', Book_List.as_view()),
     #url('^$', add_book)
    #  url(r'^$', index),
    #  url(r'^index', index),
     url(r'^add_book', add_book),
     url(r'^add_category', add_category),
    #  path('add_category',add_category,name = "add_category"),
     url(r'^contact', contact),
    #  url(r'^Book_List', Book_List.as_view()),
     #url(r'^Book_Delete', Book_Delete),
     path('Book_Delete/<int:pk>', Book_Delete,name = "Book_Delete"),
    #  path('Book_Delete/<int:pk>/Book_Delete/Book_List', Book_List,name = "Book_List"),
    #  path('Book_Delete/<int:pk>/Book_List', Book_Delete,name = ),
     #path('<int:id>/Book_Delete/', Book_Delete)
     #path('Book_Delete', Book_Delete),
]