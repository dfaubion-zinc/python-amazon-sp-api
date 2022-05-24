from __future__ import absolute_import
from sp_api.base import Client, sp_endpoint
from sp_api.base.helpers import create_md5, fill_query_params
import urllib2, urllib, urlparse


class Upload(Client):
    @sp_endpoint(u'/uploads/2020-11-01/uploadDestinations/{}', method=u'POST')
    def upload_document(self, resource, file, content_type=u'application/pdf', **kwargs):
        md5 = urllib.quote(create_md5(file))
        kwargs.update({
            u'contentMD5': md5,
            u'contentType': kwargs.pop(u'contentType', content_type),
            u'marketplaceIds': self.marketplace_id
        })
        return self._request(fill_query_params(kwargs.pop(u'path'), resource), params=kwargs)
