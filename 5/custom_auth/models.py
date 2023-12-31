from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.core.validators import RegexValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Please enter a valid phone number!"
    )
    phone_number = models.CharField(max_length=16, verbose_name="User Phone Number",
                                    validators=phone_regex, unique=True)
    email = models.EmailField()
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        
    def __str__(self) -> str:
        return self.email
        
        
class CustomGroup(Group):
    class Meta:
        permissions = (
            ('change_user', 'To Update User Profile'),
            ('view_user', 'To See User Details'),
            ('delete_user', 'To Delete a User'),
        )