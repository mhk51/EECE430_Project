from django.db import models
from Accounts.models import Student
from datetime import datetime, timedelta

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
    owner = models.CharField(max_length=40,default = "No owner")
    #cover_image = models.ImageField(upload_to='img', blank=True, null=True)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=15)
    isBorrowed = models.BooleanField(default=False)
    summary = models.TextField(max_length=300)
    remainingDays = models.IntegerField(default=30)
    borrowed_time = models.DateTimeField(default=datetime.now())

    #pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.title

class Contact(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField()
    isAnswered = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Carrel(models.Model):
    timeslot = models.CharField(max_length=30)
    isReserved = models.BooleanField(default=False)
    owner_Carrel = models.CharField(max_length=30,default="No Owner")
    #carrellist = ArrayField(models.CharField(max_length=20), blank = True)
    
    # def create(cls, beginningtimeslot, endtimeslot): M
    #     carrel = cls(beginningtimeslot = beginningtimeslot, endtimeslot=endtimeslot)
    #     return carrel  

    # def __init__(self, beginningtimeslot, endtimeslot):
    #     self.beginningtimeslot = beginningtimeslot
    #     self.endtimeslot = endtimeslot      

    # def __str__(self):
    #     return self.beginningtimeslot + "-" + self.endtimeslot

    def __str__(self):
        return self.timeslot
