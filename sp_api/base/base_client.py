from __future__ import absolute_import
from sp_api.__version__ import __version__


class BaseClient(object):
    scheme = u'https://'
    method = u'GET'
    content_type = u'application/x-www-form-urlencoded;charset=UTF-8'
    user_agent = u'python-sp-api-%(version)s' % {u"version": __version__}
