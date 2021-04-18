

ip_type = 'pcie_7x'

#-------------------------------------------------------------------
#
#   General
#
params['Device_Port_Type'    ] = 'PCI_Express_Endpoint_device'
params['Interface_Width'     ] = '64_bit'
params['Maximum_Link_Width'  ] = 'X' + cfg_params[LINK_WIDTH]
params['Link_Speed'          ] = cfg_params[LINK_SPEED]+'_GT/s'
params['Ref_Clk_Freq'        ] = '100_MHz'
                             
params['pipe_mode_sim'       ] = 'Enable_Pipe_Simulation'
params['pipe_sim'            ] = True
                             ] =
params['mode_selection'      ] = 'Advanced'
params['PCIe_Debug_Ports'    ] = False                               # disable DRP
                             
params['Xlnx_Ref_Board'      ] = 'AC701'
                             
params['Extended_Tag_Default'] = True
params['Extended_Tag_Field'  ] = True

#-------------------------------------------------------------------
#
#   IDs
#
#CONFIG.Device_ID      7024

#-------------------------------------------------------------------
#
#   BAR0
#
params['Bar0_64bit'       ] =  False
params['Bar0_Enabled'     ] =  True
params['Bar0_Prefetchable'] =  False
params['Bar0_Scale'       ] =  'Kilobytes'
params['Bar0_Size'        ] =  2
params['Bar0_Type'        ] =  'Memory'

#-------------------------------------------------------------------
#
#   BAR3
#
params['Bar3_64bit'       ] = True
params['Bar3_Enabled'     ] = True
params['Bar3_Prefetchable'] = False
params['Bar3_Scale'       ] = 'Kilobytes'
params['Bar3_Size'        ] = 16
params['Bar3_Type'        ] = 'Memory'

#-------------------------------------------------------------------
#
#   Resources
#
params['Max_Payload_Size' ] = cfg_params['PCIE_MPS']+'_bytes'
params['Perf_Level'       ] = 'High'
params['Buf_Opt_BMA'      ] = True

#-------------------------------------------------------------------
#
#   Interrupts
#
params['MSI_64b'                 ] = True
params['MSI_Enabled'             ] = True
params['Multiple_Message_Capable'] = '1_vector'

