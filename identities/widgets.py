# encoding: utf-8
# Copyright 2013 maker
# License

"""
	Identities module widgets
"""

WIDGETS = {'widget_contact_me': {'title': 'My Contact Card',
                            'size': "95%"}}

def get_widgets(request):
    "Returns a set of all available widgets"
        
    return WIDGETS