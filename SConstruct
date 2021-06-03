

import os
import sys

sys.dont_write_bytecode = True

#-------------------------------------------------------------------------------
#
#    Help info
#
help_info ="""
********************************************************************************     
    Available variants:
    ~~~~~~~~~~~~~~~~~~~
        ac701 (default)
        7a35t
        7a50t
     
    Usage:
    ~~~~~  
    scons [variant=<name>] [targets]
"""

Help(help_info)

#-------------------------------------------------------------------------------
#
#    General Settings
#

variant = ARGUMENTS.get('variant', 'ac701')

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

variant_path = os.path.join('src', 'cfg', variant, variant + '.scons')
if not os.path.exists(variant_path):
    print('\nError: unsupported variant: ', variant)
    print(help_info)
    sys.exit(-3)

SConscript(variant_path, exports='envx')
#-------------------------------------------------------------------------------

if 'dump' in ARGUMENTS:
    env_key = ARGUMENTS[ 'dump' ]
    if env_key == 'env':
        print( envx.Dump() )
    else:
        print( envx.Dump(key = env_key) )


#-------------------------------------------------------------------------------

