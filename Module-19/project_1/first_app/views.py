from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name','rahat',expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name=request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name':name})

def delete_cookie(request):
    response = render(request, 'del.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    # data={
    #     'name':'Rahat',
    #     'age':23,
    #     'Languages':'Bangla'
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name'] = 'Rahat'
    return render (request, 'home.html')

def get_sessions(request):
    if 'name' in request.session:
        name=request.session.get('name')
        # age=request.session.get('age')
        # return render(request, 'get_session.html', {'name':name, 'age':age,})
        request.session.modified = True
        return render(request, 'get_session.html', {'name':name})
    else:
        return HttpResponse("Your Session Expired - Please Login again")

def delete_sessions(request):
    request.session.flush()
    return render(request, 'delete_session.html')