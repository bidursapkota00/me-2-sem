# Unit III: ARM Cortex-M3 Programming

# 3.1 ARM Cortex-M3 Architecture

> **Design the 3-stage pipeline operation of NVIC and how it enables low-latency interrupt servicing. [4+3]**
>
> **Explain the interrupt masking mechanism using BASEPRI, PRIMASK, and FAULTMASK with example scenarios. [7]**

The ARM Cortex-M3 is a 32-bit processor core based on the ARMv7-M architecture, designed specifically for deeply embedded, deterministic, real-time applications. It uses the Thumb-2 instruction set (a mix of 16-bit and 32-bit instructions), a Harvard bus architecture with separate instruction and data buses, and an integrated Nested Vectored Interrupt Controller (NVIC) for efficient exception handling.

## 3.1.1 Pipeline, Memory Map, and NVIC

**The 3-Stage Pipeline:**

The Cortex-M3 uses a 3-stage pipeline to increase instruction throughput by overlapping the execution of successive instructions.

**1. Fetch Stage:**

The processor fetches the next instruction from program memory (Flash) using the instruction bus (I-Code bus). A prefetch buffer fetches instructions ahead of time to reduce wait states caused by slower Flash memory.

**2. Decode Stage:**

The fetched instruction is decoded to determine the operation to perform, the source and destination registers, and the addressing mode. This stage also includes branch prediction logic that speculatively fetches the target instruction of a branch to minimize pipeline stalls.

**3. Execute Stage:**

The decoded instruction is executed. This includes performing arithmetic or logical operations in the ALU, computing memory addresses, reading from or writing to data memory using the data bus (D-Code bus or System bus), and updating the program counter and status flags.

The pipeline allows up to three instructions to be in different stages of processing simultaneously. While one instruction is being executed, the next is being decoded, and the one after that is being fetched. This ideally achieves a throughput of one instruction per clock cycle, although pipeline stalls due to branches, data dependencies, or multi-cycle instructions reduce this ideal throughput.

**The Cortex-M3 Memory Map:**

The Cortex-M3 defines a fixed, architecturally standardized 4 GB (32-bit) memory map. This fixed layout ensures software portability across different Cortex-M3 microcontrollers from different silicon vendors. The major regions are as follows.

**1. Code Region (0x00000000 to 0x1FFFFFFF, 512 MB):**

This region is intended for program code. It is accessed via the I-Code and D-Code buses, which are optimized for instruction fetches. On most microcontrollers, on-chip Flash is mapped here. The vector table, which must start at address 0x00000000 on reset, resides at the beginning of this region.

**2. SRAM Region (0x20000000 to 0x3FFFFFFF, 512 MB):**

This region is for on-chip SRAM used as data memory (variables, stack, heap). It is accessed via the System bus. The first 1 MB of this region (0x20000000 to 0x200FFFFF) can be bit-banded, meaning each bit in this region can be individually addressed and atomically set or cleared through a corresponding 32-bit alias address in the bit-band alias region.

**3. Peripheral Region (0x40000000 to 0x5FFFFFFF, 512 MB):**

This region is for memory-mapped peripheral registers (GPIO, UART, SPI, I2C, timers, ADC, etc.). Like the SRAM region, the first 1 MB of the peripheral region is bit-band accessible, allowing atomic bit-level access to peripheral control and status registers.

**4. External RAM Region (0x60000000 to 0x9FFFFFFF, 1 GB):**

This region is for external memory such as off-chip SRAM or SDRAM, used by systems that require more memory than the on-chip SRAM provides.

**5. External Device Region (0xA0000000 to 0xDFFFFFFF, 1 GB):**

This region is for external peripherals or devices connected through external buses.

**6. Private Peripheral Bus and System Region (0xE0000000 to 0xFFFFFFFF, 512 MB):**

This region contains the processor's internal system components, including the NVIC registers, System Control Block (SCB), SysTick timer, Memory Protection Unit (MPU) configuration registers, and debug components (ITM, DWT, FPB). These are accessible only in privileged mode.

**Nested Vectored Interrupt Controller (NVIC):**

The NVIC is tightly integrated into the Cortex-M3 processor core and is responsible for managing all exceptions and interrupts. It supports up to 240 external interrupt sources (IRQs) with up to 256 programmable priority levels (the actual number of priority bits is implementation-defined, typically 3 to 8 bits).

**1. Vectored Operation:**

When an exception occurs, the NVIC automatically looks up the address of the corresponding Interrupt Service Routine (ISR) from the vector table in memory. It then automatically saves the processor context (registers R0–R3, R12, LR, PC, and xPSR) onto the current stack before branching to the ISR. This hardware-automated stacking eliminates the need for software to save context, reducing interrupt latency.

**2. Nested Interrupts:**

The NVIC supports priority-based preemption. If a higher-priority interrupt occurs while a lower-priority ISR is executing, the processor suspends the current ISR, stacks its context, and services the higher-priority interrupt first. This nesting can occur to any depth, limited only by available stack space.

**3. Tail-Chaining:**

When an ISR completes and another interrupt of equal or lower priority is pending, the NVIC skips the unstacking and restacking steps. Instead, it directly fetches the vector of the next pending interrupt and begins executing its ISR. This eliminates the overhead of restoring and re-saving the processor context between back-to-back interrupts, reducing the inter-interrupt latency to as few as 6 clock cycles.

**4. Late Arrival:**

If a higher-priority interrupt arrives during the stacking phase of a lower-priority interrupt (before the ISR has started executing), the NVIC redirects execution to the higher-priority ISR without restarting the stacking process. The stacking that is already in progress is reused, and the higher-priority interrupt is serviced first. The lower-priority interrupt is then handled via tail-chaining after the higher-priority ISR completes.

**5. Deterministic Latency:**

The combination of hardware stacking, tail-chaining, and late arrival ensures that the worst-case interrupt latency is deterministic and short (12 clock cycles from interrupt assertion to the first instruction of the ISR, in zero-wait-state memory conditions).

## 3.1.2 Operating Modes: Thread, Handler, Privileged, Unprivileged

The Cortex-M3 defines two operating modes and two privilege levels that work together to provide a secure execution environment suitable for RTOS-based systems.

**Thread Mode:**

Thread mode is the normal execution mode for application code. The processor enters Thread mode after reset and returns to Thread mode after all exception handlers complete. The main application, including RTOS tasks, runs in Thread mode. Thread mode can operate at either the privileged or unprivileged level, as configured by the CONTROL register.

**Handler Mode:**

Handler mode is entered automatically by the hardware whenever an exception (interrupt, fault, or system exception) occurs. All exception handlers (ISRs) execute in Handler mode. Handler mode always runs at the privileged level, regardless of the CONTROL register setting. The processor returns to Thread mode when the exception handler completes by writing a special EXC_RETURN value to the PC.

**Privileged Level:**

Code running at the privileged level has full, unrestricted access to all processor resources, including the NVIC, System Control Block, MPU configuration, and all memory regions. After reset, the processor operates in privileged Thread mode. The OS kernel, device drivers, and all exception handlers typically run at the privileged level.

**Unprivileged Level:**

Code running at the unprivileged level has restricted access. It cannot directly access the NVIC, SCB, or certain system control registers. If an MPU is present and configured, unprivileged code may also be restricted from accessing specific memory regions. Unprivileged code cannot change its own privilege level by writing to the CONTROL register. To elevate privilege, it must execute a Supervisor Call (SVC) instruction, which triggers an exception that is handled in privileged Handler mode. User application tasks in an RTOS typically run at the unprivileged level for system protection.

**The CONTROL Register:**

The CONTROL register is a special register that determines the privilege level and stack pointer selection for Thread mode. Bit 0 (nPRIV) controls the privilege level in Thread mode: 0 means privileged, 1 means unprivileged. Bit 1 (SPSEL) selects the stack pointer used in Thread mode: 0 means MSP (Main Stack Pointer), 1 means PSP (Process Stack Pointer). In Handler mode, the processor always uses the MSP and always runs at the privileged level, regardless of the CONTROL register value.

## 3.1.3 Register Set and Stack Management

**Core Register Set:**

The Cortex-M3 has sixteen 32-bit core registers (R0–R15) and several special-purpose registers.

**1. R0–R12 (General-Purpose Registers):**

R0 through R12 are general-purpose registers used for data processing. R0–R3 are used for passing arguments to functions and returning results (per the ARM Architecture Procedure Call Standard, AAPCS). R4–R11 are callee-saved registers (a called function must preserve their values). R12 (also called IP, the Intra-Procedure call scratch register) is used by the linker as a scratch register.

**2. R13 (Stack Pointer, SP):**

R13 is the Stack Pointer. It is banked, meaning there are two physical copies: the Main Stack Pointer (MSP) and the Process Stack Pointer (PSP). Only one is active at a time, determined by the CONTROL register and the current operating mode. The stack is full-descending: the SP points to the last item pushed onto the stack, and the stack grows downward in memory (toward lower addresses).

**3. R14 (Link Register, LR):**

R14 is the Link Register. When a function is called using the BL (Branch with Link) instruction, the return address is automatically stored in LR. When an exception occurs, LR is loaded with a special EXC_RETURN value that encodes information about the exception context (which mode and which stack pointer to return to).

**4. R15 (Program Counter, PC):**

R15 is the Program Counter. It holds the address of the current instruction being fetched. Writing to the PC causes a branch to the written address. Due to the pipeline, reading the PC returns the address of the current instruction plus 4.

**5. Program Status Registers (xPSR):**

The combined Program Status Register (xPSR) is composed of three sub-registers. The Application PSR (APSR) contains the condition flags (Negative, Zero, Carry, Overflow) set by arithmetic and logical instructions. The Interrupt PSR (IPSR) contains the exception number of the currently active exception. The Execution PSR (EPSR) contains the Thumb state bit (always set to 1 on Cortex-M3, as only Thumb instructions are supported).

**Stack Management:**

**1. Main Stack Pointer (MSP):**

The MSP is the default stack pointer active after reset. It is used by the OS kernel, initialization code, and all exception handlers. The initial value of the MSP is loaded from the first entry (address 0x00000000) of the vector table during reset.

**2. Process Stack Pointer (PSP):**

The PSP is an alternative stack pointer that can be used by application tasks in Thread mode. An RTOS typically configures each task with its own stack and switches the PSP to point to the active task's stack during a context switch. This separation ensures that a stack overflow in a user task does not corrupt the kernel or exception handler stacks.

**3. Automatic Context Saving (Stacking):**

When an exception occurs, the processor hardware automatically pushes eight registers onto the current stack: R0, R1, R2, R3, R12, LR, PC (the return address), and xPSR. When the exception handler returns (by writing EXC_RETURN to the PC), the hardware automatically pops (unstacks) these registers, restoring the pre-exception state. This hardware stacking and unstacking is the mechanism that enables the low-latency, deterministic interrupt handling.

---

# 3.2 Programming for Bare-Metal Environments

> **Explain in detail about Bare Metal Programming along with startup code and linker script used in ARM Cortex-M3 programming. Highlight memory mapping and initialization steps. [7]**

Bare-metal programming means writing firmware that runs directly on the processor hardware without an operating system. The programmer has full control over the hardware and must manually initialize the processor, memory, peripherals, and the C runtime environment.

## 3.2.1 C Programming for Cortex-M3 (Startup Code, Linker Scripts)

**The Boot Sequence:**

When the Cortex-M3 is powered on or reset, the hardware performs two automatic actions. First, it reads the 32-bit value at address 0x00000000 and loads it into the Main Stack Pointer (MSP). Second, it reads the 32-bit value at address 0x00000004 and loads it into the Program Counter (PC). This second value is the address of the Reset_Handler function, which is the entry point of the startup code. Execution begins at Reset_Handler.

**The Vector Table:**

The vector table is an array of 32-bit addresses located at the beginning of the Flash memory. The first entry is the initial stack pointer value, and the subsequent entries are the addresses of exception and interrupt handlers. The vector table is typically defined in C as an array of function pointers, placed in a special linker section (`.isr_vector`) that the linker maps to address 0x00000000.

```c
extern uint32_t _estack;  // Defined by linker script (top of stack)
void Reset_Handler(void);
void NMI_Handler(void);
void HardFault_Handler(void);
// ... other handlers ...

__attribute__((section(".isr_vector")))
const uint32_t vector_table[] = {
    (uint32_t)&_estack,          // Initial MSP value
    (uint32_t)&Reset_Handler,    // Reset handler
    (uint32_t)&NMI_Handler,      // NMI handler
    (uint32_t)&HardFault_Handler,// Hard fault handler
    // ... remaining exception and IRQ vectors ...
};
```

**Startup Code (Reset_Handler):**

The Reset_Handler is the first code that runs after reset. Its purpose is to prepare the C runtime environment before calling `main()`. It performs the following initialization steps.

**1. Copy the `.data` section from Flash to RAM:**

Initialized global and static variables (e.g., `int x = 42;`) have their initial values stored in Flash (non-volatile). At runtime, these variables must reside in RAM (volatile, read-write). The startup code copies the initialization values from their load address in Flash to their runtime address in RAM.

**2. Zero-initialize the `.bss` section in RAM:**

Uninitialized global and static variables (e.g., `int y;`) are placed in the `.bss` section, which must be set to zero before `main()` is called. The startup code fills this RAM region with zeros.

**3. Call SystemInit():**

The `SystemInit()` function (defined by CMSIS) configures the system clock, PLL, Flash wait states, and other low-level hardware settings. This is called before `main()` to ensure the clock system is properly configured.

**4. Call main():**

After the runtime environment is initialized, the startup code calls the application's `main()` function.

```c
extern uint32_t _sidata, _sdata, _edata, _sbss, _ebss;

void Reset_Handler(void) {
    // Copy .data section from Flash to RAM
    uint32_t *src = &_sidata;
    uint32_t *dst = &_sdata;
    while (dst < &_edata) *dst++ = *src++;

    // Zero-fill .bss section
    dst = &_sbss;
    while (dst < &_ebss) *dst++ = 0;

    // Initialize system clock
    SystemInit();

    // Call main
    main();

    // Infinite loop if main returns
    while (1);
}
```

**The Linker Script:**

The linker script tells the linker how to map the compiled code and data sections into the physical memory of the microcontroller. It defines the memory layout and section placement.

**1. MEMORY Block:**

The MEMORY block defines the available physical memory regions, their start addresses, sizes, and access permissions.

```
MEMORY {
    FLASH (rx)  : ORIGIN = 0x08000000, LENGTH = 128K
    RAM   (rwx) : ORIGIN = 0x20000000, LENGTH = 20K
}
```

**2. SECTIONS Block:**

The SECTIONS block maps compiler output sections to memory regions.

The `.isr_vector` section is placed at the very beginning of Flash so that the vector table starts at address 0x00000000 (or 0x08000000, which is aliased to 0x00000000 on many STM32 devices). The `.text` section contains the program code and read-only constants, and is placed in Flash. The `.data` section contains initialized global and static variables. It has a load address in Flash (where initial values are stored) and a virtual (runtime) address in RAM (where the variables actually reside during execution). The `.bss` section contains uninitialized global and static variables and is placed in RAM.

**3. Linker Symbols:**

The linker script defines symbols such as `_sidata` (start of `.data` initialization values in Flash), `_sdata` and `_edata` (start and end of `.data` in RAM), `_sbss` and `_ebss` (start and end of `.bss` in RAM), and `_estack` (top of stack, usually the end of RAM). These symbols are used by the startup code to perform the data copy and BSS clearing.

## 3.2.2 Inline Assembly for Performance-Critical Tasks

While nearly all Cortex-M3 programming is done in C, certain operations require inline assembly because they involve special processor instructions that have no C equivalent.

**1. Accessing Special Registers:**

Special registers such as PRIMASK, BASEPRI, FAULTMASK, CONTROL, MSP, and PSP can only be accessed using the MSR (Move to Special Register) and MRS (Move from Special Register) instructions.

```c
// Disable all configurable interrupts
__asm volatile ("cpsid i");  // Set PRIMASK = 1

// Enable all configurable interrupts
__asm volatile ("cpsie i");  // Clear PRIMASK = 0

// Read the current PRIMASK value
uint32_t primask;
__asm volatile ("mrs %0, primask" : "=r" (primask));
```

**2. Memory Barrier Instructions:**

Data Synchronization Barrier (DSB), Data Memory Barrier (DMB), and Instruction Synchronization Barrier (ISB) are used to enforce ordering of memory accesses and ensure that configuration changes (such as writing to the NVIC or SCB registers) take effect before subsequent instructions execute.

```c
__asm volatile ("dsb");  // Wait for all memory accesses to complete
__asm volatile ("isb");  // Flush the instruction pipeline
```

**3. Wait for Interrupt (WFI) and Wait for Event (WFE):**

These instructions put the processor into a low-power sleep state until an interrupt or event occurs. They are used in idle loops to save power.

```c
__asm volatile ("wfi");  // Sleep until an interrupt occurs
```

**4. Supervisor Call (SVC):**

The SVC instruction triggers a Supervisor Call exception, used by unprivileged code to request services from the privileged OS kernel.

```c
__asm volatile ("svc #0");  // Trigger SVC exception with immediate value 0
```

## 3.2.3 Clock and Reset Configuration

The clock system determines the operating frequency of the processor and peripherals. Proper clock configuration is essential for correct system timing, peripheral operation, and power management.

**1. Clock Sources:**

Most Cortex-M3 microcontrollers provide multiple clock sources. The High-Speed Internal oscillator (HSI) is an on-chip RC oscillator (typically 8 MHz) available immediately after reset. The High-Speed External oscillator (HSE) uses an external crystal (typically 4–25 MHz) for higher accuracy. The Low-Speed Internal oscillator (LSI, typically 32–40 kHz) is used for the watchdog timer. The Low-Speed External oscillator (LSE, typically 32.768 kHz) is used for the Real-Time Clock (RTC).

**2. Phase-Locked Loop (PLL):**

The PLL multiplies the input clock frequency to produce a higher system clock. For example, an 8 MHz HSE can be multiplied by 9 to produce a 72 MHz system clock. The PLL configuration involves setting the input source (HSI or HSE), the multiplication factor, and waiting for the PLL to lock (stabilize) before switching the system clock to the PLL output.

**3. Clock Tree and Prescalers:**

The system clock (SYSCLK) is distributed to different buses through prescalers (dividers). The AHB prescaler divides SYSCLK to produce the HCLK (the clock for the CPU, memory, and DMA). The APB1 prescaler divides HCLK to produce the clock for low-speed peripherals (max 36 MHz on STM32F1). The APB2 prescaler divides HCLK to produce the clock for high-speed peripherals.

**4. Flash Wait States:**

As the system clock frequency increases, the Flash memory may not be fast enough to serve instruction fetches in a single clock cycle. Wait states must be configured to match the system clock frequency. For example, on STM32F1: 0 wait states for SYSCLK up to 24 MHz, 1 wait state for 24–48 MHz, and 2 wait states for 48–72 MHz.

**5. Reset Types:**

The Cortex-M3 supports three types of reset. Power-On Reset (POR) occurs when the supply voltage rises above the threshold, resetting the entire chip. System Reset resets the processor and most peripherals but may preserve certain backup domain registers. Processor Reset resets only the processor core without affecting peripherals.

**6. Reset and Clock Control (RCC) Peripheral:**

The RCC peripheral (specific to STM32 implementations) provides registers to configure the clock source, PLL parameters, bus prescalers, and peripheral clock enables. Each peripheral's clock must be explicitly enabled through the RCC before the peripheral can be accessed.

---

# 3.3 Interrupts and Exception Handling

> **Write short notes on: Exception types [5]**

## 3.3.1 NVIC Setup, Interrupt Priorities, and Vector Table

**NVIC Configuration:**

The NVIC is configured through memory-mapped registers in the Private Peripheral Bus region (starting at 0xE000E100). Key NVIC registers include the Interrupt Set-Enable Registers (ISER), which enable specific interrupts; the Interrupt Clear-Enable Registers (ICER), which disable specific interrupts; the Interrupt Set-Pending Registers (ISPR), which manually set an interrupt as pending; the Interrupt Clear-Pending Registers (ICPR), which clear a pending interrupt; and the Interrupt Priority Registers (IPR), which set the priority level of each interrupt.

**Priority Configuration:**

Each exception has a priority value that determines its urgency. Lower numerical values indicate higher priority. Reset has a fixed priority of -3 (the highest), NMI has a fixed priority of -2, and HardFault has a fixed priority of -1. All other exceptions have configurable priorities. The priority value is stored in the upper bits of an 8-bit field. If the implementation uses 3 priority bits, priority values range from 0 (highest) to 7 (lowest), stored in bits [7:5] of the priority register.

**Priority Grouping:**

The priority field can be split into two sub-fields: a group priority (preemption priority) and a sub-priority (used for tie-breaking when two exceptions of the same group priority are pending simultaneously). The Application Interrupt and Reset Control Register (AIRCR) in the System Control Block configures how the priority bits are divided between group priority and sub-priority. A higher group priority exception can preempt a lower group priority ISR. If two pending exceptions have the same group priority, the one with the lower sub-priority (or the lower exception number, if sub-priorities are also equal) is serviced first.

**Vector Table:**

The vector table occupies the first portion of the code memory. The first 16 entries (addresses 0x00000000 to 0x0000003C) are reserved for system exceptions. Entries from offset 0x00000040 onward correspond to external interrupts (IRQ0, IRQ1, ...). The Vector Table Offset Register (VTOR) in the System Control Block allows the vector table to be relocated to a different base address, which is useful for bootloaders or systems that load application code at a non-zero address.

## 3.3.2 Exception Types: Faults, IRQs, and SysTick

The Cortex-M3 defines 15 system exception types (exception numbers 1–15) and up to 240 external interrupt types (exception numbers 16–255).

**System Exceptions:**

**1. Reset (Exception #1, Priority -3):**

Reset is the highest-priority exception. It is triggered when the processor is powered on or a reset signal is asserted. It initializes the MSP from the vector table and begins execution at the Reset_Handler address.

**2. NMI (Non-Maskable Interrupt, Exception #2, Priority -2):**

NMI cannot be disabled or masked by PRIMASK or BASEPRI. It is typically connected to critical system events such as a clock security failure or a watchdog timeout.

**3. HardFault (Exception #3, Priority -1):**

HardFault is a generic fault handler that catches all faults that are not handled by a more specific fault handler (MemManage, BusFault, or UsageFault), or when those specific fault handlers are disabled.

**4. MemManage Fault (Exception #4, Configurable Priority):**

MemManage is triggered by memory access violations detected by the Memory Protection Unit (MPU), such as accessing a forbidden memory region or executing code from a non-executable region.

**5. BusFault (Exception #5, Configurable Priority):**

BusFault is triggered by errors on the bus during a memory access, such as accessing an invalid address, an unaligned access to a region that does not support it, or a bus error during instruction fetch or data access.

**6. UsageFault (Exception #6, Configurable Priority):**

UsageFault is triggered by instruction execution errors such as executing an undefined instruction, an illegal unaligned access, dividing by zero (if configured), or attempting to switch to ARM state (which is not supported on Cortex-M3).

**7. SVCall (Exception #11, Configurable Priority):**

SVCall is triggered by the SVC instruction. It is used by application code to request services from the OS kernel in a controlled manner, similar to a system call in a general-purpose OS.

**8. PendSV (Exception #14, Configurable Priority):**

PendSV is a pendable, software-triggered system exception typically used by an RTOS for context switching. It is usually configured with the lowest priority so that context switches occur only after all other pending interrupts have been serviced.

**9. SysTick (Exception #15, Configurable Priority):**

SysTick is generated by the built-in 24-bit down-counter timer. It is commonly used by an RTOS as the system tick timer for time-slicing and periodic task scheduling. The SysTick timer counts down from a reload value to zero, generates an exception, reloads, and repeats.

**External Interrupts (IRQs):**

External interrupts (IRQ0 through IRQ239) are generated by on-chip peripherals such as GPIO, UART, SPI, I2C, ADC, timers, and DMA controllers. Each IRQ has a configurable priority and can be individually enabled, disabled, and pended through the NVIC registers.

**Interrupt Masking Registers:**

**1. PRIMASK:**

PRIMASK is a 1-bit register. When set to 1, it disables all exceptions with configurable priority (all exceptions except Reset, NMI, and HardFault). It is used for critical sections where no interrupts should be allowed. The CPSID I instruction sets PRIMASK, and CPSIE I clears it.

**2. FAULTMASK:**

FAULTMASK is a 1-bit register. When set to 1, it disables all exceptions except Reset and NMI, effectively masking even HardFault. It is used in fault handlers that need to perform recovery without being interrupted by another fault. FAULTMASK is automatically cleared when the processor returns from an exception handler (except NMI).

**3. BASEPRI:**

BASEPRI is a register that masks exceptions based on priority level. When a non-zero value is written to BASEPRI, all exceptions with a priority value equal to or greater than (numerically, meaning lower urgency than) the BASEPRI value are disabled. Exceptions with a priority value less than (higher urgency than) the BASEPRI value remain enabled. This allows selective masking of lower-priority interrupts while keeping critical high-priority interrupts active.

```c
// Example: Disable all interrupts with priority >= 3
// (assuming 3-bit priority, value 3 = 0x60 in upper bits)
__asm volatile ("msr basepri, %0" :: "r" (0x60));

// Example: Re-enable all interrupts
__asm volatile ("msr basepri, %0" :: "r" (0x00));
```
