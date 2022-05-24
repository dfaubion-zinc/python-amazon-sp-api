from __future__ import absolute_import
from datetime import datetime, timedelta, timezone

import pytz

from sp_api.api import Sales
from sp_api.base import Granularity

tz = pytz.timezone(u'US/Central')
fmt = u'%Y-%m-%dT%H:%M:%S%z'

interval = (datetime.now(tz) - timedelta(days=185)), (datetime.now(tz))


def test_sales_granularity_total():
    res = Sales().get_order_metrics(interval, Granularity.TOTAL, granularityTimeZone=u'US/Central')
    assert res.payload[0].get(u'unitCount') == 2


def test_sales_granularity_day():
    res = Sales().get_order_metrics(interval, Granularity.DAY, granularityTimeZone=u'US/Central')
    assert res.payload[0].get(u'unitCount') == 1


def test_sales_granularity_total_by_asin():
    res = Sales().get_order_metrics(interval, Granularity.TOTAL, granularityTimeZone=u'US/Central', asin=u'B008OLKVEW')
    assert res.payload[0].get(u'unitCount') == 1


def test_sales_granularity_day_by_asin():
    res = Sales().get_order_metrics(interval, Granularity.DAY, granularityTimeZone=u'US/Central', asin=u'B008OLKVEW')
    assert res.payload[0].get(u'unitCount') == 1

