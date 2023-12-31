
from django.urls import path
from .import views
urlpatterns = [
   path('signup/',views.register,name='signup'),
   # path('login/',views.user_login,name='login'),
   path('login/',views.UserLoginView.as_view(),name='login'),
   # path('logout/',views.user_logout,name='logout'),
   path('logout/',views.UserLogoutView.as_view(),name='logout'),
   path('profile/',views.profile,name='profile'),
   path('profile/edit',views.edit_profile,name='edit_profile'),
   # path('profile/edit/<int:id>',views.UpdateProfileView.as_view(),name='edit_profile'),
   path('profile/edit/pass_change',views.pass_change,name='pass_change'),

]