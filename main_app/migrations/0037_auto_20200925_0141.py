# Generated by Django 3.0.8 on 2020-09-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0036_auto_20200925_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='font_background_color',
            field=models.CharField(choices=[('black', 'black'), ('white', 'white'), ('blue', 'blue'), ('red', 'red'), ('green', 'green')], default='white', max_length=100),
        ),
    ]