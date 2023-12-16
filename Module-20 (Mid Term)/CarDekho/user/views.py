from typing import Any
from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from order.models import Order
from car.models import Car
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    cars=Order.objects.filter(user=request.user)
    return render(request,'profile.html',{'cars':cars})

# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         register_form=forms.RegistrationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             messages.success(request,'Account Created Successfully')
#             return redirect('signup')
#     else:
#         register_form=forms.RegistrationForm()
#         return render(request,'form.html',{'form':register_form,'type':'Signup'})

class RegistrationView(CreateView):
    template_name='form.html'
    form_class=forms.RegistrationForm
    
    def get_success_url(self):
        return reverse_lazy('homepage')
 
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type']='Signup'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)
    
    
class UserLoginView(LoginView):
    template_name='form.html'
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request,'Login successful')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,'Login Information Invalid')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type']='login'
        return context
    
class UserLogoutView(LogoutView):
    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    

@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_form=forms.ChangeDataForm(request.POST,instance=request.user)
        if edit_form.is_valid:
            edit_form.save()
            return redirect('homepage')
        
    else:
        edit_form=forms.ChangeDataForm(instance=request.user)
    return render(request,'form.html',{'form':edit_form,'type':'update'})

@login_required
def order(request,id):
    car=Car.objects.get(pk=id)
    if car.quantity>0:
        car.quantity-=1
        messages.success(request,'Car Added Successfully')
        car.save()
        Order.objects.create(user=request.user,car=car)
    else:
        messages.warning(request,'Sorry this Car is Stock out')
    return redirect('profile')