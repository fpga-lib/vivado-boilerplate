

import os
import sys

sys.dont_write_bytecode = True

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

variant = ARGUMENTS.get('variant', 'top')

print('variant:', variant)

#-------------------------------------------------------------------------------
#
#    Environment
#
envx = Environment() #( tools = {} )


#-------------------------------------------------------------------------------
#
#    Project configurations
#

SConscript('src/cfg/top/top.scons', exports='envx')
#-------------------------------------------------------------------------------

if 'dump' in ARGUMENTS:
    env_key = ARGUMENTS[ 'dump' ]
    if env_key == 'env':
        print( envx.Dump() )
    else:
        print( envx.Dump(key = env_key) )


#-------------------------------------------------------------------------------

