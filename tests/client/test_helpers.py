from __future__ import absolute_import
import enum
import os
from datetime import datetime, timedelta
from io import BytesIO

from sp_api.api import FulfillmentInbound, Orders
from sp_api.base import fill_query_params, sp_endpoint, create_md5, nest_dict, deprecated
from sp_api.util import KeyMaker, load_all_pages, throttle_retry, load_date_bound
from sp_api.util.load_all_pages import make_sleep_time

key_mapping = {
    u'sku': [u'seller_sku', u'sellerSku'],
    u'title': [u'product_name']
}
test_obj = {
    u'goo': {u'x': {}},
    u'seller_sku': 1,
    u'product_name': {
        u'sellerSku': [
            u'seller_sku',
            3,
            {
                u'sellerSku': 22,
                u'product_name': {
                    u'title': u'Foo',
                    u'x': u'bar'
                }
            }
        ]
    }
}


def test_key_maker_from_dict():
    r = KeyMaker(key_mapping, deep=True).convert_keys(test_obj)
    assert isinstance(r, dict)
    assert r.get(u'sku') == 1
    assert r.get(u'seller_sku') is None
    assert isinstance(r.get(u'title'), dict)
    assert isinstance(r.get(u'title').get(u'sku'), list)


def test_key_maker_from_list():
    r = KeyMaker(key_mapping, deep=True).convert_keys([test_obj])
    assert isinstance(r, list)
    assert len(r) == 1

    assert r[0].get(u'sku') == 1
    assert r[0].get(u'seller_sku') is None
    assert isinstance(r[0].get(u'title'), dict)
    assert isinstance(r[0].get(u'title').get(u'sku'), list)


def test_key_maker_from_dict_not_deep():
    r = KeyMaker(key_mapping, deep=False).convert_keys(test_obj)
    assert r.get(u'sku') == 1
    assert r.get(u'seller_sku') is None
    assert isinstance(r.get(u'title'), dict)
    assert isinstance(r.get(u'title').get(u'sellerSku'), list)


def test_load_all_pages():
    @throttle_retry()
    @load_all_pages(extras=dict(QueryType=u'NEXT_TOKEN'))
    def load_shipments(**kwargs):
        return FulfillmentInbound().get_shipments(**kwargs)

    for x in load_shipments(QueryType=u'SHIPMENT'):
        assert x.payload is not None


def test_load_all_pages_orders():
    @throttle_retry()
    @load_all_pages()
    def load_all_orders(**kwargs):
        return Orders().get_orders(**kwargs)

    for x in load_all_orders(CreatedAfter=u'TEST_CASE_200', MarketplaceIds=[u"ATVPDKIKX0DER"]):
        assert x.payload is not None


def test_make_sleep_time():
    x = make_sleep_time(2, False, 2)
    assert x == 2

    y = make_sleep_time(2, True, 2)
    assert y == 0.5


def test_load_all_pages1():
    x = load_all_pages()
    assert x is not None


def test_fill_query_params():
    assert fill_query_params(u'{}/{}', u'foo', u'bar') == u'foo/bar'


def test_sp_endpoint_():
    assert sp_endpoint(u'foo') is not None


def test_create_md5():
    b = BytesIO()
    b.write('foo')
    b.seek(0)
    m = create_md5(b)
    assert m == u'rL0Y20zC+Fzt72VPzMSk2A=='


def test_nest_dict():
    x = nest_dict({
        u"AmazonOrderId":1,
        u"ShipFromAddress.Name" : u"Seller",
        u"ShipFromAddress.AddressLine1": u"Street",
    })
    assert x[u'ShipFromAddress'][u'AddressLine1'] == u'Street'


def test_deprecated():
    assert deprecated(lambda x: x + 1)(1) == 2


@load_date_bound()
def dummy(**kwargs):
    return lambda: kwargs


def test_load_date_bound():
    start = datetime.now() - timedelta(days=70)
    end = datetime.now()
    x = list(dummy(dataStartTime=start, dataEndTime=end))
    assert len(x) == 3
    assert x[1]()[u'dataStartTime'] == start + timedelta(days=30)
    assert x[1]()[u'dataEndTime'] == start + timedelta(days=60)
