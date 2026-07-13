---
marp: true
theme: default
paginate: true
math: mathjax
style: |
  * {
    box-sizing: border-box;
  }
  /* Slide container */
  section {
    background-color: #fff;
    font-family: 'Times New Roman', Times, serif;
    font-size: 28pt;
    color: black;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: 0;
    padding-bottom: 10pt;
  }

  /* Heading banner */
  section h1 {
    background-color: rgb(25, 107, 36);
    color: white;
    font-family: 'Times New Roman', Times, serif;
    font-size: 30pt;
    margin: 0;
    padding: 8pt;
    text-align: center;
    width: 100%;
  }

  /* Body content fills remaining space */
  section p,
  section ul,
  section ol,
  section pre {
    font-family: 'Times New Roman', Times, serif;
    font-size: 28pt;
    color: black;
    margin: 0;
  }

  section ul {
    text-align: left;
    list-style-type: disc;
    list-style-position: inside;
    padding: 0;
  }

  section ol {
    text-align: left;
    list-style-type: decimal;
    list-style-position: inside;
    padding: 0;
  }

  section ol li::marker {
    font-weight: bold;
  }

  section ul li::marker {
    margin-right: 10pt;
    content: "•  ";
  }

  section pre {
    font-size: 20pt;
  }

  section::after {
    bottom: 5px;
  }

  h1 {
    margin-bottom: 10pt;
  }

  h1 ~ * {
    margin: 0 10pt;
  }

  /* Title slide - no green banner */
  section.title-slide {
    justify-content: center;
    align-items: center;
    padding: 40pt 100pt;
  }

  section.title-slide h1 {
    background-color: transparent;
    color: black;
    font-size: 40pt;
    font-weight: bold;
    text-align: center;
    padding: 0;
    margin-bottom: 30pt;
  }

  section.title-slide p {
    text-align: right;
    font-size: 28pt;
    width: 100%;
    margin: 0;
    line-height: 1.6;
  }

  section p:has(img) {
    display: flex;
    justify-content: center;
    align-items: center;
    flex: 1 1 0;
    min-height: 0;
    margin: 0;
  }

  img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }

  marp-pre {
    margin: 10pt;
  }

  blockquote {
    margin-bottom: 20pt;
  }

  section h3 {
    margin-top: 15pt;
    margin-bottom: 15pt;
  }

  section h4 {
    margin-top: 10pt;
    margin-bottom: 10pt;
  }

  table {
    margin: 0;
    padding: 0 10pt;
  }

  th, td {
    border: 1px solid black !important;
  }

  tr {
    background: white !important;
  }

  th img, td img {
    max-height: 390pt;
  }
---

<!-- _class: title-slide -->

# A Reconfigurable Energy Storage Architecture for Energy-harvesting Devices

**Authors:**
_Alexei Colin, Emily Ruppel, Brandon Lucia_

<br>

Presented by Bidur Sapkota
July 2026

---

# Introduction

- Run entirely on energy collected from the environment (solar, RF, vibration) without a battery
- Enables maintenance-free deployment in extreme or remote environments (glaciers, orbit, etc)
- Operate intermittently by accumulating charge, running until depleted, powering off, recharging, and repeating

---

# Problem

- Buffer energy in a capacitor and run only while charge lasts
- Fixed-size buffer cannot satisfy conflicting task needs
- Small buffer provides fast recharge and good reactivity but too little energy for demanding atomic tasks
- Large buffer provides enough energy but long recharge leaves device off and unresponsive
- Tasks needing both instant reaction and high energy are unsupported

---

# Solution

- Co-designed hardware and software power system with runtime-reconfigurable energy storage
- Software declares per-task energy needs while hardware reconfigures capacity to match

---

# Key Innovation

1. **Software:**

- config(mode) charges to a specific capacity before running a capacity-constrained task
- burst(mode) runs instantly using energy pre-charged earlier for reactive and temporal tasks
- preburst(bmode, emode) pre-charges a future burst task's bank ahead of time and off the critical path

---

# Key Innovation

2. **Hardware:**

- Array of capacitor banks connected via state-retaining switches
- Software controls total capacitance rather than voltage thresholds
- Faster to cold-start and cheaper in area and leakage

---

# Results

- Achieves 2 to 4 times better event-detection accuracy vs fixed-capacity systems
- Deployed on a nano-satellite (CapySat) under extreme size and temperature limits using a simplified switch at 20% the area

---

# Conclusion

- Fixed buffers force a tradeoff between atomicity and reactivity
- Capybara removes this by reconfiguring capacity and pre-charging bursts at runtime
- Enables reactive applications previously impossible on energy-harvesting hardware
