# -*- coding: utf-8 -*-

from .helpers import get_attribute
from .utils import EMPTY_VALUES, undefined


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

    @property
    def is_bound(self):
        return hasattr(self, 'field_name') and hasattr(self, 'adapter')

    def get_attribute(self, obj):
        return get_attribute(obj, self.lookup_attrs)

    def adapt(self, data):
        if data in EMPTY_VALUES or data is undefined:
            if self.default is not undefined:
                return self.default
            elif self.required:
                if self.is_bound:
                    error = (
                        "Required value not found for field "
                        "`{adapter_name}.{field_name}`. "
                        "Provide a default value."
                    ).format(
                        adapter_name=self.adapter.__class__.__name__,
                        field_name=self.field_name,
                    )
                else:
                    error = "Required value not found. Provide a default value."
                raise ValueError(error)
            else:
                return undefined
        else:
            return self.prepare(data)

    def prepare(self, data):
        return data
