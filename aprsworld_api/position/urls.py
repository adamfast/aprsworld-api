from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # latest - will only return one record
    # can pass a ?format=<serialization format> to get it in your preferred format. yaml, json, xml
    url(r'^latest/(?P<callsign>[-\w]+)/$', 'aprsworld_api.position.views.station_latest_position'),

    # all - will return 10 unless you pass in the (optional) number_requested parameter
    # can pass a ?format=<serialization format> to get it in your preferred format. yaml, json, xml
    url(r'^(?P<callsign>[-\w]+)/(?P<number_requested>\d+)/$', 'aprsworld_api.position.views.station_positions'),
    url(r'^(?P<callsign>[-\w]+)/$', 'aprsworld_api.position.views.station_positions'),
)
