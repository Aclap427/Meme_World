from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

class Meme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_URL = models.CharField(max_length=200, null=True)
    top_text = models.CharField(max_length=100, blank=True)
    bottom_text = models.CharField(max_length=100, blank=True)
    created_on = models.DateField(default=date.today)
    
    

    def __str__(self):
        return self.top_text

 