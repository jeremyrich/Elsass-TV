# Generated by Django 2.0 on 2019-02-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20190205_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='known_for_department',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='place_of_birth',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='popularity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile_path',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
