from django.urls import path
from .views import add_page, home

urlpatterns = [
    path('', home, name='homepage'),
]