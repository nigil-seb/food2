# Generated by Django 3.2.3 on 2021-05-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodoorapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
