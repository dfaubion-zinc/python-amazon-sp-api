from __future__ import absolute_import
from sp_api.base.helpers import sp_endpoint, fill_query_params
from sp_api.base import Client, Marketplaces, deprecated, NotificationType, ApiResponse


def merge_dicts(*dict_args):
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key-value pairs in latter dictionaries.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

class Notifications(Client):
    u"""
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/notifications-api/notifications.md
    """
    grantless_scope = u'sellingpartnerapi::notifications'

    @deprecated
    def add_subscription(self, notification_type, **kwargs):
        u"""deprecated, use create_subscription"""
        return self.create_subscription(notification_type, **kwargs)

    @sp_endpoint(u'/notifications/v1/subscriptions/{}', method=u'POST')
    def create_subscription(self, notification_type, destination_id = None,
                            **kwargs):
        u"""
        create_subscription(self, notification_type: NotificationType or str, destination_id: str = None, **kwargs) -> ApiResponse
        Creates a subscription for the specified notification type to be delivered to the specified destination.
        Before you can subscribe, you must first create the destination by calling the createDestination operation.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                Notifications().create_subscription(NotificationType.MFN_ORDER_STATUS_CHANGE, destination_id='dest_id')

        Args:
            notification_type: NotificationType or str
            destination_id: str
            **kwargs:


        Returns:
            ApiResponse:

        """
        data = {
            u'destinationId': kwargs.pop(u'destinationId', destination_id),
            u'payloadVersion': kwargs.pop(u'payload_version', u'1.0')
        }
        return self._request(fill_query_params(kwargs.pop(u'path'),
                                               notification_type if isinstance(notification_type,
                                                                               unicode) else notification_type.value),
                             data=dict(kwargs, **data))

    @sp_endpoint(u'/notifications/v1/subscriptions/{}')
    def get_subscription(self, notification_type, **kwargs):
        u"""
        get_subscription(self, notification_type: NotificationType or str, **kwargs) -> ApiResponse
        Returns information about subscriptions of the specified notification type. You can use this API to get subscription information when you do not have a subscription identifier.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                Notifications().get_subscription(NotificationType.REPORT_PROCESSING_FINISHED)

        Args:
            notification_type: NotificationType or str
            **kwargs:

        Returns:
            ApiResponse:

        """
        return self._request(fill_query_params(kwargs.pop(u'path'), notification_type if isinstance(notification_type,
                                                                                                   unicode) else notification_type.value),
                             params=dict(kwargs))

    @sp_endpoint(u'/notifications/v1/subscriptions/{}/{}', method=u'DELETE')
    def delete_notification_subscription(self, notification_type, subscription_id,
                                         **kwargs):
        u"""
        delete_notification_subscription(self, notification_type: NotificationType or str, subscription_id: str, **kwargs) -> ApiResponse
        Deletes the subscription indicated by the subscription identifier and notification type that you specify.
        The subscription identifier can be for any subscription associated with your application. After you successfully call this operation, notifications will stop being sent for the associated subscription. The deleteSubscriptionById API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            Notifications().delete_notification_subscription(NotificationType.MFN_ORDER_STATUS_CHANGE, 'subscription_id')

        Args:
            notification_type: NotificationType or str
            subscription_id: str
            **kwargs:

        Returns:
            ApiResponse:

        """
        return self._request(
            fill_query_params(kwargs.pop(u'path'),
                              notification_type if isinstance(notification_type, unicode) else notification_type.value,
                              subscription_id),
            params=dict(kwargs))

    @sp_endpoint(path=u'/notifications/v1/destinations', method=u'POST')
    def create_destination(self, name, arn, account_id = None, region = None, **kwargs):
        u"""
        create_destination(self, name: str, arn: str, **kwargs) -> ApiResponse
        Creates a destination resource to receive notifications. The createDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        Examples:
            literal blocks::

                Notifications().create_destination(name='test', arn='arn:aws:sqs:us-east-2:444455556666:queue1')

        Args:
            account_id:
            region:
            name: str
            arn: str
            **kwargs:

        Returns:
            ApiResponse:

        """
        resource_name = u'sqs' if not account_id else u'eventBridge'
        region = region if region else self.region

        data = {
            u'resourceSpecification': {
                resource_name: {
                    u'arn': arn
                } if not account_id else {
                    u'region': region,
                    u'accountId': account_id
                }
            },
            u'name': name,
        }

        return self._request_grantless_operation(kwargs.pop(u'path'), data=merge_dicts(kwargs, data))

    @sp_endpoint(u'/notifications/v1/destinations', method=u'GET')
    def get_destinations(self, **kwargs):
        u"""
        get_destinations(self, **kwargs) -> ApiResponse
        Returns information about all destinations. The getDestinations API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            **kwargs:

        Returns:
            ApiResponse:

        """
        return self._request_grantless_operation(kwargs.pop(u'path'), params=kwargs.copy())

    @sp_endpoint(u'/notifications/v1/destinations/{}', method=u'GET')
    def get_destination(self, destination_id, **kwargs):
        u"""
        get_destination(self, destination_id: str, **kwargs) -> ApiResponse
        Returns information about all destinations. The getDestinations API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.


        Args:
            destination_id: str
            **kwargs:

        Returns:
            ApiResponse:


        """
        return self._request_grantless_operation(fill_query_params(kwargs.pop(u'path'), destination_id),
                                                 params=kwargs.copy())

    @sp_endpoint(u'/notifications/v1/destinations/{}', method=u'DELETE')
    def delete_destination(self, destination_id, **kwargs):
        u"""
        delete_destination(self, destination_id: str, **kwargs) -> ApiResponse
        Deletes the destination that you specify. The deleteDestination API is grantless. For more information, see "Grantless operations" in the Selling Partner API Developer Guide.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       5
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            destination_id: str
            **kwargs:

        Returns:
            ApiResponse:

        """
        return self._request_grantless_operation(fill_query_params(kwargs.pop(u'path'), destination_id),
                                                 params=kwargs.copy())
