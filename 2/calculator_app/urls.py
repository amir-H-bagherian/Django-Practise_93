from django.urls import path
from .views import home, addition_page, subtraction_page, multiplication_page, division_page


urlpatterns = [
    path('', home, name='homepage'),
    path('add/', addition_page, name='Addition'),
    path('sub/', subtraction_page, name='Subtraction'),
    path('mul/', multiplication_page, name='Multiplication'),
    path('div/', division_page, name='Division'),
]