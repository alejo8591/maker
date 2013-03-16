# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of maker.
# License www.tree.io/license

"""
API admin definitions
"""

from django.contrib import admin
from maker.core.api.models import Consumer, Token, Nonce

admin.site.register(Consumer)
admin.site.register(Token)
admin.site.register(Nonce)
