# vim: set ts=8 sw=4 sts=4 et ai tw=79:
"""
Helper for relation/contact resources.

This file is part of the Exact Online REST API Library in Python
(EORALP), licensed under the LGPLv3+.
Copyright (C) 2017 Walter Doekes, OSSO B.V.
"""
from .manager import Manager


class Costcenters(Manager):
    resource = 'hrm/Costcenters'

    def filter(self, code, **kwargs):
        if 'select' not in kwargs:
            kwargs['select'] = 'ID,Code,Description,Active,Division'

        if code is not None:
            self._filter_append(kwargs, u'Code eq %s' % code)
        return super(Costcenters, self).filter(**kwargs)
