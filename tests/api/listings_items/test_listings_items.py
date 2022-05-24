from __future__ import absolute_import
from sp_api.api import ListingsItems
from sp_api.base import Marketplaces


def test_get_listings_item():
    res = ListingsItems().get_listings_item(u'xxx', u'xxx')
    assert res is not None


def test_put_listings_item():
    res = ListingsItems().put_listings_item(u'xxx', u'xxx', body={
              u"productType": u"string",
              u"requirements": u"LISTING",
              u"attributes": {},

            }, marketplaceIds=[Marketplaces.US.marketplace_id])
    assert res(u'status') == u'ACCEPTED'


def test_patch_listings_item():
    res = ListingsItems().patch_listings_item(u'xxx', u'xxx', body={
              u"productType": u"string",
              u"patches": [
                {
                  u"op": u"add",
                  u"path": u"string",
                  u"value": [
                    {}
                  ]
                }
              ]
            })
    assert res(u'status') == u'ACCEPTED'


def test_delete_listings_item():
    res = ListingsItems().delete_listings_item(u'xxx', u'xxx')
    assert res(u'status') == u'ACCEPTED'
