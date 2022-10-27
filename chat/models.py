from django.db import models


class Message(models.Model):
    user = models.CharField(max_length=10)
    message = models.TextField(max_length=1000)
    image = models.FileField(upload_to="media", null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.user + "_" + str(self.id)
