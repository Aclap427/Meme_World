from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

COLORS = (
    ('black', 'black'),
    ('blue', 'blue'),
    ('red', 'red'),
    ('green', 'green'),
)

FONTS = (
    ("Comic Neue", "Comic Neue"),
    ("Just Another Hand", "Just Another Hand")
)


class Meme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_URL = models.CharField(max_length=200, blank=True, null=True)
    top_text = models.CharField(max_length=100, blank=True, null=True)
    bottom_text = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateField(default=date.today)
    text_color = models.CharField(
        max_length=5,
        choices=COLORS,
        default=COLORS[0][0]
    )
    font = models.CharField(
        max_length=100,
        choices=FONTS,
        default=FONTS[0][0]
    )
    
    

    def __str__(self):
        return self.top_text

class Photo(models.Model):
    url = models.CharField(max_length=200)
    meme = models.ForeignKey(Meme, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for meme_id: {self.meme_id} @{self.url}"

