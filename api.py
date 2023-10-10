from a.all import *
from d.all import *
from m import *

from IPython import start_ipython

banner = "\n\t._ _    _.  ._   _|_  o   _ \n\t| | |  (_|  | |   |_  |  _> \n\n"

def embed():
    start_ipython(
        display_banner=False,
        user_ns=globals(),
        exec_lines=["print(\"\"\"" + banner + "\"\"\")"]
    )