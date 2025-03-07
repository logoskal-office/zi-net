# Generated by Django 5.1.6 on 2025-02-06 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('logo', models.ImageField(upload_to='logos/feature-type-logos')),
            ],
            options={
                'verbose_name': 'Feature Type',
                'verbose_name_plural': 'Feature Types',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('logo', models.ImageField(upload_to='logos/vehicle-producers/')),
            ],
            options={
                'verbose_name': 'Producer',
                'verbose_name_plural': 'Producers',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('logo', models.ImageField(upload_to='logos/feature-logos')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vehicles.featuretype')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=40, verbose_name='Model')),
                ('common_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Common Name')),
                ('production_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Production Year')),
                ('production_country', models.CharField(choices=[('JP', 'Japan'), ('US', 'United States'), ('DE', 'Germany'), ('CN', 'China'), ('IN', 'India'), ('IT', 'Italy'), ('MX', 'Mexico'), ('KR', 'South Korea'), ('BR', 'Brazil'), ('FR', 'France'), ('ES', 'Spain'), ('CA', 'Canada'), ('UK', 'United Kingdom'), ('RU', 'Russia'), ('TR', 'Turkey'), ('NN', 'Other')], max_length=10, null=True, verbose_name='Production Country')),
                ('price', models.PositiveIntegerField(null=True, verbose_name='Price')),
                ('price_negotiability', models.BooleanField(choices=[('Yes', True), ('No', False)], null=True, verbose_name='Negotiable')),
                ('existing_debt', models.IntegerField(blank=True, default=0, null=True, verbose_name='Existing-Debt')),
                ('body_type', models.CharField(choices=[('SD', 'Sedan'), ('SV', 'SUV'), ('HB', 'Hatchback'), ('CP', 'Coupe'), ('CM', 'Compact'), ('CV', 'Convertible'), ('MV', 'Minivan'), ('PU', 'Pickup Truck'), ('SC', 'Sports Car'), ('LC', 'Luxury Car'), ('CN', 'Construction Vehicle'), ('LM', 'Limousine'), ('NN', 'Other')], max_length=20, null=True, verbose_name='Body Type')),
                ('color', models.CharField(blank=True, choices=[('BK', 'Black'), ('WT', 'White'), ('SV', 'Silver'), ('RD', 'Red'), ('BL', 'Blue'), ('GY', 'Gray'), ('BG', 'Beige'), ('BN', 'Brown'), ('BZ', 'Bronze'), ('CA', 'Caramel'), ('CH', 'Charcoal'), ('CP', 'Copper'), ('CY', 'Cyan'), ('EM', 'Emerald'), ('FC', 'Fuchsia'), ('GD', 'Gold'), ('GN', 'Green'), ('IV', 'Ivory'), ('LM', 'Lime'), ('MT', 'Mint'), ('NV', 'Navy'), ('OG', 'Orange'), ('PN', 'Pink'), ('PU', 'Purple'), ('TQ', 'Turquoise'), ('YL', 'Yellow'), ('NN', 'Other')], max_length=20, null=True, verbose_name='Color')),
                ('seat_size', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number Of Seats')),
                ('cylinder_number', models.SmallIntegerField(blank=True, null=True, verbose_name='Cylinder Number')),
                ('mileage', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Mileage')),
                ('condition', models.CharField(blank=True, choices=[('S', 'Brand New'), ('A', 'Excellent'), ('B', 'Good'), ('C', 'Sub-Optimal'), ('D', 'Bad'), ('F', 'Non-Working'), ('NN', 'Other')], max_length=20, null=True, verbose_name='Condition')),
                ('condition_check', models.BooleanField(blank=True, choices=[('Yes', True), ('No', 'False')], null=True)),
                ('transmission', models.CharField(blank=True, choices=[('AU', 'Automatic'), ('MN', 'Manual'), ('SM', 'Semi-Auto'), ('NN', 'Other')], max_length=20, null=True, verbose_name='Transmission')),
                ('fuel_type', models.CharField(blank=True, choices=[('BN', 'Benzene'), ('DS', 'Diesel'), ('EL', 'Electric'), ('HY', 'Hybrid'), ('NN', 'Other')], max_length=20, null=True, verbose_name='Fuel')),
                ('plate_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Plate Number')),
                ('plate_ownership', models.PositiveIntegerField(blank=True, null=True, verbose_name='Type of Plate Number')),
                ('plate_state', models.CharField(blank=True, choices=[('AA', 'Addis Ababa'), ('OR', 'Oromia'), ('FD', 'Federal'), ('NN', 'Other')], max_length=20, null=True, verbose_name='State Of Issued Plated')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Description')),
                ('issues', models.TextField(blank=True, max_length=2000, null=True)),
                ('images', models.ImageField(blank=True, upload_to='albums/temp/')),
                ('features', models.ManyToManyField(blank=True, to='vehicles.feature', verbose_name='Features')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vehicles.producer', verbose_name='Producer/Manufacturer')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
            },
        ),
    ]
