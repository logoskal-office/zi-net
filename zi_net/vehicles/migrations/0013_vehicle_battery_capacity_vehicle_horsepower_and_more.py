# Generated by Django 5.1.6 on 2025-02-12 16:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0012_alter_vehicleimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='battery_capacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(500000)], verbose_name='Battery Capacity In kWh'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='horsepower',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2000)]),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='range',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2000)], verbose_name='Range In KM'),
        ),
        migrations.AlterField(
            model_name='vehicleimage',
            name='image',
            field=models.FileField(upload_to='vehicles/images/'),
        ),
    ]
