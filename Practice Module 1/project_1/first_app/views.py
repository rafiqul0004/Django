from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d={
        'join': ['My', 'Name', 'is','Rahat'],
        'date': datetime.datetime.now(),
        'mybirthdate': datetime.datetime(2001, 1, 1), 
        'empty':None,
        'add':100,
        'name': 'rahat',
        'cut': 'Rafiqul Islam Rahat',
        'dic':[
                     {'name': 'Rahat', 'age': 23},
                     {'name': 'Zehat', 'age': 16},
                     {'name': 'Fahad', 'age': 3},
                  ],

        'text': '<b>I</b> <button>love</button> <span>Python</span>',

        'array':[1, 2, 3, 4, 5],
    }
    return render(request, 'home.html',d)