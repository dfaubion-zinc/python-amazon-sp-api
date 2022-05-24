from __future__ import absolute_import
from sp_api.api import FeedsV2 as Feeds
from sp_api.base import SellingApiBadRequestException, SellingApiServerException, SellingApiForbiddenException
from sp_api.base.feedTypes import FeedType


def test_create_feed():
    res = Feeds().create_feed(
        FeedType.POST_PRODUCT_DATA,
        u'3d4e42b5-1d6e-44e8-a89c-2abfca0625bb',
         marketplaceIds=[u"ATVPDKIKX0DER", u"A1F83G8C2ARO7P"]
    )
    assert res.payload.get(u'feedId') == u'3485934'


def test_get_feed():
    feed_id = u'feedId1'
    res = Feeds().get_feed(feed_id)
    assert res.payload.get(u'feedId') == u'FeedId1'
    assert res.payload.get(u'processingStatus') == u'CANCELLED'


def test_get_feed_expect_400():
    try:
        Feeds().get_feed(u'badFeedId1')
    except SellingApiBadRequestException, br:
        assert type(br) == SellingApiBadRequestException
        assert br.code == 400


def test_get_feed_expect_500():
    try:
        Feeds().get_feed(u'giberish')
    except SellingApiServerException, br:
        assert type(br) == SellingApiServerException
        assert br.code == 500


def test_request():
    try:
        Feeds()._request(u'', data={})
    except SellingApiForbiddenException:
        assert True
