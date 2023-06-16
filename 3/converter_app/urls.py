from django.urls import path
from .views import converter_view, create_result


urlpatterns = [
    path('', converter_view, name='home'),
    path('create-result/', create_result, name='result'),
]
