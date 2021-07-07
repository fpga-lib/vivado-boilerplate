#------------------------------------------------------------------------------
#
#       Project:        Any
#
#       Description:    Display summary reports
#
#       Author:         Harry E. Zhurov
#
#------------------------------------------------------------------------------

import os
import re
from tabulate import tabulate
from utils    import *


#-------------------------------------------------------------------------------
#
#   Timing report
#
def timing_report(env):
    slack_pattern = 'Design Timing Summary[^$]+WNS\(ns\)\s+TNS\(ns\)\s+.+WHS\(ns\)\s+THS\(ns\).+\n[\s\-]+([0-9\.]+)\s+([0-9\.]+)\s+([0-9\.]+)\s+([0-9\.]+)\s+([0-9\.]+)\s+([0-9\.]+)\s+'

    filepath = os.path.join(env['BUILD_SYN_PATH'], env['VIVADO_PROJECT_NAME'] + '.runs', 'impl_1', env['TOP_NAME'] + '_final_timing.rpt')
    if not os.path.exists(filepath):
        print( colorize('Timing Summary Report file does not exist', 'yellow', True) )
        return
        
    with open(filepath) as fn:
        contents = fn.read()
        
                
    columns  = ['WNS, ns', 'TNS, ns', 'WHS, ns', 'THS, ns']
    res = re.search(slack_pattern, contents)
    slacks = []
    if res:
        slacks.append([colorize(str(i), 'red', True) for i in res.groups()])
        del slacks[0][2:4]
        
    out = str(tabulate(slacks, headers = [colorize(c, 'cyan', True) for c in columns], tablefmt='plain', stralign='left'))
    print('-'*60)
    print(' '*20, colorize('Timing', 'blue', True), os.linesep)
    print(out)

#-------------------------------------------------------------------------------
#
#
#
def utilization_report(env):
    
    patterns = { 
        'CLB'             : '\|\s+CLB\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'Slice'           : '\|\s+Slice\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'CLB LUT'         : '\|\s+CLB LUTs\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'Slice LUT'       : '\|\s+Slice LUTs\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        '  LUT Logic'     : '\|\s+LUT as Logic\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        '  LUT RAM'       : '\|\s+LUT as Memory\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'CLB Registers'   : '\|\s+CLB Registers\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'Slice Registers' : '\|\s+Slice Registers\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        '  FF'            : '\|\s+Register as Flip Flop\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        '  LATCH'         : '\|\s+Register as Latch\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'BUFG'            : '\|\s+GLOBAL CLOCK BUFFERs\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'BUFGCTRL'        : '\|\s+BUFG.*\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'PLL'             : '\|\s+PLL.+\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'MMCM'            : '\|\s+MMCM.+\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'I/O'             : '\|\s+Bonded IOB\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|',
        'GT'              : '\|\s+GT.+CHANNEL\s+\|\s+(\d+)\s+\|\s+\d+\s+\|\s+(\d+)\s+\|\s+([<0-9\.]+)\s+\|'
    }
        
    filepath = os.path.join(env['BUILD_SYN_PATH'], env['VIVADO_PROJECT_NAME'] + '.runs', 'impl_1', env['TOP_NAME'] + '_final_utilization.rpt')
    if os.path.exists(filepath):
        with open(filepath) as fn:
            contents = fn.read()
    else:
        print( colorize('Final Utilization Report file does not exist', 'yellow', True) )
        return
        
    out = []
    for k in patterns:
        res = re.search(patterns[k], contents)
        if res:
            vals = [colorize(str(i), 'red', True) for i in res.groups()]
            out.append([colorize(k, 'white', True)] + vals)
        
    color   = 'cyan'
    columns = ['Resource', 'Used', 'Available', 'Utilization %']
            
    print('-'*60)
    print(' '*20, colorize('Utilization', 'blue', True), os.linesep)
    print(tabulate(out, headers=[colorize(c, color, True) for c in columns], tablefmt='plain', stralign='left'))
    print('')

#-------------------------------------------------------------------------------
#    
#   Log file filter 
#    
def log_file_filter(env):
    syn_logpath  = os.path.join(env['BUILD_SYN_PATH'], env['VIVADO_PROJECT_NAME'] + '.runs', 'synth_1', 'runme.log')
    impl_logpath = os.path.join(env['BUILD_SYN_PATH'], env['VIVADO_PROJECT_NAME'] + '.runs', 'impl_1',  'runme.log')
    
    warn_pattern      = '(WARNING:)(.+)'
    crit_warn_pattern = '(CRITICAL WARNING:)(.+)'
    synlog  = ''
    impllog = ''

    if os.path.exists(syn_logpath):
        with open(syn_logpath, 'r') as lfile:
            synlog = lfile.read()
            
    if os.path.exists(impl_logpath):
        with open(impl_logpath, 'r') as lfile:
            impllog = lfile.read()
            
            
    syn_warn       = re.findall( warn_pattern,      synlog  )
    syn_crit_warn  = re.findall( crit_warn_pattern, synlog  )
    impl_warn      = re.findall( warn_pattern,      impllog )
    impl_crit_warn = re.findall( crit_warn_pattern, impllog )
    
    return syn_warn, syn_crit_warn, impl_warn, impl_crit_warn
    
#-------------------------------------------------------------------------------
def warning_report(env, opt='all'):
    syn_warn, syn_crit_warn, impl_warn, impl_crit_warn = log_file_filter(env)
    
    if 'syn' in opt or 'all' in opt:
        for w in syn_warn:
            print( colorize(w[0], 'yellow'), w[1] )
        for cw in syn_crit_warn:
            print( colorize(cw[0], 'yellow'), cw[1] )

    if 'impl' in opt or 'all' in opt:
        for w in impl_warn:
            print( colorize(w[0], 'yellow'), w[1] )
        for cw in impl_crit_warn:
            print( colorize(cw[0], 'yellow'), cw[1] )

    color   = 'cyan'
    columns = ['Message Type', 'Synthesis', 'Implementation']

    warn      = [colorize('Warnings',          'yellow'), colorize(str(len(syn_warn))     , 'red', True) , colorize(str(len(impl_warn)),      'red', True)] 
    crit_warn = [colorize('Critical Warnings', 'yellow'), colorize(str(len(syn_crit_warn)), 'red', True) , colorize(str(len(impl_crit_warn)), 'red', True)] 

    print('')
    print('-'*60)
    print(' '*20, colorize('Messages', 'blue', True), os.linesep)
    print(tabulate([warn, crit_warn], headers=[colorize(c, color, True) for c in columns], tablefmt='plain', stralign='left'))
    print('-'*60)
    print('')
    
#-------------------------------------------------------------------------------
    
