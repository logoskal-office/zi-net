from django.core.management.base import BaseCommand
from vehicles.models import Feature, FeatureType

class Command(BaseCommand):
    help = 'Populate the Feature model with default data'

    def handle(self, *args, **kwargs):
        features_data = [
            {'name': 'Cruise Control', 'description': 'Description for feature 1'},
            {'name': 'Self Driving', 'description': 'Description for feature 2'},
            {'name': 'Rear View Camera', 'description': 'Description for feature 2'},
            {'name': 'Bluetooth', 'description': 'Description for feature 2'},
            {'name': 'WiFi Hotspot', 'description': 'Description for feature 2'},
            {'name': 'Leather Seats', 'description': 'Description for feature 2'},
            {'name': 'Anti-Lock Brakes', 'description': 'Description for feature 2'},
            {'name': 'Heated Seats', 'description': 'Description for feature 2'},
            # Add more as needed
        ]

        for feature_data in features_data:
            feature, created = Feature.objects.update_or_create(
                name=feature_data['name'],
                defaults={'description': feature_data['description']},
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created {feature.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'{feature.name} already exists'))
