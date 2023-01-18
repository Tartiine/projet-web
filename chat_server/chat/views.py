from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.http import JsonResponse
from django.utils import timezone
from .models import Chat, Message
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

class IndexView(TemplateView):
    template_name = "chat/index.html"
    
    
    
    def get(self, request, *args, **kwargs):
        if 'actual_conv' in request.session:
            conv_name = request.session['actual_conv']
            try:
                conv = Chat.objects.get(name=conv_name)
                message_list = Message.objects.filter(chat=conv).order_by('-publication_date')
            except Chat.DoesNotExist:
                message_list = Message.objects.order_by('-publication_date')[::-1]
        else:
            message_list = Message.objects.order_by('-publication_date')[::-1]
        conversation_list = Chat.objects.order_by('-creation_date')[:]
        if 'actual_conv' in request.session:
            context = {'conversation_list': conversation_list,'message_list': message_list, 'actual_conv':conv_name}
        else:
            context = {'conversation_list': conversation_list,'message_list': message_list}
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
                    new_chat = Chat(name=new_conv,creator=request.user, creation_date=timezone.now())
                    new_chat.save()
                    
            msg = request.POST.get('new-message', None)
            print(msg)
            if msg:
                print(msg)
                last_chat = Chat.objects.order_by('-creation_date')[0]   #Replace with active chat
                new_message = Message(author=request.user,chat=last_chat, content=msg, publication_date=timezone.now() )
                new_message.save()   
        return redirect('index-view')

def moderation(request):
    template_name = "chat/moderation.html"
    conversation_list = Chat.objects.order_by('-creation_date')[:]
    user_list = User.objects.order_by('-date_joined')[:]
    context = {'conversation_list': conversation_list, 'user_list': user_list}
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
# for test purposes only
def init(request):
    print(request)
    user1 = User.objects.create_user(username="user1", password="UsEr1")
    user1.save()
    user2 = User.objects.create_user(username="user2", password="UsEr2")
    user2.save()
    chat = Chat(name="general", creator=user1, creation_date=timezone.now())
    chat.save()
    m1 = Message(author=user1, chat=chat, content="The first of a lot of random messages",
                 publication_date=timezone.now())
    m1.save()
    m2 = Message(author=user1, chat=chat, content="The second of a lot of random messages",
                 publication_date=timezone.now())
    m2.save()
    m3 = Message(author=user2, chat=chat, content="The third of a lot of random messages",
                 publication_date=timezone.now())
    m3.save()
    m4 = Message(author=user1, chat=chat, content="The fourth of a lot of random messages",
                 publication_date=timezone.now())
    m4.save()
    m5 = Message(author=user2, chat=chat, content="The fifth of a lot of random messages",
                 publication_date=timezone.now())
    m5.save()
    m6 = Message(author=user2, chat=chat, content="The sixth of a lot of random messages",
                 publication_date=timezone.now())
    m6.save()
    m7 = Message(author=user1, chat=chat, content="The seventh of a lot of random messages",
                 publication_date=timezone.now())
    m7.save()
    m8 = Message(author=user1, chat=chat, content="The eighth of a lot of random messages",
                 publication_date=timezone.now())
    m8.save()
    m9 = Message(author=user1, chat=chat, content="The ninth of a lot of random messages",
                 publication_date=timezone.now())
    m9.save()
    m10 = Message(author=user2, chat=chat, content="The tenth of a lot of random messages",
                  publication_date=timezone.now())
    m10.save()


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
    return


def saveMessage(request):
    print(request)
    return
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
            print("function actualConv")   
            return redirect('index-view')
        
def deleteUser(request):
            import json
            user_name = json.loads(request.body.decode())['data']
            if user_name:
                user = User.objects.filter(username=user_name)
                user.delete()
            return redirect('../moderation')