from __future__ import absolute_import
import os
import pytest

from sp_api.api import FulfillmentInbound
from sp_api.base import AccessTokenClient
from sp_api.base import Marketplaces, MissingCredentials, Client, SellingApiForbiddenException
from sp_api.base.credential_provider import FromCodeCredentialProvider, FromEnvironmentVariablesCredentialProvider, \
    FromSecretsCredentialProvider, FromConfigFileCredentialProvider, required_credentials
from sp_api.base.exceptions import MissingScopeException

refresh_token = u'<refresh_token>'
lwa_app_id = u'<lwa_app_id>'
lwa_client_secret = u'<lwa_client_secret>'
aws_secret_key = u'<aws_secret_access_key>'
aws_access_key = u'<aws_access_key_id>'
role_arn = u'<role_arn>'


class Res(object):
    status_code = 200
    method = u'GET'
    headers = {}
    def json(self):
        return {u'foo': u'bar'}

    def __getattr__(self, item):
        return item


def test_client_request():
    try:
        Client()._request(u'', data=dict())
    except SellingApiForbiddenException, e:
        assert isinstance(e, SellingApiForbiddenException)


def test_api_response_has_next_token():
    res = FulfillmentInbound().get_shipments(QueryType=u'SHIPMENT')
    assert res.next_token is not None


def test_marketplaces():
    assert Marketplaces.DE.region == u'eu-west-1'
    assert Marketplaces.US.marketplace_id == u'ATVPDKIKX0DER'


def test_from_code_credential_provider():
    p = FromCodeCredentialProvider(credentials=dict(
        refresh_token=refresh_token,
        lwa_app_id=lwa_app_id,
        lwa_client_secret=lwa_client_secret,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
        role_arn=role_arn,
    ))
    assert p.credentials is not None
    assert isinstance(p.credentials, dict)


def test_from_code_credential_provider_no_role():
    p = FromCodeCredentialProvider(credentials=dict(
        refresh_token=refresh_token,
        lwa_app_id=lwa_app_id,
        lwa_client_secret=lwa_client_secret,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
    ))
    assert p.credentials is not None
    assert isinstance(p.credentials, dict)
    assert p.credentials.get(u'role_arn') is None


def test_from_code_credential_provider_no_role_no_refresh_token():
    p = FromCodeCredentialProvider(credentials=dict(
        lwa_app_id=lwa_app_id,
        lwa_client_secret=lwa_client_secret,
        aws_secret_key=aws_secret_key,
        aws_access_key=aws_access_key,
    ))
    assert p.credentials is not None
    assert isinstance(p.credentials, dict)
    assert p.credentials.get(u'role_arn') is None
    assert p.credentials.get(u'refresh_token') is None


@pytest.mark.order(-2)
def test_env_vars_provider():
    os.environ[u'SP_API_REFRESH_TOKEN'] = u'foo'
    os.environ[u'LWA_APP_ID'] = u'foo'
    os.environ[u'LWA_CLIENT_SECRET'] = u'foo'
    os.environ[u'SP_API_ACCESS_KEY'] = u'foo'
    os.environ[u'SP_API_SECRET_KEY'] = u'foo'
    os.environ[u'SP_API_ROLE_ARN'] = u'foo'

    p = FromEnvironmentVariablesCredentialProvider()()
    assert u'refresh_token' in p

    os.environ.pop(u'SP_API_REFRESH_TOKEN')
    os.environ.pop(u'LWA_APP_ID')
    os.environ.pop(u'LWA_CLIENT_SECRET')
    os.environ.pop(u'SP_API_ACCESS_KEY')
    os.environ.pop(u'SP_API_SECRET_KEY')
    os.environ.pop(u'SP_API_ROLE_ARN')


@pytest.mark.order(-1)
def test_from_secrets():
    os.environ[u'SP_API_AWS_SECRET_ID'] = u'testing/sp-api-foo'
    try:
        p = FromSecretsCredentialProvider()()
        assert u'refresh_token' in p
        assert p.get(u'refresh_token') == u'foo'
        os.environ.pop(u'SP_API_AWS_SECRET_ID')
    except MissingCredentials, e:
        assert isinstance(e, MissingCredentials)


def test_from_config_file_provider():
    try:
        p = FromConfigFileCredentialProvider()()
        assert p.get(u'refresh_token') is not None
    except MissingCredentials, e:
        assert isinstance(e, MissingCredentials)


def test_req():
    assert len(required_credentials) == 4


def test_client():
    client = Client(marketplace=Marketplaces.UK)
    assert client.marketplace_id == Marketplaces.UK.marketplace_id
    assert client.credentials is not None
    assert client.endpoint == Marketplaces.UK.endpoint
    assert client.region == Marketplaces.UK.region
    assert client.boto3_client is not None
    assert client.restricted_data_token is None
    assert isinstance(client._auth, AccessTokenClient)

    assert isinstance(client._get_cache_key(), unicode)
    assert isinstance(client._get_cache_key(u'test'), unicode)

    assert client.set_role() is not None

    assert client.headers[u'host'] == client.endpoint[8:]
    assert len(client.headers.keys()) == 5

    assert client.auth is not None
    try:
        x = client.grantless_auth
    except MissingScopeException, e:
        assert isinstance(e, MissingScopeException)

    assert client.role is not None
    assert client._sign_request is not None

    try:
        client._request(u'', data={})
    except SellingApiForbiddenException, e:
        assert isinstance(e, SellingApiForbiddenException)
    try:
        client._request(u'', params={})
    except SellingApiForbiddenException, e:
        assert isinstance(e, SellingApiForbiddenException)

    check = client._check_response(Res())
    assert check.payload[u'foo'] == u'bar'

    r = Res()
    r.method = u'POST'
    check = client._check_response(r)
    assert check.payload[u'foo'] == u'bar'
    assert check(u'foo') == u'bar'
    assert check.foo == u'bar'
    assert check()[u'foo'] == u'bar'

    r.method = u'DELETE'
    check = client._check_response(r)
    assert check.payload[u'foo'] == u'bar'
    assert check(u'foo') == u'bar'
    assert check.foo == u'bar'
    assert check()[u'foo'] == u'bar'

    client.grantless_scope = u'sellingpartnerapi::notifications'
    assert client.grantless_auth is not None

    try:
        client._request_grantless_operation(u'')
    except SellingApiForbiddenException, e:
        assert isinstance(e, SellingApiForbiddenException)
