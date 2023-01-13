from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=40)
    rights = models.IntegerField()

class Chat(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField()

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.CharField(max_length=400)
    publication_date = models.DateTimeField()