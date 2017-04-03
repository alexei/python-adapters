# -*- coding: utf-8 -*-

from __future__ import unicode_literals


__all__ = ['Adapter', 'CharField']


class undefined:
    pass


class BaseField(object):
    def __init__(self, source=None, default=undefined):
        pass

    def adapt(self):
        pass


class CharField(BaseField):
    pass


class Adapter(BaseField):
    def __init__(self, data=None, *args, **kwargs):
        super(Adapter, self).__init__(*args, **kwargs)
