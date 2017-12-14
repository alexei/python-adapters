# -*- coding: utf-8 -*-

import collections

from .utils import undefined


__all__ = ['get_attribute']


def get_attribute(obj, attrs):
    for attr in attrs:
        if obj is None:
            return undefined

        try:
            if isinstance(obj, collections.Mapping):
                obj = obj[attr]
            elif isinstance(obj, collections.Iterable):
                obj = obj[int(attr)]
            else:
                obj = getattr(obj, attr)
        except Exception:
            return undefined

        if isinstance(obj, collections.Callable):
            obj = obj()

    return obj
