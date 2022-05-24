from __future__ import absolute_import
import urllib2, urllib, urlparse

from sp_api.api import ProductFees
from sp_api.base import Marketplaces


def test_get_fees_for_sku():
    res = ProductFees().get_product_fees_estimate_for_sku(u"UmaS1", 10, currency=u'USD', shipping_price=10, is_fba=False,
                                                          points={
                                                              u"PointsNumber": 0,
                                                              u"PointsMonetaryValue": {
                                                                  u"CurrencyCode": u"USD",
                                                                  u"Amount": 0
                                                              }
                                                          })
    assert res.payload.get(u'FeesEstimateResult').get(u'Status') == u'Success'


def test_get_fees_for_asin():
    res = ProductFees().get_product_fees_estimate_for_asin(u"UmaS1", 10, currency=u'USD', shipping_price=10, is_fba=False,
                                                           points={
                                                               u"PointsNumber": 0,
                                                               u"PointsMonetaryValue": {
                                                                   u"CurrencyCode": u"USD",
                                                                   u"Amount": 0
                                                               }
                                                           })
    assert res.payload.get(u'FeesEstimateResult').get(u'Status') == u'Success'
