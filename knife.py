import requests as r

host = '10.3.25.12'

class Knife (object):

    def __init__(self, url, pwd, encoding='utf-8'):
        self.url = url
        self.pwd = pwd
        self.encoding = encoding

    def _data(self, action, p1=None, p2=None):
        data_dict = {
            self.pwd: action,
            'z0': self.encoding,
            'z1': p1,
            'z2': p2
        }
        return {k:v for k,v in data_dict.items() if v}

    def _parse(self, content):
        return content.lstrip("->|").rstrip("|<-")

    def test(self):
        data = self._data('A')
        return data;

url = "http://10.3.25.12:8004/rescloud/temp/a2f19f84-4ed9-4935-87ca-abec975ea328.jsp"
if __name__ == '__main__':
    kf = Knife(url, 'twsm')
