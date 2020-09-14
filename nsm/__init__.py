import sys
from .nsm import *
if (sys.version_info > (3, 0)):
        from .nsm3 import nsm3 as nsm
else:   
        from .nsm2 import nsm
if __name__=='__main__':
        main()
