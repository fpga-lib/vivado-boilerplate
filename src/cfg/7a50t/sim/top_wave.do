onerror {resume}
radix define DOUT {
    "'b0001" "SLON" -color "#FF0040",
    "'b0101" "S100" -color "#00FF80",
    -default binary
    -defaultcolor #008080
}
quietly WaveActivateNextPane {} 0
add wave -noupdate /top_tb/ref_clk_p
add wave -noupdate /top_tb/ref_clk_n
add wave -noupdate /top_tb/out
add wave -noupdate /top_tb/top_inst/clk
add wave -noupdate /top_tb/top_inst/pll_locked
add wave -noupdate /top_tb/top_inst/out
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {34095045 ps} 0} {{Cursor 2} {540943 ps} 0 Gold Salmon}
quietly wave cursor active 2
configure wave -namecolwidth 500
configure wave -valuecolwidth 148
configure wave -justifyvalue left
configure wave -signalnamewidth 0
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 3000
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ns
update
WaveRestoreZoom {105743 ps} {976143 ps}
