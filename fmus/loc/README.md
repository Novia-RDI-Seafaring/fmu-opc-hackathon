## Lube Oil Cooling (LOC) FMU Description
The *control valve* controls the *lubrication oil temperature* at a constant *setpoint* at the engine inlet using a PI controller. The lube oil cooler transfers heat from the lubrication oil to the cooling water circuit. An illustration of the `LOC.fmu` model is given below.

![Lube oil cooling system](https://raw.githubusercontent.com/Novia-RDI-Seafaring/fmu-opc-hackathon/448139ed5be242f642801508d2f360dcb7232fa6/fmus/loc/LOC.drawio.svg)

### Parameters, Input, and Output Signal Descriptions
The **input signals** are the following:
- `temperature_cold_circuit_inlet`: The temperature of the cooling water entering the lube oil cooler.
- `massflow_cold_circuit`: The mass flow rate of the cooling water through the circuit.
- `engine_load`: The current load on the engine, which can influence the heat generated.
- `setpoint_temperature_lube_oil`: The setpoint temperature of the lube oil entering the engine.

The **output signals** are the following:
- `temperature_cold_circuit_outlet`: The temperature of the cooling water exiting the lube oil cooler.
- `massflow_cold_circuit_outlet`: The mass flow rate of the cooling water exiting the cooler.
- `temperature_lube_oil`: The temperature of the lube oil after being cooled.
- `control_valve_position`: The position of the control valve regulating the flow of lube oil through the cooler.

Descriptions of all parameters, input, and output signals, together with typical value ranges, can be found in the [io_specification.json](https://github.com/Novia-RDI-Seafaring/fmu-opc-hackathon/blob/main/fmus/loc/io_specification.json).

## Exporting FMU from Simulink
The FMU `LOC.fmu` was exported from the Simulink model `LOC.slx` using MATLAB 2024a and the [FMU Builder for Simulink tool](https://www.mathworks.com/products/fmubuilder.html). The following MATLAB toolboxes are required for exporting the model:
- Simulink Compiler

## Testing the FMU
The FMU can be simulated/tested with the [`fmpy.gui`](https://fmpy.readthedocs.io/en/latest/tutorial/). 

### Simulation parameters

The output interval has to be specified and as an input file a time series of the inputs in `.csv` file has to be provided. Example input file (`LOC_in.csv`) uploaded here.

### Results with the LOC_in.csv and stop time of 2000
![results of the simulation](https://iili.io/JQSIwlV.md.png)

## TODO
- Review I/O and parameter names in FMU
- Define internal variables for simulation
- Add units and descriptions to signals in FMU


