import requests as r

default_host = 'aischool2.zzedu.net.cn'
default_port = 8002
default_headers = {
        'X-Device-Id': 'AAAAAAAAAA',
        'X-Device-type': '4',
        'X-PC-Authenticate-key': 'AAAAAAAAAA',
        'X-Request-Platform': '10014000',
        'X-User-Account': 'S000586600000005903'
        }

class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]

class TWClient(object):
    def __init__(self, host, port=default_port, headers=None):
        self.host = host
        self.port = port
        self.headers = default_headers
        if headers:
            assert isinstance(headers, dict)
            self.headers.extend(headers)

# 获取作品库图片和文件夹
_url = '/portal/ClientApi/getPicAndCatalog'
_data = {
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
        "pageNum":1
        }
GetPicturesData = TWApi(_url, **_data)

# 获取作品点赞数
_url = '/portal/ClientApi/getPictureLikeClick'
_data = {"picId":"S000586600001108452"}
GetLikesData = TWApi(_url, **_data)
