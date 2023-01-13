from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

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

def getChats(request):
    print(request)
    chats = Chat.objects.all()
    data = [chat.to_dict() for chat in chats]
    return JsonResponse({'chats' : data})

def getMessages(request):
    print(request)
    chat = Chat.objects.get(name="general")
    messages = chat.message_set.only('author', 'chat', 'content', 'publication_date').all()
    data = [message.to_dict() for message in messages]

    return JsonResponse({'chat' : chat.name, 'messages':data})

def createChat(request):
    print(request)
    return

def saveMessage(request):
    print(request)
    return