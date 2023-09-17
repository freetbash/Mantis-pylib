def GenerateC(ip_prefix, begin, end) -> list :
    """
    GenerateC("192.168.0", 1, 255)-
    """
    return [ip_prefix+'.' + str(i) for i in range(begin, end)]
    