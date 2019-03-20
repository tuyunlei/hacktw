import requests as r

host = '10.3.25.12'
url = f'http://{host}:8004/rescloud/resource/resourceFileUpload'

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'"
}

def upload(url, content):
    a = r.post(url, headers=headers, files={'file':content})
    return a.text


