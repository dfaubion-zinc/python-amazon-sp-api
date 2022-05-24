from __future__ import absolute_import
import json
import os

import confuse
import boto3
from botocore.exceptions import ClientError
from cachetools import Cache

required_credentials = [
    u'aws_access_key',
    u'aws_secret_key',
    u'lwa_app_id',
    u'lwa_client_secret'
]


class MissingCredentials(Exception):
    u"""
    Credentials are missing, see the error output to find possible causes
    """
    pass


class BaseCredentialProvider(object):
    errors = []
    credentials = None

    def __init__(self, account = u'default', *args, **kwargs):
        self.account = account

    def __call__(self, *args, **kwargs):
        self.load_credentials()
        return self.check_credentials()

    def load_credentials(self):
        raise NotImplementedError()

    def check_credentials(self):
        try:
            self.errors = [c for c in required_credentials if
                           c not in self.credentials.keys() or not self.credentials[c]]
        except (AttributeError, TypeError):
            raise MissingCredentials(u'Credentials are missing: ' + u", ".join(required_credentials))
        if not len(self.errors):
            return self.credentials
        raise MissingCredentials(u'Credentials are missing: ' + u", ".join(self.errors))


class FromCodeCredentialProvider(BaseCredentialProvider):
    def load_credentials(self):
        return None

    def __init__(self, credentials, *args, **kwargs):
        super(FromCodeCredentialProvider, self).__init__(u'default', credentials)
        self.credentials = credentials


class FromConfigFileCredentialProvider(BaseCredentialProvider):
    def load_credentials(self):
        try:
            config = confuse.Configuration(u'python-sp-api')
            config_filename = os.path.join(config.config_dir(), u'credentials.yml')
            config.set_file(config_filename)
            account_data = config[self.account].get()
            self.credentials = account_data
        except (confuse.exceptions.NotFoundError, confuse.exceptions.ConfigReadError):
            return


class FromSecretsCredentialProvider(BaseCredentialProvider):
    def load_credentials(self):
        if not os.environ.get(u'SP_API_AWS_SECRET_ID', None):
            return
        try:
            client = boto3.client(u'secretsmanager')
            response = client.get_secret_value(
                SecretId=os.environ.get(u'SP_API_AWS_SECRET_ID')
            )
            secret = json.loads(response.get(u'SecretString'))
            account_data = dict(
                refresh_token=secret.get(u'SP_API_REFRESH_TOKEN'),
                lwa_app_id=secret.get(u'LWA_APP_ID'),
                lwa_client_secret=secret.get(u'LWA_CLIENT_SECRET'),
                aws_secret_key=secret.get(u'SP_API_SECRET_KEY'),
                aws_access_key=secret.get(u'SP_API_ACCESS_KEY'),
                role_arn=secret.get(u'SP_API_ROLE_ARN')
            )
        except ClientError:
            return
        else:
            self.credentials = account_data


class FromEnvironmentVariablesCredentialProvider(BaseCredentialProvider):
    def load_credentials(self):
        account_data = dict(
            refresh_token=self._get_env(u'SP_API_REFRESH_TOKEN'),
            lwa_app_id=self._get_env(u'LWA_APP_ID'),
            lwa_client_secret=self._get_env(u'LWA_CLIENT_SECRET'),
            aws_secret_key=self._get_env(u'SP_API_SECRET_KEY'),
            aws_access_key=self._get_env(u'SP_API_ACCESS_KEY'),
            role_arn=self._get_env(u'SP_API_ROLE_ARN')
        )
        self.credentials = account_data

    def _get_env(self, key):
        return os.environ.get(u'{key}_{account}'.format(key=key, account=self.account))


class CredentialProvider(object):
    credentials = None
    cache = Cache(maxsize=10)

    CREDENTIAL_PROVIDERS = [
        FromCodeCredentialProvider,
        FromEnvironmentVariablesCredentialProvider,
        FromSecretsCredentialProvider,
        FromConfigFileCredentialProvider
    ]

    def __init__(self, account=u'default', credentials=None):
        self.account = account
        for cp in self.CREDENTIAL_PROVIDERS:
            try:
                self.credentials = cp(account=account, credentials=credentials)()
                break
            except MissingCredentials:
                continue
        if self.credentials:
            self.credentials = self.Config(**self.credentials)
        else:
            raise MissingCredentials(u'Credentials are missing: ' + u", ".join(required_credentials))

    class Config(object):
        def __init__(self, **kwargs):
            self.refresh_token = kwargs.get(u'refresh_token')
            self.lwa_app_id = kwargs.get(u'lwa_app_id')
            self.lwa_client_secret = kwargs.get(u'lwa_client_secret')
            self.aws_access_key = kwargs.get(u'aws_access_key')
            self.aws_secret_key = kwargs.get(u'aws_secret_key')
            self.role_arn = kwargs.get(u'role_arn')
