# Generated by Django 2.0 on 2019-02-20 13:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0009_auto_20190207_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
