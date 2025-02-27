from vehicles.models import Producer

def phone_numbers(request):
    return {'phone_number_1': '+111', 'phone_number_2': '+222', 'phone_number_3': '+333'}

def emails(request):
    return {'email_1': 'email@gmail.com', 'email_2': 'email@zi-net.com'}

def socials(request):
    return {'whatsapp_1': 'whatsapp_1',
            'whatsapp_2': 'whatsapp_2',
            'whatsapp_3': 'whatsapp_3',
            'telegram': 'telegram',
            'instagram': 'instagram',
            'facebook': 'facebook',
            'linkedin': 'linkedin',
            }

def global_data(request):
    return {'site_name': 'Zi-Mekina',
        'producers':Producer.objects.all()}