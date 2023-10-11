import pyperclip
import requests
# import asyncio


class ipr:
    d = []
    def __init__(self, r):
        """
        ip list input
        """
        self.d = r
        
    def tF(self, file="ip.txt"):
        """
        ips to File
        """
        with open(file,'w') as f:
            for i in self.d:
                f.write(i+'\n')
        
    def tC(self, delim='\n'):     
        """
        ips to Clipboard
        """
        pyperclip.copy(self.tS(delim=delim))
        
    def tS(self, delim='\n'):
        """
        ips toString
        """
        s = ''
        for i in self.d: s+= i+delim
        return s
    
    def append(self, ipr_list):
        self.d.append(ipr_list)
       
    def __str__(self):
        return str(self.d)
    def __len__(self):
        return len(self.d)


def gip(ip_template, begin=1, end=255):
    """
    Generate ip
    gip("192.168.0.{}", 1, 255)-
    """
    return ipr([ip_template.format(i) for i in range(begin, end+1)])
    
def lpip(ip_list, port):
    """
    use ipr to generate ip:port
    lpip(ipr, 4001, 4010)
    """
    return ipr([i+':'+str(port) for i in ip_list.d])

def pip(ip, begin, end):
    """
    Generate ip:port
    pip("192.168.0.103", 4001, 4010)
    """
    return ipr([ip+':'+str(i) for i in range(begin, end+1)])

def it(file="ip.txt"):
    """
    import a file to ipr target
    it(file)
    """
    with open(file,"r") as f:
        return ipr([i.replace('\n', '') for i in f.readlines()])
    
def cw(ip, web_path, h="http",headers={}):
    """
    web_path = /asd/asd
    """
    url = h + "://" + ip + web_path
    try:
        r = requests.get(url,headers=headers, timeout=7)
        if r.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def cwt(targets, web_path, h="http",headers={}):
    """
    check web targets
    this func will return a  ipr tuple (ok_ipr, no_ipr)
    targets is a ipr
    use the func cw()
    """
    ok=[]
    no=[]
    for i in targets.d:
        if cw(i,web_path,h,headers):
            ok.append(i)
        else:
            no.append(i)
    return (ipr(ok), ipr(no))

    
    