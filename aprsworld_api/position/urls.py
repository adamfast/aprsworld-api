from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<callsign>[-\w]+)/(?P<number_requested>\d+)', 'aprsworld_api.position.views.station_info'),
)
