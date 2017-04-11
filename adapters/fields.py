# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from decimal import Decimal

from .base import BaseField


__all__ = [
    'BooleanField', 'CharField', 'DecimalField', 'Field', 'FloatField',
    'IntField']


class BooleanField(BaseField):
    def adapt(self, data):
        return bool(data)


class CharField(BaseField):
    def adapt(self, data):
        return unicode(data)


class DecimalField(BaseField):
    def adapt(self, data):
        return Decimal(data)


class Field(BaseField):
    pass


class FloatField(BaseField):
    def adapt(self, data):
        return float(data)


class IntField(BaseField):
    def adapt(self, data):
        return int(data)
