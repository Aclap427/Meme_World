# Generated by Django 3.1.1 on 2020-09-24 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0032_auto_20200923_2250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meme',
            options={'ordering': ['-id']},
        ),
    ]
