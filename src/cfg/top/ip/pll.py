
from settings import params 

ip_type = 'clk_wiz'
 
ip_config = {}

ip_config['PRIMITIVE'                 ] = 'PLL'
ip_config['PRIM_IN_FREQ'              ] = params['REF_CLK_FREQ']
ip_config['CLKOUT1_REQUESTED_OUT_FREQ'] = params['CLK_FREQ']
ip_config['USE_LOCKED'                ] = True
ip_config['USE_RESET'                 ] = False
ip_config['USE_SAFE_CLOCK_STARTUP'    ] = True
 
 

