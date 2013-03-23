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

#identities resources
contactFieldResource = CsrfExemptResource(handler = handlers.ContactFieldHandler, **ad)
contactTypeResource = CsrfExemptResource(handler = handlers.ContactTypeHandler, **ad)
contactResource = CsrfExemptResource(handler = handlers.ContactHandler, **ad)

urlpatterns = patterns('',
#Identities
    url(r'^doc$', documentation_view, kwargs={'module': handlers}, name="api_identities_doc"),
    url(r'^fields$', contactFieldResource, name="api_identities_fields"),
    url(r'^field/(?P<object_ptr>\d+)', contactFieldResource, name="api_identities_fields"),
    url(r'^types$', contactTypeResource, name="api_identities_types"),
    url(r'^type/(?P<object_ptr>\d+)', contactTypeResource, name="api_identities_types"),
    url(r'^contacts$', contactResource, name="api_identities_contacts"),
    url(r'^contact/(?P<object_ptr>\d+)', contactResource, name="api_identities_contacts"),
)
