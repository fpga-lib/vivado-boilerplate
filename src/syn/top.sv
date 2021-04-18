//-------------------------------------------------------------------------------
//
//     Project: Any
//
//     Purpose: Default top-level file
//
//
//-------------------------------------------------------------------------------

//`include "cfg_params_generated.svh"

`define WIDTH 4

`define DIFF_REFCLK

module automatic top
(
`ifdef DIFF_REFCLK
    input  logic              ref_clk_p,
    input  logic              ref_clk_n,
`else                         
    input  logic              ref_clk,
`endif

    output logic [`WIDTH-1:0] out
);

//------------------------------------------------------------------------------
//
//    Settings
//

//------------------------------------------------------------------------------
//
//    Types
//

//------------------------------------------------------------------------------
//
//    Objects
//
`ifdef DIFF_REFCLK
logic ref_clk;
`endif

logic clk;

//------------------------------------------------------------------------------
//
//    Functions and tasks
//

//------------------------------------------------------------------------------
//
//    Logic
//
always_ff @(posedge clk) begin
    out <= out + 1;
end

//------------------------------------------------------------------------------
//
//    Instances
//
`ifdef DIFF_REFCLK
IBUFDS diff_clk_200
(
    .I  ( ref_clk_p ),
    .IB ( ref_clk_n ),
    .O  ( ref_clk   )
);
`endif
//------------------------------------------------------------------------------
pll pll_inst
(
    .clk_in1  ( ref_clk    ),
    .clk_out1 ( clk        ),
    .locked   ( pll_locked )
);

endmodule
//-------------------------------------------------------------------------------
