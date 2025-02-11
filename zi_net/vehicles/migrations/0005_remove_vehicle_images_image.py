# Generated by Django 5.1.6 on 2025-02-11 09:15

import django.db.models.deletion
import vehicles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_remove_feature_logo_alter_featuretype_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='images',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=vehicles.models.get_upload_location_based_on_id)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='vehicles.vehicle')),
            ],
        ),
    ]
