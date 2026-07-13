# Pokhara University

## Faculty of Science and Technology

- **Course Code:** CMP 555 (3 Credits)
- **Course Title:** Embedded Systems Design (3-0-0)
- **Nature of the course:** Theory
- **Level:** Master
- **Full marks:** 100
- **Pass marks:** 60
- **Total Lectures:** 45 hrs
- **Program:** MCE

---

### 1. Course Description

This graduate-level course provides an in-depth exploration of embedded systems design, integrating hardware and software to meet real-time, power, and performance constraints. Students will master ARM Cortex-M3 programming, real-time operating systems (RTOS), design patterns, and IoT system concepts. Through lectures and case studies, students will develop skills to design robust embedded and IoT systems for modern applications.

### 2. General Objectives

The course is designed with the following general objectives:

- To enable the students to design and develop embedded systems using Cortex-M3 microcontrollers in bare-metal and RTOS environments.
- To equip the students with skills to interface peripherals, implement communication protocols, and apply software design patterns for system reliability.
- To acquaint the students with IoT system design, including networking, data management, and integration of smart devices.

### 3. Methods of Instruction

1. Lectures and class discussions
2. Project-based learning
3. Presentations and group assignments

---

### 4. Contents in Detail

| Specific objectives                                                           | Contents                                                 |
| ----------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Explain embedded system components, characteristics, and design processes** | **Unit I: Introduction to Embedded Systems (6 hrs)**<br> |

<br>1.1 Embedded Computing Systems<br>

<br>1.1.1 Basic components: Processor, Memory, Peripherals and I/O Devices<br>

<br>1.1.2 Characteristics of Embedded computing applications<br>

<br>1.1.3 Performance in embedded computing<br>

<br>1.1.4 Embedded and general-purpose computing<br>

<br>1.1.5 Challenges in embedded computing system design<br>

<br>1.2 Embedded System Design Process<br>

<br>1.2.1 Requirements analysis and specification<br>

<br>1.2.2 Architecture design and component selection<br>

<br>1.2.3 Hardware-software partitioning<br>

<br>1.2.4 Integration, testing, and deployment |
| **Design embedded system architectures and analyze processor choices.** | **Unit II: Embedded System Architectures (6 hrs)**<br>

<br>2.1 Embedded Computing Platform Architecture<br>

<br>2.1.1 System-on-chip (SoC) design principles<br>

<br>2.1.2 Bus architectures (AMBA, AHB, APB)<br>

<br>2.1.3 Memory-mapped I/O and peripheral integration<br>

<br>2.2 Processor and Memory Systems<br>

<br>2.2.1 Processor types: RISC vs. CISC, DSP vs. Microcontroller<br>

<br>2.2.2 Memory hierarchies and access patterns<br>

<br>2.2.3 Instruction set design and performance considerations |
| **Develop and debug software for bare-metal Cortex-M3 environments.** | **Unit III: ARM Cortex-M3 Programming (5 hrs)**<br>

<br>3.1 ARM Cortex-M3 Architecture<br>

<br>3.1.1 Pipeline, memory map, and NVIC<br>

<br>3.1.2 Operating modes: Thread, handler, privileged, unprivileged<br>

<br>3.1.3 Register set and stack management<br>

<br>3.2 Programming for Bare-Metal Environments<br>

<br>3.2.1 C programming for Cortex-M3 (startup code, linker scripts)<br>

<br>3.2.2 Inline assembly for performance-critical tasks<br>

<br>3.2.3 Clock and reset configuration<br>

<br>3.3 Interrupts and Exception Handling<br>

<br>3.3.1 NVIC setup, interrupt priorities, and vector table<br>

<br>3.3.2 Exception types: Faults, IRQs, and SysTick |
| **Design and implement real-time systems with RTOS integration.** | **Unit IV: Real-Time Systems and RTOS (7 hrs)**<br>

<br>4.1 Real-Time Requirements and System Models<br>

<br>4.1.1 Hard and soft real-time systems<br>

<br>4.1.2 Task models: Periodic, aperiodic, and sporadic<br>

<br>4.1.3 Deadline and jitter analysis<br>

<br>4.2 Task Scheduling: Fixed and Dynamic Priority<br>

<br>4.2.1 Rate monotonic scheduling (RMS)<br>

<br>4.2.2 Earliest deadline first (EDF) scheduling<br>

<br>4.2.3 Priority inversion, and mitigation (priority inheritance and priority ceiling)<br>

<br>4.3 Real-Time Operating Systems (RTOS) Fundamental<br>

<br>4.3.1 Kernel, scheduler, IPC<br>

<br>4.3.2 Timer, Interrupts, and System Tick<br>

<br>4.4 Memory handling in RTOS<br>

<br>4.5 Design using FreeRTOS<br>

<br>4.5.1 Task creation, scheduling, and synchronization<br>

<br>4.5.2 Debugging with FreeRTOS |
| **Apply design patterns to improve embedded software quality.** | **Unit V: Design Patterns and Embedded Software Quality (8 hrs)**<br>

<br>5.1 Software Practices for Embedded Systems<br>

<br>5.1.1 Code readability, commenting, and documentation<br>

<br>5.1.2 Modular design and separation of concerns<br>

<br>5.1.3 Version control and coding standards<br>

<br>5.2 Software Maintainability<br>

<br>5.2.1 Refactoring and lifecycle considerations<br>

<br>5.3 State Machines, Encapsulation, and Modularity<br>

<br>5.3.1 Finite state machines (FSMs) and hierarchical FSMs<br>

<br>5.3.2 Encapsulation for hardware abstraction<br>

<br>5.3.3 Modular design with interfaces<br>

<br>5.4 Design Patterns and Testing<br>

<br>5.4.1 Event queues and Watchdogs timers<br>

<br>5.4.2 Unit testing with frameworks (Unity)<br>

<br>5.4.3 Static and Dynamic Analysis |
| **Interface peripherals and implement communication protocols.** | **Unit VI: Interfaces, Communication, and Peripherals (8 hrs)**<br>

<br>6.1 Peripheral Interfacing: GPIO, ADC, DAC, Timers<br>

<br>6.1.1 Timers for PWM and event triggering<br>

<br>6.2 Communication Protocols: UART, SPI, I2C<br>

<br>6.2.1 Protocol timing and error handling<br>

<br>6.3 Low-Level Drivers and Interrupt Service Routines<br>

<br>6.3.1 Writing reusable peripheral drivers<br>

<br>6.3.2 Interrupt service routines for efficiency<br>

<br>6.3.3 Driver testing and validation<br>

<br>6.4 Sensor Interfacing and Timing Issues<br>

<br>6.5 Low-Power Design<br>

<br>6.5.1 Sleep modes and power-efficient peripheral use |
| **Explain the principles of IoT networking and manage data storage solutions for IoT systems.** | **Unit VII: IoT Systems (5 hrs)**<br>

<br>7.1 IoT system applications<br>

<br>7.2 IoT system architectures<br>

<br>7.3.1 Edge Devices, Gateways, and Cloud Integration<br>

<br>7.3 Networks for IoT<br>

<br>7.3.1 Internet Protocol (IP) and MQTT/CoAP<br>

<br>7.3.2 IoT networking concepts: Scalability, Low-Power<br>

<br>7.3.3 IoT Security Basics: TLS, Device Authentication<br>

<br>7.4 Databases and Timewheels<br>

<br>7.4.1 Data storage for IoT (SQLite)<br>

<br>7.4.2 Timewheels for event scheduling |

---

### 5. Evaluation system and Students’ Responsibilities

#### Evaluation System

In addition to the formal exam(s) conducted by the Office of the Controller of Examination of Pokhara University, the internal evaluation of a student may consist of class attendance, class participation, quizzes, assignments, presentations, written exams, etc. The tabular presentation of the evaluation system is as follows:

| External Evaluation      | Marks           | Internal Evaluation                   | Marks  |
| ------------------------ | --------------- | ------------------------------------- | ------ |
| Semester-End Examination | 40              | Class attendance and participation    | 5      |
|                          |                 | Field visit and report                | 10     |
|                          |                 | Quizzes/assignments and presentations | 10     |
|                          |                 | Research paper review                 | 10     |
|                          |                 | Internal Term Exam                    | 25     |
| **Total External**       | **40**          | **Total Internal**                    | **60** |
| **Full Marks**           | **40+60 = 100** |                                       |        |

#### Students’ Responsibilities:

Each student must secure at least 60% marks in the internal evaluation with 80% attendance in the class to appear in the Semester End Examination. Failing to obtain such a score will be given NOT QUALIFIED (NQ) and the student will not be eligible to appear in the End-Term examinations. Students are advised to attend all the classes and complete all the assignments within the specified time period. If a student does not attend the class(es), it is his/her sole responsibility to cover the topic(s) taught during the period. If a student fails to attend a formal exam, quiz, test, etc. there will not be any provision for a re-exam.

---

### 6. Prescribed Books and References

- Wolf, M. _Computers as Components: Principles of Embedded Computing System Design_, $5^{th}$ Ed., 2023, Morgan Kaufmann, Elsevier, US.
- Lewis D.W. _Fundamentals of Embedded Software with the ARM Cortex-M3_, $2^{nd}$ Ed., 2013, Person, US.
- White, E. _Making Embedded Systems: Design Patterns for Great Software_, $2^{nd}$ Ed., 2024, O'Reilly Media, US.
