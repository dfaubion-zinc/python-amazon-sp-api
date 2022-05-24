from __future__ import absolute_import
from sp_api.api import FbaInboundEligibility


def test_inbound_eligibility():
    res = FbaInboundEligibility().get_item_eligibility_preview(asin=u'TEST_CASE_200', program=u"INBOUND")
    assert res.payload is not None
