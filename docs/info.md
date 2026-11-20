<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

BIO-COLOR MINI is a simple digital optical intensity classifier designed for Tiny Tapeout.

The circuit receives an 8-bit digital intensity value through ui_in[7:0], representing a measurement from an external optical sensing and analog-to-digital conversion system.

It compares the input value against a fixed threshold of 128.

If the intensity is below 128, uo_out[0] is 0.

If the intensity is 128 or greater, uo_out[0] is 1.

The remaining output bits are set to zero. The design is combinational and does not require a clock.

This project demonstrates a basic digital processing block that could be integrated into a future colorimetric measurement system. It is not a standalone clinical diagnostic device.

## How to test

Apply an 8-bit intensity value to ui_in[7:0] and observe uo_out[0].

Example test cases:

Input intensity    Expected output
      0                  0
     50                  0
    127                  0
    128                  1
    200                  1
    255                  1

The threshold is 128. All 256 possible 8-bit input values have been tested in functional simulation.

The automated Cocotb testbench can also be executed through the repository's GitHub Actions test workflow.

## External hardware

List external hardware used in your project (e.g. PMOD, LED display, etc), if any
