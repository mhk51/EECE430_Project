from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    ISBN = models.IntegerField(max_length=20)
    price = models.IntegerField(default=0)
    #cover_image = models.ImageField(upload_to='img', blank=True, null=True)
    author = models.CharField(max_length=50)
    summary = models.TextField(max_length=300)
    category = models.CharField(max_length=15)
    #pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.title

class Contact(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    def __str__(self):
        return self.username
