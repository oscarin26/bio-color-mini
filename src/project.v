/*
 * BIO-COLOR MINI
 * Digital optical intensity classifier
 * Tiny Tapeout - GlobalFoundries
 */

`default_nettype none

module tt_um_bio_color_mini (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    // Clasificador de intensidad optica
    wire resultado;

    assign resultado = (ui_in >= 8'd128);

    // Solo utilizamos el bit 0 de salida
    assign uo_out = {7'b0000000, resultado};

    // No utilizamos los pines bidireccionales
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Entradas no utilizadas en este diseno
    wire _unused = &{uio_in, ena, clk, rst_n};

endmodule

`default_nettype wire
