from django.shortcuts import render

from .form import contactForm,StudentData,PasswordValidationProject
# Create your views here.

def home(request):
    return render(request, 'first_app/home.html')

def about(request):
    if request.method == 'POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        rating=request.POST.get('rating')
        return render(request, 'first_app/about.html', {'name':name, 'email':email, 'rating':rating})
    return render(request, 'first_app/about.html')

def submit_form(request):
    # if request.method == 'POST':
    #     name=request.POST.get('username')
    #     email=request.POST.get('email')
    #     return render(request, 'first_app/form.html', {'name':name, 'email':email})
    return render(request, 'first_app/form.html')
def django_form(request):
    if request.method == 'POST':
        form=contactForm(request.POST,request.FILES)
        if form.is_valid():
            # file=form.cleaned_data['file']
            # with open('first_app/upload/' +file.name, 'wb+')as destination:
            #     for chunk in file.chunks():
            #        destination.write(chunk)
            print (form.cleaned_data)
            # return render(request, 'first_app/django_form.html', {'form': form})
    else:
        form=contactForm()
    return render(request, 'first_app/django_form.html', {'form': form})

def StudentForm(request):
    if request.method == 'POST':
        form=StudentData(request.POST,request.FILES)
        if form.is_valid():
            print (form.cleaned_data)
    else:
        form=StudentData()
    return render(request, 'first_app/django_form.html', {'form': form})

def Passwordvalidation(request):
    if request.method == 'POST':
        form=PasswordValidationProject(request.POST,request.FILES)
        if form.is_valid():
            print (form.cleaned_data)
    else:
        form=PasswordValidationProject()
    return render(request, 'first_app/django_form.html', {'form': form})
