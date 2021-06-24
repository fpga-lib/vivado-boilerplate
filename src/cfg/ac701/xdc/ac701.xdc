#-------------------------------------------------------------------------------
#   project:       vivado-bullet
#   cfg:           xilinx_AC701
#
#   description:   slon5 start-up
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 3.3 [current_design]

#-------------------------------------------------------------------------------
#    Clocks
#-------------------------------------------------------------------------------

create_clock -period $REF_CLK_PERIOD [get_ports ref_clk_p]

#set_property -dict {PACKAGE_PIN E3 IOSTANDARD LVCMOS33} [get_ports ref_clk]
set_property PACKAGE_PIN R3 [get_ports ref_clk_p]
set_property PACKAGE_PIN P3 [get_ports ref_clk_n]
set_property IOSTANDARD LVDS_25 [get_ports ref_clk_p]
set_property IOSTANDARD LVDS_25 [get_ports ref_clk_n]

# EMCCLK
#set_property PACKAGE_PIN P16 [get_ports emcclk]
#set_property IOSTANDARD LVCMOS33 [get_ports emcclk]

set_switching_activity -deassert_resets

#-------------------------------------------------------------------------------
#    dnum: mapped to user leds
#-------------------------------------------------------------------------------
set_property PACKAGE_PIN R26   [get_ports {out[3]}]
set_property PACKAGE_PIN T25   [get_ports {out[2]}]
set_property PACKAGE_PIN T24   [get_ports {out[1]}]
set_property PACKAGE_PIN M26   [get_ports {out[0]}]

set_property IOSTANDARD LVCMOS33 [get_ports {out}]

set_property BITSTREAM.CONFIG.EXTMASTERCCLK_EN DIV-1 [current_design]
set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]
set_property BITSTREAM.CONFIG.SPI_FALL_EDGE YES [current_design]
set_property CONFIG_MODE SPIx4 [current_design]
