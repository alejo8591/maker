# encoding: utf-8
# Copyright 2013 maker
# License

#!/usr/bin/python

OBJECTS_NUM = 100

# setup environment
import sys, os
sys.path.append('../')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.management import setup_environ
from maker import settings
from maker.core.models import Object, User
from maker.projects.models import Project

setup_environ(settings)

user = User.objects.all()[0]

for i in range(0, OBJECTS_NUM):
    project = Project(name='test'+unicode(i))
    project.set_user(user)
    project.save()
    objects = Object.filter_permitted(user, Project.objects)
    allowed = 0
    for obj in objects:
        if user.has_permission(obj):
            allowed += 1
    print len(list(objects)), ':', allowed
