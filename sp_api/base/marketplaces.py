u"""
Country	marketplaceId	Country code
Canada	A2EUQ1WTGCTBG2	CA
United States of America	ATVPDKIKX0DER	US
Mexico	A1AM78C64UM0Y8	MX
Brazil	A2Q3Y263D00KWC	BR
Europe

Country	marketplaceId	Country code
Spain	A1RKKUPIHCS9HS	ES
United Kingdom	A1F83G8C2ARO7P	GB
France	A13V1IB3VIYZZH	FR
Netherlands	A1805IZSGTT6HS	NL
Germany	A1PA6795UKMFR9	DE
Italy	APJ6JRA9NG5V4	IT
Sweden	A2NODRKZP88ZB9	SE
Poland	A1C3SOZRARQ6R3	PL
Turkey	A33AVAJ2PDY3EV	TR
United Arab Emirates	A2VIGQ35RCS4UG	AE
India	A21TJRUUN4KGV	IN
Far East

Country	marketplaceId	Country code
Singapore	A19VAU5U5O7RUS	SG
Australia	A39IBJ37TRP1C6	AU
Japan	A1VC38T7YXB528	JP
"""
from __future__ import absolute_import
import sys
from enum import Enum
import os
from collections import namedtuple


class AwsEnv(Enum):
    PRODUCTION = u"PRODUCTION"
    SANDBOX = u"SANDBOX"


AWS_ENVIRONMENT = os.getenv(u"AWS_ENV", AwsEnv.PRODUCTION.name)
BASE_URL = u"https://sellingpartnerapi"

if AwsEnv(AWS_ENVIRONMENT) == AwsEnv.SANDBOX:
    BASE_URL = u"https://sandbox.sellingpartnerapi"


Marketplace = namedtuple('Marketplace', ['endpoint', 'marketplace_id', 'region'])
class Marketplaces(Enum):
    u"""Enumeration for MWS marketplaces, containing endpoints and marketplace IDs.
    Example, endpoint and ID for UK marketplace:
        endpoint = Marketplaces.UK.endpoint
        marketplace_id = Marketplaces.UK.marketplace_id
    """

    AE = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A2VIGQ35RCS4UG", u"eu-west-1")
    DE = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A1PA6795UKMFR9", u"eu-west-1")
    PL = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A1C3SOZRARQ6R3", u"eu-west-1")
    EG = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"ARBP9OOSHTCHU", u"eu-west-1")
    ES = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A1RKKUPIHCS9HS", u"eu-west-1")
    FR = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A13V1IB3VIYZZH", u"eu-west-1")
    GB = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A1F83G8C2ARO7P", u"eu-west-1")
    IN = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A21TJRUUN4KGV", u"eu-west-1")
    IT = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"APJ6JRA9NG5V4", u"eu-west-1")
    NL = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A1805IZSGTT6HS", u"eu-west-1")
    SA = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A17E79C6D8DWNP", u"eu-west-1")
    SE = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A2NODRKZP88ZB9", u"eu-west-1")
    TR = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A33AVAJ2PDY3EV", u"eu-west-1")
    UK = Marketplace(u"%s-eu.amazon.com" % BASE_URL, u"A1F83G8C2ARO7P", u"eu-west-1")  # alias for GB
    AU = Marketplace(u"%s-fe.amazon.com" % BASE_URL, u"A39IBJ37TRP1C6", u"us-west-2")
    JP = Marketplace(u"%s-fe.amazon.com" % BASE_URL, u"A1VC38T7YXB528", u"us-west-2")
    SG = Marketplace(u"%s-fe.amazon.com" % BASE_URL, u"A19VAU5U5O7RUS", u"us-west-2")
    US = Marketplace(u"%s-na.amazon.com" % BASE_URL, u"ATVPDKIKX0DER", u"us-east-1")
    BR = Marketplace(u"%s-na.amazon.com" % BASE_URL, u"A2Q3Y263D00KWC", u"us-east-1")
    CA = Marketplace(u"%s-na.amazon.com" % BASE_URL, u"A2EUQ1WTGCTBG2", u"us-east-1")
    MX = Marketplace(u"%s-na.amazon.com" % BASE_URL, u"A1AM78C64UM0Y8", u"us-east-1")

    @classmethod
    def by_marketplace_id(cls, marketplace_id):
        return {
            "A13V1IB3VIYZZH": cls.FR,
            "A17E79C6D8DWNP": cls.SA,
            "A1805IZSGTT6HS": cls.NL,
            "A19VAU5U5O7RUS": cls.SG,
            "A1AM78C64UM0Y8": cls.MX,
            "A1C3SOZRARQ6R3": cls.PL,
            # "A1F83G8C2ARO7P": cls.GB,
            "A1F83G8C2ARO7P": cls.UK,
            "A1PA6795UKMFR9": cls.DE,
            "A1RKKUPIHCS9HS": cls.ES,
            "A1VC38T7YXB528": cls.JP,
            "A21TJRUUN4KGV": cls.IN,
            "A2EUQ1WTGCTBG2": cls.CA,
            "A2NODRKZP88ZB9": cls.SE,
            "A2Q3Y263D00KWC": cls.BR,
            "A2VIGQ35RCS4UG": cls.AE,
            "A33AVAJ2PDY3EV": cls.TR,
            "A39IBJ37TRP1C6": cls.AU,
            "APJ6JRA9NG5V4": cls.IT,
            "ARBP9OOSHTCHU": cls.EG,
            "ATVPDKIKX0DER": cls.US,
        }.get(marketplace_id)

    def __init__(self, endpoint, marketplace_id, region):
        self.endpoint = endpoint
        self.marketplace_id = marketplace_id
        self.region = region
