from django.forms import ModelForm
from .models import ToDoItem


class ToDoCreateForm(ModelForm):
    class Meta: 
        model = ToDoItem
        fields = (
            'title',
            'desc',
            'to_do_table'
        )