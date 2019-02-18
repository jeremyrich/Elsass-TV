# Generated by Django 2.0 on 2019-02-15 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20190215_0836'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFriend',
            new_name='UserCustom',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='user',
        ),
        migrations.AddField(
            model_name='friendship',
            name='source_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserCustom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friendship',
            name='target_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='target_user', to='accounts.UserCustom'),
            preserve_default=False,
        ),
    ]