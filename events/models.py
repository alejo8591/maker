# encoding: utf-8
# Copyright 2013 maker
# License


"""
    Events module objects.
    Depends on: maker.core, maker.identities
"""

from django.db import models
from django.core.urlresolvers import reverse
from maker.identities.models import Contact
from maker.core.models import Object, Location

class Event(Object):
    """ 
        Single Event 
    """
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)
    details = models.TextField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField()
    
    class Meta:
        "Event"
        ordering = ['-end']
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        "Returns absolute URL of the object"
        try:
            return reverse('events_event_view', args=[self.id])
        except Exception:
            return ""
    

class Invitation(models.Model):
    """ 
        Invitation to an Event 
    """
    contact = models.ForeignKey(Contact)
    event = models.ForeignKey(Event)
    status = models.CharField(max_length=255, choices=(('attending', 'Attending'),
                                                       ('pending', 'Pending'),
                                                       ('not-attending', 'Not Attending')))

    
    
