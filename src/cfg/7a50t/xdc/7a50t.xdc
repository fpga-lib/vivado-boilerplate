#-------------------------------------------------------------------------------
#   project:       vivado-boilerplate
#   cfg:           7a50t
#
#   description:   
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 3.3 [current_design]

#-------------------------------------------------------------------------------
#    ref_clk
#-------------------------------------------------------------------------------

#create_clock -period $REF_CLK_PERIOD [get_ports ref_clk]

set_property -dict {PACKAGE_PIN N11 IOSTANDARD LVCMOS33} [get_ports ref_clk]
set_switching_activity -deassert_resets

#-------------------------------------------------------------------------------
#    dnum
#-------------------------------------------------------------------------------
set_property PACKAGE_PIN M1  [get_ports {out[3]}]
set_property PACKAGE_PIN N1  [get_ports {out[2]}]
set_property PACKAGE_PIN M2  [get_ports {out[1]}]
set_property PACKAGE_PIN N2  [get_ports {out[0]}]

set_property IOSTANDARD LVCMOS33 [get_ports {out}]
#set_property IOB TRUE [get_ports {dnum}]


