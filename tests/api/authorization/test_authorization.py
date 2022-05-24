from __future__ import absolute_import
from sp_api.api import Authorization


def test_get_auth_code():
    res = Authorization().get_authorization_code(mwsAuthToken=u'test', developerId=u'test', sellingPartnerId=u'test')
    assert res.payload[u'authorizationCode'] == u'ANDMxqpCmqWHJeyzdbMH'
