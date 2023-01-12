from django.db import models
from django.forms import model_to_dict

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=40)
    rights = models.IntegerField()

class Chat(models.Model):
    name = models.CharField(max_length=40)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField()

    def to_dict(self):

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    publication_date = models.DateTimeField()

    def to_dict(self):
        dicmessage = {}
        dicmessage['author'] = model_to_dict(self.author)
        dicmessage['chat'] = model_to_dict(self.chat)
        dicmessage['content'] = self.content
        dicmessage['publication_date'] = self.publication_date
        return dicmessage
