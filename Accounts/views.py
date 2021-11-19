from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import CreateUserForm


def registerPage(request):
	form= CreateUserForm()

	if request.method == 'POST':
		form= CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request, 'Account Was Created for '+ user)
			return redirect('login')


	context={'form':form}
	return render(request,'Accounts/register.html',context)

def loginPage(request):
	context={}
	return render(request,'Accounts/login.html',context)
