import os, pkgutil
__all__ = list(module for _, module, _ in pkgutil.iter_modules([os.path.dirname(__file__)]))
print("loaded modules " + str(__all__))
