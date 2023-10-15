from IPython import start_ipython

from t.all import *
from d.all import *
from a.all import *

from m import *


banner = "\n\t._ _    _.  ._   _|_  o   _ \n\t| | |  (_|  | |   |_  |  _> \n\n"

def embed():
    start_ipython(
        display_banner=False,
        user_ns=globals(),
        exec_lines=["print(\"\"\"" + banner + "\"\"\")"]
    )