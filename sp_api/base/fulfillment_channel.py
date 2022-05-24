from __future__ import absolute_import
from enum import Enum


class FulfillmentChannel(unicode, Enum):
    AFN = u'AFN'
    MFN = u'MFN'
