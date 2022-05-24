from __future__ import absolute_import
from sp_api.base import AccessTokenClient
from sp_api.base import Credentials, CredentialProvider
from sp_api.base import AuthorizationError
from sp_api.base.credential_provider import FromCodeCredentialProvider
refresh_token = u'<refresh_token>'
lwa_app_id = u'<lwa_app_id>'
lwa_client_secret = u'<lwa_client_secret>'
aws_secret_key = u'<aws_secret_access_key>'
aws_access_key = u'<aws_access_key_id>'
role_arn = u'<role_arn>'



def test_auth_exception():
    e = AuthorizationError(200, u'Foo', 999)
    assert e.status_code == 999
    assert e.error_code == 200
    assert e.message == u'Foo'


def test_credentials():
    x = CredentialProvider()
    assert x.credentials.lwa_app_id is not None
    assert x.credentials.lwa_client_secret is not None
    assert x.credentials.aws_secret_key is not None
    assert x.credentials.aws_access_key is not None


def test_auth_client():
    client = AccessTokenClient(credentials=CredentialProvider(credentials=dict(
        refresh_token=refresh_token,
        lwa_app_id=lwa_app_id,
        lwa_client_secret=lwa_client_secret,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
        role_arn=role_arn,
    )).credentials)
    x = client._auth_code_request_body(u'foo')
    assert x.get(u'grant_type') == u'authorization_code'

    try:
        client.authorize_auth_code(u'foo')
    except AuthorizationError, e:
        assert isinstance(e, AuthorizationError)

    try:
        client._request(u'https://jsonplaceholder.typicode.com/posts/1', {}, {})
    except AuthorizationError, e:
        assert isinstance(e, AuthorizationError)
