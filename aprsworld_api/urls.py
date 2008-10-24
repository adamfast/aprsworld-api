from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^positions/', include('aprsworld_api.position.urls')),

)
