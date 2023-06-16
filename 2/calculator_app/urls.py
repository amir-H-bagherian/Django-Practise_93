from django.urls import path
from .views import addition_page, home

urlpatterns = [
    path('', home, name='homepage'),
    path('add/', addition_page, name='Addition'),
]