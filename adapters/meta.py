# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import collections

from .base import BaseField


__all__ = ['AdapterMetaClass']


class AdapterMetaClass(type):
    def __new__(meta, name, bases, attrs):
        fields = [
            (key, attrs.pop(key))
            for key in attrs.keys() if isinstance(attrs[key], BaseField)
        ]

        for base in reversed(bases):
            if hasattr(base, 'declared_fields'):
                fields = list(base.declared_fields.items()) + fields

        attrs['declared_fields'] = collections.OrderedDict(fields)

        cls = super(AdapterMetaClass, meta).__new__(meta, name, bases, attrs)

        return cls
