# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
import dateutil.parser
from decimal import Decimal

from .base import BaseField


__all__ = [
    'AdapterMethodField',
    'BooleanField',
    'CharField',
    'DateField',
    'DateTimeField',
    'DecimalField',
    'FloatField',
    'IntField',
    'TimeField',
    'VerbatimField',
]


class AdapterMethodField(BaseField):
    def __init__(self, method_name=None):
        self.method_name = method_name

    def bind(self, field_name, adapter):
        self.field_name = field_name
        self.adapter = adapter

    def get_attribute(self, obj):
        metod_name = self.method_name or 'get_' + self.field_name
        return getattr(self.adapter, metod_name)(obj)


class BooleanField(BaseField):
    def adapt(self, data):
        return bool(data)


class CharField(BaseField):
    def adapt(self, data):
        return unicode(data)


class DateField(BaseField):
    def adapt(self, data):
        if isinstance(data, datetime.date):
            return data
        elif isinstance(data, (str, unicode)):
            return dateutil.parser.parse(data).date()
        else:
            raise ValueError("Invalid date argument")


class DateTimeField(BaseField):
    def adapt(self, data):
        if isinstance(data, datetime.datetime):
            return data
        elif isinstance(data, (str, unicode)):
            return dateutil.parser.parse(data)
        else:
            raise ValueError("Invalid date argument")


class DecimalField(BaseField):
    def adapt(self, data):
        return Decimal(data)


class VerbatimField(BaseField):
    pass


class FloatField(BaseField):
    def adapt(self, data):
        return float(data)


class IntField(BaseField):
    def adapt(self, data):
        return int(data)


class TimeField(BaseField):
    def adapt(self, data):
        if isinstance(data, datetime.time):
            return data
        elif isinstance(data, (str, unicode)):
            return dateutil.parser.parse(data).timetz()
        else:
            raise ValueError("Invalid time argument")
