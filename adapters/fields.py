# -*- coding: utf-8 -*-

from builtins import str
import datetime
import dateutil.parser
from decimal import Decimal
import six

from .base import BaseField
from .utils import EMPTY_VALUES, undefined


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
    def __init__(self, method_name=None, **kwargs):
        self.method_name = method_name
        super(AdapterMethodField, self).__init__(**kwargs)

    def bind(self, field_name, adapter):
        self.field_name = field_name
        self.adapter = adapter

    def get_attribute(self, obj):
        metod_name = self.method_name or 'get_' + self.field_name
        return getattr(self.adapter, metod_name)(obj)


class BooleanField(BaseField):
    def adapt(self, data):
        if data in EMPTY_VALUES or data is undefined:
            data = False
        return super(BooleanField, self).adapt(data)

    def prepare(self, data):
        return bool(data)


class CharField(BaseField):
    def prepare(self, data):
        return str(data)


class DateField(BaseField):
    def prepare(self, data):
        if isinstance(data, datetime.date):
            return data
        elif isinstance(data, six.string_types):
            return dateutil.parser.parse(data).date()
        else:
            raise ValueError("Invalid date argument")


class DateTimeField(BaseField):
    def prepare(self, data):
        if isinstance(data, datetime.datetime):
            return data
        elif isinstance(data, six.string_types):
            return dateutil.parser.parse(data)
        else:
            raise ValueError("Invalid date argument")


class DecimalField(BaseField):
    def prepare(self, data):
        return Decimal(data)


class VerbatimField(BaseField):
    pass


class FloatField(BaseField):
    def prepare(self, data):
        return float(data)


class IntField(BaseField):
    def prepare(self, data):
        return int(data)


class TimeField(BaseField):
    def prepare(self, data):
        if isinstance(data, datetime.time):
            return data
        elif isinstance(data, six.string_types):
            return dateutil.parser.parse(data).timetz()
        else:
            raise ValueError("Invalid time argument")
