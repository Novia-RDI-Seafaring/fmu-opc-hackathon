## Model Exchange vs. Co-Simulation FMU
**NOTE**: This summary was generated by gpt4o based on information found [here](https://modelon.com/blog/fmi-functional-mock-up-unit-types/) and should thus be verified. 

| Criteria                   | Model Exchange (ME)                        | Co-Simulation (CS)                           |
|----------------------------|-------------------------------------------|----------------------------------------------|
| **Solver Requirements**    | Requires external solver                  | Includes its own solver                      |
| **Use Case**               | Tight integration with host simulation tool | Decoupled simulation of individual components|
| **Solver Control**         | Host tool controls the numerical integration | FMU controls the numerical integration       |
| **Time Step Management**   | Host tool determines the time steps       | FMU determines its own time steps            |
| **Performance Considerations** | Potentially faster if host solver is optimized | Might be slower due to overhead of embedded solver |
| **Coupling**               | Suitable for tightly coupled systems      | Suitable for loosely coupled systems         |
| **Flexibility**            | More flexibility in solver choice and tuning | Easier setup, especially with complex or legacy models |
| **Application Examples**   | Real-time simulations requiring precise solver control | Multi-domain simulations, hardware-in-the-loop (HIL) |
| **Complexity**             | Requires more detailed integration setup  | Easier to integrate as a black-box component  |
| **Output**             | the time derivatives of the continuous-time state variables | the new values of the state variables after time integration |

**Key Points to Consider:**
- **Model Exchange (ME)**: Best used when you need tight integration with the host tool's solver, offering more control over the simulation process and potentially better performance if the host solver is highly optimized. This approach is ideal for scenarios where the simulation requires precise control over time steps and solver settings, such as real-time simulations and applications with stringent accuracy requirements.
- **Co-Simulation (CS)**: Ideal for scenarios where different parts of a system are simulated in different tools, each with its own solver. This method simplifies the integration of complex or legacy models and is well-suited for multi-domain simulations or applications involving hardware-in-the-loop (HIL) testing. Co-simulation is beneficial when components of a system need to be simulated at different time steps or when decoupling the solver from the host tool can reduce complexity.

For detailed use cases and further information, you can refer to the [Modelon blog on FMI types](https://modelon.com/blog/fmi-functional-mock-up-unit-types/).
or https://www.iea-annex60.org/finalReport/activity_1_2.html