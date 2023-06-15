from django.db import models
from django.contrib.auth.models import User, AnonymousUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(to=User,
                               on_delete=models.SET_DEFAULT,
                               default=AnonymousUser
                               )
    publication_date = models.DateField(null=True)
    ISBN = models.BigIntegerField()
    availability_status = models.BooleanField(default=True)
    
class Author:
    name = models.CharField(max_length=200)
    biography = models.TextField()
    
class Memeber:
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_number = models.BigIntegerField()