from t.all import *
import paramiko


def msp(tip:str):
    """
    modify ssh password
    password must be complex
    """
    a = tip.split(':')
    ip = a[0]
    port = int(a[1])
    print(f"[*] Changing the ssh password for the {tip}")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        s.connect(ip,port,mp.user,mp.dpwd)
        stdin, stdout, stderr = s.exec_command("passwd")
        stdin.write(mp.dpwd+'\n'+mp.pwd+'\n'+mp.pwd+'\n')
        out,err=stdout.read(),stderr.read()
        print(f"[+] {tip} ok!")
        s.close()
    except Exception as e:
        print(e)
        print(f"[-] chpasswd {tip}")
    
def mmsp(ips:ipr):
    """
    batch modify ssh password
    """
    print(f"[*] Changing the ssh password for the {ips}")
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(12) as executer:
        executer.map(msp, ips.d)
        
        

    