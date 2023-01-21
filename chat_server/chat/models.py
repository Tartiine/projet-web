from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def permission_to_dict(permission):
    dicperm = {}
    dicperm['name'] = permission.name
    dicperm['content_type'] = permission.content_type
    dicperm['codename'] = permission.codename
    return dicperm
def user_to_dict(user):
    dicuser = {}
    dicuser['username'] = user.username
    return dicuser

class Chat(models.Model):
    name = models.CharField(max_length=40)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    creation_date = models.DateTimeField()

    def to_dict(self):
        dicchat = {}
        dicchat['name'] = self.name
        dicchat['creator'] = user_to_dict(self.creator)
        dicchat['creation_date'] = self.creation_date
        return dicchat

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    publication_date = models.DateTimeField()

    def to_dict(self):
        dicmessage = {}
        dicmessage['author'] = user_to_dict(self.author)
        dicmessage['chat'] = self.chat.to_dict()
        dicmessage['content'] = self.content
        dicmessage['publication_date'] = self.publication_date
        return dicmessage
