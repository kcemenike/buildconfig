from __future__ import print_function

import sys
import os

if sys.platform == 'darwin' and 'DISPLAY' in os.environ:
    import runpersistent_helpercmd
    runpersistent_helpercmd.sessioncmd = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'background-process-darwin.sh')
    from runpersistent_helpercmd import *
elif sys.platform == 'linux':
    import runpersistent_helpercmd
    runpersistent_helpercmd.sessioncmd = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'background-process-screen.sh')
    from runpersistent_helpercmd import *
else:
    raise NotImplementedError('no support for this platform')

