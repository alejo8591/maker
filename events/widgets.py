# encoding: utf-8
# Copyright 2013 maker
# License


"""
	Events module widgets
"""

WIDGETS = {'widget_week_view': {'title': 'Calendar: This Week',
                                'size': "95%"}}

def get_widgets(request):
    "Returns a set of all available widgets"    
    return WIDGETS