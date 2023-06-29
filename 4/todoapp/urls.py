from django.urls import path
from .views import HomeToDoListView, CreateToDoView

urlpatterns = [
    path('', HomeToDoListView.as_view(), name='home'),
    path('create/', CreateToDoView.as_view(), name='create-todo'),
]