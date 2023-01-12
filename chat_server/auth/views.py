from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from allauth.account.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

class CustomSignupView(SignupView):
    template_name = "register.html"
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username,password)
        if username and password:
           u,created = user.objects.get_or_create(username)
           if created:
              # user was created
              return render(request, 'register.html', {'error': 'Account created'})
              # set the password here
           else:
              # user was retrieved
              return render(request, 'register.html', {'error': 'Error the account was not created'})
        else:
            return render(request, 'register.html', {'error': 'This username is already associated to a account'})
           # request was empty

class CustomLoginView(LoginView):
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index-view')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})