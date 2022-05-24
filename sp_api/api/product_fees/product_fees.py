from __future__ import absolute_import
from urllib import quote_plus

from sp_api.base.helpers import sp_endpoint, fill_query_params
from sp_api.base import Client, ApiResponse


class ProductFees(Client):
    u"""
    :link: https://github.com/amzn/selling-partner-api-docs/tree/main/references/product-fees-api
    """

    @sp_endpoint(u'/products/fees/v0/listings/{}/feesEstimate', method=u'POST')
    def get_product_fees_estimate_for_sku(self, seller_sku, price, shipping_price=None, currency=u'USD',
                                          is_fba=False, points = None, marketplace_id = None,
                                          optional_fulfillment_program = None, force_safe_sku = True,
                                          **kwargs):
        u"""
        get_product_fees_estimate_for_sku(self, seller_sku, price: float, shipping_price=None, currency='USD', is_fba=False, points: dict = dict, **kwargs) -> ApiResponse

        Returns fees for sku

        Examples:
            literal blocks::

                ProductFees().get_product_fees_estimate_for_sku("UmaS1", 10, currency='USD', shipping_price=10, is_fba=False,
                                                          points={
                                                              "PointsNumber": 0,
                                                              "PointsMonetaryValue": {
                                                                  "CurrencyCode": "USD",
                                                                  "Amount": 0
                                                              }
                                                          })

        Args:
            seller_sku:
            price:
            shipping_price:
            currency:
            is_fba:
            points:
            marketplace_id: str | Defaults to self.marketplace_id
            optional_fulfillment_program:
            force_safe_sku: bool | Force user SKU quote
            **kwargs:

        Returns:
            ApiResponse:

        """

        if force_safe_sku:
            #handle `forward slash` issue in SKU
            seller_sku = quote_plus(seller_sku)

        kwargs.update(self._create_body(price, shipping_price, currency, is_fba, seller_sku, points, marketplace_id, optional_fulfillment_program))
        return self._request(fill_query_params(kwargs.pop(u'path'), seller_sku), data=kwargs)

    @sp_endpoint(u'/products/fees/v0/items/{}/feesEstimate', method=u'POST')
    def get_product_fees_estimate_for_asin(self, asin, price, currency=u'USD', shipping_price=None, is_fba=False,
                                           points = None, marketplace_id = None,
                                           optional_fulfillment_program = None,
                                           **kwargs):
        u"""
        get_product_fees_estimate_for_asin(self, asin, price: float, currency='USD', shipping_price=None, is_fba=False,  points: dict = dict, **kwargs) -> ApiResponse

        Returns fees for asin

        Examples:
            literal blocks::

                ProductFees().get_product_fees_estimate_for_asin("UmaS1", 10, currency='USD', shipping_price=10, is_fba=False,
                                                           points={
                                                               "PointsNumber": 0,
                                                               "PointsMonetaryValue": {
                                                                   "CurrencyCode": "USD",
                                                                   "Amount": 0
                                                               }
                                                           })

        Args:
            asin:
            price:
            currency:
            shipping_price:
            is_fba:
            points:
            marketplace_id: str | Defaults to self.marketplace_id
            optional_fulfillment_program:
            **kwargs:

        Returns:
            ApiResponse:

        """
        kwargs.update(self._create_body(price, shipping_price, currency, is_fba, asin, points, marketplace_id, optional_fulfillment_program))
        return self._request(fill_query_params(kwargs.pop(u'path'), asin), data=kwargs)

    def _create_body(self, price, shipping_price=None, currency=u'USD', is_fba=False, identifier=None,
                     points = None, marketplace_id = None, optional_fulfillment_program=None):
        u"""
        Create request body

        Args:
            price:
            shipping_price:
            currency:
            is_fba:
            identifier:
            points:

        Returns:

        """
        return {
            u'FeesEstimateRequest': {
                u'Identifier': identifier or unicode(price),
                u'PriceToEstimateFees': {
                    u'ListingPrice': {
                        u'Amount': price,
                        u'CurrencyCode': currency
                    },
                    u'Shipping': {
                        u'Amount': shipping_price,
                        u'CurrencyCode': currency
                    } if shipping_price else None,
                    u'Points': points or None
                },
                u'IsAmazonFulfilled': is_fba,
                u'OptionalFulfillmentProgram': optional_fulfillment_program if is_fba is True and optional_fulfillment_program else None,
                u'MarketplaceId': marketplace_id or self.marketplace_id
            }
        }
