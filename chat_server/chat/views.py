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
        conversation_list = Chat.objects.order_by('-creation_date')[:]
        context = {'conversation_list': conversation_list}
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
        return redirect('index-view')

def moderation(request):
    return render(request, 'chat/moderation.html')

def thread(request):
    return render(request, 'thread.html')

# for test purposes only
def init(request):
    print(request)
    user1 = User(username="user1", rights=1)
    user1.save()
    user2 = User(username="user2", rights=1)
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
    data = [message.to_dict() for message in messages]
   
    return JsonResponse({'chat': chat.name, 'messages': data})


def createChat(request):
    print(request)
    return


def saveMessage(request):
    print(request)
    return
