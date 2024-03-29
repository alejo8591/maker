# encoding: utf-8
# Copyright 2013 maker
# License

"""
    Handle objects from this module relevant to a Contact or a User
"""
from maker.core.models import Object
from maker.sales.templatetags.sales import sales_order_list, sales_lead_list, sales_opportunity_list

CONTACT_OBJECTS = {}
CONTACT_OBJECTS['saleorder_set']  = {
     'label': 'Sale Orders',
     'objects': [],
     'templatetag': sales_order_list
}

CONTACT_OBJECTS['lead_set']  = {
    'label': 'Leads',
    'objects': [],
    'templatetag': sales_lead_list
}

CONTACT_OBJECTS['opportunity_set']  = {
    'label': 'Opportunities',
    'objects': [],
    'templatetag': sales_opportunity_list
}

USER_OBJECTS = {}
USER_OBJECTS['sales_saleorder_assigned'] = {'label': 'Assigned Orders',
                            'objects': [],
                            'templatetag': sales_order_list}


def get_contact_objects(current_user, contact):
    """
        Returns a dictionary with keys specified as contact attributes
        and values as dictionaries with labels and set of relevant objects.
    """
    
    objects = dict(CONTACT_OBJECTS)
    
    for key in objects:
        if hasattr(contact, key):
            objects[key]['objects'] = Object.filter_permitted(current_user, getattr(contact, key))
    
    return objects


def get_user_objects(current_user, user):
    """
    Returns a dictionary with keys specified as contact attributes
    and values as dictionaries with labels and set of relevant objects.
    """
    
    objects = dict(USER_OBJECTS)
    
    for key in objects:
        if hasattr(user, key):
            objects[key]['objects'] = Object.filter_permitted(current_user, getattr(user, key))
            
    return objects

    
