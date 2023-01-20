from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.http import JsonResponse
from django.utils import timezone
from .models import Chat, Message
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.

class IndexView(TemplateView):
    template_name = "chat/index.html"
    


    def get(self, request, *args, **kwargs):
    
        if Chat.objects.exists():
            if 'actual_conv' not in request.session:
                request.session['actual_conv'] = Chat.objects.order_by('-creation_date')[0].name
            conv_name = request.session['actual_conv']
            conv = Chat.objects.get(name=conv_name)
            message_list = Message.objects.filter(chat=conv).order_by('publication_date')[:] 
            conversation_list = Chat.objects.order_by('-creation_date')[:] 
            context = {'conversation_list': conversation_list,'message_list': message_list, 'actual_conv':conv_name}
        else:
            context = {}
        if request.GET.get('logout'):
            logout(request)
        return render(request, self.template_name, context)
        
        
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if not request.user.is_authenticated:
                return redirect('account_login')

            new_conv = request.POST.get('new-conv', None)
            if new_conv:
                if Chat.objects.filter(name=new_conv).exists():   
                    messages.error(request, 'This chat already exists')
                else:
                    new_chat = Chat(name=new_conv,creator=request.user, creation_date=timezone.make_aware(datetime.datetime.now()))
                    new_chat.save()

            msg = request.POST.get('new-message', None)
            if msg:
                if Chat.objects.exists():
                    new_message = Message(author=request.user,chat=Chat.objects.get(name=request.session['actual_conv']), content=msg, publication_date=timezone.make_aware(datetime.datetime.now()) )
                    new_message.save()
                else: 
                    messages.error(request, 'You have to create a chat room to send messages')
        return redirect('index-view')

def moderation(request):
    template_name = "chat/moderation.html"
    conversation_list = Chat.objects.order_by('-creation_date')[:]
    user_list = User.objects.order_by('-date_joined')[:]
    context = {'conversation_list': conversation_list, 'user_list': user_list}
    return render(request, template_name, context)

def rights_view(request, username):
    template_name = "chat/rights.html"
    main_user = get_object_or_404(User, username=username)
    conversation_list = Chat.objects.order_by('-creation_date')[:]
    context = {'main_user': main_user, 'conversation_list':conversation_list}
    return render(request, template_name, context)


def changePassword(request):
    new_password = request.POST.get('new-password', None)
    if new_password:
        current_user = request.user
        if current_user.check_password(new_password):
            messages.error(request, 'You can\'t chose the same password')
            return redirect('../moderation')
        else:
            # Update the user's password
            current_user.set_password(new_password)
            current_user.save()
            messages.success(request, 'Password successfully changed')
            return redirect('index-view')
    else:
        messages.error(request, 'No password provided')
        return redirect('../moderation')

def thread(request):
    return render(request, 'thread.html')

"""
def getChats(request):
    chats = Chat.objects.all()
    data = [chat.to_dict() for chat in chats]
    return JsonResponse({'chats': data})


def getMessages(request):
    chat = Chat.objects.get(name=request.GET['chatName'])
    messages = chat.message_set.only('author', 'chat', 'content', 'publication_date').all()
    print(messages)
    data = [message.to_dict() for message in messages]
   
    return JsonResponse({'chat': chat.name, 'messages': data})


def createChat(request):
    print(request)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('account_login')
        new_conv = request.POST.get('chatName', None)
        if new_conv:
            if Chat.objects.filter(name=new_conv).exists():
                messages.error(request, 'This chat already exists')
            else:
                new_chat = Chat(name=new_conv, creator=request.user, creation_date=timezone.now())
                new_chat.save()

    chat = Chat.objects.get(name=new_conv)
    chat_messages = chat.message_set.only('author', 'chat', 'content', 'publication_date').all()
    print(chat_messages)
    data = [message.to_dict() for message in chat_messages]

    return JsonResponse({'chat': chat.name, 'messages': data})

@csrf_exempt
def saveMessage(request):
    print(request)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('account_login')
        new_content = request.POST.get('content', None)
        if new_content:
            if new_content == "":
                messages.error(request, 'This message is empty !')
            else:
                new_message = Message(content=new_content, chat=Chat.objects.get(name=request.POST.get('chat',None)), author=request.user, publication_date=timezone.now())
                new_message.save()

    chat = Chat.objects.get(name=request.POST.get('chat',None))
    chat_messages = chat.message_set.only('author', 'chat', 'content', 'publication_date').all()
    print(chat_messages)
    data = [message.to_dict() for message in chat_messages]

    return JsonResponse({'chat': chat.name, 'messages': data})
"""

def deleteConversation(request):
            import json
            chat_name = json.loads(request.body.decode())['data']
            if chat_name:
                chat = Chat.objects.filter(name=chat_name)
                chat.delete()
            return redirect('../moderation')

def deleteUser(request):
            import json
            user_name = json.loads(request.body.decode())['data']
            if user_name:
                user = User.objects.filter(username=user_name)
                user.delete()
            return redirect('../moderation')

def actualConv(request):
            import json
            conv_name = json.loads(request.body.decode())['data']
            if conv_name:
                request.session['actual_conv'] = conv_name
            return redirect('index-view')

def changeRights(request):
            import json
            main_user = json.loads(request.body.decode())['data']
            if main_user:
                user = User.objects.filter(username=main_user)
                user.is_staff = True
            return redirect('../rights')