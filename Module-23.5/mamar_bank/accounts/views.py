from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout,update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string

def send_email(user,subject,template):
    message=render_to_string(template,{
        'user': user,
        
    })
    send_mail=EmailMultiAlternatives(subject, '',to=[user.email])
    send_mail.attach_alternative(message,"text/html")
    send_mail.send()

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        # print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        # print(user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')

def UserLogout(request):
    # def get_success_url(self):
    #     if self.request.user.is_authenticated:
    #         logout(self.request)
        # return reverse_lazy('home')
    logout(request)
    return redirect('home')


class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    
@login_required  
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            send_email(request.user,"Passward Change","accounts/pass_email.html")
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/form.html', {'form' : form,'type': 'Cgange Password'})