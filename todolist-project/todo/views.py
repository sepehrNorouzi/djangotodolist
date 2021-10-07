from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'todo/home.html')

@csrf_protect
def signupuser(request):
    if request.method == "GET":
        return render(request, 'todo/signupuser.html', {'signupform': UserCreationForm()})
    else:
        postObj = request.POST
        if postObj['password1'] == postObj['password2']:
            try:
                user = User.objects.create_user(postObj['username'], password=postObj['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'signupform': UserCreationForm(), 'err': 'Username taken already!'})

        else:
            return render(request, 'todo/signupuser.html', {'signupform': UserCreationForm(), 'err': 'Passwords did not match!'})

@csrf_protect
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'loginform': AuthenticationForm()})
    else:
        userdata = request.POST
        user = authenticate(username=userdata['username'], password=userdata['password'])
    if user is None:
        return render(request, 'todo/loginuser.html', {'loginform': AuthenticationForm(), 'err': 'Username or Password is not correct!'})
    else:
        login(request, user)
        return redirect('home')



@csrf_protect
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
