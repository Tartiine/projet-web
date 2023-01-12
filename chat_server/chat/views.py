from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def thread(request):
    return render(request, 'thread.html')
from django.shortcuts import render

