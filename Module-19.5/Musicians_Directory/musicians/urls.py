from django.urls import path
from .import views
urlpatterns = [
    path('add/',views.add_musicians,name='add_musicians'),
    path('edit_musician/<int:id>',views.EditMusicianView.as_view(),name='edit_musicians')
]