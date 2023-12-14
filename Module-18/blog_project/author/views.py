from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form=forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')
#     else:
#         author_form=forms.AuthorForm()
#     return render(request,'add_author.html',{'form':author_form})
def register(request):
    if request.method == 'POST':
        register_form=forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('signup')
    else:
        register_form=forms.RegistrationForm()
    return render(request,'signup.html',{'form':register_form,'type':'Signup'})

def user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Logged in successfully')
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Incorrect username or password')
                return redirect('signup')
    else:
        form=AuthenticationForm()
    return render(request,'signup.html',{'form':form,'type':'login'})
    
@login_required   
def profile(request):
    data=Post.objects.filter(author=request.user)
    return render(request,'profile.html',{'data':data})

@login_required   
def edit_profile(request):
    if request.method == 'POST':
        profile_form=forms.ChangeUserForm(request.POST,instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Account Updated Successfully')
            return redirect('profile')
    else:
        profile_form=forms.ChangeUserForm(instance=request.user)
    return render(request,'update_profile.html',{'form':profile_form})

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

def user_logout(request):
    logout(request)
    return redirect('login')
