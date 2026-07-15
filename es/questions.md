**1. a)** During peak traffic on a rainy day, a vehicle equipped with ABS encounters sudden braking at 80 km/h. The road surface is slippery, and the system must adapt to prevent skidding while ensuring stopping efficiency. Propose an ABS embedded system design for this scenario, highlighting its key components and their roles. **[7]**

**b)** Embedded Systems are everywhere, but you rarely see them. Justify this statement with suitable example. **[8]**

**2. a)** Compare and contrast DSPs and Microcontrollers in the context of embedded system use cases. Highlight scenarios where each would be more suitable. **[7]**

**b)** Discuss about AMBA bus architecture standards: AHB and APB. Explain their respective roles in system integration and performance optimization within embedded systems. Provide a block diagram to illustrate a typical SoC bus hierarchy. **[8]**

**3. a)** Explain the concept of priority inversion in an RTOS. Illustrate how it can occur and critically evaluate the effectiveness of priority inheritance and priority ceiling protocols in mitigating it. **[7]**

**b)** Consider a real-time embedded system controlling a robotic arm, which performs three periodic tasks. **[8]**

| Task                   | Execution Time (C) | Period (T) | Deadline (D) |
| ---------------------- | ------------------ | ---------- | ------------ |
| T1 – Sensor Sampling   | 1 ms               | 4 ms       | 4 ms         |
| T2 – Motor Control     | 1.5 ms             | 5 ms       | 5 ms         |
| T3 – Telemetry Logging | 2 ms               | 10 ms      | 10 ms        |

&nbsp;&nbsp;&nbsp;i. Check whether these tasks are schedulable using Earliest Deadline First (EDF) Scheduling.
&nbsp;&nbsp;&nbsp;ii. If yes, apply Rate Monotonic Scheduling and Earliest Deadline First Scheduling to schedule these tasks.

**4. a)** A rural farming cooperative deploys an IoT-based smart agriculture system with battery-powered sensor nodes, a local edge gateway, and cloud analytics. As an embedded systems engineer, propose a suitable Cloud–Edge–Device architecture for this application. Explain the roles of each layer and how data flows between them. **[8]**

**b)** Explain in detail about Bare Metal Programming along with startup code and linker script used in ARM Cortex-M3 programming. Highlight memory mapping and initialization steps. **[7]**

**OR**

Explain the interrupt masking mechanism using BASEPRI, PRIMASK, and FAULTMASK with example scenarios.

**5. a)** Evaluate the statement: "Good embedded software is not just about meeting functional requirements, but also about maintainability." Discuss the role of modularity, abstraction, and version control in achieving long-term software maintainability. **[7]**

**b)** How do design patterns improve embedded software quality? Using the Finite State Machine (FSM) pattern, explain how it simplifies the implementation of a complex control system compared to a monolithic procedural approach. **[8]**

**6. a)** Describe the data transmission sequence in I2C from start to stop condition. Explain common sleep modes in low power design. **[7]**

**b)** Explain different Driver Testing and Validation Techniques. What is the role of a low-level driver in embedded systems? Explain how an ISR improves efficiency and power consumption. **[8]**

**7.** Write short notes on: (Any two) **[2×5]**
&nbsp;&nbsp;&nbsp;a) IOT security basics
&nbsp;&nbsp;&nbsp;b) Unit Testing
&nbsp;&nbsp;&nbsp;c) UART and SPI Protocol
&nbsp;&nbsp;&nbsp;d) Exception types

---

**1. a)** A smart building in Kathmandu is equipped with a centralized Smart Air Conditioning System that adjusts temperature and airflow based on occupancy, external weather, and energy efficiency goals. The system uses temperature sensors, humidity sensors, CO₂ sensors, and PIR motion detectors across multiple zones. At 2:00 PM on a humid summer day, the external temperature is 34°C and indoor humidity is 70%. The meeting room (Zone 3) suddenly registers high CO₂ levels and multiple motion events, indicating increased occupancy. Meanwhile, the energy management system signals a need to reduce power consumption by 20% due to peak load pricing.
**Task:** Design an embedded system of Smart Air Conditioning System along with its components. **[7]**

**b)** How do modern heterogeneous SoCs differ from traditional monolithic microcontroller-based design? Explain bus architecture in details, highlighting how interconnect strategies. **[4+4]**

**2. a)** A remote environmental monitoring station uses an ARM Cortex-M based microcontroller to collect and transmit data from multiple sensors, including temperature, humidity, and soil moisture. The system is designed to operate under FreeRTOS, with strict timing constraints for sensor polling and wireless transmission. During operation, the following events occur in rapid succession:

- A temperature sensor triggers an interrupt due to threshold breach.
- A UART module raises an interrupt for incoming configuration data.
- A timer interrupt fires for scheduled data transmission.

The microcontroller uses the Nested Vectored Interrupt Controller (NVIC) to manage these events efficiently.
**Task:** Design the 3-stage pipeline operation of NVIC and how it enables low-latency interrupt servicing. **[4+3]**

**b)** A precision agriculture company is deploying an autonomous irrigation control system across rice fields in Nepal. The system uses embedded controllers to manage water flow based on soil moisture, weather forecasts, and crop growth stages. It must respond to sensor inputs and actuator commands under strict real-time constraints to avoid over- or under-irrigation, which could impact yield. The system includes:

- Soil moisture sensors (sampled every 100 ms)
- Weather data from satellite feeds (updated every 5 minutes)
- Actuator control for water valves (must respond within 50 ms)
- Communication with a central server for logging and remote override

**Task:** Identify and classify the system's real-time requirements with validation for the reason **[2]**

- Which tasks are hard real-time? **[2]**
- Which are soft real-time?
- Model the system using event-triggered and time-triggered paradigms. **[4]**

**3. a)** Explain how modular design and separation of concerns contribute to the scalability of embedded systems with the relevant example. **[7]**

**b)** Comparison of UART, SPI, and I²C protocols, with emphasis on timing, synchronization, and error handling.

**4.** A rural farming cooperative is deploying an IoT-based smart agriculture system to monitor soil moisture, temperature, and crop health across multiple fields. The system uses battery-powered sensor nodes, a local edge gateway, and cloud-based analytics for decision support. As an embedded systems engineer, you are tasked with designing and evaluating the system architecture and communication strategy.
**Task:** Propose a suitable Cloud–Edge–Device architecture for this application. Explain the roles of each layer and how data flows between them. **[5]**

**OR**

Analyze the CPU utilization using Rate Monotonic Scheduling and Earliest Deadline First on the following three periodic tasks in a real time embedded system

| TASK | EXECUTION TIME (E) | PERIOD (P) |
| ---- | ------------------ | ---------- |
| T1   | 1 ms               | 4 ms       |
| T2   | 2 ms               | 5 ms       |
| T3   | 2 ms               | 10 ms      |
