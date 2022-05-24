from __future__ import absolute_import
from sp_api.api import ListingsRestrictions


def test_listing_restrictions():
    res = ListingsRestrictions().get_listings_restrictions(sellerId=u'A3F26DF64ZIPJZ', asin=u'B07HRD6JKK')
    assert res(u'restrictions') is not None
    assert isinstance(res(u'restrictions'), list)

