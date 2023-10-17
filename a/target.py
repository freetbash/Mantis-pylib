from t.all import *
import requests


def gip(ip_template:ipr, begin=1, end=255):
    """
    Generate ip
    gip("192.168.0.{}", 1, 255)-
    """
    return ipr([ip_template.format(i) for i in range(begin, end+1)])
    
def lpip(ip_list:ipr, port=80):
    """
    use ipr to generate ip:port
    lpip(ipr, 80)
    """
    return ipr([i+':'+str(port) for i in ip_list.d])

def pip(ip:str, begin:int, end:int):
    """
    Generate ip:port
    pip("192.168.0.103", 4001, 4010)
    """
    return ipr([ip+':'+str(i) for i in range(begin, end+1)])

def lhip(ips:ipr, h:str="http"):
    """
    add http or https to ipr
    """
    return ipr([h+'://'+i for i in ips.d])

def it(file:str="ip.txt"):
    """
    import a file to ipr target
    it(file)
    """
    with open(file,"r") as f:
        return ipr([i.replace('\n', '') for i in f.readlines()])
    
def cw(hip:str, web_path:str,headers:dict={}):
    """
    web_path = /asd/asd
    """
    url = hip + web_path
    try:
        r = requests.get(url,headers=headers, timeout=7)
        if r.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def cwt(targets:ipr, web_path:str,headers:dict={}):
    """
    check web targets
    this func will return a  ipr tuple (ok_ipr, no_ipr)
    targets is a ipr
    use the func cw()
    """
    ok=[]
    no=[]
    for i in targets.d:
        if cw(i,web_path,headers):
            ok.append(i)
        else:
            no.append(i)
    return (ipr(ok), ipr(no))

    
    