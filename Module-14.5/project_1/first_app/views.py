from django.shortcuts import render
from first_app.forms import SampleForm
# Create your views here.
def home(request):
    form=SampleForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'home.html',{'form':form})
