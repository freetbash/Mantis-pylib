import pyperclip
class ipr:
    d = []
    def __init__(self, r:list):
        """
        ip list input
        """
        self.d = r
        
    def tF(self, file:str ="ip.txt"):
        """
        ips to File
        """
        with open(file,'w') as f:
            for i in self.d:
                f.write(i+'\n')
        
    def tC(self, delim:str ='\n'):     
        """
        ips to Clipboard
        """
        pyperclip.copy(self.tS(delim=delim))
        
    def tS(self, delim:str ='\n'):
        """
        ips toString
        """
        s = ''
        for i in self.d: s+= i+delim
        return s
    
    def append(self, ipr_list:list):
        self.d.append(ipr_list)
    
    def remove(self, ip:str):
        self.d.remove(ip)
        
       
    def __str__(self):
        return str(self.d)
    def __len__(self):
        return len(self.d)
