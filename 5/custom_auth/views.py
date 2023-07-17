from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomLoginView(LoginView):
    template_name = 'custom_auth/login.html'
    redirect_authenticated_user = True
    fields = '__all__'
    
class CustomLogoutView(LogoutView):
    template_name = 'custom_auth/logout.html'
    
    
class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'custom_auth/signup.html'
    success_url = reverse_lazy('profile')
    
class CustomDetailView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):    
    model = CustomUser
    template_name = 'custom_auth/profile.html'
    permission_required = 'auth.view_user'
    
    
class CustomUserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'custom_auth/edit_profile.html'
    success_url = reverse_lazy('profile')
    permission_required = 'auth.change_user'
    
class CustomUserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('signup')
    permission_required = 'auth.delete_user'