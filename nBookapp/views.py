import os

from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateCategoryForm, CreateBookForm, CreateContactForm
from .models import *
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.urls import reverse


class Book_List(ListView):
    model = Book
    
def bookList(request):
    item = Book.objects.all()
    # print("Myoutput", item)
    return render(request, 'nBookapp/Book_Details.html', {'item':item})


# def confirm_Delete(request,pk):
#     instance = Book.objects.get(pk=id)
#     return render(request,"nBookapp/Book_Delete.html",{'title':instance.title})

def Book_Delete(request, pk):
   #instance = Book.objects.get(pk=id)
   #instance.delete()
   #return redirect("Book_List")
   context = {}
   #order = Book.objects.get(id=pk)
   #if request.method == "POST":
    #    order.delete()
    #    return redirect('Book_List.html')
   #obj = get_object_or_404(Book, ISBN=ISBN)
   obj = Book.objects.get(id = pk)
   if request.method == "POST":
       obj.delete()
       #render(request, 'Book_List.html')
       return HttpResponseRedirect(reverse('success'))
   else:
       context = {"book": obj}
       return render(request, 'nBookapp/Book_Delete.html', context)
       # HttpResponseRedirect('/success')
   #return redirect('Book_List.html')
   #context ={"object": obj}
   #return HttpResponseRedirect('/success')

def index(request):
    return render(request, 'nBookapp/index.html')


def contact(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            username = formdata['username']
            email = formdata['email']
            subject = formdata['subject']
            Contact.objects.create(username=username, email=email, subject=subject)
            return HttpResponseRedirect(reverse('success'))
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
            # pdf = formdata['pdf']
            Book.objects.create(title=title, author=author, ISBN=ISBN, category=category, price=price, summary=summary)
            return HttpResponseRedirect(reverse('success'))
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
            return HttpResponseRedirect(reverse('success'))
    else:
        form = CreateCategoryForm()
    return render(request, 'nBookapp/add_category.html', {'form': form})

def update_Book(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = CreateBookForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('success'))
    context = {
        'form': form
    }
    return render(request, "nBookapp/update_Book.html", context)

def success(request):
    return render(request, 'nBookapp/success.html')

def search_book(request):
    searched_books = Book.objects.filter(title__icontains = request.POST.get('name_of_book'))
    return render(request, 'nBookapp/search.html', {'searched_books':searched_books})