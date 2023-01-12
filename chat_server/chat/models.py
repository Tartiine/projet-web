from django.db import models

# Create your models here.

class Chat(models.Model):
    creation_date = models.DateTimeField()

class User(models.Model):
    username = models.CharField(max_length=40)
    rights = models.IntegerField()

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    publication_date = models.DateTimeField()

