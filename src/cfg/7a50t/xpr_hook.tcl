#--------------------------------------------------------------------------------
#
#     Project:     Any
#
#     Description: Xilinx AC701 Vivado Project settings
#
#     Author:      Harry E. Zhurov
#
#--------------------------------------------------------------------------------

source $BUILD_SRC_DIR/cfg_params.tcl

#-------------------------------------------------------------------------------
#
#    Custom tool settings
#

set synth_strategy Flow_AreaOptimized_high

if { ${BASE_CLK} > 150 } {
    set impl_strategy  Performance_ExploreWithRemap
} else {
    set impl_strategy  {Vivado Implementation Defaults}
}

if { ${VERBOSE} } {
    puts ""
    puts "    Synthesis strategy:  ${synth_strategy}"
    puts "    P&R strategy:        ${impl_strategy}"
    puts ""
}

set_property strategy ${synth_strategy} [get_runs synth_1]

set_property STEPS.PHYS_OPT_DESIGN.IS_ENABLED true [get_runs impl_1]
set_property strategy ${impl_strategy}             [get_runs impl_1]

#-------------------------------------------------------------------------------
#
#    Set constraint files only for P&R state for out-of-context IPs 
#    that are black boxes at synthesis stage
#
set ip_ooc [get_files {*ip_ooc.xdc}]

foreach f $ip_ooc {
    if { [file exists $f] == 1 } {
        common::send_msg_id "CFG_PRJ 01-001" "INFO" "Clear 'Used in Synthesis' flag for file '$f'"
        set_property USED_IN_SYNTHESIS false $f
    } else {
        puts "No file " $f
    }    
}
#-------------------------------------------------------------------------------
#
#    Set constraint files only for P&R state for out-of-context IPs 
#    that are black boxes at synthesis stage
#
set impl_xdc [get_files {*_impl.xdc}]

foreach f $impl_xdc {
    if { [file exists $f] == 1 } {
        common::send_msg_id "CFG_PRJ 01-002" "INFO" "Clear 'Used in Synthesis' flag for file '$f'"
        set_property USED_IN_SYNTHESIS false $f
    } else {
        puts "No file " $f
    }    
}
#-------------------------------------------------------------------------------
#
#    Set message rules
#
common::send_msg_id "CFG_PRJ 02-001" "INFO" "Add message rules"

#---------------------------------------
#
#  XPM
#
set_msg_config -id "Synth 8-3331" -regexp -string [list ".+design xpm_.+ has unconnected port.+"]                                               -suppress
set_msg_config -id "Synth 8-6104" -regexp -string [list ".+Input port 'value' has an internal driver.+data/ip/xpm/xpm_fifo/hdl/xpm_fifo.sv.+"]  -suppress
set_msg_config -id "Synth 8-6014" -regexp -string [list ".+Unused sequential element.+was removed.+data/ip/xpm/xpm_fifo/hdl/xpm_fifo.sv.+"]     -suppress
set_msg_config -id "Synth 8-6014" -regexp -string [list ".+Unused sequential element.+was removed.+data/ip/xpm/xpm_memory/hdl/xpm_memory.sv.+"] -suppress
set_msg_config -id "Synth 8-6014" -regexp -string [list ".+Unused sequential element.+was removed.+data/ip/xpm/xpm_cdc/hdl/xpm_cdc.sv.+"]       -suppress
set_msg_config -id "Synth 8-3332" -regexp -string [list ".+Sequential element.+is unused and will be removed from module xpm_fifo_base.+"]      -suppress


#---------------------------------------
#
#  Memory generating 
#
set_msg_config -id "Synth 8-5856" -string "3D RAM m_data_reg  for this pattern/configuration is not supported. This will most likely be implemented in registers" -suppress
set_msg_config -id "Synth 8-4767" -string "Trying to implement RAM 'ram_reg' in registers. Block RAM or DRAM implementation is not possible; see log for reasons" -suppress

#-------------------------------------------------------------------------------

