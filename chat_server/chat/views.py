from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from .models import Chat

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        conversation_list = Chat.objects.order_by('-creation_date')[:]
        context = {'conversation_list': conversation_list}
        if request.GET.get('logout'):
            print(request.user) #check the user before
            logout(request)
        return render(request, self.template_name, context)
    
def moderation(request):
    return render(request, 'moderation.html')

def thread(request):
    return render(request, 'thread.html')

"""
def getChats(request):

def getMessages(request):

def createChat(request):

def saveMessage(request):
"""