from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    
    def create_user(self, phone_number, password, **extra_fields):
        
        if not phone_number:
            raise ValueError('Phone number is required!!!')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_super_user(self, phone_number, password, **extra_fields):
        
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff attribute set to True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser attribute set to True")
        
        return self.create_user(phone_number, password, **extra_fields)