import requests as r

default_host = 'aischool2.zzedu.net.cn'
default_port = 8002

class TWApi (object):
    def __init__(self, url, data):
        self.headers = {
                'X-Device-Id': 'AAAAAAAAAA',
                'X-Device-type': '4',
                'X-PC-Authenticate-key': 'AAAAAAAAAA',
                'X-Request-Platform': '10014000',
                'X-User-Account': 'S000586600000005903'
                }
        self.data = data

    def get(self):
        pass

    def post(self, data, host=default_host, port=default_port):
        self.data.extend(data)
        #TODO Implemetn

getPicAndCatalogData = {
        "isQuerySelf":"1",
        "catalogId":"0",
        "classId":"S000586600000000005",
        "catalogType":"1,3",
        "dateRange":"3",
        "startTime":"",
        "endTime":"",
        "name":"",
        "resourceType":"",
        "numPerPage":20,
        "pageNum":1	}
getPicAndCatalogAPI = TWApi('/portal/ClientApi/getPicAndCatalog', getPicAndCatalogData)
