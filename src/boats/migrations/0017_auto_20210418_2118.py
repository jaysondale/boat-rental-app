# Generated by Django 3.1.7 on 2021-04-18 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0016_rentalitem_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentalitem',
            name='endDay',
        ),
        migrations.RemoveField(
            model_name='rentalitem',
            name='startDay',
        ),
    ]
