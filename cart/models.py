from django.db import models
from nBookapp.models import Book
from Accounts.models import Student
# Create your models here.

class OrderItem(models.Model):
    book = models.OneToOneField(Book, on_delete=models.SET_NULL, null=True) 
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.book.title



class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.book.price for item in self.items.all()])

   
