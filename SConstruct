

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
#    Help info
#
Help("""
********************************************************************************     
Xilinx Vivado Non-Project Flow
    
    Available configurations:
    ~~~~~~~~~~~~~~~~~~~~~~~~ 
        top (default)
        slon
        ac701
        all
     
    Usage:
    ~~~~~  
    scons [cfg=<cfg-name>] [targets]
"""
)

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
envNpf = Environment() #( tools = {} )


#-------------------------------------------------------------------------------
#
#    Project Structure
#

SConscript('src/cfg/top/top.scons', exports='envNpf')

