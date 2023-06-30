from typing import Any, Optional
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from .models import CustomUser


class phoneNumberBackend(BaseBackend):
    
    def authenticate(self, request, phone_number=None, password=None, **kwargs) -> AbstractBaseUser | None:
        try:
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        return None
    
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None