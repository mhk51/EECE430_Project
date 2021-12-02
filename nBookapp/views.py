import os

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateCategoryForm, CreateBookForm, CreateContactForm, CreateCarrelForm
from .models import *
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.urls import reverse
from datetime import datetime, timedelta


class Book_List(ListView):
    model = Book
    
def bookList_L(request):
    item = Book.objects.all()
    # print("Myoutput", item)
    return render(request, 'nBookapp/Book_Details_Librarian.html', {'item':item})

def bookList_U(request):
    item = Book.objects.all()
    # print("Myoutput", item)
    return render(request, 'nBookapp/Book_Details_User.html', {'item':item})

# def confirm_Delete(request,pk):
#     instance = Book.objects.get(pk=id)
#     return render(request,"nBookapp/Book_Delete.html",{'title':instance.title})



def Librarian_index(request):
    return render(request, 'nBookapp/Librarian_index.html')
def User_index(request):
    return render(request, 'nBookapp/User_index.html')
def inquiries(request):
    ques = Contact.objects.all()
    return render(request, 'nBookapp/inquiries.html', {'ques':ques})


def contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            username = formdata['username']
            email = formdata['email']
            subject = formdata['subject']
            Contact.objects.create(username=username, email=email, subject=subject)
            return HttpResponseRedirect(reverse('U_success'))
    else:
        form = CreateContactForm()
    return render(request, 'nBookapp/contact.html', {'form': form})


def add_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            title = formdata['title']
            ISBN = formdata['ISBN']
            author = formdata['author']
            category = formdata['category']
            price = formdata['price']
            # coverpage = formdata['coverpage']
            summary = formdata['summary']
            # owner = formdata['owner']
            # isBorrowed = formdata['isBorrowed']
            # pdf = formdata['pdf']
            Book.objects.create(title=title, author=author, ISBN=ISBN, category=category, price=price, summary=summary,isBorrowed=False,owner = 'No owner',remainingDays=30,borrowed_time = datetime.now())
            return HttpResponseRedirect(reverse('L_success'))
    else:
        form = CreateBookForm()
    return render(request, 'nBookapp/add_book.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            name = formdata['name']
            Category.objects.create(name=name)
            return HttpResponseRedirect(reverse('L_success'))
    else:
        form = CreateCategoryForm()
    return render(request, 'nBookapp/add_category.html', {'form': form})

def Inquiry_Delete(request, pk):

   context = {}
   obj = Contact.objects.get(id = pk)
   if request.method == "POST":
       obj.delete()
       return HttpResponseRedirect(reverse('L_success'))
   else:
       context = {"contact": obj}
       return render(request, 'nBookapp/Inquiry_Delete.html', context)
def Book_Delete(request, pk):

   context = {}
   obj = Book.objects.get(id = pk)
   if request.method == "POST":
       obj.delete()
       return HttpResponseRedirect(reverse('L_success'))
   else:
       context = {"book": obj}
       return render(request, 'nBookapp/Book_Delete.html', context)

def update_Book(request, id):
    obj = Book.objects.get(id=id)
    form = CreateBookForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('L_success'))
    context = {
            'form': form,
           "book": obj
    }
    return render(request, "nBookapp/update_Book.html", context)

def L_success(request):
    return render(request, 'nBookapp/L_success.html')

def U_success(request):
    return render(request, 'nBookapp/U_success.html')

def search_book_user(request):
    searched_books = Book.objects.filter(title__icontains = request.POST.get('name_of_book'))
    return render(request, 'nBookapp/User_search.html', {'searched_books':searched_books})

def search_book_librarian(request):
    searched_books = Book.objects.filter(title__icontains = request.POST.get('name_of_book'))
    return render(request, 'nBookapp/Librarian_search.html', {'searched_books':searched_books})

def Book_Borrow(request, pk):
   context = {}
   obj = Book.objects.get(id = pk)
   print(obj.borrowed_time)
   if request.method == "POST":
       obj.isBorrowed = True
       obj.owner = str(request.user)
       obj.borrowed_time = datetime.now()
       obj.remainingDays = 30
       obj.save()
       return HttpResponseRedirect(reverse('U_success'))
   else:
       context = {"book": obj}
       return render(request, 'nBookapp/Book_Borrow.html', context)

def Answer_Inquiry(request, pk):
   context = {}
   obj = Contact.objects.get(id = pk)
   if request.method == "POST":
       obj.isAnswered = True
       obj.save()
       return HttpResponseRedirect(reverse('L_success'))
   else:
       context = {"contact": obj}
       return render(request, 'nBookapp/Answer_Inquiry.html', context)

def Reserve(request, pk):
    context = {}
    obj = Carrel.objects.get(id = pk)
    if request.method == "POST":
        obj.isReserved = True
        obj.owner_Carrel = str(request.user)
        obj.save()
        return HttpResponseRedirect(reverse('U_success'))
    else:
        context = {"carrel": obj}
        return render(request, 'nBookapp/Carrel_validation.html', context)

def add_carrel(request):
    if request.method == 'POST':
        form = CreateCarrelForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            timeslot = formdata['timeslot']
            Carrel.objects.create(timeslot=timeslot,isReserved= False,owner_Carrel ="No owner")
            return HttpResponseRedirect(reverse('L_success'))
    else:
        form = CreateCarrelForm()
    return render(request, 'nBookapp/add_carrel.html', {'form': form})

def Carrel_List(request):
    #Carrel.objects.create(name = "", email = "", ID = 1, major = "", beginningtimeslot=0, endtimeslot=1, isReserved = False)
    obj = Carrel.objects.all()
    return render(request, 'nBookapp/Carrel_List.html', {'obj':obj})

def Carrel_Delete(request, pk):
    context = {}
    obj = Carrel.objects.get(id = pk)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('L_success'))
    else:
        context = {"carrel": obj}
        return render(request, 'nBookapp/Carrel_Delete.html', context)

def Carrel_List_Lib(request):
    #Carrel.objects.create(name = "", email = "", ID = 1, major = "", beginningtimeslot=0, endtimeslot=1, isReserved = False)
    obj = Carrel.objects.all()
    return render(request, 'nBookapp/Carrel_List_Lib.html', {'obj':obj})

def userBook_List(request):
    searched_books = Book.objects.filter(owner__icontains = "moe")
    for book in searched_books:
        book.remainingDays = 30 - (datetime.now()-book.borrowed_time.replace(tzinfo=None) ).days
    return render(request,'nBookapp/myBooks.html',{'item':searched_books})

def returnBook(request,pk):
    context = {}
    obj = Book.objects.get(id = pk)
    if request.method == "POST":
        obj.isBorrowed = False
        obj.owner = "No Owner"
        obj.save()
        return HttpResponseRedirect(reverse('U_success'))
    else:
        context = {"book": obj}
        return render(request, 'nBookapp/returnBook.html', context)