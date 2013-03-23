# encoding: utf-8
# Copyright 2013 maker
# License

#-*- coding: utf-8 -*-

from __future__ import absolute_import, with_statement

__all__ = [
           'KnowledgeFolderHandler',
           'KnowledgeCategoryHandler',
           'KnowledgeItemHandler',
           ]

from maker.core.api.utils import rc
from maker.core.api.handlers import ObjectHandler, getOrNone
from maker.knowledge.models import KnowledgeFolder, KnowledgeCategory, KnowledgeItem
from maker.knowledge.forms import KnowledgeFolderForm, KnowledgeItemForm, KnowledgeCategoryForm, \
                                     FilterForm, MassActionForm

class KnowledgeFolderHandler(ObjectHandler):
    "Entrypoint for KnowledgeFolder model."
    model = KnowledgeFolder
    form = KnowledgeFolderForm

    @staticmethod
    def resource_uri():
        return ('api_knowledge_folders', ['id'])

    def check_create_permission(self, request, mode):
        return True

    def flatten_dict(self, request):
        dct = super(KnowledgeFolderHandler, self).flatten_dict(request)
        dct['knowledgeType_id'] = None
        parent = request.data.get('parent')
        if parent:
            parent = getOrNone(KnowledgeFolder, pk=parent)
            if not parent or not request.user.get_profile().has_permission(parent, mode='x'):
                request.data['parent'] = None
        return dct

class KnowledgeCategoryHandler(ObjectHandler):
    "Entrypoint for KnowledgeCategory model."
    model = KnowledgeCategory
    form = KnowledgeCategoryForm

    @staticmethod
    def resource_uri():
        return ('api_knowledge_categories', ['id'])

    def flatten_dict(self, request):
        return {'data': request.data}

    def check_create_permission(self, request, mode):
        return True

class KnowledgeItemHandler(ObjectHandler):
    "Entrypoint for KnowledgeItem model."
    model = KnowledgeItem
    form = KnowledgeItemForm

    @staticmethod
    def resource_uri():
        return ('api_knowledge_items', ['id'])

    def flatten_dict(self, request):
        return {'data': request.data}

    def check_create_permission(self, request, mode):
        return True

    def flatten_dict(self, request):
        dct = super(KnowledgeFolderHandler, self).flatten_dict(request)
        dct['knowledgeType_id'] = None
        return dct
