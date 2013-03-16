# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of maker.
# License www.tree.io/license

"""
Events: admin page
"""
from maker.events.models import Event
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
    """ Event admin """
    list_display = ('name', 'start', 'end')

admin.site.register(Event, EventAdmin)
