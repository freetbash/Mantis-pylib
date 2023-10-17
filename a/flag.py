from .target import *

def sf(target:str,flag:str, func):
    """
    submit a flag to server
    """
    func(target, flag)

def gf(target:str, func, **payloads):
    """
    get a flag by func
    """
    return func(target, **payloads)

def gwfc(target:str, **paylods):
    """
    get a web flag func
    gwf("http://123.132.123.123:80",path='/flag.txt', headers={}, data={})
    """
    
    print(paylods)
    path = paylods.get('path')
    if path is None: return 'not path. mantis'

    headers = paylods.get('headers')
    if headers is None: headers={}
    
    data = paylods.get('data')
    if data is None:
        return requests.get(target+path, headers=headers).text
    else:
        return requests.post(target+path, headers=headers, data=data).text
    
    
    

def msf(targets:ipr, payload, func):
    for ip in targets.d:
        flag = gf(ip, payload, func)
        sf(ip, flag, func)
    pass

def mgf(targets:ipr, func, **payloads):
    """
    batch get flag by func
    mgf(ipr, gwfc, path='/flag.txt')
    
    ipr = lhip(pip("192.168.152.130", 8001, 8003))
    """
    return [func(ip, **payloads) for ip in targets.d]
    