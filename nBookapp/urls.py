from django.conf.urls import url
from django.urls import path
from .views import add_book, add_category,Librarian_index,Inquiry_Delete, User_index,U_success, L_success, contact, Book_Delete,search_book_user, search_book_librarian, update_Book,Book_Borrow, Answer_Inquiry, bookList_L, bookList_U, inquiries, Carrel_List, add_carrel, Reserve, Carrel_Delete, Carrel_List_Lib,userBook_List,returnBook
#from . import views


urlpatterns = [
    path('Librarian_index/', Librarian_index, name='Librarian_index'),
    path('User_index/', User_index, name='User_index'),
    path('L_success/',L_success, name= "L_success"),
    path('U_success/',U_success, name= "U_success"),
    path('Book_List_Librarian/',bookList_L,name ="Book_List_Librarian"),
    path('Book_List_User/',bookList_U,name ="Book_List_User"),
    path('User_search/',search_book_user,name ="User_search"),
    path('Librarian_search/',search_book_librarian, name ="Librarian_search"),
    path('Answer_Inquiry/<int:pk>',Answer_Inquiry,name ="Answer_Inquiry"),
    path('inquiries/',inquiries,name ="inquiries"),
    path('update_Book/<int:id>', update_Book, name="update_Book"),
    path('borrow_Book/<int:pk>',Book_Borrow,name = "Book_Borrow"),
    path('myBooks/',userBook_List,name = "userBooks"),
    path('returnBook/<int:pk>',returnBook,name = "returnBook"),

    #  url('Book_Delete/Book_Delete', success),
    #  url('Book_Delete/Book_List', Book_List.as_view()),
     #url('^$', add_book)
    #  url(r'^$', index),
    #  url(r'^index', index),
    path('contact/',contact,name ="contact"),
    path('add_book/',add_book,name ="add_book"),
    path('add_category/',add_category,name ="add_category"),

    #  path('add_category',add_category,name = "add_category"),
     #url(r'^contact', contact),
    #  url(r'^Book_List', Book_List.as_view()),
     #url(r'^Book_Delete', Book_Delete),
     path('Book_Delete/<int:pk>', Book_Delete,name = "Book_Delete"),
    path('Inquiry_Delete/<int:pk>', Inquiry_Delete,name = "Inquiry_Delete"),
    path('Carrel_Delete/<int:pk>', Carrel_Delete,name = "Carrel_Delete"),
    path('Carrel_List', Carrel_List, name = "Carrel_List"),
    path('Carrel_List_Lib', Carrel_List_Lib, name = "Carrel_List_Lib"),
    path('Reserve/<int:pk>', Reserve, name = "Reserve"),
    path('add_carrel', add_carrel, name = "add_carrel"),
    #path('Carrel_validation', Carrel_validation, name = "Carrel_validation")
    #  path('Book_Delete/<int:pk>/Book_Delete/Book_List', Book_List,name = "Book_List"),
    #  path('Book_Delete/<int:pk>/Book_List', Book_Delete,name = ),
     #path('<int:id>/Book_Delete/', Book_Delete)
     #path('Book_Delete', Book_Delete),
]