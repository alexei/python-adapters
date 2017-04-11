# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from decimal import Decimal

from .base import BaseField


__all__ = ['Field', 'CharField', 'DecimalField', 'FloatField', 'IntField']


class Field(BaseField):
    pass


class CharField(BaseField):
    def adapt(self, data):
        return unicode(data)


class DecimalField(BaseField):
    def adapt(self, data):
        return Decimal(data)


class FloatField(BaseField):
    def adapt(self, data):
        return float(data)


class IntField(BaseField):
    def adapt(self, data):
        return int(data)
