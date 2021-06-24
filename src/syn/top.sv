//-------------------------------------------------------------------------------
//
//     Project: Any
//
//     Purpose: Default top-level file
//
//
//-------------------------------------------------------------------------------

`include "cfg_params.svh"

`define WIDTH 4

module automatic top
(
`ifdef DIFF_REFCLK
    input  logic              ref_clk_p,
    input  logic              ref_clk_n,
`else                         
    input  logic              ref_clk,
`endif

    output logic [`WIDTH-1:0] out = 0
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
logic pll_locked;

//------------------------------------------------------------------------------
//
//    ILA debug
//
`ifdef TOP_ENABLE_ILA

(* mark_debug = "true" *) logic [`WIDTH-1:0] dbg_out;
(* mark_debug = "true" *) logic              dbg_pll_locked;

assign dbg_out        = out;
assign dbg_pll_locked = pll_locked;

`endif // TOP_DEBUG_ENABLE


//------------------------------------------------------------------------------
//
//    Functions and tasks
//

//------------------------------------------------------------------------------
//
//    Logic
//
always_ff @(posedge clk) begin
    if(pll_locked) begin
        out <= out + 1;
    end
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
