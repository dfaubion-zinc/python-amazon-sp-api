from __future__ import absolute_import
from enum import Enum


class Granularity(unicode, Enum):
    HOUR = u'Hour'
    DAY = u'Day'
    WEEK = u'Week'
    MONTH = u'Month'
    YEAR = u'Year'
    TOTAL = u'Total'


class BuyerType(unicode, Enum):
    B2B = u'B2B' # Business to business.
    B2C = u'B2C' # Business to customer.
    ALL = u'All' # Both of above


class FirstDayOfWeek(unicode, Enum):
    MO = u'Monday'
    SU = u'Sunday'


