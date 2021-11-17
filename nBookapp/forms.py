from django import forms

class CreateCategoryForm(forms.Form):
    name = forms.CharField(label='name')

class CreateBookForm(forms.Form):
    title = forms.CharField(label='title')
    price = forms.IntegerField(label='price')
    ISBN = forms.IntegerField(label='ISBN')
    #cover_image = forms.ImageField(label='cover_image')
    author = forms.CharField(label='author')
    summary = forms.CharField(label='summary')
    category = forms.CharField(label='category')
    #pdf = forms.FileField(label='pdf')

class CreateContactForm(forms.Form):
    username = forms.CharField(label='username')
    email = forms.EmailField(label='email')
    subject = forms.CharField(label='subject')
