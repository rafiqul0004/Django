
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogout,UserBankAccountUpdateView
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogout, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
]