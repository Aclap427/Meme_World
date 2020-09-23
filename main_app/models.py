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
    ("Just Another Hand", "Just Another Hand"),
    ("Impact, fantasy", "Impact, fantasy")
)

FACES = (
    ('', ''),
    ('https://i.imgur.com/YN5GR31.png', 'Me Gusta'),
    ('https://i.imgur.com/YOFpfXA.png', 'Troll Face'),
    ('https://i.imgur.com/TyBY8zX.png', 'Why U new'),
    ('https://i.imgur.com/zqWWfQu.png', 'Y U NO'),
    ('https://i.imgur.com/RNafstk.png', 'LOL Face'),
    ('https://i.imgur.com/dXAPOYu.png', 'Pepe Frog'),
    ('https://i.imgur.com/0aRNUzu.png', 'Pepe Smug'),
    ('https://i.imgur.com/Lw1iFG2.png', 'Okay Guy'),
    ('https://i.imgur.com/FJ1S2YA.png', 'No Guy'),
    ('https://i.imgur.com/jS8MkcK.png', 'FTS Guy')
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
    face = models.CharField(
        max_length=100,
        choices=FACES,
        default='',
        blank=True
    )

    def __str__(self):
        return f"{self.top_text if self.top_text else ''}"
