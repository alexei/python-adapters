# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class Struct(object):
    def __init__(self, **data):
        self.__dict__.update(data)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
