# Unit VI: Interfaces, Communication, and Peripherals

# 6.1 Peripheral Interfacing: GPIO, ADC, DAC, Timers

> **Describe the data transmission sequence in I2C from start to stop condition. Explain common sleep modes in low power design. [7 marks] (2025)**
>
> **Provide a comparative technical analysis of UART and SPI communication protocols, considering speed, complexity, and reliability. [7 marks] (2024)**
>
> **Comparison of UART, SPI, and I²C protocols, with emphasis on timing, synchronization, and error handling. (Model)**

In embedded systems, the microcontroller interacts with the external world through peripherals. Peripherals are hardware modules integrated into or connected to the microcontroller that perform specific input/output functions. On ARM Cortex-M based microcontrollers, all peripherals are memory-mapped, meaning the CPU accesses them by reading from and writing to specific memory addresses (registers). Before using any peripheral, its clock must be enabled through the system's clock control register, because peripheral clocks are disabled by default to conserve power. Additionally, since most microcontroller pins are multiplexed (capable of serving multiple functions), the pin function must be configured to select between GPIO mode and an alternate peripheral function such as ADC input, timer output, or UART.

**1. GPIO (General Purpose Input/Output):**

GPIO is the most fundamental peripheral interface. It allows the microcontroller to read digital input signals (e.g., from switches, buttons, or digital sensors) and drive digital output signals (e.g., to LEDs, relays, or other logic devices). Each GPIO pin can be individually configured as input or output. Input pins can be configured with internal pull-up or pull-down resistors to define a default logic level when the pin is unconnected. Output pins can be configured as push-pull (actively drives both high and low) or open-drain (actively drives low, requires external pull-up for high). GPIO operations involve writing to Set/Clear registers to change output states and reading from Pin registers to detect input states. GPIO is the building block upon which higher-level peripheral interactions are constructed.

**2. ADC (Analog-to-Digital Converter):**

The ADC converts continuous analog voltage signals from sensors (temperature, pressure, light, etc.) into discrete digital values that the microcontroller can process. Key parameters include resolution (commonly 10-bit or 12-bit, determining the number of discrete levels — a 12-bit ADC provides 4096 levels), reference voltage (defines the input voltage range), sampling rate (how frequently conversions occur), and conversion time. The ADC workflow involves enabling the ADC clock, configuring the input pin for analog mode, setting the conversion parameters (channel, resolution, sampling time), starting the conversion, and reading the result from the data register when the conversion-complete flag is set. Multiple ADC channels can be multiplexed to read several analog inputs using a single ADC module. ADC conversions can be triggered by software commands, timer events, or external signals.

**3. DAC (Digital-to-Analog Converter):**

The DAC performs the inverse operation of the ADC. It converts a digital value written by the microcontroller into a corresponding analog voltage on a designated output pin. DACs are used for generating audio waveforms, control voltages for analog actuators, reference voltages for other analog circuits, and signal synthesis. The operation is straightforward: the firmware writes a digital value to the DAC data register, and the hardware generates the proportional analog voltage. A 12-bit DAC with a 3.3V reference produces output voltages in steps of 3.3V/4096 ≈ 0.8 mV.

**4. Timers:**

Timers are among the most versatile peripherals in a microcontroller. A timer is essentially a hardware counter that increments (or decrements) at a rate derived from the system clock through a configurable prescaler. Timers serve multiple purposes: generating precise time delays, measuring the duration of external events (input capture), producing periodic interrupts for task scheduling, counting external events, and generating PWM signals.

## 6.1.1 Timers for PWM and Event Triggering

**1. Pulse Width Modulation (PWM):**

PWM is a technique for controlling the average power delivered to a load by rapidly switching a digital output between high and low states at a fixed frequency while varying the ratio of on-time to off-time. The duty cycle is the percentage of one period during which the signal is high. A 0% duty cycle means the output is always low (zero average voltage), a 50% duty cycle produces an average voltage equal to half the supply voltage, and a 100% duty cycle means the output is always high.

In hardware PWM generation, a timer counts from zero up to a value stored in the Auto-Reload Register (ARR), which defines the period (and thus the frequency) of the PWM signal. A Capture/Compare Register (CCR) stores the duty cycle threshold. While the timer count is less than the CCR value, the output pin is held high; when the count exceeds the CCR value, the output goes low. The timer automatically resets and repeats the cycle. A Prescaler (PSC) divides the system clock to achieve the desired timer frequency.

PWM frequency = System Clock / ((PSC + 1) × (ARR + 1)). Duty Cycle (%) = (CCR / ARR) × 100.

PWM is used extensively in motor speed control, LED brightness dimming, servo motor positioning, power supply regulation, and audio signal generation. Hardware PWM runs entirely in the timer peripheral with no CPU overhead after initial configuration.

**2. Event Triggering:**

Timers can trigger actions when their counter reaches specific values. A Match Register (or Compare Register) stores a target count value. When the timer counter equals the match value, the timer can generate an interrupt, toggle an output pin, reset the counter, or trigger other peripherals such as ADC conversions. This mechanism is fundamental for implementing periodic sampling of sensors at precise intervals, generating time-based events in control systems, implementing timeout detection, and producing complex timing waveforms.

**3. Input Capture:**

In input capture mode, the timer records its current counter value into a capture register when an external event (rising edge, falling edge, or both) occurs on a designated input pin. By capturing the counter values at successive edges, the firmware can measure the period, frequency, or pulse width of an external signal. This is used in applications such as measuring motor speed via encoder signals, decoding IR remote control protocols, and measuring ultrasonic sensor echo times.

---

# 6.2 Communication Protocols: UART, SPI, I2C

> **Describe the data transmission sequence in I2C from start to stop condition. [7 marks] (2025)**
>
> **Explain different Driver Testing and Validation Techniques. What is the role of a low-level driver in embedded systems? Explain how an ISR improves efficiency and power consumption. [8 marks] (2025)**
>
> **Provide a comparative technical analysis of UART and SPI communication protocols, considering speed, complexity, and reliability. [7 marks] (2024)**
>
> **Evaluate the strengths and weaknesses of the I2C protocol in multi-device embedded systems. [8 marks] (2024)**
>
> **Write short notes on: UART and SPI Protocol [5 marks] (2025)**
>
> **Comparison of UART, SPI, and I²C protocols, with emphasis on timing, synchronization, and error handling. (Model)**

Serial communication protocols are the primary means by which microcontrollers exchange data with sensors, actuators, memory devices, displays, and other controllers. The three most widely used protocols in embedded systems are UART, SPI, and I2C. Each has distinct characteristics suited to different application requirements.

**1. UART (Universal Asynchronous Receiver/Transmitter):**

UART is an asynchronous, full-duplex, point-to-point serial communication protocol. It uses two data lines: TX (transmit) and RX (receive), plus a common ground. Because UART is asynchronous, there is no shared clock signal; instead, both the transmitter and receiver must be independently configured to the same baud rate (data rate in bits per second).

Data is transmitted in discrete units called frames. A standard UART frame consists of a Start Bit (one bit, logic low, signals the beginning of a frame and synchronizes the receiver), Data Bits (typically 8 bits, transmitted least significant bit first), an optional Parity Bit (used for basic error detection — even parity, odd parity, or none), and Stop Bit(s) (one or two bits, logic high, signals the end of the frame and provides idle time before the next frame). A common configuration is denoted as 8N1: 8 data bits, No parity, 1 stop bit.

Standard baud rates include 9600, 19200, 38400, 57600, and 115200 bps. Because UART relies on matched baud rates rather than a shared clock, clock drift between the transmitter and receiver can cause bit misalignment and data corruption. Typically, a clock accuracy within ±2% is required for reliable communication.

UART is simple to implement, requires minimal hardware (two wires plus ground), and supports full-duplex communication. However, it is limited to point-to-point connections (one transmitter and one receiver), has relatively low speed (typically up to 1 Mbps), and provides only basic error detection through parity. UART is commonly used for debug consoles, GPS and Bluetooth module interfaces, and inter-processor communication.

**2. SPI (Serial Peripheral Interface):**

SPI is a synchronous, full-duplex serial communication protocol designed for high-speed data transfer between a master device and one or more slave devices. SPI uses four signal lines: SCLK (Serial Clock, generated by the master), MOSI (Master Out Slave In, data from master to slave), MISO (Master In Slave Out, data from slave to master), and SS/CS (Slave Select/Chip Select, one per slave, active low, selects the target slave device).

The master generates the clock on SCLK and asserts the appropriate SS line to select the slave. Data is simultaneously shifted out on MOSI and shifted in on MISO with each clock edge, making SPI inherently full-duplex. Two configuration parameters define the clock behavior: Clock Polarity (CPOL) determines the idle state of the clock (high or low), and Clock Phase (CPHA) determines whether data is sampled on the leading or trailing clock edge. These parameters define four SPI modes (Mode 0 through Mode 3).

SPI supports very high data rates (commonly 10–50 MHz, some devices exceeding 100 MHz) because it uses a dedicated clock line and simple shift-register architecture. It has no protocol overhead (no addressing, no acknowledgment) and achieves full-duplex operation. However, SPI requires one additional SS line per slave device, consuming GPIO pins as the number of slaves increases. It has no built-in error detection mechanism (no ACK/NACK), no standardized flow control, and is practical only for short-distance, board-level communication due to signal integrity concerns at high speeds.

SPI is the preferred protocol for high-speed peripherals such as flash memory, SD cards, displays (TFT/OLED), high-speed ADCs/DACs, and wireless transceiver modules.

**3. I2C (Inter-Integrated Circuit):**

I2C is a synchronous, half-duplex, multi-master, multi-slave serial communication protocol. It uses only two signal lines: SDA (Serial Data) and SCL (Serial Clock). Both lines are open-drain and require external pull-up resistors to the supply voltage. This open-drain configuration allows multiple devices to share the same bus without electrical conflicts — any device can pull a line low, but the line returns high only when all devices release it.

Each device on the I2C bus has a unique 7-bit (or 10-bit) address. The master initiates all communication by addressing the target slave. The I2C data transmission sequence from start to stop condition proceeds as follows:

- **START Condition:** The master pulls SDA low while SCL remains high. This unique signal condition (SDA transitioning low while SCL is high) alerts all slaves that a transaction is beginning.
- **Address Byte:** The master transmits a 7-bit slave address followed by a Read/Write bit (0 for write, 1 for read) on the SDA line, clocked by SCL. Data on SDA must be stable while SCL is high; SDA may only change while SCL is low.
- **ACK/NACK:** After every 8 bits transmitted, the receiver (slave during address/write; master during read) must respond with an Acknowledge bit on the 9th clock pulse. ACK is signaled by pulling SDA low; NACK is indicated by leaving SDA high. If the slave does not recognize the address or cannot accept data, it sends NACK.
- **Data Bytes:** After a successful address ACK, data bytes are transmitted (MSB first), each followed by an ACK/NACK from the receiver. In a write operation, the master sends data bytes to the slave. In a read operation, the slave sends data bytes to the master.
- **Repeated START (optional):** The master can issue a new START condition without first issuing a STOP, allowing it to begin a new transaction (e.g., switching from writing a register address to reading data) without releasing the bus.
- **STOP Condition:** The master releases SDA (allowing it to go high) while SCL is high. This unique signal condition terminates the transaction and frees the bus for other masters.

I2C operates at defined speed modes: Standard Mode (100 kHz), Fast Mode (400 kHz), Fast Mode Plus (1 MHz), and High Speed Mode (3.4 MHz). I2C supports clock stretching, where a slow slave holds SCL low to pause the master until it is ready to continue. Multi-master arbitration is handled through the open-drain bus: if two masters transmit simultaneously, the one that detects a discrepancy between what it transmitted and what appears on SDA loses arbitration and backs off without corrupting the other master's transaction.

The strengths of I2C include minimal wiring (only two lines regardless of the number of devices), built-in addressing (no additional select lines), hardware-level ACK/NACK for transmission verification, support for multi-master configurations, and clock stretching for handling slow devices. The weaknesses include lower speed compared to SPI, half-duplex operation (data flows in only one direction at a time), bus capacitance limitations (typically 400 pF, limiting cable length and number of devices), susceptibility to noise on long traces due to open-drain signaling, and protocol overhead from addressing and ACK bits that reduces effective throughput.

I2C is widely used for interfacing low-to-moderate speed peripherals such as temperature sensors, accelerometers, EEPROMs, real-time clocks, and OLED displays.

## 6.2.1 Protocol Timing and Error Handling

**1. Timing Considerations:**

Each protocol has distinct timing requirements that must be respected for reliable communication.

- **UART:** Timing is entirely defined by the baud rate. Both devices independently generate their bit timing from their local oscillators. If the baud rate mismatch exceeds approximately ±2–3%, the receiver will sample bits at incorrect positions, causing framing errors or corrupted data. The start bit serves as the synchronization reference for each frame — the receiver detects the falling edge of the start bit and then samples subsequent bits at the center of each bit period.
- **SPI:** Timing is governed by the master's clock. The critical timing parameters are setup time (how long data must be stable before the sampling clock edge) and hold time (how long data must remain stable after the sampling clock edge). At very high clock rates, propagation delay across PCB traces and through level shifters can violate these requirements, causing signal integrity issues. CPOL and CPHA must be correctly matched between master and slave.
- **I2C:** Timing is governed by the master's clock on SCL, with minimum high and low periods defined by the I2C specification for each speed mode. The SDA line must be stable during the entire SCL high period; transitions on SDA while SCL is high are reserved for START and STOP conditions. Clock stretching introduces variable timing that the master must tolerate by monitoring SCL before proceeding.

**2. Error Handling:**

- **UART:** Provides minimal error detection. Parity checking detects single-bit errors but cannot correct them. Framing errors occur when the stop bit is not detected at the expected position, typically indicating a baud rate mismatch or noise. Overrun errors occur when new data arrives before the previous data has been read from the receive register. Higher-level protocols (e.g., checksums, CRCs) must be implemented in software for robust error detection.
- **SPI:** Has no built-in error detection or acknowledgment mechanism. The protocol provides no feedback on whether data was received correctly. Applications requiring reliability must implement software-level checksums or CRCs. Some SPI devices use a status register that can be read back to verify operation.
- **I2C:** Provides hardware-level error detection through the ACK/NACK mechanism. The master can detect if no slave responds to the address (NACK on address), if the slave cannot accept further data (NACK on data byte), or if bus arbitration is lost in multi-master systems. Bus stuck conditions (SDA or SCL held low indefinitely) require timeout detection and bus recovery procedures (toggling SCL to release a stuck slave).

---

# 6.3 Low-Level Drivers and Interrupt Service Routines

> **Explain different Driver Testing and Validation Techniques. What is the role of a low-level driver in embedded systems? Explain how an ISR improves efficiency and power consumption. [8 marks] (2025)**

A low-level driver is a software module that provides a well-defined interface between the application software and a specific hardware peripheral. The driver encapsulates all direct register-level access, timing requirements, and hardware-specific details, exposing only clean, functional API calls to the rest of the system. Without drivers, every part of the application would need to manipulate hardware registers directly, resulting in duplicated code, tight hardware coupling, and extreme difficulty in porting to different platforms. The role of a low-level driver includes initializing and configuring the peripheral hardware, providing read/write functions that abstract register operations, managing peripheral state and error conditions, handling interrupt setup and processing, and ensuring safe concurrent access to shared hardware resources.

## 6.3.1 Writing Reusable Peripheral Drivers

Reusable drivers reduce development time across projects and improve code quality through repeated testing and refinement. Writing reusable peripheral drivers requires adherence to several design principles.

**1. Layered Architecture:**

The driver should be structured in layers. The lowest layer (Hardware Abstraction Layer or HAL) contains all register-level access code specific to a particular microcontroller. The driver layer sits above the HAL and implements the peripheral's protocol logic using HAL functions. The application interacts only with the driver layer's public API. This separation ensures that porting the driver to a different microcontroller requires rewriting only the HAL, not the protocol logic.

**2. Configuration Separation:**

Hardware-specific parameters such as pin assignments, clock frequencies, baud rates, and buffer sizes should not be hardcoded inside the driver. Instead, they should be passed through configuration structures during initialization. This allows the same driver code to support multiple instances of a peripheral (e.g., UART1 and UART2) and to be reused across different boards with different pin mappings.

```c
typedef struct {
    uint32_t baud_rate;
    uint8_t  tx_pin;
    uint8_t  rx_pin;
    uint8_t  data_bits;
    uint8_t  parity;
} uart_config_t;

void uart_init(uart_config_t *config);
void uart_send(uint8_t *data, uint16_t length);
uint16_t uart_receive(uint8_t *buffer, uint16_t max_length);
```

**3. Consistent API Design:**

All drivers in a project should follow a consistent naming convention and API pattern: `peripheral_init()`, `peripheral_read()`, `peripheral_write()`, `peripheral_deinit()`. This consistency reduces the learning curve for developers and makes the codebase predictable.

**4. Error Reporting:**

Drivers should return status codes or error codes rather than silently failing. A standardized error enumeration (e.g., `DRIVER_OK`, `DRIVER_TIMEOUT`, `DRIVER_BUSY`, `DRIVER_ERROR`) allows the application to detect and respond to hardware failures.

**5. Non-Blocking and Blocking Modes:**

Well-designed drivers offer both blocking (synchronous) and non-blocking (asynchronous) operation. Blocking functions wait until the operation completes and are simple to use but waste CPU cycles. Non-blocking functions initiate the operation and return immediately, using callbacks or flags to notify the application when the operation completes. Non-blocking operation is essential for real-time systems where the CPU must remain available for higher-priority tasks.

## 6.3.2 Interrupt Service Routines for Efficiency

An Interrupt Service Routine (ISR) is a function that executes automatically in response to a hardware interrupt signal. Instead of the CPU continuously checking (polling) whether a peripheral needs attention, the hardware interrupt mechanism allows the peripheral to signal the CPU only when an event actually occurs. This fundamental difference between interrupt-driven and polling-based architectures has profound implications for both system efficiency and power consumption.

**1. How ISRs Improve Efficiency:**

In a polling approach, the CPU executes a tight loop that repeatedly reads a peripheral's status register to check if data is available or an event has occurred. This wastes CPU cycles on unproductive status checks, prevents the CPU from performing other useful work, and introduces latency because the event is not detected until the next polling cycle. In an interrupt-driven approach, the CPU executes application code or enters a low-power sleep mode. When the peripheral needs attention (e.g., data has arrived, a conversion is complete, a timer has expired), it asserts an interrupt. The CPU immediately suspends its current execution, saves the context (registers), and jumps to the ISR. The ISR performs the minimum necessary processing and returns, restoring the previous context. This approach ensures near-zero latency for event detection, maximum CPU utilization on productive work between events, and deterministic response times critical for real-time systems.

**2. How ISRs Improve Power Consumption:**

In battery-powered embedded systems, the CPU is the largest power consumer. With polling, the CPU must remain fully active at all times, continuously executing instructions even when no events are occurring. With interrupt-driven design, the CPU can enter a sleep mode (where the clock is stopped and power consumption drops dramatically) and wake up only when an interrupt occurs. The CPU processes the event, then returns to sleep. This sleep-wake-process pattern is the foundation of all low-power embedded system design. As Wolf notes in *Computers as Components*, the combination of interrupt-driven peripheral management with aggressive use of sleep modes can reduce system power consumption by orders of magnitude compared to polling.

**3. Best Practices for Writing ISRs:**

- **Keep ISRs short:** An ISR should do the absolute minimum — typically clearing the interrupt flag, reading or writing a data register, setting a flag or posting to a queue, and returning. Lengthy processing inside an ISR delays the servicing of other interrupts and can cause deadline violations.
- **Defer complex processing:** The ISR should signal the main loop or an RTOS task to perform any complex data processing, calculations, or state machine transitions. This is the "top-half / bottom-half" pattern.
- **Avoid blocking operations:** Never call functions that block or wait inside an ISR (e.g., `delay()`, `printf()`, `malloc()`). These can cause deadlocks or unbounded interrupt latency.
- **Use `volatile` for shared variables:** Any variable shared between an ISR and the main code must be declared `volatile` to prevent the compiler from optimizing away reads/writes that appear redundant from a single-threaded perspective.
- **Protect critical sections:** Multi-byte shared data structures accessed by both the ISR and main code must be protected. This is typically done by briefly disabling interrupts around the access in the main code to prevent the ISR from modifying the data mid-access.
- **Use callbacks for flexibility:** Rather than hardcoding application logic into the ISR, register function pointers (callbacks) that the ISR invokes. This keeps the ISR generic and reusable across projects.

## 6.3.3 Driver Testing and Validation

Driver testing is challenging because drivers interact directly with hardware. A comprehensive testing strategy uses multiple complementary techniques at different levels.

**1. Host-Based Unit Testing (Software-in-the-Loop / SIL):**

The driver's logic is compiled and tested on the development PC rather than on the target hardware. Hardware register accesses are replaced with mock objects or stubs that simulate the hardware's behavior. Frameworks such as Unity (with CMock) or Google Test can automatically generate mock implementations of HAL functions. This approach allows rapid test execution, is independent of hardware availability, and catches logic errors, boundary conditions, and error handling paths early in development. The key requirement is that the driver must be designed with a clean HAL separation so that the hardware-dependent layer can be mocked.

**2. Hardware-in-the-Loop Testing (HIL):**

The driver is compiled for the target and tested with the actual hardware in a controlled environment. HIL testing uses automated test equipment to stimulate the peripheral inputs and monitor the outputs. This is essential for validating timing-sensitive operations (e.g., SPI clock timing, I2C setup/hold times), interrupt latency and ISR behavior, DMA transfer correctness, and interaction with specific hardware errata. HIL testing catches issues that host-based testing cannot, such as timing violations, electrical noise sensitivity, and hardware-specific behavior.

**3. Static Analysis:**

Static analysis tools examine the driver source code without executing it, checking for common defects such as null pointer dereferences, buffer overflows, uninitialized variables, non-reentrant function calls from ISRs, MISRA C violations, and race conditions on shared variables. Static analysis is particularly important for driver code because drivers operate at a low level where bugs can cause hardware damage or system crashes.

**4. Integration Testing:**

After individual drivers are validated, integration testing verifies that multiple drivers work correctly together and with the application. This includes testing for resource conflicts (e.g., two drivers attempting to use the same DMA channel or interrupt priority), correct initialization ordering (e.g., clock configuration before peripheral initialization), and system-level timing under realistic workloads.

**5. Regression Testing:**

All driver tests should be automated and executed on every code change through a Continuous Integration (CI) pipeline. This prevents regressions — new changes that inadvertently break previously working functionality. Host-based unit tests run on every commit; HIL tests run on a regular schedule or before releases.

---

# 6.4 Sensor Interfacing and Timing Issues

Sensors convert physical quantities (temperature, pressure, acceleration, humidity, light, proximity) into electrical signals that the microcontroller can read. Reliable sensor interfacing requires attention to signal conditioning, conversion accuracy, timing, and data validation.

**1. Analog Sensor Interfacing:**

Analog sensors produce a continuous voltage or current proportional to the measured quantity. The microcontroller reads this signal through its ADC. Signal conditioning circuits between the sensor and the ADC may include amplification (boosting weak sensor signals to match the ADC input range using operational amplifiers), filtering (low-pass filters to remove high-frequency noise and prevent aliasing, where frequencies above half the sampling rate fold back into the measured band), voltage level shifting (translating sensor output levels to the ADC's input range), and linearization (compensating for sensors with nonlinear output characteristics, either through analog circuits or firmware lookup tables/polynomial correction).

**2. Digital Sensor Interfacing:**

Many modern sensors contain built-in ADCs and signal conditioning, communicating with the microcontroller over I2C, SPI, or a proprietary digital protocol. Digital sensors simplify the hardware design but require the firmware to implement the sensor's communication protocol, including register addressing, configuration sequences, and data format conversion (e.g., combining two 8-bit registers into a 16-bit temperature value and applying scaling factors from the datasheet).

**3. Timing Issues:**

Timing is a critical and often underestimated challenge in sensor interfacing.

- **Sampling Rate:** The sampling rate must be at least twice the highest frequency component in the measured signal (Nyquist criterion) to avoid aliasing. In practice, sampling at 5–10 times the signal bandwidth is recommended for accurate reconstruction.
- **Conversion Time:** ADC conversions take a finite time. If the firmware does not account for this delay (waiting for the conversion-complete flag before reading the result), it will read stale or invalid data.
- **Sensor Response Time:** Physical sensors have inherent response times determined by their construction and the physical quantity being measured. A temperature sensor may require hundreds of milliseconds to settle after a step change, while an accelerometer may respond in microseconds. The firmware must not sample faster than the sensor can physically respond.
- **Bus Contention:** When multiple sensors share a communication bus (I2C or SPI), bus access must be scheduled to prevent contention and ensure each sensor is read at its required rate. Long transactions to slow sensors can delay access to fast sensors.
- **Interrupt Latency:** In interrupt-driven sensor systems, the time between the sensor asserting an interrupt and the ISR executing determines the system's responsiveness. If multiple interrupts occur simultaneously or if higher-priority interrupts are being serviced, the sensor ISR may be delayed (jitter), affecting measurement accuracy.
- **Debouncing:** Mechanical switches and contact-based sensors produce electrical bounce — rapid, spurious transitions when the contact opens or closes. Without debouncing, a single button press may register as multiple presses. Hardware debouncing uses RC filters or Schmitt trigger circuits. Software debouncing ignores input transitions for a defined lockout period (typically 20–50 ms) after the first edge, or requires the input to remain stable for several consecutive samples before accepting a state change.

---

# 6.5 Low-Power Design

> **Describe the data transmission sequence in I2C from start to stop condition. Explain common sleep modes in low power design. [7 marks] (2025)**

Power consumption is a primary design constraint in battery-powered and energy-harvesting embedded systems. The goal of low-power design is to minimize energy consumption while maintaining the system's functional and real-time requirements. As Wolf explains in *Computers as Components*, power-aware design must be considered at every level — hardware selection, system architecture, peripheral management, and firmware design.

## 6.5.1 Sleep Modes and Power-Efficient Peripheral Use

**1. Sources of Power Consumption:**

Power consumption in a microcontroller system comes from two primary sources. Dynamic power is consumed by switching transistors during active computation and is proportional to the clock frequency and the square of the supply voltage (P_dynamic ∝ f × V²). Static power (leakage current) flows even when transistors are not switching and increases with temperature and the number of powered-on circuits. Peripherals consume power independently of the CPU — an active ADC, UART, or timer draws current even if the CPU is idle.

**2. Common Sleep Modes:**

ARM Cortex-M processors provide standardized low-power modes that progressively disable system components to reduce power consumption.

- **Sleep Mode:** The CPU clock is stopped, halting instruction execution. All peripherals, memory, and the system clock remain active and operational. Any configured interrupt wakes the CPU, which resumes execution immediately with near-zero wake-up latency. Power savings are moderate because peripherals continue to draw current. Sleep mode is entered using the WFI (Wait For Interrupt) or WFE (Wait For Event) instruction.
- **Deep Sleep Mode:** The CPU clock, system clock, and high-speed oscillators (e.g., PLL, HSE) are disabled. Most peripherals are shut down. Only a low-power oscillator (e.g., 32 kHz LSE for the real-time clock) and specific wake-up peripherals (e.g., RTC alarm, external interrupt pins, low-power UART) remain active. Power consumption drops to microamps or even nanoamps, but wake-up latency increases significantly because the high-speed oscillator and PLL must re-stabilize (typically microseconds to milliseconds). RAM contents may be retained (standby with RAM retention) or lost (shutdown mode) depending on the specific mode.
- **Stop Mode:** An intermediate mode where the CPU and most clocks are stopped, but the voltage regulator remains active, preserving SRAM and register contents. Wake-up is possible through external interrupts or RTC. Power consumption is lower than sleep but higher than deep sleep.
- **SLEEPONEXIT:** The Cortex-M System Control Register provides a SLEEPONEXIT bit. When set, the processor automatically re-enters sleep mode immediately after returning from an ISR, without executing any main loop code. This is ideal for purely interrupt-driven systems where all processing occurs in ISRs and the main loop has no work to do.

**3. Power-Efficient Peripheral Use:**

Minimizing peripheral power consumption requires a disciplined approach.

- **Clock Gating:** Disable the clock to every peripheral that is not currently in use. A UART that is clocked but not transmitting still consumes significant dynamic power. Enable the peripheral clock only when a transaction is about to begin, and disable it immediately after the transaction completes.
- **Interrupt-Driven Operation:** Replace polling loops with interrupt-driven or DMA-driven peripheral access. Polling keeps the CPU active and consuming power. Interrupt-driven design allows the CPU to sleep between events.
- **DMA (Direct Memory Access):** Configure DMA channels to transfer data between peripherals and memory without CPU involvement. For example, an ADC can be configured to convert multiple channels in sequence, with DMA transferring the results directly to a memory buffer. The CPU sleeps during the entire sequence and wakes up only when the DMA transfer-complete interrupt fires, indicating all samples are ready for processing.
- **Peripheral Power Gating:** If a peripheral will not be used for an extended period, disable its power supply entirely (not just its clock) using the microcontroller's power control registers or external load switches. This eliminates both dynamic and static (leakage) power consumption from that peripheral.
- **Reduce Sampling Frequency:** Sample sensors at the lowest rate that meets the application's requirements. Each ADC conversion consumes energy. Reducing the sampling rate from 1 kHz to 10 Hz reduces the ADC's energy consumption by a factor of 100.
- **Batch Processing:** Instead of processing each sensor reading immediately, accumulate readings in a buffer (using DMA) and process the entire batch at once. This allows the CPU to remain in sleep mode for longer continuous periods, which is more power-efficient than frequent short wake-ups because each wake-up incurs energy overhead for oscillator startup and context restoration.
- **Voltage Scaling:** Use the lowest supply voltage that supports the required clock frequency. Since dynamic power is proportional to V², reducing the supply voltage from 3.3V to 1.8V reduces dynamic power by approximately 70%.
- **Avoid Floating Inputs:** Unconnected digital input pins can oscillate between logic levels due to noise, causing the input buffer transistors to switch continuously and waste power. All unused GPIO pins should be configured as outputs (driven low) or as inputs with pull-up or pull-down resistors enabled.
