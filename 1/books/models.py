from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ManyToManyField("Author")
    publication_date = models.DateField(null=True)
    ISBN = models.BigIntegerField()
    availability_status = models.BooleanField(default=True)
    
class BorrowModel(models.Model):
    member = models.ForeignKey("Memeber", on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()
    
class Author(models.Model):
    name = models.CharField(max_length=200)
    biography = models.TextField()
    
class Memeber(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_number = models.BigIntegerField()
    is_active = models.BooleanField(default=True)
    