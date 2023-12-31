
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogout,UserBankAccountUpdateView,pass_change
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogout, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
    path('pass_change/',pass_change , name='pass_change' ),
]