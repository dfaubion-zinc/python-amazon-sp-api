from __future__ import absolute_import
from sp_api.api import Inventories
from sp_api.base import SellingApiServerException, SellingApiForbiddenException, Marketplaces


def test_get_inventory_summary_marketplace():
    res = Inventories().get_inventory_summary_marketplace(**{
        u"details": True,
        u"marketplaceIds": [u"ATVPDKIKX0DER"]
    })
    assert res.errors is None
    assert res.pagination.get(u'nextToken') == u'seed'
    assert res.payload.get(u'granularity').get(u'granularityType') == u'Marketplace'


def test_get_inventory_summary_marketplace_expect_500():
    try:
        Inventories().get_inventory_summary_marketplace(**{
            u"marketplaceIds": [u"1"],
        })
    except SellingApiForbiddenException, se:
        assert se.code == 403

