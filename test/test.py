
# SPDX-FileCopyrightText: © 2026 BIO-COLOR MINI
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_bio_color_mini(dut):

    dut._log.info("Iniciando prueba exhaustiva BIO-COLOR MINI")

    # Inicializar entradas no utilizadas
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 1
    dut.uio_in.value = 0

    # Comprobar todas las entradas de 8 bits
    for intensidad in range(256):

        dut.ui_in.value = intensidad

        # Permitir que se estabilice la lógica combinacional
        await Timer(10, unit="ns")

        esperado = 1 if intensidad >= 128 else 0
        obtenido = int(dut.uo_out.value) & 1

        assert obtenido == esperado, (
            f"ERROR: intensidad={intensidad}, "
            f"obtenido={obtenido}, esperado={esperado}"
        )

        # Verificar también las salidas no utilizadas
        assert int(dut.uo_out.value) >> 1 == 0
        assert int(dut.uio_oe.value) == 0
        assert int(dut.uio_out.value) == 0

    dut._log.info("PASS: 256 DE 256 PRUEBAS SUPERADAS")
