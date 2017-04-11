# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

from .helpers import get_attribute
from .utils import undefined


class BaseField(object):
    def __init__(self, source=None, default=undefined, required=True):
        self.source = source
        self.default = default
        self.required = required

    def bind(self, field_name, adapter):
        if field_name == self.source:
            raise ValueError((
                "The `source='{field_name}'` kwarg is redundant on "
                "field `{adapter_name}.{field_name}`. "
                "Remove the `source` kwarg."
            ).format(
                field_name=field_name,
                adapter_name=adapter.__class__.__name__,
            ))

        self.field_name = field_name
        self.adapter = adapter

        if self.source is None:
            self.source = self.field_name

        if self.source == '*':
            self.lookup_attrs = []
        else:
            self.lookup_attrs = self.source.split('.')

    def get_attribute(self, obj):
        value = get_attribute(obj, self.lookup_attrs)
        if value is undefined:
            if self.default is not undefined:
                return self.default
            elif self.required:
                raise ValueError((
                    "Required value not found for field "
                    "`{adapter_name}.{field_name}`. Provide a default value."
                ).format(
                    adapter_name=self.adapter.__class__.__name__,
                    field_name=self.field_name,
                ))
            else:
                return undefined
        else:
            return value

    def adapt(self, data):
        return data
