# -*- coding: utf-8 -*-

import collections


__all__ = ['BindingDict', 'EMPTY_VALUES', 'undefined']


EMPTY_VALUES = [None, '', [], (), {}]


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
