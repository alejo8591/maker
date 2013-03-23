# encoding: utf-8
# Copyright 2013 maker
# License

"""
	Core Search module URLs
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('maker.core.search.views',
        url(r'^(\.(?P<response_format>\w+))?/?$', 'search_query', name='core_search_query'),
)

