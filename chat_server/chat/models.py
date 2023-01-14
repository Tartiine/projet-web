from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Chat(models.Model):
    name = models.CharField(max_length=40)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    creation_date = models.DateTimeField()

    def to_dict(self):
        dicchat = {}
        dicchat['name'] = self.name
        dicchat['author'] = self.creator.to_dict()
        dicchat['creation_date'] = self.creation_date
        return dicchat

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
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
