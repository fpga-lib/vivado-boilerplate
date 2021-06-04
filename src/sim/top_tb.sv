//-------------------------------------------------------------------------------
//
//     Project: Any
//
//     Purpose: Default testbench file
//
//
//-------------------------------------------------------------------------------

`include "cfg_params.svh"

`timescale 1ns/1ps

module top_tb;

localparam CLK_HALF_PERIOD = `CLK_HALF_PERIOD;
localparam WIDTH           = `WIDTH;
    
logic [WIDTH-1:0] out; 

`ifdef DIFF_REFCLK
logic ref_clk_p = 0;
logic ref_clk_n = 1;
`else
logic ref_clk = 0;
`endif

    
`ifdef DIFF_REFCLK
always begin
    #CLK_HALF_PERIOD
    ref_clk_p = ~ref_clk_p;
    ref_clk_n = ~ref_clk_n;
end
`else
always begin
    #CLK_HALF_PERIOD
     ref_clk = ~ref_clk;
end
`endif


initial begin
    #10us
    $display("\n%c[1;32m ******************** SIMULATION RUN FINISHED SUCCESSFULLY ********************%c[0m", 27, 27);
    $stop(2);   
end 

top top_inst
(
`ifdef DIFF_REFCLK
    .ref_clk_p ( ref_clk_p ),
    .ref_clk_n ( ref_clk_n ),
`else                        
    .ref_clk   ( ref_clk   ),
`endif

    .out       ( out       )
);

endmodule
//-------------------------------------------------------------------------------
