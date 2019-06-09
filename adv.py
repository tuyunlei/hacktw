import requests as r

headers = {
        'X-Device-Id': 'AAAAAAAAAA',
        'X-Device-type': '4',
        'X-PC-Authenticate-key': 'AAAAAAAAAA',
        'X-Request-Platform': '10014000',
        'X-User-Account': 'S000586600000005903'
        }

def getRootPictures(classid, pagenum=1, numperpage=20):
    url = '/portal/ClientApi/getPicAndCatalog'
    data = {
        "isQuerySelf": "1",
        "catalogId": "0",
        "catalogType": "1,3",
        "dateRange": "3",
        "startTime": "",
        "endTime": "",
        "name": "",
        "resourceType": "",
        "numPerPage": numperpage,
        "pageNum": pagenum
        "classId": classid,
        }
    rep = r.post(url, headers=header, json=data)
    return rep.json()

def getPictures(catalogid, pagenum=1, numperpage=20):
    url = '/portal/ClientApi/getPicAndCatalog'
    data = {
        "isQuerySelf": "1",
        "catalogType": "1,3",
        "dateRange": "3",
        "startTime": "",
        "endTime": "",
        "name": "",
        "resourceType": "",
        "pageNum": pagenum
        "catalogId": catalogid,
        "numPerPage": numperpage,
        }
    rep = r.post(url, headers=header, json=data)
    return rep.json()

def addPicture(ca

