# Generated by Django 3.1.7 on 2021-04-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0015_event_interested'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalitem',
            name='image',
            field=models.ImageField(default="test.jpg", upload_to='images'),
            preserve_default=False,
        ),
    ]
