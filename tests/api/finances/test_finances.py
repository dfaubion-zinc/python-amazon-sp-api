from __future__ import absolute_import
import json
from datetime import datetime, timedelta

from sp_api.api import Finances
from sp_api.base import SellingApiBadRequestException


def test_for_order():
    res = Finances().get_financial_events_for_order(u'485-734-5434857', MaxResultsPerPage=10)
    assert res.payload.get(u'NextToken') == u'Next token value'


def test_for_order_expect_400():
    try:
        Finances().get_financial_events_for_order(u'BAD-ORDER', MaxResultsPerPage=10)
    except SellingApiBadRequestException, br:
        assert br.code == 400
        assert type(br) == SellingApiBadRequestException

