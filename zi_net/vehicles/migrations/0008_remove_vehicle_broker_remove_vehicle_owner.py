# Generated by Django 5.1.6 on 2025-02-11 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0007_vehicle_broker_vehicle_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='broker',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='owner',
        ),
    ]
