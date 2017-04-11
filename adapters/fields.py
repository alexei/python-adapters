# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .base import BaseField


__all__ = ['Field', 'CharField']


class Field(BaseField):
    pass


class CharField(BaseField):
    def adapt(seld, data):
        return unicode(data)
