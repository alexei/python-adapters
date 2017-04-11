# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .base import BaseField


__all__ = ['Field', 'CharField', 'IntField']


class Field(BaseField):
    pass


class CharField(BaseField):
    def adapt(self, data):
        return unicode(data)


class IntField(BaseField):
    def adapt(self, data):
        return int(data)
