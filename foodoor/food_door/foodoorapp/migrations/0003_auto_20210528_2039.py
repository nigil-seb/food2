# Generated by Django 3.2.3 on 2021-05-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodoorapp', '0002_product_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='item'),
        ),
    ]
