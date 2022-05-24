from __future__ import absolute_import
from datetime import datetime, timedelta

from sp_api.api import FulfillmentInbound


def test_item_guidance():
    res = FulfillmentInbound().item_guidance(SellerSKUList=u','.join([u"sku1", u"sku2"]), MarketplaceId=u'MarketplaceId')
    assert res.errors is None


def test_plans():
    res = FulfillmentInbound().plans({
        u"ShipFromAddress": {
            u"Name": u"Name",
            u"AddressLine1": u"123 any st",
            u"AddressLine2": u"AddressLine2",
            u"DistrictOrCounty": u"Washtenaw",
            u"City": u"Ann Arbor",
            u"StateOrProvinceCode": u"MI",
            u"CountryCode": u"US",
            u"PostalCode": u"48188"
        },
        u"LabelPrepPreference": u"SELLER_LABEL",
        u"ShipToCountryCode": u"ShipToCountryCode",
        u"ShipToCountrySubdivisionCode": u"ShipToCountrySubdivisionCode",
        u"InboundShipmentPlanRequestItems": [
            {
                u"SellerSKU": u"SellerSKU",
                u"ASIN": u"ASIN",
                u"Condition": u"NewItem",
                u"Quantity": 1,
                u"QuantityInCase": 1,
                u"PrepDetailsList": [
                    {
                        u"PrepInstruction": u"Polybagging",
                        u"PrepOwner": u"AMAZON"
                    }
                ]
            }
        ]
    })
    assert res.errors is None


def test_create_inbound_shipment():
    res = FulfillmentInbound().create_shipment(u'123', {
        u"InboundShipmentHeader": {
            u"ShipmentName": u"43545345",
            u"ShipFromAddress": {
                u"Name": u"35435345",
                u"AddressLine1": u"123 any st",
                u"DistrictOrCounty": u"Washtenaw",
                u"City": u"Ann Arbor",
                u"StateOrProvinceCode": u"Test",
                u"CountryCode": u"US",
                u"PostalCode": u"48103"
            },
            u"DestinationFulfillmentCenterId": u"AEB2",
            u"AreCasesRequired": True,
            u"ShipmentStatus": u"WORKING",
            u"LabelPrepPreference": u"SELLER_LABEL",
            u"IntendedBoxContentsSource": u"NONE"
        },
        u"InboundShipmentItems": [
            {
                u"ShipmentId": u"345453",
                u"SellerSKU": u"34534545",
                u"FulfillmentNetworkSKU": u"435435435",
                u"QuantityShipped": 0,
                u"QuantityReceived": 0,
                u"QuantityInCase": 0,
                u"ReleaseDate": u"2020-04-23",
                u"PrepDetailsList": [
                    {
                        u"PrepInstruction": u"Polybagging",
                        u"PrepOwner": u"AMAZON"
                    }
                ]
            }
        ],
        u"MarketplaceId": u"MarketplaceId"
    })
    assert res.errors is None


def test_update_shipment():
    res = FulfillmentInbound().update_shipment(u'123', {
        u"MarketplaceId": u"ATVPDKIKX0DER",
        u"InboundShipmentHeader": {
            u"ShipmentName": u"Shipment for FBA15DJCQ1ZF",
            u"ShipFromAddress": {
                u"Name": u"Uma Test",
                u"AddressLine1": u"123 any st",
                u"AddressLine2": u"",
                u"DistrictOrCounty": u"Washtenaw",
                u"City": u"Ann Arbor",
                u"StateOrProvinceCode": u"CO",
                u"CountryCode": u"US",
                u"PostalCode": u"48104"
            },
            u"DestinationFulfillmentCenterId": u"ABE2",
            u"ShipmentStatus": u"WORKING",
            u"LabelPrepPreference": u"SELLER_LABEL"
        },
        u"InboundShipmentItems": [
            {
                u"SellerSKU": u"PSMM-TEST-SKU-Apr-03_21_17_20-0379",
                u"QuantityShipped": 1
            }
        ]
    })
    assert res.errors is None


def test_preorder():
    res = FulfillmentInbound().preorder(u'shipmentId1', MarketplaceId=u'MarketplaceId1')
    assert res.errors is None

#
# def test_confirm_preorder():
#     res = FulfillmentInbound().confirm_preorder('shipmentId1', **{
#         "NeedByDate": "2020-10-10",
#         "MarketplaceId": "MarketplaceId1"
#     })
#     assert res.errors is None


def test_get_prep_orders():
    res = FulfillmentInbound().prep_instruction({u"ShipToCountryCode": u"US", u"ASINList": [u"ASIN1"]})
    assert res.errors is None


def test_get_transport():
    res = FulfillmentInbound().get_transport_information(u'shipmentId1')
    assert res.errors is None


def test_void_transport():
    res = FulfillmentInbound().void_transport(u'shipmentId1')
    assert res.errors is None


def test_estimate_transport():
    res = FulfillmentInbound().estimate_transport(u'shipmentId1')
    assert res.errors is None


def test_get_bill_of_lading():
    res = FulfillmentInbound().bill_of_lading(u'shipmentId')
    assert res.errors is None


def test_get_shipments():
    res = FulfillmentInbound().get_shipments(QueryType=u'SHIPMENT', MarketplaceId=u"ATVPDKIKX0DER")
    assert res.errors is None


def test_get_shipment_items():
    res = FulfillmentInbound().shipment_items_by_shipment(u'FBA15DJ9SVVD', MarketplaceId=u"ATVPDKIKX0DER")
    assert res.errors is None


def test_get_items():
    res = FulfillmentInbound().shipment_items(QueryType=u'SHIPMENT', MarketplaceId=u"ATVPDKIKX0DER", NextToken=u'NextToken')
    assert res.errors is None
