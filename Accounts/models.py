from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from nBookapp.models import Book

# Create your models here.

class Student(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name = models.CharField(max_length=200,null=True)
	student_ID = models.CharField(max_length=200,null=True)
	email = models.CharField(max_length=200,null=True)
	date_created= models.DateTimeField(auto_now_add=True,null=True)
	books = models.ManyToManyField(Book, blank=True)
	

	def __str__(self):
		return self.name


def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
    	Student.objects.get_or_create(user=instance)


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)