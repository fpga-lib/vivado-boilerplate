

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
    
    Available variants:
    ~~~~~~~~~~~~~~~~~~~~~~~~ 
        ac701 (default)
        7a35t
        7a50t
     
    Usage:
    ~~~~~  
    scons [variant=<name>] [targets]
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
envx['ENV']['PATH'] = os.environ['PATH']


#-------------------------------------------------------------------------------
#
#    Project configurations
#

SConscript('src/cfg/ac701/ac701.scons', exports='envx')
#-------------------------------------------------------------------------------

if 'dump' in ARGUMENTS:
    env_key = ARGUMENTS[ 'dump' ]
    if env_key == 'env':
        print( envx.Dump() )
    else:
        print( envx.Dump(key = env_key) )


#-------------------------------------------------------------------------------

