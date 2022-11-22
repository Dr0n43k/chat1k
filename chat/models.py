from django.db import models
from django.dispatch import receiver
from django.db.models import signals
import telebot
import json
class Message(models.Model):
    user = models.CharField(max_length=10, null=True,blank=True)
    message = models.TextField(max_length=1000, null=True,blank=True)
    image = models.FileField(upload_to="media", null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

@receiver(signals.post_save,sender=Message)
def on_create(sender,instance,**kwargs):
    if kwargs['created']:
        with open('data.json', 'w') as outfile:
            json.dump({'user':Message.objects.latest('id').user,'message':Message.objects.latest('id').message}, outfile)
        print(" я отправил")

