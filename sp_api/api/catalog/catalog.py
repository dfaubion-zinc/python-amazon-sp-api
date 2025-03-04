from __future__ import absolute_import
import urllib2, urllib, urlparse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class Catalog(Client):
    u"""
    :link: https://github.com/amzn/selling-partner-api-docs/blob/main/references/catalog-items-api/catalogItemsV0.md

    """

    @sp_endpoint(u'/catalog/v0/items/{}')
    def get_item(self, asin, **kwargs):
        u"""
        get_item(self, asin: str, **kwargs) -> ApiResponse
        Returns a specified item and its attributes.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = Catalog().get_item('ASIN_200', MarketplaceId='TEST_CASE_200')

        Args:
            asin: str
            key MarketplaceId: str
            **kwargs:

        Returns:
            GetCatalogItemResponse:
        """
        return self._request(fill_query_params(kwargs.pop(u'path'), asin), params=kwargs)

    @sp_endpoint(u'/catalog/v0/items')
    def list_items(self, **kwargs):
        u"""
        list_items(self, **kwargs) -> ApiResponse
        Returns a list of items and their attributes, based on a search query or item identifiers that you specify. When based on a search query, provide the Query parameter and optionally, the QueryContextId parameter. When based on item identifiers, provide a single appropriate parameter based on the identifier type, and specify the associated item value. MarketplaceId is always required.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       1
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                res = Catalog().list_items(MarketplaceId='TEST_CASE_200', SellerSKU='SKU_200')

        Args:
            key MarketplaceId: str
            key Query: str
            key QueryContextId: str
            key SellerSKU: str
            key UPC: str
            key EAN: str
            key ISBN: str
            key JAN: str

        Returns:
            ListCatalogItemsResponse:
        """
        if u'Query' in kwargs:
            kwargs.update({u'Query': urllib.quote_plus(kwargs.pop(u'Query'))})
        return self._request(kwargs.pop(u'path'), params=kwargs)

    @sp_endpoint(u'/catalog/v0/categories')
    def list_categories(self, **kwargs):
        u"""
        list_categories(self, **kwargs) -> ApiResponse
        Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        1                                       40
        ======================================  ==============


        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Args:
            key MarketplaceId: str
            key ASIN: str
            key SellerSKU: str

        Returns:
            ListCatalogCategoriesResponse:
        """
        if u'Query' in kwargs:
            kwargs.update({u'Query': urllib.quote_plus(kwargs.pop(u'Query'))})
        return self._request(kwargs.pop(u'path'), params=kwargs)
