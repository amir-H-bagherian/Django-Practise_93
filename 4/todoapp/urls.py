from django.urls import path
from .views import HomeToDoListView

urlpatterns = [
    path('', HomeToDoListView.as_view(), name='home'),
]