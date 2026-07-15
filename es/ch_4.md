# Unit IV: Real-Time Systems and RTOS

# 4.1 Real-Time Requirements and System Models

> **Identify and classify the system's real-time requirements. Which tasks are hard real-time? Which are soft real-time? [2+2]**
>
> **Model the system using event-triggered and time-triggered paradigms. [4]**

A real-time system is a computing system that must respond to external events within a specified time constraint called a deadline. Correctness in a real-time system depends not only on the logical result of the computation but also on the time at which the result is produced. Real-time systems are the foundation of most embedded applications, including automotive control, robotics, avionics, medical devices, and industrial automation.

## 4.1.1 Hard and Soft Real-Time Systems

**Hard Real-Time Systems:**

A hard real-time system is one in which missing a deadline constitutes a total system failure and may lead to catastrophic consequences. The system must guarantee that every task completes before its deadline under all circumstances, including worst-case conditions. The consequences of a missed deadline are severe: loss of life, damage to equipment, or mission failure. Examples include anti-lock braking systems (ABS), flight control systems, pacemakers, airbag deployment controllers, and nuclear reactor control systems. Hard real-time systems require formal timing analysis and verification to prove that all deadlines will always be met.

**Soft Real-Time Systems:**

A soft real-time system is one in which meeting deadlines is desirable for performance and quality of service, but occasionally missing a deadline does not result in system failure. The system continues to function correctly, though the quality of output may degrade. The consequences of a missed deadline are reduced quality rather than failure. Examples include multimedia streaming, video conferencing, user interface rendering, and non-critical sensor logging. Soft real-time systems tolerate occasional deadline misses and use statistical performance measures rather than absolute guarantees.

**Firm Real-Time Systems:**

A firm real-time system is an intermediate category in which a missed deadline makes the result useless (the late result has zero value), but the system does not fail catastrophically. An example is a weather forecasting computation: a forecast delivered after the forecast period is worthless, but the system itself is not destroyed.

## 4.1.2 Task Models: Periodic, Aperiodic, and Sporadic

Real-time workloads are modeled using three fundamental task types based on their arrival patterns.

**Periodic Tasks:**

A periodic task is released at regular, fixed time intervals. Each instance (or job) of the task is characterized by a period (T), a worst-case execution time (C), and a deadline (D). The period defines the time between successive releases. For example, a temperature sensor sampled every 100 ms is a periodic task with T = 100 ms. Periodic tasks are the most common workload model in embedded systems and are directly analyzable using scheduling algorithms like Rate Monotonic Scheduling (RMS) and Earliest Deadline First (EDF).

**Aperiodic Tasks:**

An aperiodic task arrives at random, unpredictable instants with no guaranteed minimum inter-arrival time. These tasks typically have soft deadlines or no deadlines at all. Examples include user button presses, network packet arrivals for non-critical data, and diagnostic queries. Because their arrival is unpredictable, aperiodic tasks are often handled by server mechanisms such as polling servers or deferrable servers that execute aperiodic work within the slack time of periodic schedules, ensuring that periodic task deadlines are not jeopardized.

**Sporadic Tasks:**

A sporadic task arrives at irregular intervals but is constrained by a minimum inter-arrival time (MIT). Unlike aperiodic tasks, sporadic tasks have hard deadlines and must be guaranteed to complete on time. The minimum inter-arrival time provides a bound on the worst-case arrival rate, making schedulability analysis possible. Examples include emergency shutdown signals, hardware fault interrupts, and critical alarm events in industrial control systems.

## 4.1.3 Deadline and Jitter Analysis

**Deadline Analysis:**

Every real-time task has an associated deadline by which it must complete execution. Deadline analysis determines whether a given set of tasks can meet all their deadlines under a specified scheduling policy. The key metric is the worst-case response time (WCRT), which is the longest time from the release of a task to its completion. A task is schedulable if its WCRT does not exceed its deadline. For fixed-priority systems, the WCRT of a task i is computed iteratively as:

R_i = C_i + B_i + Σ ⌈R_i / T_j⌉ × C_j (for all higher-priority tasks j)

Here, C_i is the execution time, B_i is the maximum blocking time from lower-priority tasks holding shared resources, and the summation accounts for interference from all higher-priority tasks.

**Jitter:**

Jitter is the variation in the timing of a recurring event. Release jitter is the variation in the actual release time of a periodic task from its expected release time. Completion jitter is the variation in the completion time across different instances of the same task. Sources of jitter include interrupt latency, scheduler overhead, bus contention, and non-preemptible critical sections. Excessive jitter can destabilize control loops, degrade signal processing accuracy, and cause deadline violations. In safety-critical systems, jitter must be bounded and accounted for in the schedulability analysis.

---

# 4.2 Task Scheduling: Fixed and Dynamic Priority

> **Check whether tasks are schedulable using Earliest Deadline First (EDF) Scheduling. Apply Rate Monotonic Scheduling and Earliest Deadline First Scheduling. [8]**
>
> **Analyze the CPU utilization using Rate Monotonic Scheduling and Earliest Deadline First on periodic tasks. [5]**

Task scheduling is the mechanism by which the operating system or runtime determines which task should execute on the processor at any given time. In real-time systems, the scheduling algorithm must ensure that all tasks meet their deadlines.

## 4.2.1 Rate Monotonic Scheduling (RMS)

Rate Monotonic Scheduling is a fixed-priority, preemptive scheduling algorithm for periodic tasks. Priorities are assigned statically at design time based on the task period: the shorter the period, the higher the priority. A task with a 4 ms period receives a higher priority than a task with a 10 ms period. RMS is optimal among all fixed-priority scheduling algorithms, meaning that if any fixed-priority assignment can schedule a task set, RMS can also schedule it.

**Schedulability Test (Liu and Layland Bound):**

A set of n independent, preemptible, periodic tasks with deadlines equal to their periods is guaranteed to be schedulable under RMS if:

U = Σ (C_i / T_i) ≤ n(2^(1/n) − 1)

The bound values for small n are:

- n = 1: U ≤ 1.000 (100%)
- n = 2: U ≤ 0.828 (82.8%)
- n = 3: U ≤ 0.780 (78.0%)
- n → ∞: U ≤ ln(2) ≈ 0.693 (69.3%)

This is a sufficient but not necessary condition. If the utilization exceeds the bound, the task set may still be schedulable. In such cases, exact schedulability can be determined using Response Time Analysis (RTA), which computes the WCRT for each task and checks it against the deadline.

**Example:**

Given three tasks: T1(C=1, T=4), T2(C=1.5, T=5), T3(C=2, T=10).

U = 1/4 + 1.5/5 + 2/10 = 0.25 + 0.30 + 0.20 = 0.75

The Liu and Layland bound for n=3 is 3(2^(1/3) − 1) ≈ 0.780.

Since U = 0.75 ≤ 0.780, the task set is guaranteed schedulable under RMS.

Priority assignment: T1 has the highest priority (shortest period = 4 ms), followed by T2 (period = 5 ms), then T3 (period = 10 ms).

## 4.2.2 Earliest Deadline First (EDF) Scheduling

Earliest Deadline First is a dynamic-priority, preemptive scheduling algorithm. At every scheduling decision point, the task with the closest absolute deadline is assigned the highest priority. Priorities change dynamically as new task instances are released and deadlines shift.

**Schedulability Test:**

A set of independent, preemptible, periodic tasks is schedulable under EDF if and only if:

U = Σ (C_i / T_i) ≤ 1

This is both a necessary and sufficient condition. EDF can achieve 100% CPU utilization, making it theoretically optimal among all uniprocessor scheduling algorithms. If any scheduling algorithm can schedule a task set without missing deadlines, EDF can too.

**Advantages over RMS:**

EDF achieves higher processor utilization (up to 100% vs. approximately 69.3% for RMS). It can schedule task sets that RMS cannot.

**Disadvantages:**

EDF is more complex to implement because priorities must be recalculated dynamically. Under transient overload conditions, EDF behaves unpredictably because it is unclear which tasks will miss their deadlines. RMS, in contrast, guarantees that the highest-priority (shortest-period) tasks will still meet their deadlines under overload.

**Example:**

Using the same tasks: U = 0.75. Since 0.75 ≤ 1.0, the task set is schedulable under EDF.

## 4.2.3 Priority Inversion, and Mitigation (Priority Inheritance and Priority Ceiling)

> **Explain the concept of priority inversion in an RTOS. Illustrate how it can occur and critically evaluate the effectiveness of priority inheritance and priority ceiling protocols in mitigating it. [7]**

**Priority Inversion:**

Priority inversion is a scheduling anomaly in which a high-priority task is indirectly blocked by a lower-priority task for an unbounded duration. It occurs when tasks of different priorities share a resource protected by a mutual exclusion mechanism such as a mutex.

The classic scenario involves three tasks: a high-priority task (H), a medium-priority task (M), and a low-priority task (L).

1. L acquires a mutex to access a shared resource.
2. H becomes ready and preempts L. H attempts to acquire the same mutex and blocks because L holds it.
3. M becomes ready. Since M has higher priority than L, M preempts L and runs.
4. H is now indirectly blocked by M, even though H has higher priority than M and they share no resources. H cannot run until M finishes and L resumes, completes its critical section, and releases the mutex.

The danger is that the blocking of H is unbounded: any number of medium-priority tasks can preempt L and further delay H.

**Real-World Example (Mars Pathfinder, 1997):**

The Mars Pathfinder spacecraft experienced repeated system resets caused by priority inversion. The VxWorks RTOS used a mutex shared between a high-priority bus management task and a low-priority meteorological data collection task. A medium-priority communications task preempted the low-priority task while it held the mutex, blocking the high-priority task long enough to trigger a watchdog timer reset. The issue was resolved by remotely enabling priority inheritance on the mutex.

**Priority Inheritance Protocol (PIP):**

When a high-priority task blocks on a mutex held by a lower-priority task, the lower-priority task temporarily inherits the priority of the highest-priority task waiting for the mutex. This prevents medium-priority tasks from preempting the mutex-holding task, ensuring that the critical section completes quickly and the mutex is released. Once the mutex is released, the task's priority reverts to its original value. PIP eliminates unbounded priority inversion but does not prevent deadlocks. Chained blocking can still occur when multiple mutexes are involved.

**Priority Ceiling Protocol (PCP):**

Each mutex is assigned a priority ceiling equal to the highest priority of any task that may ever lock it. A task is permitted to lock a mutex only if its active priority is strictly higher than the priority ceilings of all mutexes currently locked by other tasks. If this condition is not met, the task blocks immediately. PCP provides two guarantees that PIP does not: it prevents deadlocks entirely, and it bounds the maximum blocking time to at most one critical section of a lower-priority task. PCP is more restrictive and introduces higher runtime overhead due to the ceiling checks, but it provides stronger guarantees.

---

# 4.3 Real-Time Operating Systems (RTOS) Fundamentals

A Real-Time Operating System (RTOS) is a specialized operating system designed to serve real-time applications that require deterministic, predictable timing behavior. Unlike general-purpose operating systems (GPOS) such as Linux or Windows, which optimize for throughput and fairness, an RTOS optimizes for worst-case response time and guaranteed deadline compliance.

## 4.3.1 Kernel, Scheduler, IPC

**The RTOS Kernel:**

The kernel is the core of the RTOS and provides the fundamental services required by application tasks. These services include task management (creation, deletion, suspension, and resumption of tasks), scheduling (deciding which task runs next), synchronization (mutexes, semaphores), communication (message queues, mailboxes), memory management, and timer services. The kernel must be small, efficient, and deterministic. Its operations must have bounded worst-case execution times so that timing analysis of the application is possible.

**The Scheduler:**

The scheduler is the component of the kernel that determines which task executes at any given time. Most RTOS schedulers implement priority-based preemptive scheduling. The highest-priority task in the ready state is always selected for execution. If a higher-priority task becomes ready while a lower-priority task is running, the lower-priority task is immediately preempted (its context is saved) and the higher-priority task begins execution. Tasks of equal priority are typically scheduled using round-robin (time-slicing), where each task receives a fixed time quantum before the scheduler switches to the next equal-priority task.

Task states in a typical RTOS are as follows.

1. **Running:** The task is currently executing on the processor. Only one task can be in this state at a time on a single-core processor.
2. **Ready:** The task is ready to execute and waiting for the scheduler to grant it the CPU. It has no pending wait conditions.
3. **Blocked:** The task is waiting for an event such as a semaphore, a queue message, a timer expiry, or an I/O completion. Blocked tasks do not consume CPU time.
4. **Suspended:** The task has been explicitly suspended by an API call and will not be scheduled until explicitly resumed.

**Inter-Process Communication (IPC):**

IPC mechanisms allow tasks to exchange data and synchronize their execution safely.

1. **Mutexes:** A mutex (mutual exclusion) is a locking mechanism used to protect shared resources. Only one task can hold a mutex at a time. If a task attempts to acquire a mutex that is already held, it blocks until the mutex is released. RTOS mutexes typically include priority inheritance to mitigate priority inversion.

2. **Semaphores:** A semaphore is a signaling mechanism. A binary semaphore has two states (available/taken) and is used for task synchronization, such as signaling from an ISR to a task. A counting semaphore maintains a count and is used to manage access to a pool of resources. Unlike mutexes, semaphores do not have ownership and do not support priority inheritance.

3. **Message Queues:** A message queue is a FIFO buffer used to pass data between tasks or between ISRs and tasks. The sending task writes data items to the queue, and the receiving task reads from it. If the queue is full, the sender can block until space is available. If the queue is empty, the receiver blocks until data arrives. Queues decouple the producer and consumer, allowing them to operate at different rates.

## 4.3.2 Timer, Interrupts, and System Tick

**System Tick (SysTick):**

The system tick is a periodic hardware timer interrupt that serves as the heartbeat of the RTOS. On ARM Cortex-M processors, the SysTick timer is a dedicated 24-bit down-counter that generates an interrupt at a configurable rate, typically every 1 ms. The system tick drives all time-dependent kernel operations: task delay management (vTaskDelay), timeout handling for blocked tasks, round-robin time-slicing for equal-priority tasks, and software timer expiration checks. The tick rate is configured via the configTICK_RATE_HZ macro in FreeRTOSConfig.h.

**Software Timers:**

Software timers allow deferred function execution after a specified delay or at periodic intervals without creating a dedicated task. When a software timer expires, a user-defined callback function is executed in the context of the timer service task (daemon task). Software timers are built on top of the system tick and have a resolution limited to the tick period.

**Interrupts in an RTOS:**

Interrupts are hardware signals that cause the processor to suspend the current task and execute an Interrupt Service Routine (ISR). In an RTOS environment, ISRs must be kept short and deterministic. They should perform only the minimum necessary work (such as reading a hardware register and clearing the interrupt flag) and then signal a task using a semaphore, queue, or task notification to perform the remaining processing. This design pattern is called deferred interrupt processing. It ensures that the ISR completes quickly, minimizing interrupt latency for other interrupts, and that the bulk of the work is done in a schedulable task context where RTOS services like blocking and priority management are available.

---

# 4.4 Memory Handling in RTOS

Memory management in real-time systems must be deterministic and safe. Standard dynamic memory allocation functions like malloc() and free() from the C standard library are generally unsuitable for real-time systems because their execution time is non-deterministic (it depends on the state of the heap), they can cause heap fragmentation over time, and they are typically not thread-safe.

**Static Allocation:**

Memory is allocated at compile time using global variables, static arrays, or statically declared RTOS objects. All memory requirements are known and fixed before the system starts. There is no risk of allocation failure, fragmentation, or memory leaks at runtime. Static allocation is preferred in safety-critical and hard real-time systems because it is entirely deterministic. FreeRTOS supports static allocation through xTaskCreateStatic(), xQueueCreateStatic(), and similar APIs where the application provides pre-allocated memory buffers for the task stack and the Task Control Block (TCB).

**Dynamic Allocation:**

Memory is allocated at runtime from a heap. It provides flexibility when memory requirements are not known at compile time. However, dynamic allocation introduces risks: allocation time is non-deterministic, fragmentation can cause allocation failures even when sufficient total free memory exists, and memory leaks can occur if allocated memory is not properly freed.

**FreeRTOS Heap Schemes:**

FreeRTOS provides five portable heap management implementations, allowing the developer to choose the scheme best suited to the application.

1. **heap_1:** Allocates memory from a static array but does not support freeing. It is the simplest and most deterministic scheme, suitable for systems where all RTOS objects are created once at startup and never deleted.
2. **heap_2:** Supports both allocation and freeing using a best-fit algorithm but does not coalesce adjacent free blocks. This can lead to fragmentation over time.
3. **heap_3:** Wraps the standard C library malloc() and free() with thread safety (by suspending the scheduler during allocation). It inherits all the non-determinism of the C library heap.
4. **heap_4:** Supports allocation and freeing with a first-fit algorithm and coalesces adjacent free blocks to reduce fragmentation. It is the most commonly used scheme for general-purpose FreeRTOS applications.
5. **heap_5:** Extends heap_4 to allow the heap to span multiple non-contiguous memory regions, useful in microcontrollers with multiple SRAM banks.

**Memory Pools (Fixed-Size Block Allocation):**

A memory pool pre-allocates a fixed number of blocks of identical size. Allocation and deallocation are O(1) operations (constant time), making them fully deterministic. Fragmentation is completely eliminated because all blocks are the same size. Memory pools are ideal for real-time systems that frequently allocate and free fixed-size data structures such as network packets, sensor readings, or message buffers.

**Memory Protection Unit (MPU):**

The MPU is a hardware component available on ARM Cortex-M3 and higher processors that enforces memory access permissions. The RTOS can configure the MPU to restrict each task's access to specific memory regions, preventing a faulty task from corrupting the memory of other tasks or the kernel. If a task attempts an unauthorized memory access, the MPU triggers a MemManage fault exception, allowing the system to handle the error gracefully. FreeRTOS provides an MPU-enabled port (FreeRTOS-MPU) that runs user tasks in unprivileged mode with restricted memory access while the kernel operates in privileged mode.

---

# 4.5 Design Using FreeRTOS

> **Consider a real-time embedded system controlling a robotic arm, which performs three periodic tasks. Check schedulability and apply RMS and EDF. [8]**

FreeRTOS is a widely used, open-source, real-time operating system kernel designed for microcontrollers and small embedded systems. It is written in C and supports over 40 processor architectures including ARM Cortex-M, RISC-V, and MSP430. FreeRTOS provides a preemptive, priority-based scheduler with optional time-slicing, and its kernel is small enough to run on processors with as little as 4 KB of RAM.

## 4.5.1 Task Creation, Scheduling, and Synchronization

**Task Creation:**

A task in FreeRTOS is an independent thread of execution with its own stack and priority. Tasks are created using the xTaskCreate() API:

```c
BaseType_t xTaskCreate(
    TaskFunction_t pvTaskCode,    // Pointer to the task function
    const char * const pcName,    // Descriptive name (for debugging)
    uint16_t usStackDepth,        // Stack size in words
    void *pvParameters,           // Parameter passed to the task
    UBaseType_t uxPriority,       // Task priority (0 = lowest)
    TaskHandle_t *pxCreatedTask   // Handle to the created task
);
```

The task function is an infinite loop that never returns. A typical task function structure is:

```c
void vSensorTask(void *pvParameters) {
    for (;;) {
        // Read sensor data
        // Process data
        // Send to queue
        vTaskDelay(pdMS_TO_TICKS(100)); // Delay for 100 ms
    }
}
```

For static allocation, xTaskCreateStatic() is used, where the application provides the stack buffer and TCB memory at compile time.

**Scheduling:**

The FreeRTOS scheduler starts when vTaskStartScheduler() is called. It selects the highest-priority ready task for execution. If multiple tasks share the same priority, they are scheduled using round-robin time-slicing, where each task runs for one tick period before being preempted. The configMAX_PRIORITIES macro defines the number of available priority levels. Priority 0 is the lowest, and the idle task always runs at priority 0.

**Synchronization Mechanisms:**

FreeRTOS provides several synchronization primitives.

1. **Binary Semaphores:** Created using xSemaphoreCreateBinary(). Used primarily for synchronization between ISRs and tasks. An ISR gives (signals) the semaphore using xSemaphoreGiveFromISR(), and the task takes (waits on) it using xSemaphoreTake(). Binary semaphores do not include priority inheritance.

2. **Mutexes:** Created using xSemaphoreCreateMutex(). Used for mutual exclusion when protecting shared resources. FreeRTOS mutexes include a built-in priority inheritance mechanism. When a high-priority task blocks on a mutex held by a lower-priority task, the lower-priority task's priority is temporarily raised.

3. **Queues:** Created using xQueueCreate(). Queues are the primary mechanism for passing data between tasks. Data is copied into and out of the queue by value. The xQueueSend() and xQueueReceive() APIs support optional blocking with a timeout. Queues are also ISR-safe through the xQueueSendFromISR() and xQueueReceiveFromISR() variants.

4. **Task Notifications:** Each task has a built-in 32-bit notification value. Task notifications are approximately 45% faster than binary semaphores and consume no additional RAM because they do not require a separate kernel object. They are used for lightweight signaling, event flags, and simple counting semaphore functionality when only one receiving task is involved.

5. **Event Groups:** An event group is a set of event bits that tasks can set, clear, and wait on. A task can block until any combination of bits is set, enabling complex synchronization patterns where a task waits for multiple events simultaneously.

## 4.5.2 Debugging with FreeRTOS

Debugging real-time systems is inherently difficult because timing-dependent bugs (race conditions, priority inversion, stack overflows) may not be reproducible with traditional breakpoint-based debugging, which disrupts the system's timing behavior.

**configASSERT():**

This macro is defined in FreeRTOSConfig.h and is the primary mechanism for catching programming errors during development. It checks a condition and, if the condition is false, halts execution by disabling interrupts and entering an infinite loop. This allows the developer to inspect the call stack and register values in the debugger. A typical definition is:

```c
#define configASSERT(x) if ((x) == 0) { taskDISABLE_INTERRUPTS(); for(;;); }
```

configASSERT() is effective at catching common errors such as calling ISR-unsafe API functions from within an ISR, using invalid interrupt priority levels, and passing NULL pointers to kernel APIs.

**Stack Overflow Detection:**

Stack overflow is a frequent cause of memory corruption in embedded systems. FreeRTOS provides two detection methods controlled by the configCHECK_FOR_STACK_OVERFLOW macro. Method 1 checks whether the stack pointer remains within the valid stack range during each context switch. Method 2 fills the stack with a known pattern (0xA5A5A5A5) at task creation and checks whether the pattern has been overwritten during context switches. When an overflow is detected, the kernel calls the user-defined vApplicationStackOverflowHook() callback. The uxTaskGetStackHighWaterMark() API returns the minimum free stack space a task has had since creation, aiding in tuning stack sizes.

**Runtime Statistics:**

FreeRTOS can track the percentage of processing time consumed by each task. Enabling configGENERATE_RUN_TIME_STATS and providing a high-resolution timer base allows the vTaskGetRunTimeStats() API to generate a report showing each task's CPU usage. This helps identify tasks that consume excessive CPU time or tasks that are starved of execution time.

**Trace Tools:**

Professional trace tools such as SEGGER SystemView and Percepio Tracealyzer provide real-time visualization of task execution, context switches, ISR activity, and queue operations. These tools hook into the FreeRTOS kernel through trace macros (enabled by configUSE_TRACE_FACILITY) and record events with minimal overhead, allowing the developer to analyze timing behavior, detect priority inversion, and identify deadlocks without disrupting the system.
