# encoding: utf-8
# Copyright 2013 maker
# License


"""
    Domain middleware: enables multi-tenancy in a single Tree.io process
"""
from maker.core.domains import setup_domain, setup_domain_database
from maker.core.db import DatabaseNotFound
from maker.core.conf import settings
from django.http import HttpResponseRedirect
from django.db.utils import DatabaseError
from django.core.urlresolvers import reverse
from pandora import box

class DomainMiddleware():
    "Handles multiple domains within the same Django process"
    
    def process_request(self, request):
        "Identify the current domain and database, set up appropriate variables in the pandora box"
        
        domain = request.get_host().split('.')[0]
        try:
            setup_domain(domain)
        except DatabaseNotFound:
            evergreen_url = getattr(settings, 'EVERGREEN_BASE_URL', 'http://tree.io/')
            return HttpResponseRedirect(evergreen_url)
        except DatabaseError:
            from django.db import router
            from maker.core.models import ConfigSetting
            setup_domain_database(router.db_for_read(ConfigSetting))
            return HttpResponseRedirect(reverse('database_setup'))
        box['request'] = request

    def process_exception(self, request, exception):
        if isinstance(exception, DatabaseNotFound):
            evergreen_url = getattr(settings, 'EVERGREEN_BASE_URL', 'http://tree.io/')
            return HttpResponseRedirect(evergreen_url)
