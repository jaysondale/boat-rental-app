# Generated by Django 3.1.7 on 2021-03-17 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0002_auto_20210317_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rentalitem',
            old_name='weekdayPrice',
            new_name='weekPrice',
        ),
    ]
