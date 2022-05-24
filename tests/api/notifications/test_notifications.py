from __future__ import absolute_import
from sp_api.api import Notifications, Reports, Finances
from sp_api.base import SellingApiException, NotificationType, ReportType, Marketplaces
from sp_api.util import throttle_retry, load_all_pages


def test_create_destination():
    res = Notifications().create_destination(name=u'test', arn=u'arn:aws:sqs:us-east-2:444455556666:queue1')
    assert res.payload.get(u"destinationId") == u"TEST_CASE_200_DESTINATION_ID"
    assert res.payload.get(u"resource").get(u'sqs').get(u'arn') == u"arn:aws:sqs:us-east-2:444455556666:queue1"


def test_create_subscription():
    res = Notifications().create_subscription(NotificationType.MFN_ORDER_STATUS_CHANGE, destination_id=u'dest_id')
    assert res.payload.get(u'destinationId') == u'TEST_CASE_200_DESTINATION_ID'
    assert res.payload.get(u'subscriptionId') == u'TEST_CASE_200_SUBSCRIPTION_ID'


def test_delete_subscription():
    res = Notifications().delete_notification_subscription(NotificationType.MFN_ORDER_STATUS_CHANGE, u'subscription_id')
    assert res.errors is None


def test_get_subscriptions():
    res = Notifications().get_subscription(NotificationType.REPORT_PROCESSING_FINISHED)
    assert res.payload.get(u'destinationId') == u'TEST_CASE_200_DESTINATION_ID'
    assert res.payload.get(u'subscriptionId') == u'TEST_CASE_200_SUBSCRIPTION_ID'
