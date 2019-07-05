from django.conf import settings
import urllib.parse


class OAuthQQ(object):
    """
    QQ认证辅助工具类
    """

    def __init__(self, client_id=None, redirect_uri=None, state=None):
        self.client_id = client_id if client_id else settings.QQ_CLIENT_ID
        self.redirect_uri = redirect_uri if redirect_uri else settings.QQ_REDIRECT_URI
        # self.state=state if state else settings.QQ_STATE
        self.state = state or settings.QQ_STATE

    def get_qq_login_url(self):
        url = 'https://graph.qq.com/oauth2.0/authorize?'
        params = {
            'response_type': 'code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'state': self.state,
        }
        url += urllib.parse.urlencode(params)
        return url
