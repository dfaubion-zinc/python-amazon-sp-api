from __future__ import absolute_import
from sp_api.api import Orders


def test_get_orders():
    res = Orders().get_orders(CreatedAfter=u'TEST_CASE_200', MarketplaceIds=[u"ATVPDKIKX0DER"])
    assert res.errors is None
    assert res.payload.get(u'Orders') is not None


def test_get_order_items():
    res = Orders().get_order_items(u'TEST_CASE_200')
    assert res.errors is None
    assert res.payload.get(u'AmazonOrderId') is not None


def test_get_order_address():
    res = Orders().get_order_address(u'TEST_CASE_200')
    assert res.errors is None
    assert res.payload.get(u'AmazonOrderId') is not None


def test_get_order_buyer_info():
    res = Orders().get_order_buyer_info(u'TEST_CASE_200')
    assert res.errors is None
    assert res.payload.get(u'AmazonOrderId') is not None


def test_get_order():
    res = Orders().get_order(u'TEST_CASE_200')
    assert res.errors is None
    assert res.payload.get(u'AmazonOrderId') is not None


def test_get_order_items_buyer_info():
    res = Orders().get_order_items_buyer_info(u'TEST_CASE_200')
    assert res.errors is None
    assert res.payload.get(u'AmazonOrderId') is not None


def test_get_orders_400_error():
    from sp_api.base import SellingApiBadRequestException
    try:
        Orders().get_orders(CreatedAfter=u'TEST_CASE_400')
    except SellingApiBadRequestException, sep:
        assert sep.code == 400
        assert sep.amzn_code == u'InvalidInput'


def test_get_order_api_response_call():
    res = Orders().get_order(u'TEST_CASE_200')
    print res(u'DefaultShipFromLocationAddress')
    assert res(u'DefaultShipFromLocationAddress') is not None
    assert res.errors is None
    assert res.payload.get(u'AmazonOrderId') is not None


def test_get_orders_attr():
    res = Orders().get_orders(CreatedAfter=u'TEST_CASE_200', MarketplaceIds=[u"ATVPDKIKX0DER"])
    assert res.Orders is not None
    assert res.errors is None
    assert res.payload.get(u'Orders') is not None


def test_get_order_api_response_call2():
    res = Orders().get_order(u'TEST_CASE_200')
    assert res() is not None
    assert isinstance(res(), dict)
    assert res.errors is None
    assert res.payload.get(u'AmazonOrderId') is not None

