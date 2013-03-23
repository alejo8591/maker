# encoding: utf-8
# Copyright 2013 maker
# License

"""
	API admin definitions
"""

from django.contrib import admin
from maker.core.api.models import Consumer, Token, Nonce

admin.site.register(Consumer)
admin.site.register(Token)
admin.site.register(Nonce)
