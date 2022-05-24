from __future__ import absolute_import
from sp_api.api import Catalog
from sp_api.base import Marketplaces, SellingApiBadRequestException, ApiResponse


def test_get_catalog_item():
    res = Catalog().get_item(u'ASIN_200', MarketplaceId=u'TEST_CASE_200')
    assert res.errors is None
    assert isinstance(res, ApiResponse)


def test_list_catalog_items():
    res = Catalog().list_items(MarketplaceId=u'TEST_CASE_200', SellerSKU=u'SKU_200')
    assert res.errors is None


def test_list_catalog_expect_400():
    try:
        Catalog().list_items(MarketplaceId=u'TEST_CASE_400', SellerSKU=u'SKU_400')
    except SellingApiBadRequestException, br:
        assert type(br) == SellingApiBadRequestException

