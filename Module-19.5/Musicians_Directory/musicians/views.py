from django.shortcuts import render,redirect
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
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

@method_decorator(login_required,name='dispatch')
class EditMusicianView(UpdateView):
      model=models.Musician
      form_class=forms.MusicianForm
      template_name='add_musicians.html'
      pk_url_kwarg = 'id'
      success_url=reverse_lazy('homepage')