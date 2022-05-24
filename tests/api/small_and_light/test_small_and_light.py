from __future__ import absolute_import
from sp_api.api import FbaSmallAndLight
from sp_api.base import Marketplaces


def test_get_small_and_light_eligibility_by_seller_sku():
    res = FbaSmallAndLight().get_small_and_light_eligibility_by_seller_sku(u'TEST_CASE_200')
    assert res.payload is not None


def test_get_small_and_light_fee_preview():
    res = FbaSmallAndLight().get_small_and_light_fee_preview(**{
        u'marketplaceId': Marketplaces.US.marketplace_id,
        u"items": [
            {
                u"asin": u"B076ZL9PB5",
                u"price": {
                    u"currencyCode": u"USD",
                    u"amount": 6.5
                }
            }
        ]})
    assert res(u'data') is not None
    assert res.payload is not None


def test_delete_small_and_light_enrollment_by_seller_sku():
    res = FbaSmallAndLight().delete_small_and_light_enrollment_by_seller_sku(u'SKU_ENROLLED_FOR_SMALL_AND_LIGHT', marketplaceIds=u'ATVPDKIKX0DER')
    assert res(u'status_code') == 204


def test_get_small_and_light_enrollment_by_seller_sku():
    res = FbaSmallAndLight().get_small_and_light_enrollment_by_seller_sku(u'SKU_ENROLLED_IN_SMALL_AND_LIGHT')
    assert res(u'status') == u'ENROLLED'


def test_put_small_and_light_enrollment_by_seller_sku():
    res = FbaSmallAndLight().put_small_and_light_enrollment_by_seller_sku(u'SKU_ELIGIBLE_FOR_SMALL_AND_LIGHT')
    assert res() is not None
