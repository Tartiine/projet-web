from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.forms import model_to_dict

from chat.models import Message, Chat, User


# Create your views here.

def init(request):
    user1 = User(username="user1", rights=1)
    user1.save()
    user2 = User(username="user2", rights=1)
    user2.save()
    chat = Chat(name="general", creator=user1, creation_date=timezone.now())
    chat.save()
    m1 = Message(author=user1, chat=chat,  content="The first of a lot of random messages", publication_date=timezone.now())
    m1.save()
    m2 = Message(author=user1, chat=chat, content="The second of a lot of random messages", publication_date=timezone.now())
    m2.save()
    m3 = Message(author=user2, chat=chat, content="The third of a lot of random messages", publication_date=timezone.now())
    m3.save()
    m4 = Message(author=user1, chat=chat, content="The fourth of a lot of random messages", publication_date=timezone.now())
    m4.save()
    m5 = Message(author=user2, chat=chat, content="The fifth of a lot of random messages", publication_date=timezone.now())
    m5.save()
    m6 = Message(author=user2, chat=chat, content="The sixth of a lot of random messages", publication_date=timezone.now())
    m6.save()
    m7 = Message(author=user1, chat=chat, content="The seventh of a lot of random messages", publication_date=timezone.now())
    m7.save()
    m8 = Message(author=user1, chat=chat, content="The eighth of a lot of random messages", publication_date=timezone.now())
    m8.save()
    m9 = Message(author=user1, chat=chat, content="The ninth of a lot of random messages", publication_date=timezone.now())
    m9.save()
    m10 = Message(author=user2, chat=chat, content="The tenth of a lot of random messages", publication_date=timezone.now())
    m10.save()


def gettestchat(request):
    chat = Chat.objects.get(name="general")
    messages = chat.message_set.only('author', 'chat', 'content', 'publication_date').all()
    print(messages)

    data = [message.to_dict() for message in messages]
    print(data)

    response = JsonResponse({'chatName': chat.name, 'messages': data})
    return response
