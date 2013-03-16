# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of maker.
# License www.tree.io/license

"""
Utilities to deal with multitenancy within a single Hardtree
"""
from django.conf import settings
from maker.core.models import ConfigSetting
from pandora import box

def setup_domain(domain):
    box['CURRENT_DOMAIN'] = domain
    box['CURRENT_DATABASE_NAME'] = domain
    
    word = getattr(settings, 'HARDTREE_MULTITENANCY_REPLACE_WORD', 'seed') 
    box['STATIC_DOC_ROOT'] = getattr(settings, 'STATIC_DOC_ROOT', './static').replace(word, domain)
    if hasattr(settings, 'MEDIA_ROOT_SEED'):
        box['MEDIA_ROOT'] = getattr(settings, 'MEDIA_ROOT_SEED').replace(word, domain)
    else:
        box['MEDIA_ROOT'] = getattr(settings, 'MEDIA_ROOT', './static/media/').replace(word, domain)
    
    #box['TEMPLATE_DIRS'] = (dir.replace(word, domain) for dir in settings.TEMPLATE_DIRS)
    
    #box['JOHNNY_MIDDLEWARE_KEY_PREFIX'] = getattr(settings, 'JOHNNY_MIDDLEWARE_KEY_PREFIX', 'jc_maker_seed').replace(word, domain)
    
    box['WHOOSH_INDEX'] = getattr(settings, 'WHOOSH_INDEX', '/srv/vhosts/maker.com/subdomains/seed/maker/storage/search').replace(word, domain)
    
    box['WKPATH'] = getattr(settings, 'WKPATH', '/srv/vhosts/maker.com/maker/bin/wkhtmltopdf').replace(word, domain)
    box['WKCWD'] = getattr(settings, 'WKCWD', '/srv/vhosts/maker.com/subdomains/seed/maker/').replace(word, domain)
    
    for setting in ConfigSetting.objects.all():
        box[setting.name] = setting.loads()
    return box

def setup_domain_database(domain, load_initial = False):
    from maker.core.db.creation import DatabaseCreation

    dc = DatabaseCreation(domain)
    dc.create_db(load_initial)
    dc.connection.close()

