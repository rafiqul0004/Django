from django.shortcuts import render,redirect
from .import forms
# Create your views here.
def add_musicians(request):
    if request.method == 'POST':
        musician_form=forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musicians')
    else:
        musician_form=forms.MusicianForm()
    return render(request, 'add_musicians.html', {'form': musician_form})