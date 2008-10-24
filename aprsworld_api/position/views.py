from django.core import serializers
from models import Position, LastPosition

def station_info(callsign, number_requested):
    print('Call: *%s*, Number: *%s*' % (callsign, number_requested))
    data = Position.objects.filter(callsign__startswith=callsign)[number_requested]
    return HttpResponse(serializers.serialize("xml", data))
