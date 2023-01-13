from django.shortcuts import render, redirect
from allauth.account.views import SignupView
from allauth.account.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.

class CustomSignupView(SignupView):
    template_name = "register.html"
    
    def post(self, request, *args, **kwargs):
        userName = request.POST.get('username')
        Password = request.POST.get('password')
        password_confirm = request.POST.get('password-confirm')
        if Password == password_confirm:
            if User.objects.filter(username=userName).exists():
                return render(request, 'register.html', {'error': 'This username is already associated to a account'})
            else:
                user = User.objects.create_user(username=userName, password=Password)
                user.save()
                return redirect('account_login')
                return render(request, 'login.html', {'error': 'Account created'})
        else:
            return render(request, 'register.html', {'error': 'Error the account was not created'})

class CustomLoginView(LoginView):
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        userName = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=userName, password=Password)
        if user is not None:
            login(request, user)
            return redirect('index-view')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})