import requests
from libs.constants import ROOT_ZONE, HTTP


def call_api(path, method=HTTP.GET, data=None):
    url = f"{ROOT_ZONE}/{path}"
    if method == HTTP.GET:
        res = requests.get(url)
        if res.status_code != 200:
            raise Exception(f"{method}: {path} returned {res.status_code}")
    elif method == HTTP.POST:
        res = requests.post(url, data)
    elif method == HTTP.DELETE:
        res = requests.delete(url)
    elif method == HTTP.PUT:
        res = requests.put(url, data)
    else:
        raise Exception(f"{method} is not supported")
    return res
