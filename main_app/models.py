from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Meme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200, null=True)
    top_text = models.CharField(max_length=100, null=True)
    bottom_text = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.top_text
