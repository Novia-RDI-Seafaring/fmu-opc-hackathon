## Lube Oil Cooling (LOC) FMU Description
This is the same system as LOC.fmu divided into two parts: Control and physical system. The inputs and outputs are described below.

### LOC_CNTRL.fmu
Control part of the LOC. The **Input signals** are: 
- `setpoint_temperature_lube_oil`: The setpoint temperature of the lube oil entering the engine.
- `temperature_lube_oil`: The temperature of the lube oil after being cooled.

**Output signals:**
- `control_valve_position`: The position of the control valve regulating the flow of lube oil through the cooler.

### LOC_SYSTEM.fmu
Physical system part of the LOC. The **Input signals** are: 
- `temperature_cold_circuit_inlet`: The temperature of the cooling water entering the lube oil cooler.
- `massflow_cold_circuit`: The mass flow rate of the cooling water through the circuit.
- `engine_load`: The current load on the engine, which can influence the heat generated.
- `control_valve_position`: The position of the control valve regulating the flow of lube oil through the cooler.

**Output signals:**
- `temperature_cold_circuit_outlet`: The temperature of the cooling water exiting the lube oil cooler.
- `massflow_cold_circuit_outlet`: The mass flow rate of the cooling water exiting the cooler.
- `temperature_lube_oil`: The temperature of the lube oil after being cooled.


