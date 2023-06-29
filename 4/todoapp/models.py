from django.db import models
from django.urls import reverse

# Create your models here.
class ToDoItem (models.Model):

    title = models.CharField(max_length=100)
    desc = models.TextField()
    
    class Meta:
        verbose_name = _("To do Item")
        verbose_name_plural = _("To do Items")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})
