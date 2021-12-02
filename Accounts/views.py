from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
import random

# Create your views here.
from .models import *
from .forms import CreateUserForm

def User_registerPage(request):
	form= CreateUserForm()

	if request.method == 'POST':
		form= CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request, 'Account Was Created for '+ user)
			return redirect('User_login')


	context={'form':form}
	return render(request,'Accounts/register.html',context)


#def Librarian_index(request):
#    return render(request, 'nBookapp/Librarian_index.html')
#def User_index(request):
#    return render(request, 'nBookapp/User_index.html')
def loginPage(request):

	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			token = random.randrange(100000,10000000)
			send_mail('Email Verification','Please use the following token: '+str(token),'mohammad.kachmar1201@gmail.com',
			[user.email],fail_silently=False,) 
			#context = {'user':user}
			return redirect('Activate',token)

	context={}
	return render(request,'Accounts/User_login.html',context)

def activate(request,token):
	if request.method == 'POST':
		tokeninput = request.POST.get('tokeninput')
		print(token,tokeninput)
		if token == int(tokeninput):
			print('correct')
			return redirect('User_index')
	return render(request,'Accounts/Activate.html')

def loginPage_L(request):

	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('Librarian_index')

	context={}
	return render(request,'Accounts/Librarian_login.html',context)


def homePage(request):
	context={}
	return render(request,'Accounts/home.html',context)