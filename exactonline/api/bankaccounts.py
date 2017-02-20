# vim: set ts=8 sw=4 sts=4 et ai tw=79:
"""
Helper for relation/contact resources.

This file is part of the Exact Online REST API Library in Python
(EORALP), licensed under the LGPLv3+.
Copyright (C) 2017 Walter Doekes, OSSO B.V.
"""
from .manager import Manager


class BankAccounts(Manager):
    resource = 'crm/BankAccounts'

    def filter(self, guid=None, **kwargs):
        if 'select' not in kwargs:
            kwargs['select'] = 'ID,BankAccountHolderName,BankAccount,Main'

        if guid is not None:
            self._filter_append(kwargs, u'ID eq %s' % self._remote_guid(guid))
        return super(BankAccounts, self).filter(**kwargs)
