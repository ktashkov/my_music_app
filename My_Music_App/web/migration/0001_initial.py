# Generated by Django 4.2.2 on 2023-06-22 00:01

import My_Music_App.web.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('POP MUSIC', 'Pop Music'), ('JAZZ MUSIC', 'Jazz Music'), ('R&B MUSIC', 'R&B Music'), ('ROCK MUSIC', 'Rock Music'), ('COUNTRY MUSIC', 'Country Music'), ('DANCE MUSIC', 'Dance Music'), ('HIP HOP MUSIC', 'Hip Hop Music'), ('OTHER', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'The price cannot be below 0.0')])),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), My_Music_App.web.models.validate_username])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]