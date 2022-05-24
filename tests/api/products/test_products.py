from __future__ import absolute_import
from sp_api.api.products.products import Products
from sp_api.base import Marketplaces, SellingApiBadRequestException


def test_pricing_for_sku():
    res = Products().get_product_pricing_for_skus([], MarketplaceId=u"ATVPDKIKX0DER")
    assert res.payload[0].get(u'status') == u'Success'


def test_pricing_for_asin():
    res = Products().get_product_pricing_for_asins([], MarketplaceId=u"ATVPDKIKX0DER")
    assert res.payload[0].get(u'status') == u'Success'


def test_pricing_for_asin_expect_400():
    try:
        Products().get_product_pricing_for_asins([u'TEST_CASE_400'], MarketplaceId=u'TEST_CASE_400')
    except SellingApiBadRequestException:
        pass


def test_competitive_pricing_for_sku():
    res = Products().get_competitive_pricing_for_skus([], MarketplaceId=u"ATVPDKIKX0DER")
    assert res.payload[0].get(u'status') == u'Success'


def test_competitive_pricing_for_asin():
    res = Products().get_competitive_pricing_for_asins([], MarketplaceId=u"ATVPDKIKX0DER")
    assert res.payload[0].get(u'status') == u'Success'
