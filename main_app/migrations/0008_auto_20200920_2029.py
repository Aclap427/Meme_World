# Generated by Django 3.1.1 on 2020-09-20 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20200920_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meme',
            old_name='photo',
            new_name='photo_URL',
        ),
    ]
