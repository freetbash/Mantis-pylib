class MP:
    """
    Mantis Project Object
    """
    user="ctf"
    dpwd="ctf"
    pwd="qazwsxcde123"
    
    def __str__(self):
        return str({
            "user":self.user,
            "dpwd":self.dpwd,
            "pwd":self.pwd
            })

mp=MP()
