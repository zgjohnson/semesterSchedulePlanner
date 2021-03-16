from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import IntegrityError


# Create your views here.
def landingPage(request):
    return render(request, 'accounts/landingPage.html')


def loginUser(request):
    return render(request, 'accounts/loginUser.html')


def signupUser(request):
    if request.method == 'GET':
        return render(request, 'accounts/signupUser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('schedule:allCourses')

            except IntegrityError:
                return render(request, 'accounts/signupUser.html',
                              {'form': UserCreationForm(),
                               'error': 'That username has already been taken. Please choose a new username.'})
        else:
            return render(request, 'accounts/signupUser.html',
                          {'form': UserCreationForm(), 'error': 'Passwords did not match'})






