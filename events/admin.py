# encoding: utf-8
# Copyright 2013 maker
# License

"""
	Events: admin page
"""
from maker.events.models import Event
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    """ 
    	Event admin 
    """
    list_display = ('name', 'start', 'end')

#admin.site.register(Event, EventAdmin)
