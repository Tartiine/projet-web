from django.db import models
from django.forms import model_to_dict

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=40)
    rights = models.IntegerField()

    def to_dict(self):
        dicuser = {}
        dicuser['username'] = self.username
        dicuser['rights'] = self.rights
        return dicuser

class Chat(models.Model):
    name = models.CharField(max_length=40)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField()

    def to_dict(self):
        dicchat = {}
        dicchat['name'] = self.name
        dicchat['author'] = self.creator.to_dict()
        dicchat['creation_date'] = self.creation_date
        return dicchat

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    publication_date = models.DateTimeField()

    def to_dict(self):
        dicmessage = {}
        dicmessage['author'] = self.author.to_dict()
        dicmessage['chat'] = self.chat.to_dict()
        dicmessage['content'] = self.content
        dicmessage['publication_date'] = self.publication_date
        return dicmessage
