# encoding: utf-8
# Copyright 2013 maker
# License

"""
    Hardtree URLs
"""
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

def if_installed(appname, *args, **kwargs):
    ret = url(*args, **kwargs)
    if appname not in settings.INSTALLED_APPS:
        ret = url(r'^(\.(?P<response_format>\w+))?$', 'maker.core.dashboard.views.index', name='home')
        #ret.resolve = lambda *args: None
    return ret

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(\.(?P<response_format>\w+))?$', 'maker.core.dashboard.views.index', name='home'),
    
    (r'^user/', include('maker.core.urls')),
    (r'^accounts/', include('maker.core.urls')),
    
    (r'^account/', include('maker.account.urls')),
    
    (r'^search/', include('maker.core.search.urls')),
    (r'^dashboard/', include('maker.core.dashboard.urls')),
    (r'^admin/', include('maker.core.administration.urls')),
    
    (r'^trash/', include('maker.core.trash.urls')),
    
    (r'^documents/', include('maker.documents.urls')),
    (r'^calendar/', include('maker.events.urls')),
    (r'^finance/', include('maker.finance.urls')),
    (r'^contacts/', include('maker.identities.urls')),
    (r'^infrastructure/', include('maker.infrastructure.urls')),
    (r'^knowledge/', include('maker.knowledge.urls')),
    (r'^messaging/', include('maker.messaging.urls')),
    (r'^news/', include('maker.news.urls')),
    (r'^projects/', include('maker.projects.urls')),
    (r'^sales/', include('maker.sales.urls')),
    (r'^services/', include('maker.services.urls')),
    (r'^reports/', include('maker.reports.urls')),
    
    # API handlers
    (r'^api/', include('maker.core.api.urls')),
    
    # Forest
    if_installed('maker.forest', r'^forest/', include('maker.forest.urls')),

    # Mobile handler
    url(r'^m(?P<url>.+)?$', 'maker.core.views.mobile_view', name='core_mobile_view'),
    
    # Help handler
    url(r'^help(?P<url>[a-zA-Z0-9-_/]+)?(\.(?P<response_format>\w+))?$', 'maker.core.views.help_page', name='core_help_page_view'),
    
    # Close iframe
    url(r'^iframe/?$', 'maker.core.views.iframe_close', name='core_iframe_close'),
    
    # Nuvius Connector
    (r'^nuconnector/', include('nuconnector.urls')),

    # Captcha Config
    url(r'^captcha/', include('captcha.urls')),
    
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Changed to backend (because it's backend!)
     (r'^backend/', include(admin.site.urls)),
     (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )
