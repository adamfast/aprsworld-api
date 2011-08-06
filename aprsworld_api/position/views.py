from django.core import serializers
from django.http import HttpResponse
from models import Position, LastPosition

def station_positions(request, callsign, number_requested=10):
    data = Position.objects.using('aprs').filter(source__startswith=callsign).order_by('-packet_date')[:number_requested]

    # handle different formats, but make sure it's something valid
    if request.GET['format'] == 'xml':
        format = 'xml'
    elif request.GET['format'] == 'json':
        format = 'json'
    else:
        format = 'yaml'

    return HttpResponse(serializers.serialize(format, data))

def station_latest_position(request, callsign):
    data = LastPosition.objects.using('aprs').filter(source__startswith=callsign)
    if data:
        # handle different formats, but make sure it's something valid
        if request.GET['format'] == 'xml':
            format = 'xml'
        elif request.GET['format'] == 'json':
            format = 'json'
        else:
            format = 'yaml'

        return HttpResponse(serializers.serialize(format, data))
    else:
        return HttpResponse("")
