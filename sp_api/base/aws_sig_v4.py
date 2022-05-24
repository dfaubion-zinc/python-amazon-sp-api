from __future__ import absolute_import
from __future__ import print_function
import os
import datetime
import hashlib
import hmac
import logging

from collections import OrderedDict
from requests.auth import AuthBase
from requests.compat import urlencode, quote, urlparse
from itertools import imap

__version__ = u'0.4'

log = logging.getLogger(__name__)


def sign_msg(key, msg):
    u''' Sign message using key '''
    return hmac.new(key, msg.encode(u'utf-8'), hashlib.sha256).digest()


class AWSSigV4(AuthBase):

    def __init__(self, service, **kwargs):
        self.service = service
        self.aws_access_key_id = kwargs.get(u'aws_access_key_id')
        self.aws_secret_access_key = kwargs.get(u'aws_secret_access_key')
        self.aws_session_token = kwargs.get(u'aws_session_token')
        if self.aws_access_key_id is None or self.aws_secret_access_key is None:
            raise KeyError(u"AWS Access Key ID and Secret Access Key are required")
        self.region = kwargs.get(u'region')

    def __call__(self, r):
        t = datetime.datetime.utcnow()
        self.amzdate = t.strftime(u'%Y%m%dT%H%M%SZ')
        self.datestamp = t.strftime(u'%Y%m%d')
        log.debug(u"Starting authentication with amzdate=%s", self.amzdate)
        p = urlparse(r.url)

        host = p.hostname
        uri = quote(p.path)

        # sort query parameters alphabetically
        if len(p.query) > 0:
            split_query_parameters = list(imap(lambda param: param.split(u'='), p.query.split(u'&')))
            ordered_query_parameters = sorted(split_query_parameters, key=lambda param: (param[0], param[1]))
        else:
            ordered_query_parameters = list()

        ordered_query_parameters = [[elm[0], elm[1].replace(u'+', u'%20')] for elm in ordered_query_parameters] # hack to get around amazon bug
        canonical_querystring = u"&".join(imap(lambda param: u"=".join(param), ordered_query_parameters))

        headers_to_sign = {u'host': host, u'x-amz-date': self.amzdate}
        if self.aws_session_token is not None:
            headers_to_sign[u'x-amz-security-token'] = self.aws_session_token
            r.headers[u'x-amz-security-token'] = self.aws_session_token

        ordered_headers = OrderedDict(sorted(headers_to_sign.items(), key=lambda t: t[0]))
        canonical_headers = u''.join(imap(lambda h: u":".join(h) + u'\n', ordered_headers.items()))
        signed_headers = u';'.join(ordered_headers.keys())

        if r.method == u'GET':
            payload_hash = hashlib.sha256(u''.encode(u'utf-8')).hexdigest()
        else:
            if not r.body:
                r.body = u""
            payload_hash = hashlib.sha256(r.body.encode(u'utf-8')).hexdigest()

        canonical_request = u'\n'.join([r.method, uri, canonical_querystring,
                                       canonical_headers, signed_headers, payload_hash])

        credential_scope = u'/'.join([self.datestamp, self.region, self.service, u'aws4_request'])
        string_to_sign = u'\n'.join([u'AWS4-HMAC-SHA256', self.amzdate,
                                    credential_scope, hashlib.sha256(canonical_request.encode(u'utf-8')).hexdigest()])
        log.debug(u"String-to-Sign: '%s'", string_to_sign)

        kDate = sign_msg((u'AWS4' + self.aws_secret_access_key).encode(u'utf-8'), self.datestamp)
        kRegion = sign_msg(kDate, self.region)
        kService = sign_msg(kRegion, self.service)
        kSigning = sign_msg(kService, u'aws4_request')
        signature = hmac.new(kSigning, string_to_sign.encode(u'utf-8'), hashlib.sha256).hexdigest()

        authorization_header = u"AWS4-HMAC-SHA256 Credential={}/{}, SignedHeaders={}, Signature={}".format(
            self.aws_access_key_id, credential_scope, signed_headers, signature)
        r.headers.update({
            u'host': host,
            u'x-amz-date': self.amzdate,
            u'Authorization': authorization_header,
        })
        return r
