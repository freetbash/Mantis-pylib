from .target import *

def sf(target,flag, func):
    """
    submit a flag to server
    """
    func(target, flag)

def gf(func, payload):
    """
    get a flag by func
    """
    return func(payload)

def gwf(target, path, headers={}, data={}):
    """
    get a web flag
    gwf("http://123.132.123.123:80","/flag.txt")
    """
    payload = target + path
    def a(payload):
        return requests.get(payload,headers=headers,data=data).text
    return gf(a,payload)

def msf():
    pass

def mgf():
    pass
    