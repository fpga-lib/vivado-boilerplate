

import os
import sys
import subprocess
import re
import shutil

sys.dont_write_bytecode = True

from utils import *

#print(GetLaunchDir())

#-------------------------------------------------------------------------------
#
#    General Settings
#
#ip       = ['pcie']

variant = ARGUMENTS.get('variant', 'top')

print('variant:', variant)

#-------------------------------------------------------------------------------
#
#    Environment
#
env = Environment( tools = {} )



#-------------------------------------------------------------------------------
#
#    Project Structure
#

SConscript('src/cfg/top/top.scons', exports='env')



