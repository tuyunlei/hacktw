import requests as r

host = '10.3.25.12'

class Knife (object):

    def __init__(self, url, pwd, encoding='utf-8'):
        self.url = url
        self.pwd = pwd

    def _data(self, action, p1=None, p2=None):
        data_dict = {
            self.pwd: action,
            'z0': self.encoding,
            'z1': p1,
            'z2': p2
        }
        return {k:v for k,v in data_dict.items() if v}

    def _parse(self, content):
        pass

    def test():
        pass
