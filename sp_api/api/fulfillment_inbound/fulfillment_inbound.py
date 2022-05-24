from __future__ import absolute_import
from sp_api.base import Client, Marketplaces, ApiResponse
from sp_api.base import sp_endpoint, fill_query_params


def merge_dicts(*dict_args):
    """
    Given any number of dictionaries, shallow copy and merge into a new dict,
    precedence goes to key-value pairs in latter dictionaries.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


class FulfillmentInbound(Client):
    @sp_endpoint(u"/fba/inbound/v0/itemsGuidance")
    def item_guidance(self, **kwargs):
        u"""
        item_guidance(self, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().item_guidance(**{"MarkeplaceId": "US", "ASINList": ["ASIN1"]})

        Args:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop(u"path"), params=kwargs)

    @sp_endpoint(u"/fba/inbound/v0/plans", method=u"POST")
    def plans(self, data, **kwargs):
        u"""
        plans(self, data, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                res = FulfillmentInbound().plans({
                        "ShipFromAddress": {
                            "Name": "Name",
                            "AddressLine1": "123 any st",
                            "AddressLine2": "AddressLine2",
                            "DistrictOrCounty": "Washtenaw",
                            "City": "Ann Arbor",
                            "StateOrProvinceCode": "MI",
                            "CountryCode": "US",
                            "PostalCode": "48188"
                        },
                        "LabelPrepPreference": "SELLER_LABEL",
                        "ShipToCountryCode": "ShipToCountryCode",
                        "ShipToCountrySubdivisionCode": "ShipToCountrySubdivisionCode",
                        "InboundShipmentPlanRequestItems": [
                            {
                                "SellerSKU": "SellerSKU",
                                "ASIN": "ASIN",
                                "Condition": "NewItem",
                                "Quantity": 1,
                                "QuantityInCase": 1,
                                "PrepDetailsList": [
                                    {
                                        "PrepInstruction": "Polybagging",
                                        "PrepOwner": "AMAZON"
                                    }
                                ]
                            }
                        ]
                    })

        Args:
            data:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop(u"path"), data=merge_dicts(data, kwargs))

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}", method=u"POST")
    def create_shipment(self, shipment_id, data, **kwargs):
        u"""
        create_shipment(self, shipment_id, data, **kwargs)

        Examples:
            literal blocks::

                FulfillmentInbound().create_shipment('123', {
                        "InboundShipmentHeader": {
                            "ShipmentName": "43545345",
                            "ShipFromAddress": {
                                "Name": "35435345",
                                "AddressLine1": "123 any st",
                                "DistrictOrCounty": "Washtenaw",
                                "City": "Ann Arbor",
                                "StateOrProvinceCode": "Test",
                                "CountryCode": "US",
                                "PostalCode": "48103"
                            },
                            "DestinationFulfillmentCenterId": "AEB2",
                            "AreCasesRequired": True,
                            "ShipmentStatus": "WORKING",
                            "LabelPrepPreference": "SELLER_LABEL",
                            "IntendedBoxContentsSource": "NONE"
                        },
                        "InboundShipmentItems": [
                            {
                                "ShipmentId": "345453",
                                "SellerSKU": "34534545",
                                "FulfillmentNetworkSKU": "435435435",
                                "QuantityShipped": 0,
                                "QuantityReceived": 0,
                                "QuantityInCase": 0,
                                "ReleaseDate": "2020-04-23",
                                "PrepDetailsList": [
                                    {
                                        "PrepInstruction": "Polybagging",
                                        "PrepOwner": "AMAZON"
                                    }
                                ]
                            }
                        ],
                        "MarketplaceId": "MarketplaceId"
                    })

        Args:
            shipment_id:
            data:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id), data=merge_dicts(data, kwargs)
        )

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}", method=u"PUT")
    def update_shipment(self, shipment_id, data, **kwargs):
        u"""
        update_shipment(self, shipment_id, data, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().update_shipment('123', {
                        "MarketplaceId": "ATVPDKIKX0DER",
                        "InboundShipmentHeader": {
                            "ShipmentName": "Shipment for FBA15DJCQ1ZF",
                            "ShipFromAddress": {
                                "Name": "Uma Test",
                                "AddressLine1": "123 any st",
                                "AddressLine2": "",
                                "DistrictOrCounty": "Washtenaw",
                                "City": "Ann Arbor",
                                "StateOrProvinceCode": "CO",
                                "CountryCode": "US",
                                "PostalCode": "48104"
                            },
                            "DestinationFulfillmentCenterId": "ABE2",
                            "ShipmentStatus": "WORKING",
                            "LabelPrepPreference": "SELLER_LABEL"
                        },
                        "InboundShipmentItems": [
                            {
                                "SellerSKU": "PSMM-TEST-SKU-Apr-03_21_17_20-0379",
                                "QuantityShipped": 1
                            }
                        ]
                    })

        Args:
            shipment_id:
            data:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id), data=merge_dicts(data, kwargs)
        )

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}/preorder")
    def preorder(self, shipment_id, **kwargs):
        u"""
        preorder(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().preorder('shipmentId1', MarketplaceId='MarketplaceId1')

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id), params=kwargs
        )

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}/preorder/confirm", method=u"PUT")
    def confirm_preorder(self, shipment_id, **kwargs):
        u"""
        confirm_preorder(self, shipment_id, **kwargs)

        Args:
            shipment_id:
            **kwargs:

        Returns:

        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id), params=kwargs
        )

    @sp_endpoint(u"/fba/inbound/v0/prepInstructions")
    def prep_instruction(self, data, **kwargs):
        u"""
        prep_instruction(self, data, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().prep_instruction({"ShipToCountryCode": "US", "ASINList": ["ASIN1"]})

        Args:
            data:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop(u"path"), params=merge_dicts(data, kwargs))

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}/transport")
    def get_transport_information(self, shipment_id, **kwargs):
        u"""
        get_transport_information(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().get_transport_information('shipmentId1')

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id), params=kwargs
        )

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}/transport", method=u"PUT")
    def update_transport_information(self, shipment_id, **kwargs):
        u"""
        update_transport_information(self, shipment_id, **kwargs) -> ApiResponse

        putTransportDetails

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id), data=kwargs
        )

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}/transport/void", method=u"POST")
    def void_transport(self, shipment_id, **kwargs):
        u"""
        void_transport(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().void_transport('shipmentId1')

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}/transport/estimate", method=u"POST")
    def estimate_transport(self, shipment_id, **kwargs):
        u"""
        estimate_transport(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().estimate_transport('shipmentId1')

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}/transport/confirm", method=u"POST")
    def confirm_transport(self, shipment_id, **kwargs):
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id),
            data=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}/labels")
    def get_labels(self, shipment_id, **kwargs):
        u"""
        get_labels(self, shipment_id, **kwargs)

        Args:
            shipment_id:
            **kwargs:

        Returns:

        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id),
            params=kwargs,
            add_marketplace=False,
        )

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}/billOfLading")
    def bill_of_lading(self, shipment_id, **kwargs):
        u"""
        bill_of_lading(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().bill_of_lading('shipmentId')

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id), params=kwargs
        )

    @sp_endpoint(u"/fba/inbound/v0/shipments")
    def get_shipments(self, **kwargs):
        u"""
        get_shipments(self, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().get_shipments(QueryType='SHIPMENT', MarketplaceId="ATVPDKIKX0DER")

        Args:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop(u"path"), params=kwargs)

    @sp_endpoint(u"/fba/inbound/v0/shipments/{}/items")
    def shipment_items_by_shipment(self, shipment_id, **kwargs):
        u"""
        shipment_items_by_shipment(self, shipment_id, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().shipment_items_by_shipment('FBA15DJ9SVVD', MarketplaceId="ATVPDKIKX0DER")

        Args:
            shipment_id:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(
            fill_query_params(kwargs.pop(u"path"), shipment_id), params=kwargs
        )

    @sp_endpoint(u"/fba/inbound/v0/shipmentItems")
    def shipment_items(self, **kwargs):
        u"""
        shipment_items(self, **kwargs) -> ApiResponse

        Examples:
            literal blocks::

                FulfillmentInbound().shipment_items(QueryType='SHIPMENT', MarketplaceId="ATVPDKIKX0DER", NextToken='NextToken')

        Args:
            **kwargs:

        Returns:
            ApiResponse
        """
        return self._request(kwargs.pop(u"path"), params=kwargs)
