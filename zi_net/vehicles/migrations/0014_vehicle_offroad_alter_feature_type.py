# Generated by Django 5.1.6 on 2025-02-12 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0013_vehicle_battery_capacity_vehicle_horsepower_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='offroad',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='vehicles.featuretype'),
        ),
    ]
