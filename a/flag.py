from a.target import *

def sf(flag:str, func, **payloads):
    """
    submit a flag to server
    """
    func(flag, **payloads)

def gf(target:str, func, **payloads):
    """
    get a flag by func
    """
    return func(target, **payloads)

def swfc(flag, **payloads):
    """
    submit a flag to server func
    swfc("flag{asd2341v2}",server="http://192.168.0.1/submit_flag",headers={}, data={})
    swfc("flag{asd2341v2}",server="http://192.168.0.1/submit_flag?flag={}",headers={})
    """
    server = payloads.get('server')
    if server is None: return
    
    server = server.format(flag) # important
    
    headers = payloads.get('headers')
    if headers is None: headers={}
    
    data = payloads.get('data')
    if data:
        return requests.post(server, headers=headers, data=data).text
    else:
        return requests.get(server, headers=headers).text

def gwfc(target:str, **payloads):
    """
    get a web flag func
    gwf("http://123.132.123.123:80",path='/flag.txt', headers={}, data={})
    """
    
    path = payloads.get('path')
    if path is None: return 'not path. mantis'

    headers = payloads.get('headers')
    if headers is None: headers={}
    
    data = payloads.get('data')
    if data:
        return requests.post(target+path, headers=headers, data=data).text
    else:
        return requests.get(target+path, headers=headers).text
    

def msf(flags:list, func, **payloads):
    """
    batch submit flag to server by func
    msf(flags, swfc, server="http://127.0.0.1/sf?f={}",data={'i':'a'})
    flags = mgf(ipr, gwfc, path='/flag.txt')
    """
    return [func(flag, **payloads) for flag in flags]
    

def mgf(targets:ipr, func, **payloads):
    """
    batch get flag by func
    mgf(ipr, gwfc, path='/flag.txt')
    
    ipr = lhip(pip("192.168.152.130", 8001, 8003))
    """
    return [func(ip, **payloads) for ip in targets.d]
    