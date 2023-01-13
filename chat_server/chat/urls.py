"""chat_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from chat.views import IndexView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index-view'),
    path ('moderation', views.moderation, name ='moderation-view'),
    path ('thread', views.thread, name ='thread-view'),
    path('getChats', views.getChats, name ='chats-request'),
    path('getMessages', views.getMessages, name ='messages-request'),
    path('createChat', views.createChat, name ='chat-creation'),
    path('saveMessage', views.saveMessage, name ='message-creation'),
    path('init', views.init, name="test-initialization"),
    path ('', IndexView.as_view(), name = 'index-view'),
]





