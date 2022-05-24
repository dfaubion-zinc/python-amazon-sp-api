from __future__ import absolute_import
from enum import Enum


class Schedules(unicode, Enum):
    MINUTES_5 = u"PT5M"
    MINUTES_15 = u"PT15M"
    MINUTES_30 = u"PT30M"
    HOUR_1 = u"PT1H"
    HOURS_2 = u"PT2H"
    HOURS_4 = u"PT4H"
    HOURS_8 = u"PT8H"
    HOURS_12 = u"PT12H"
    DAY_1 = u"P1D"
    DAYS_2 = u"P2D"
    DAYS_3 = u"P3D"
    HOURS_84 = u"PT84H"
    DAYS_7 = u"P7D"
    DAYS_14 = u"P14D"
    DAYS_15 = u"P15D"
    DAYS_18 = u"P18D"
    DAYS_30 = u"P30D"
    MONTH_1 = u"P1M"
