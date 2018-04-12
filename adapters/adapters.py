# -*- coding: utf-8 -*-

import collections
import copy
import six

from .base import BaseField
from .meta import AdapterMetaClass
from .utils import BindingDict
from .utils import undefined


__all__ = ['Adapter']


@six.add_metaclass(AdapterMetaClass)
class Adapter(BaseField):
    def __init__(self, data=None, instance=None, *args, **kwargs):
        self.data = data
        self.instance = instance

        super(Adapter, self).__init__(*args, **kwargs)

    @property
    def fields(self):
        if not hasattr(self, '_fields'):
            self._fields = BindingDict(self)
            for key, value in self.get_fields().items():
                self._fields[key] = value
        return self._fields

    def get_fields(self):
        return copy.deepcopy(self.declared_fields)

    def adapt(self, data=None):
        instance = self.get_instance()
        for field_name, field in self.fields.items():
            value = field.get_attribute(data or self.data)
            adapted_value = field.adapt(value)
            if adapted_value is undefined:
                continue
            if isinstance(instance, collections.Mapping):
                instance[field_name] = adapted_value
            else:
                setattr(instance, field_name, adapted_value)
        return instance

    def get_instance(self):
        if self.instance:
            return self.instance
        else:
            meta = getattr(self, 'Meta', None)
            model_cls = getattr(meta, 'model', dict)
            return model_cls()
