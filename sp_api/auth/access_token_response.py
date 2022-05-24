class AccessTokenResponse(object):
    def __init__(self, **kwargs):
        self.access_token = kwargs.get(u'access_token')
        self.refresh_token = kwargs.get(u'refresh_token')
        self.expires_in = kwargs.get(u'expires')
        self.token_type = kwargs.get(u'token_type')
