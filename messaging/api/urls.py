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

#messaging resources
mlistResource = CsrfExemptResource(handler = handlers.MailingListHandler, **ad)
streamResource = CsrfExemptResource(handler = handlers.MessageStreamHandler, **ad)
messageResource = CsrfExemptResource(handler = handlers.MessageHandler, **ad)

urlpatterns = patterns('',
#Messaging
    url(r'^doc$', documentation_view, kwargs={'module': handlers}, name="api_messaging_doc"),
    url(r'^mlist$', mlistResource, name="api_messaging_mlist"),
    url(r'^mlist/(?P<object_ptr>\d+)', mlistResource, name="api_messaging_mlist"),
    url(r'^streams$', streamResource, name="api_messaging_streams"),
    url(r'^stream/(?P<object_ptr>\d+)', streamResource, name="api_messaging_streams"),
    url(r'^messages$', messageResource, name="api_messaging_messages"),
    url(r'^message/(?P<object_ptr>\d+)', messageResource, name="api_messaging_messages"),
)
