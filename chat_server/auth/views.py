from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
#from allauth.account.forms import SignupForm
#from django.contrib.auth.views import LoginView
from allauth.account.views import SignupView
from allauth.account.views import LoginView
# Create your views here.

class CustomSignupView(SignupView):
    template_name = "register.html"
    
class CustomLoginView(LoginView):
    template_name = "login.html"
    
'''def login1(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
'''
