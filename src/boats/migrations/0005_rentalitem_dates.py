# Generated by Django 3.1.7 on 2021-04-06 02:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0004_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalitem',
            name='dates',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
