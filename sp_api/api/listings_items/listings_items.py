from __future__ import absolute_import
import urllib2, urllib, urlparse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class ListingsItems(Client):
    u"""
    ListingsItems SP-API Client
    :link: 

    The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API.

For more information, see the [Listings Items API Use Case Guide](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/use-case-guides/listings-items-api-use-case-guide/listings-items-api-use-case-guide_2021-08-01.md).
    """

    @sp_endpoint(u'/listings/2021-08-01/items/{}/{}', method=u'DELETE')
    def delete_listings_item(self, sellerId, sku, **kwargs):
        u"""
        delete_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        Delete a listings item for a selling partner.
        **Usage Plans:**
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        Args:
            sellerId:string | * REQUIRED A selling partner identifier, such as a merchant account or vendor code.
            sku:string | * REQUIRED A selling partner provided identifier for an Amazon listing.
            key marketplaceIds:array | * REQUIRED A comma-delimited list of Amazon marketplace identifiers for the request.
            key issueLocale:string |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop(u'path'), sellerId, sku), data=kwargs)

    @sp_endpoint(u'/listings/2021-08-01/items/{}/{}', method=u'GET')
    def get_listings_item(self, sellerId, sku, **kwargs):
        u"""
        get_listings_item(self, sellerId, **kwargs) -> ApiResponse
        Returns details about a listings item for a selling partner.
        **Usage Plan:**
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        The `x-amzn-RateLimit-Limit` response header returns the usage plan rate limits that were applied to the requested operation, when available. The table above indicates the default rate and burst values for this operation. Selling partners whose business demands require higher throughput may see higher rate and burst values then those shown here. For more information, see [Usage Plans and Rate Limits in the Selling Partner API](https://github.com/amzn/selling-partner-api-docs/blob/main/guides/en-US/usage-plans-rate-limits/Usage-Plans-and-Rate-Limits.md).
        Args:
            sellerId:string | * REQUIRED A selling partner identifier, such as a merchant account or vendor code
            sku:string | * REQUIRED A selling partner provided identifier for an Amazon listing.
            key marketplaceIds:array | * REQUIRED A comma-delimited list of Amazon marketplace identifiers for the request.
            key issueLocale:string |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
            key includedData:array |  A comma-delimited list of data sets to include in the response. Default: summaries.
        Returns:
            ApiResponse:
        """

        return self._request(fill_query_params(kwargs.pop(u'path'), sellerId, sku), params=kwargs)

    @sp_endpoint(u'/listings/2021-08-01/items/{}/{}', method=u'PATCH')
    def patch_listings_item(self, sellerId, sku, **kwargs):
        u"""
        patch_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.
        **Usage Plans:**
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        Args:
            sellerId:string | * REQUIRED A selling partner identifier, such as a merchant account or vendor code.
            sku:string | * REQUIRED A selling partner provided identifier for an Amazon listing.
            key marketplaceIds:array | * REQUIRED A comma-delimited list of Amazon marketplace identifiers for the request.
            key issueLocale:string |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
            body: {
              "productType": "string",
              "patches": [
                {
                  "op": "add",
                  "path": "string",
                  "value": [
                    {}
                  ]
                }
              ]
            }

         Returns:
            ApiResponse:
        """
        return self._request(fill_query_params(kwargs.pop(u'path'), sellerId, sku), data=kwargs.pop(u'body'), params=kwargs)

    @sp_endpoint(u'/listings/2021-08-01/items/{}/{}', method=u'PUT')
    def put_listings_item(self, sellerId, sku, **kwargs):
        u"""
        put_listings_item(self, sellerId, sku, **kwargs) -> ApiResponse
        Creates a new or fully-updates an existing listings item for a selling partner.
        **Usage Plans:**
        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        5                                       10
        ======================================  ==============
        The x-amzn-RateLimit-Limit response header returns the usage plan rate limits that were applied to the requested operation. Rate limits for some selling partners will vary from the default rate and burst shown in the table above. For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        Args:
            sellerId:string | * REQUIRED A selling partner identifier, such as a merchant account or vendor code.
            sku:string | * REQUIRED A selling partner provided identifier for an Amazon listing.
            key marketplaceIds:array | * REQUIRED A comma-delimited list of Amazon marketplace identifiers for the request.
            key issueLocale:string |  A locale for localization of issues. When not provided, the default language code of the first marketplace is used. Examples: "en_US", "fr_CA", "fr_FR". Localized messages default to "en_US" when a localization is not available in the specified locale.
            body: {
              "productType": "string",
              "requirements": "LISTING",
              "attributes": {}
            }

        Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop(u'path'), sellerId, sku), data=kwargs.pop(u'body'), params=kwargs)
    
