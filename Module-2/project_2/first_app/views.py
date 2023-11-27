from django.shortcuts import render

# Create your views here.

def home(request):
    d={'Author':'Rahat', 'Age':15,'lst':[1,2,3,4,5],'courses':[
        {
            'id':1,
            'name':'python',
            'fee':1000
        },
        {
            'id':2,
            'name':'django',
            'fee':2000
        }
    ]
    }
    return render(request, 'home.html',d)