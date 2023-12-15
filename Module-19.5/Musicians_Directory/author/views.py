from typing import Any
from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form=forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('signup')
    else:
        register_form=forms.RegistrationForm()
    return render(request,'form.html',{'form':register_form,'type':'Signup'})

class UserLoginView(LoginView):
    template_name='form.html'
    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request,'Logged in successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,'Information incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context
    
class UserLogoutView(LogoutView):
    def get_success_url(self) -> str:
        return reverse_lazy('login')
    
# @login_required   
# def profile(request):
#     data=Post.objects.filter(author=request.user)
#     return render(request,'profile.html',{'data':data})

@login_required   
def edit_profile(request):
    if request.method == 'POST':
        profile_form=forms.ChangeUserForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Account Updated Successfully')
            return redirect('hompepage')
    else:
        profile_form=forms.ChangeUserForm(instance=request.user)
    return render(request,'form.html',{'form':profile_form})

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form})