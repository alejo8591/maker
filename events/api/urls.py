# encoding: utf-8
# Copyright 2013 maker
# License


#-*- coding: utf-8 -*-

import handlers
from django.conf.urls.defaults import *
from maker.core.api.auth import auth_engine
from maker.core.api.doc import documentation_view
from maker.core.api.resource import CsrfExemptResource

ad = { 'authentication': auth_engine }

#events resources
eventResource = CsrfExemptResource(handler = handlers.EventHandler, **ad)


urlpatterns = patterns('',
#Events
    url(r'^doc$', documentation_view, kwargs={'module': handlers}, name="api_events_doc"),
    url(r'^events$', eventResource, name="api_events"),
    url(r'^event/(?P<object_ptr>\d+)', eventResource, name="api_events"),
)
