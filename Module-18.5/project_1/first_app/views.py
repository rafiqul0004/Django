from django.shortcuts import render, redirect
from .forms import SignupForm, ChangeUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'form.html', {'form': form,'type': 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=name, password=user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged In Successfully')
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'form.html', {'form': form,'type': 'login'})

def update(request):
    if request.method == 'POST':
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, 'Account Updated Successfully')
            form.save()
            return redirect('profile')
    else:
        form = ChangeUserForm(instance=request.user)
    return render(request, 'form.html', {'form': form,'type': 'Update'})

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request, 'form.html', {'form':form,'type': 'Password Change'})
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('homepage')
