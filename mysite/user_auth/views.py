from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages
from django.template import loader


# Create your views here.
def user_login(request):
    # return HttpResponse("Hello world. You're at the auth index.")
    return render(request, 'authentication/login.html')


def sign(request):
    template = loader.get_template('authentication/login.html')
    return HttpResponse(template.render())


def reg(request):
    template = loader.get_template('authentication/register.html')
    return HttpResponse(template.render())


def authenticate_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('musicband:records'))


def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password})
    # return render(request, "polls/poll.html")


def create_user(request):
    if request.method == 'POST':
        check1 = False
        check2 = False
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['firstname']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:
                check1 = True
                messages.error(request, 'Password did not match!',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(username=username).exists():
                check2 = True
                messages.error(request, 'Username already exists!',
                               extra_tags='alert alert-warning alert-dismissible fade show')

            if check1 or check2:
                messages.error(
                    request, "Registration Failed!", extra_tags='alert alert-warning alert-dismissible fade show')
                return redirect('user_auth:register')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=None, first_name=firstname)
                messages.success(
                    request, f'Thanks for registering {user.username}.',
                    extra_tags='alert alert-success alert-dismissible fade show')
                return redirect('user_auth:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})


def test(request):
    # return HttpResponse("Hello world. You're at the auth index.")
    return redirect(request, 'polls/poll.html')
