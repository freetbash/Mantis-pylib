def help():
    print("""
a:
    ip:
        gip
            gip("192.168.0.{}", 1, 255)
        pip
            pip("192.168.0.103", 4001, 4010)
        lpip
            lpip(ipr, 80)
        lhip
            lhip(ipr, "https")
        it
            it("ip.txt")  
        cw
            cw("http://127.0.0.1", "/ok")  
        cwt
            cwt(ipr, "/ok")  
    flag:
        sf
            sf("flag{asd}", swfc, **payloads)  
        msf
            msg(ipr, swfc, **payloads)  
        swfc
            it is built-in function to submit a flag to webserver
        gf
            gf(target, gwfc, **payloads)
        mgf
            mgf(ipr, gwfc, **payloads)
        gwfc      
            it is built-in function to get a flag from webserver

d:
    password:
          msp
            msp("192.168.0.23:22")
                it is use mp.dpwd and pwd
          mmsp
            mmsp(ipr)
object:
    ipr
        tF() toFile
        tC() toClipboard
        tS() toString
        append(i)
        remove(i)
    MP
        user
        dpwd
        pwd
                
help(obj) for more information
""")