# Generated by Django 2.0 on 2019-02-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20190205_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='Popularity',
            new_name='popularity',
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tagline',
            field=models.TextField(),
        ),
    ]
