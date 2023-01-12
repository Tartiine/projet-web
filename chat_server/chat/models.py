from django.db import models
from djang.forms import model_to_dict

# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=40)
    creation_date = models.DateTimeField()

class User(models.Model):
    username = models.CharField(max_length=40)
    rights = models.IntegerField()

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
