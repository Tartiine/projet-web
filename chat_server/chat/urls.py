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
    path ('', IndexView.as_view(), name = 'index-view'),
    path('deleteConversation/', views.deleteConversation, name='delete-conversation'),
    path('deleteUser/', views.deleteUser, name='delete-user'),
    path('changePassword', views.changePassword, name='change-password'),
    path('actualConv/', views.actualConv, name='actual-conversation'),
    path('changeRights/', views.changeRights, name='change-rights'),
    path('createConvRights/', views.createConvRights, name='create-conv-rights'),
    path('deleteConvRights/', views.deleteConvRights, name='delete-conv-rights'),
    path('renameConvRights/', views.renameConvRights, name='rename-conv-rights'),
    path('rights/<str:username>/', views.rights_view, name='rights-view'),
    path('getMessages',views.getMessages, name='message-getter'),
    path('saveMessage',views.saveMessage, name='message-setter'),
]





"""
    path('getChats', views.getChats, name ='chats-request'),
    path('getMessages', views.getMessages, name ='messages-request'),
    path('createChat', views.createChat, name ='chat-creation'),
    path('saveMessage', views.saveMessage, name ='message-creation'),
    path('init', views.init, name="test-initialization"),
"""