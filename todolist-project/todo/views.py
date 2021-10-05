from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signupuser(request):
    if request.method == "GET":
        return render(request, 'todo/signupuser.html', {'signupform': UserCreationForm()})
    else:
        postObj = request.POST
        if postObj['password1'] == postObj['password2']:
            user = User.objects.create_user(postObj['username'], password=postObj['password1'])
            user.save()
        else:
            pass
