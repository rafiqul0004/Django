from django.shortcuts import render
from album.models import Album

def home(request):
    data=Album.objects.all()
    return render(request, 'home.html', {'data': data})

def profile(request,id):
    data=Album.objects.get(pk=id)
    return render(request, 'profile.html', {'data': data})
