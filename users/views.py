from django.shortcuts import render
from .models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)

                return HttpResponseRedirect(reverse('app:file_list'))
    
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth.login(request, user)

            return HttpResponseRedirect(reverse('app:file_list'))

    else:
        form = UserRegisterForm()

    context = {
        'title': 'Регистрация',
        'form': form,
    }

    return render(request, 'users/register.html', context)


@login_required
def logout(request):   
    auth.logout(request)
    return HttpResponseRedirect('app:file_list')
            
