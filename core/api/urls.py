# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of maker.
# License www.tree.io/license

#from piston.resource import Resource
from django.conf.urls.defaults import *

urlpatterns = patterns('',
   (r'^auth/', include('maker.core.api.auth.urls')),
   (r'^news/', include('maker.news.api.urls')),
   (r'^core/', include('maker.core.administration.api.urls')),
   (r'^projects/', include('maker.projects.api.urls')),
   (r'^services/', include('maker.services.api.urls')),
   (r'^sales/', include('maker.sales.api.urls')),
   (r'^finance/', include('maker.finance.api.urls')),
   (r'^knowledge/', include('maker.knowledge.api.urls')),
   (r'^messaging/', include('maker.messaging.api.urls')),
   (r'^infrastructure/', include('maker.infrastructure.api.urls')),
   (r'^calendar/', include('maker.events.api.urls')),
   (r'^documents/', include('maker.documents.api.urls')),
   (r'^identities/', include('maker.identities.api.urls')),
)


