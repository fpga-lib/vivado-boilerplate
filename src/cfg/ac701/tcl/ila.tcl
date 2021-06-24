
puts "\n------->>> Add net to debug probes <<<-------"

create_debug_core ila_core ila
set_property ALL_PROBE_SAME_MU true [get_debug_cores ila_core]
set_property ALL_PROBE_SAME_MU_CNT 1 [get_debug_cores ila_core]
set_property C_ADV_TRIGGER false [get_debug_cores ila_core]
set_property C_DATA_DEPTH 1024 [get_debug_cores ila_core]
set_property C_EN_STRG_QUAL false [get_debug_cores ila_core]
set_property C_INPUT_PIPE_STAGES 0 [get_debug_cores ila_core]
set_property C_TRIGIN_EN false [get_debug_cores ila_core]
set_property C_TRIGOUT_EN false [get_debug_cores ila_core]
set_property port_width 1 [get_debug_ports ila_core/clk]

connect_debug_port ila_core/clk [get_nets -hier -filter {NAME =~ *pll_inst/inst/clk_out1}]

#-------------------------------------------------------------------------------
#
#    Top module
#
if { $TOP_ENABLE_ILA } {
    net2probe ila_core [get_nets -hier -filter {NAME =~ dbg_out[*]}]
    net2probe ila_core [get_nets -hier -filter {NAME =~ dbg_pll_locked}]
}
puts "-----------------------------------------------\n"


