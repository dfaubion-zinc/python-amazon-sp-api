from __future__ import with_statement
from __future__ import absolute_import
import pytest

from sp_api.api.merchant_fulfillment.merchant_fulfillment import MerchantFulfillment
from sp_api.base import SellingApiServerException, SellingApiForbiddenException, SellingApiBadRequestException


def test_get_eligible_shipment_services_old():
    with pytest.raises(SellingApiForbiddenException) as info:
        res = MerchantFulfillment().get_eligible_shipment_services_old({
            u"AmazonOrderId": u"903-5563053-5647845",
            u"ItemList": [
                {
                    u"OrderItemId": u"52986411826454",
                    u"Quantity": 1
                }
            ],
            u"ShipFromAddress": {
                u"Name": u"John Doe",
                u"AddressLine1": u"300 Turnbull Ave",
                u"Email": u"jdoeasdfllkj@yahoo.com",
                u"City": u"Detroit",
                u"StateOrProvinceCode": u"MI",
                u"PostalCode": u"48123",
                u"CountryCode": u"US",
                u"Phone": u"7132341234"
            },
            u"PackageDimensions": {
                u"Length": 10,
                u"Width": 10,
                u"Height": 10,
                u"Unit": u"inches"
            },
            u"Weight": {
                u"Value": 10,
                u"Unit": u"oz"
            },
            u"ShippingServiceOptions": {
                u"DeliveryExperience": u"NoTracking",
                u"CarrierWillPickUp": False,
                u"CarrierWillPickUpOption": u"ShipperWillDropOff"
            }
        })
        assert res.errors is None
        assert res.payload.get(u'ShippingServiceList') is not None


def test_get_eligible_shipment_services():
    with pytest.raises(SellingApiForbiddenException) as info:
        res = MerchantFulfillment().get_eligible_shipment_services({
            u"AmazonOrderId": u"903-5563053-5647845",
            u"ItemList": [
                {
                    u"OrderItemId": u"52986411826454",
                    u"Quantity": 1
                }
            ],
            u"ShipFromAddress": {
                u"Name": u"John Doe",
                u"AddressLine1": u"300 Turnbull Ave",
                u"Email": u"jdoeasdfllkj@yahoo.com",
                u"City": u"Detroit",
                u"StateOrProvinceCode": u"MI",
                u"PostalCode": u"48123",
                u"CountryCode": u"US",
                u"Phone": u"7132341234"
            },
            u"PackageDimensions": {
                u"Length": 10,
                u"Width": 10,
                u"Height": 10,
                u"Unit": u"inches"
            },
            u"Weight": {
                u"Value": 10,
                u"Unit": u"oz"
            },
            u"ShippingServiceOptions": {
                u"DeliveryExperience": u"NoTracking",
                u"CarrierWillPickUp": False,
                u"CarrierWillPickUpOption": u"ShipperWillDropOff"
            }
        })
        assert res.errors is None
        assert res.payload.get(u'ShippingServiceList') is not None


def test_create_shipment():
    with pytest.raises(SellingApiForbiddenException) as info:
        res = MerchantFulfillment().create_shipment(
            shipment_request_details={
                u"AmazonOrderId": u"903-5563053-5647845",
                u"ItemList": [
                    {
                        u"OrderItemId": u"52986411826454",
                        u"Quantity": 1
                    }
                ],
                u"ShipFromAddress": {
                    u"Name": u"John Doe",
                    u"AddressLine1": u"300 Turnbull Ave",
                    u"Email": u"jdoeasdfllkj@yahoo.com",
                    u"City": u"Detroit",
                    u"StateOrProvinceCode": u"MI",
                    u"PostalCode": u"48123",
                    u"CountryCode": u"US",
                    u"Phone": u"7132341234"
                },
                u"PackageDimensions": {
                    u"Length": 10,
                    u"Width": 10,
                    u"Height": 10,
                    u"Unit": u"inches"
                },
                u"Weight": {
                    u"Value": 10,
                    u"Unit": u"oz"
                },
                u"ShippingServiceOptions": {
                    u"DeliveryExperience": u"NoTracking",
                    u"CarrierWillPickUp": False,
                    u"CarrierWillPickUpOption": u"ShipperWillDropOff"
                }
            },
            shipping_service_id=u"UPS_PTP_2ND_DAY_AIR",
            ShippingServiceOfferId=u"WHgxtyn6qjGGaCzOCog1azF5HLHje5Pz3Lc2Fmt5eKoZAReW8oJ1SMumuBS8lA/Hjuglhyiu0"
                                   u"+KRLvyJxFV0PB9YFMDhygs3VyTL0WGYkGxiuRkmuEvpqldUn9rrkWVodqnR4vx2VtXvtER"
                                   u"/Ju6RqYoddJZGy6RS2KLzzhQ2NclN0NYXMZVqpOe5RsRBddXaGuJr7oza3M52"
                                   u"+JzChocAHzcurIhCRynpbxfmNLzZMQEbgnpGLzuaoSMzfxg90/NaXFR/Ou01du/uKd5AbfMW"
                                   u"/AxAKP9ht6Oi9lDHq6WkGqvjkVLW0/jj/fBgblIwcs+t"
        )
        assert res.errors is None
        assert res.payload.get(u'ShipmentId') == u"be7a0a53-00c3-4f6f-a63a-639f76ee9253"


def test_get_shipment():
    with pytest.raises(SellingApiForbiddenException) as info:
        res = MerchantFulfillment().get_shipment(u"abcddcba-00c3-4f6f-a63a-639f76ee9253")
        assert res.errors is None
        assert res.payload.get(u'ShipmentId') == u"abcddcba-00c3-4f6f-a63a-639f76ee9253"


def test_get_shipment_400():
    with pytest.raises(SellingApiForbiddenException) as info:
        try:
            res = MerchantFulfillment().get_shipment(u"aabbccdd-1beb-4cda-8bf4-7366cfddbec1")
        except SellingApiBadRequestException, br:
            assert br.code == 400
            assert type(br) == SellingApiBadRequestException


def test_cancel_shipment():
    with pytest.raises(SellingApiForbiddenException) as info:
        res = MerchantFulfillment().cancel_shipment(u"be7a0a53-00c3-4f6f-a63a-639f76ee9253")
        assert res.errors is None
        assert res.payload.get(u'ShipmentId') == u"be7a0a53-00c3-4f6f-a63a-639f76ee9253"


def test_cancel_shipment_old():
    with pytest.raises(SellingApiForbiddenException) as info:
        res = MerchantFulfillment().cancel_shipment_old(u"be7a0a53-00c3-4f6f-a63a-639f76ee9253")
        assert res.errors is None
        assert res.payload.get(u'ShipmentId') == u"be7a0a53-00c3-4f6f-a63a-639f76ee9253"


def test_get_additional_seller_inputs_old():
    with pytest.raises(SellingApiForbiddenException) as info:
        res = MerchantFulfillment().get_additional_seller_inputs_old(
            shipping_service_id=u"UPS_PTP_GND",
            ship_from_address={
                u"Name": u"John Doe",
                u"AddressLine1": u"300 Turnbull Ave",
                u"Email": u"jdoeasdfllkj@yahoo.com",
                u"City": u"Detroit",
                u"StateOrProvinceCode": u"MI",
                u"PostalCode": u"48123",
                u"CountryCode": u"US",
                u"Phone": u"7132341234"
            },
            order_id=u"903-5563053-5647845",
        )
        assert res.errors is None
        assert res.payload.get(u'ShipmentLevelFields') is not None


def test_get_additional_seller_inputs():
    with pytest.raises(SellingApiForbiddenException) as info:
        res = MerchantFulfillment().get_additional_seller_inputs(
            shipping_service_id=u"UPS_PTP_GND",
            ship_from_address={
                u"Name": u"John Doe",
                u"AddressLine1": u"300 Turnbull Ave",
                u"Email": u"jdoeasdfllkj@yahoo.com",
                u"City": u"Detroit",
                u"StateOrProvinceCode": u"MI",
                u"PostalCode": u"48123",
                u"CountryCode": u"US",
                u"Phone": u"7132341234"
            },
            order_id=u"903-5563053-5647845",
        )
        assert res.errors is None
        assert res.payload.get(u'ShipmentLevelFields') is not None


