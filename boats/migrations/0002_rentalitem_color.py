# Generated by Django 3.1.7 on 2021-06-16 13:11

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalitem',
            name='color',
            field=colorfield.fields.ColorField(default='#90EE90', max_length=18),
        ),
    ]
