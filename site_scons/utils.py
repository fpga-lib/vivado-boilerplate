#*******************************************************************************
#*
#*    Build support utilities
#*
#*    Version 1.0
#*
#*    Copyright (c) 2016-2021, Harry E. Zhurov
#*
#*******************************************************************************

import os
import sys
import subprocess
import re
import glob
import yaml

from SCons.Script import *

#-------------------------------------------------------------------------------
# 
# 
# 
def namegen(fullpath, ext):
    basename = os.path.basename(fullpath)
    name     = os.path.splitext(basename)[0]
    return name + os.path.extsep + ext
#-------------------------------------------------------------------------------
def pexec(cmd, wdir = os.curdir):
    p = subprocess.Popen(cmd.split(),
                         cwd = wdir,
                         universal_newlines = True,
                         stdin    = subprocess.PIPE,
                         stdout   = subprocess.PIPE,
                         stderr   = subprocess.PIPE,
                         encoding = 'utf8')

    while True:
        out = p.stdout.readline()    
        if len(out) == 0 and p.poll() is not None:
            break
        if out:
            print(out.strip())

    rcode = p.poll()
    return rcode
    
#-------------------------------------------------------------------------------
def clog2(n: int) -> int:
    if n < 1:
        raise ValueError("expected argument value >= 1")
    res     = 0
    shifter = 1
    while n > shifter:
        shifter <<= 1
        res      += 1
    return res
#-------------------------------------------------------------------------------
def max_str_len(x):
    return len(max(x, key=len))
#-------------------------------------------------------------------------------
class Dict2Class(object):

    def __init__(self, in_dict, name=''):
        
        self.data = in_dict
        self.name = name

        for key in in_dict:
            setattr(self, key, in_dict[key])
            
    def get_data(self):
        return [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
            
#-------------------------------------------------------------------------------
def eval_cfg_dict(cfg_dict: dict, imps=None) -> dict:
    
#   print('\n>>>>>>>>>>>>>>')
#   print('cfg_dict:', cfg_dict)
#   print('imps:',imps)
#   print('<<<<<<<<<<<<<<\n')

    if imps:               # deflating imported parameters
        for i in imps:
            var = i
            exec( var + ' = ' + 'Dict2Class(imps[i], var)' )
        
    for key in cfg_dict:
        var = key
        exec(var + '= cfg_dict[key]')

    for key in cfg_dict:
        if type(cfg_dict[key]) == str:
            if cfg_dict[key][0] == '=':
                cfg_dict[key] = eval(cfg_dict[key][1:])            # evaluate new dict value
                if type(cfg_dict[key]) == str:
                    exec(key + ' = "' + str(cfg_dict[key]) + '"')  # update local variable
                else:
                    exec(key + ' = ' + str(cfg_dict[key]))         # update local variable
                
    return cfg_dict

#-------------------------------------------------------------------------------
def read_config(fn: str, param_sect='parameters', search_root=''):

    #print('read config:', fn)
    
    #print('read_config working path:', os.path.abspath(os.curdir))
    
    fname = os.path.basename(fn)
    
    if os.path.exists(fn):
        full_path = str.split(fn)
    else:
        full_path = glob.glob( os.path.join(search_root, '**', fname) )
    
    if not len(full_path):
        print('E: config file not found:', fn)
        sys.exit(1)
    
    if len(full_path) > 1:
        print('E: duplicate config files:', full_path)
        sys.exit(1)
    
    with open( full_path[0] ) as f:
        cfg = yaml.safe_load(f)

    imps = {}
    if 'import' in cfg:
        imports = cfg['import'].split()

        for i in imports:
            imp_fn = i + '.yml'                         # file name of imported data
            imps[i] = read_config(imp_fn, search_root=search_root)
           # print('read ', imp_fn, ':', imps[i])
                
    params = cfg[param_sect]
    params = eval_cfg_dict(params, imps)

    return params

#-------------------------------------------------------------------------------
def import_config(fn: str):
    return Dict2Class( read_config(fn) )
#-------------------------------------------------------------------------------
def read_ip_config(fn, param_sect, search_root=''):

    cfg_params = read_config(fn, param_sect, search_root)
    
    with open( fn ) as f:
        cfg = yaml.safe_load(f)
        
    ip_cfg = {}
    ip_cfg['type']     = cfg['type']
    ip_cfg[param_sect] = cfg_params
        
    return ip_cfg

#-------------------------------------------------------------------------------
def generate_title(text: str, comment: str) -> str:
    
    hsep_len = 80 - len(comment)
    
    empty_line   = comment + '*' + os.linesep
    title_header = comment + '*'*hsep_len + os.linesep + empty_line

    title_body = comment + '*' +  (4 - len(comment))*' '
    
    title_footer = empty_line + comment + '-'*hsep_len + os.linesep
    
    lines = text.split(os.linesep)
    out = title_header
    for line in lines:
        out += title_body+ line + os.linesep
        
    out += title_footer + os.linesep
    
    return out

#-------------------------------------------------------------------------------
def generate_footer(comment: str) -> str:

    hsep_len = 80 - len(comment)

    empty_line = ' ' + os.linesep
    separator  = comment + '*'*hsep_len + os.linesep

    return  empty_line + separator
#-------------------------------------------------------------------------------
def get_ip_name(node, suffix):
    
    if type(node) != str:
        path = str(node[0])
    name = os.path.split(path)[1]
    ip_name = name.replace(suffix, '')
    
    return ip_name
#-------------------------------------------------------------------------------
def create_dirs(dirs):
    for i in dirs:
        if not os.path.exists(i):
            Execute( Mkdir(i) )
    
#-------------------------------------------------------------------------------

