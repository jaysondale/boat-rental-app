# Generated by Django 3.1.7 on 2021-04-19 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boats', '0017_auto_20210418_2118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'permissions': [('view_all_system_bookings', 'Can view bookings made by all system users')]},
        ),
    ]