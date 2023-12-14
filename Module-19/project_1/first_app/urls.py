from django.urls import path
from .import views
urlpatterns = [
    path('',views.set_session,name='homepage'),
    # path('get/',views.get_cookie,name='get_cookie'),
    path('get/',views.get_sessions,name='get_session'),
    # path('del/',views.delete_cookie,name='get_cookie'),
    path('del/',views.delete_sessions,name='delete_session'),

]