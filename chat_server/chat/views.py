from django.shortcuts import render
from .models import Chat

# Create your views here.

def index(request):
    conversation_list = Chat.objects.order_by('-creation_date')[:]
    context = {'conversation_list': conversation_list}
    return render(request, 'index.html', context)

def moderation(request):
    return render(request, 'moderation.html')

def thread(request):
    return render(request, 'thread.html')

