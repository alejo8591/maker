# encoding: utf-8
# Copyright 2013 maker
# License

"""
	Projects module widgets
"""

WIDGETS = {'widget_tasks_assigned_to_me': {'title': 'Tasks Assigned To Me',
                            'size': "95%"}}

def get_widgets(request):
    "Returns a set of all available widgets"
        
    return WIDGETS