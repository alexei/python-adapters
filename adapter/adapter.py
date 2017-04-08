# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import collections
import copy
import six


__all__ = ['Adapter', 'Field']


class undefined:
    pass


class BindingDict(collections.MutableMapping):
    def __init__(self, adapter):
        self.adapter = adapter
        self.fields = collections.OrderedDict()

    def __setitem__(self, key, field):
        self.fields[key] = field
        field.bind(key, self.adapter)

    def __getitem__(self, key):
        return self.fields[key]

    def __delitem__(self, key):
        del self.fields[key]

    def __iter__(self):
        return iter(self.fields)

    def __len__(self):
        return len(self.fields)

    def __repr__(self):
        return dict.__repr__(self.fields)


def get_attribute(obj, attrs):
    for attr in attrs:
        if obj is None:
            return undefined

        try:
            if isinstance(obj, collections.Mapping):
                obj = obj[attr]
            elif isinstance(obj, (list, tuple)):
                obj = obj[int(attr)]
            else:
                obj = getattr(obj, attr)
        except Exception:
            return undefined

        if callable(obj):
            obj = obj()

    return obj


class BaseField(object):
    def __init__(self, source=None, default=undefined):
        self.source = source
        self.default = default

    def bind(self, field_name, adapter):
        if field_name == self.source:
            raise ValueError((
                "The `source='{field_name}'` kwarg is redundant on "
                "adapter `{adapter_name}. Remove the `source` kwarg."
            ).format({
                'field_name': field_name,
                'adapter_name': adapter.__class__.__name__
            }))

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
        if value is not undefined:
            return value
        else:
            return self.default

    def adapt(self, data):
        return data


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


class Field(BaseField):
    pass


@six.add_metaclass(AdapterMetaClass)
class Adapter(BaseField):
    def __init__(self, data=None, *args, **kwargs):
        self.data = data

        super(Adapter, self).__init__(*args, **kwargs)

    @property
    def fields(self):
        if not hasattr(self, '_fields'):
            self._fields = BindingDict(self)
            for key, value in self.get_fields().iteritems():
                self._fields[key] = value
        return self._fields

    def get_fields(self):
        return copy.deepcopy(self.declared_fields)

    def adapt(self, data=None):
        meta = getattr(self, 'Meta', None)
        model_cls = getattr(meta, 'model', dict)
        obj = model_cls()
        for field_name, field in self.fields.iteritems():
            value = field.get_attribute(data or self.data)
            adapted_value = field.adapt(value)
            if isinstance(obj, collections.Mapping):
                obj[field_name] = adapted_value
            else:
                setattr(obj, field_name, adapted_value)
        return obj
