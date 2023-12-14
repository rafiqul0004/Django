
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('pass_change/', views.pass_change, name='pass_change'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
