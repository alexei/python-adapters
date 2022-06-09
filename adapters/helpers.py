# -*- coding: utf-8 -*-

import six

from .utils import undefined


__all__ = ['get_attribute']


def get_attribute(obj, attrs):
    for attr in attrs:
        if obj is None:
            return undefined

        try:
            if isinstance(obj, six.moves.collections_abc.Mapping):
                obj = obj[attr]
            elif isinstance(obj, six.moves.collections_abc.Iterable):
                obj = obj[int(attr)]
            else:
                obj = getattr(obj, attr)
        except Exception:
            return undefined

        if isinstance(obj, six.moves.collections_abc.Callable):
            obj = obj()

    return obj
