# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from gs.group.member.join.join import JoinForm
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile


class JoinForm(JoinForm):
    pageTemplateFileName = 'browser/templates/join.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
