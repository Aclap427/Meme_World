from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from django.contrib.postgres.fields import ArrayField

SIZE = (
    ('14px', '14pt'),
    ('16px', '16pt'),
    ('18px', '18pt'),
    ('20px', '20pt'),
    ('22px', '22pt'),
    ('24px', '24pt'),
    ('26px', '26pt'),
)

COLORS = (
    ('black', 'black'),
    ('white', 'white'),
    ('blue', 'blue'),
    ('red', 'red'),
    ('green', 'green'),
    ('yellow', 'yellow'),
)

FONTS = (
    ("Comic Sans MS, Comic Sans, Cursive", "Comic Sans"),
    ("Comic Neue", "Comic New"),
    ("Just Another Hand", "Sharpie"),
    ("Impact, fantasy", "Impact"),
    ("Optima, sans-serif", "Optima"),
    ("American Typewriter, serif", "Type-Writer"),
    ("Luminari, fantasy", "Folklore"),
    ("fantasy", "Folklore Two"),
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
    top_text = models.CharField(max_length=40, blank=True, null=True)
    bottom_text = models.CharField(max_length=40, blank=True, null=True)
    created_on = models.DateField(default=date.today)
    text_color = models.CharField(
        max_length=15,
        choices=COLORS,
        default=COLORS[0][0]
    )
    font = models.CharField(
        max_length=100,
        choices=FONTS,
        default=FONTS[0][0]
    )
    font_background_color = models.CharField(
        max_length=100,
        choices=COLORS,
        default=COLORS[1][0],
    )
    face = models.CharField(
        max_length=100,
        choices=FACES,
        default='',
        blank=True
    )
    font_size = models.CharField(
        max_length=5,
        choices=SIZE,
        default='20px',
        blank=True
    )
    likes = models.ManyToManyField(User, related_name='meme_likes')

    def __str__(self):
        return f"{self.top_text if self.top_text else ''}"

    class Meta:
        ordering = ['-id']
