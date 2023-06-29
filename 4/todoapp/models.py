from django.db import models
from django.urls import reverse

# Create your models here.
class ToDoItem (models.Model):

    title = models.CharField(max_length=100)
    desc = models.TextField()
    to_do_table = models.ForeignKey('ToDoTable',
                                    on_delete=models.CASCADE,
                                    related_name='todo_items')
    is_completed = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = ("To do Item")
        verbose_name_plural = ("To do Items")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})

class ToDoTable (models.Model):
    
    date_of_day = models.DateField()
    
    def __str__(self) -> str:
        return f"ToDos of {self.date_of_day}"

    def get_absolute_url(self):
        return reverse("todotable_detail", kwargs={"pk": self.pk})