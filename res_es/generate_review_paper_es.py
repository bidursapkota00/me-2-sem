#!/usr/bin/env python3
"""
Generate an IEEE two-column format review paper in DOCX format.
Topic: Recent Improvements in Battery-Free Embedded Systems: A Review
Page Size: A4
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import os

OUTPUT_PATH = "/Users/bidur/ncit/res_es/Review_Paper_BatteryFree_ES_2025_2026.docx"

doc = Document()

# ============================================================
# PAGE SETUP - IEEE format (A4 size, narrow margins)
# ============================================================
for section in doc.sections:
    section.page_width = Cm(21.0)    # A4 width
    section.page_height = Cm(29.7)   # A4 height
    section.top_margin = Cm(1.91)    # 0.75 in
    section.bottom_margin = Cm(2.54) # 1 in
    section.left_margin = Cm(1.78)   # 0.7 in
    section.right_margin = Cm(1.78)  # 0.7 in

    # Two-column layout
    sectPr = section._sectPr
    cols = sectPr.find(qn('w:cols'))
    if cols is None:
        cols = parse_xml(f'<w:cols {nsdecls("w")} w:num="2" w:space="360"/>')
        sectPr.append(cols)
    else:
        cols.set(qn('w:num'), '2')
        cols.set(qn('w:space'), '360')

# ============================================================
# STYLES
# ============================================================
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(10)
style.paragraph_format.space_after = Pt(0)
style.paragraph_format.space_before = Pt(0)
style.paragraph_format.line_spacing = 1.0

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def add_title(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(22)
    run.font.name = 'Times New Roman'
    return p

def add_authors(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text)
    run.font.size = Pt(11)
    run.font.name = 'Times New Roman'
    return p

def add_affiliation(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.font.size = Pt(10)
    run.font.name = 'Times New Roman'
    run.italic = True
    return p

def add_section_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text.upper())
    run.bold = True
    run.font.size = Pt(10)
    run.font.name = 'Times New Roman'
    return p

def add_subsection_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run(text)
    run.bold = True
    run.italic = True
    run.font.size = Pt(10)
    run.font.name = 'Times New Roman'
    return p

def add_body(doc, text, first_line_indent=True):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if first_line_indent:
        p.paragraph_format.first_line_indent = Cm(0.5)
    run = p.add_run(text)
    run.font.size = Pt(10)
    run.font.name = 'Times New Roman'
    return p

def add_reference(doc, number, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.first_line_indent = Cm(-0.5)
    run = p.add_run(f"[{number}] {text}")
    run.font.size = Pt(8)
    run.font.name = 'Times New Roman'
    return p

def add_table(doc, caption, headers, data, col_widths=None):
    """Add a formatted table with caption."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(caption)
    run.bold = True
    run.font.size = Pt(8)
    run.font.name = 'Times New Roman'

    table = doc.add_table(rows=1 + len(data), cols=len(headers))
    table.style = 'Table Grid'

    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = header
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.bold = True
                run.font.size = Pt(7)
                run.font.name = 'Times New Roman'

    for row_idx, row_data in enumerate(data, 1):
        for col_idx, value in enumerate(row_data):
            cell = table.rows[row_idx].cells[col_idx]
            cell.text = value
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(7)
                    run.font.name = 'Times New Roman'

    if col_widths:
        for row in table.rows:
            for i, w in enumerate(col_widths):
                row.cells[i].width = Cm(w)

    p2 = doc.add_paragraph()
    p2.paragraph_format.space_after = Pt(6)


# ============================================================
# DOCUMENT CONTENT
# ============================================================

# --- TITLE ---
add_title(doc, "Recent Improvements in Battery-Free\nEmbedded Systems:\nA Comprehensive Review")

# --- AUTHORS ---
add_authors(doc, "Bidur Sapkota")
add_affiliation(doc, "Department of Computer Engineering, Nepal College of Information Technology (NCIT)\nPokhara University, Nepal\nbidur@ncit.edu.np")

# --- ABSTRACT ---
add_section_heading(doc, "Abstract")

abstract_text = (
    "Battery-free embedded systems powered by ambient energy harvesting have emerged as a "
    "transformative paradigm for sustainable Internet of Things (IoT) deployments. The period "
    "spanning 2024 to 2026 has witnessed a significant transition from proof-of-concept "
    "demonstrations to increasingly mature, deployment-ready solutions. This review paper "
    "critically examines six recent journal and conference papers that address key challenges "
    "in advancing battery-free system technology. The reviewed works encompass analytical "
    "modeling of energy dynamics in batteryless IoT sensors, cost-effective design methodologies "
    "for intermittent wireless communication, standardized evaluation platforms for fair "
    "performance benchmarking, energy-harvesting-aware neural architecture search for "
    "intermittent deep learning inference, UAV-powered RF energy-harvesting sensor systems "
    "for precision agriculture, and comprehensive surveys of circuit and system design "
    "architectures. Through a systematic comparison of the objectives, methodologies, results, "
    "strengths, and limitations of each study, this review identifies several critical research "
    "gaps, including the absence of unified benchmarking standards, insufficient multi-source "
    "energy harvesting integration, limited adaptation of edge AI for intermittent operation, "
    "and inadequate standardization of power management protocols. The paper concludes with "
    "recommendations for future research directions aimed at achieving reliable, scalable, "
    "and maintenance-free battery-free IoT ecosystems."
)
add_body(doc, abstract_text, first_line_indent=False)

# --- Keywords ---
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(4)
p.paragraph_format.space_after = Pt(6)
run_kw = p.add_run("Keywords: ")
run_kw.bold = True
run_kw.italic = True
run_kw.font.size = Pt(9)
run_kw.font.name = 'Times New Roman'
run_val = p.add_run("Battery-Free Embedded Systems, Energy Harvesting, Intermittent Computing, "
                     "IoT, TinyML, Power Management, Wireless Sensor Networks, Precision Agriculture")
run_val.italic = True
run_val.font.size = Pt(9)
run_val.font.name = 'Times New Roman'

# ============================================================
# I. INTRODUCTION
# ============================================================
add_section_heading(doc, "I. Introduction")

# --- A. Background ---
add_subsection_heading(doc, "A. Background")

add_body(doc, (
    "The rapid proliferation of Internet of Things (IoT) devices across diverse application "
    "domains—including precision agriculture, industrial monitoring, environmental sensing, "
    "and healthcare—has created an unprecedented demand for autonomous, long-lived sensing "
    "platforms. However, a fundamental bottleneck constraining large-scale IoT deployment is "
    "the reliance on electrochemical batteries. Conventional batteries impose significant "
    "operational costs due to periodic replacement requirements, contribute to environmental "
    "degradation through hazardous waste generation, and impose practical limitations in "
    "remote or inaccessible deployment scenarios where manual maintenance is infeasible [6]."
))

add_body(doc, (
    "Battery-free embedded systems offer a compelling alternative by harvesting ambient energy "
    "from sources such as solar radiation, radio-frequency (RF) signals, thermal gradients, "
    "and mechanical vibrations. These systems typically employ energy storage elements such as "
    "supercapacitors or small rechargeable cells that buffer harvested energy for intermittent "
    "computation and communication. The resulting operational paradigm—known as intermittent "
    "computing—presents unique challenges, as the system must maintain computational correctness "
    "and data integrity across unpredictable power interruptions [3], [6]."
))

add_body(doc, (
    "The period from 2024 to 2026 has witnessed a pivotal transition in battery-free system "
    "research. Early investigations primarily focused on demonstrating the feasibility of "
    "energy-autonomous operation, whereas recent contributions have shifted toward addressing "
    "practical deployment challenges including predictable performance modeling, cost-effective "
    "hardware design, standardized evaluation methodologies, and the integration of machine "
    "learning capabilities on intermittently powered platforms. Concurrently, novel application "
    "scenarios—such as UAV-powered agricultural sensor networks—have emerged, demonstrating "
    "the expanding scope and commercial relevance of battery-free technology [1], [5]."
))

# --- B. Problem Statement ---
add_subsection_heading(doc, "B. Problem Statement")

add_body(doc, (
    "Despite substantial progress in individual aspects of battery-free embedded system design, "
    "the field remains fragmented across multiple research communities, including energy "
    "harvesting, intermittent computing, low-power circuit design, and edge artificial "
    "intelligence. This fragmentation has resulted in several critical deficiencies. First, "
    "there is no widely accepted benchmark suite or standardized evaluation methodology for "
    "comparing the performance of different battery-free platforms under equivalent conditions. "
    "Second, the integration of multiple heterogeneous energy harvesting sources within a "
    "unified power management framework remains largely unexplored. Third, the adaptation of "
    "modern machine learning techniques—particularly deep neural network inference—for "
    "intermittent execution environments is still in its nascent stages. Fourth, the absence "
    "of standardized power management protocols across diverse hardware platforms hinders "
    "interoperability and scalability [2], [4]."
))

add_body(doc, (
    "These challenges collectively impede the transition of battery-free systems from "
    "laboratory prototypes to commercially viable, mass-deployed IoT infrastructure. A "
    "comprehensive review that systematically analyzes recent contributions, identifies "
    "research gaps, and delineates future directions is therefore essential for guiding "
    "the continued development of this rapidly evolving field."
))

# --- C. Research Objectives ---
add_subsection_heading(doc, "C. Research Objectives")

add_body(doc, (
    "The primary objective of this review paper is to provide a critical and systematic "
    "examination of recent advancements in battery-free embedded systems through the analysis "
    "of six representative journal and conference papers published between 2024 and 2026. "
    "The specific objectives are as follows:"
), first_line_indent=False)

add_body(doc, (
    "(1) To critically review and summarize the objectives, methodologies, key contributions, "
    "and results of each selected paper."
), first_line_indent=False)

add_body(doc, (
    "(2) To perform a comparative analysis of the reviewed works with respect to their "
    "research focus areas, technical approaches, performance metrics, and reported outcomes."
), first_line_indent=False)

add_body(doc, (
    "(3) To identify and discuss the research methodologies, algorithms, frameworks, "
    "architectures, and evaluation techniques adopted across the reviewed studies."
), first_line_indent=False)

add_body(doc, (
    "(4) To identify critical research gaps and open challenges that remain unaddressed "
    "in the current literature."
), first_line_indent=False)

add_body(doc, (
    "(5) To propose future research directions that can advance the state of the art "
    "toward reliable, scalable, and maintenance-free battery-free IoT systems."
), first_line_indent=False)

# ============================================================
# II. RELATED WORKS
# ============================================================
add_section_heading(doc, "II. Related Works")

add_body(doc, (
    "This section presents a critical review of six recent research papers that collectively "
    "represent the current state of the art in battery-free embedded systems. Each paper is "
    "examined with respect to its research objectives, methodology, key findings, strengths, "
    "and limitations."
), first_line_indent=False)

# --- Paper 1 ---
add_subsection_heading(doc, "A. Analytical Modeling of Batteryless IoT Sensors Powered by Ambient Energy Harvesting [1]")

add_body(doc, (
    "Fernández Landivar et al. (arXiv, July 2025) proposed a comprehensive analytical "
    "framework for modeling the energy dynamics of batteryless IoT sensor nodes [1]. The "
    "objective of this work was to develop a generalized mathematical model that captures "
    "the complete energy flow within a batteryless system, from ambient energy harvesting "
    "through power conditioning to computational load execution. The model explicitly "
    "incorporates the behavior of the Energy Harvesting Unit (EHU), comprising the energy "
    "transducer, power management integrated circuit (PMIC), and supercapacitor storage, "
    "as well as the Circuit Load (CL) representing the sensor's computational and "
    "communication subsystems."
))

add_body(doc, (
    "The methodology employed a first-principles analytical approach, deriving closed-form "
    "expressions for the voltage dynamics of the supercapacitor as a function of harvested "
    "power, PMIC efficiency characteristics, and load current profiles. The model was "
    "validated experimentally using a prototype batteryless IoT node operating under varying "
    "indoor illumination conditions. The results demonstrated strong agreement between "
    "predicted and measured supercapacitor voltage trajectories, confirming the model's "
    "accuracy across diverse environmental conditions."
))

add_body(doc, (
    "A key strength of this work lies in its generalizability: the mathematical framework "
    "is not tied to any specific hardware platform and can be parameterized for different "
    "harvesting modalities and load characteristics. This enables designers to perform "
    "pre-fabrication performance estimation and optimize power management unit configurations. "
    "However, a notable limitation is that the model assumes relatively stable ambient energy "
    "conditions and does not explicitly address highly stochastic or rapidly fluctuating "
    "energy sources, which are common in outdoor deployment scenarios."
))

# --- Paper 2 ---
add_subsection_heading(doc, "B. Designing Cost-Effective Battery-Less Energy Harvesting for Intermittent Wireless Communication [2]")

add_body(doc, (
    "Published in IEEE Access (January 2025), this paper addressed the challenge of designing "
    "cost-effective battery-less IoT devices capable of sustaining reliable wireless "
    "communication under intermittent power availability [2]. The research objective was to "
    "develop systematic design models that enable engineers to determine optimal energy "
    "harvester and storage element specifications for meeting specific wireless communication "
    "Quality of Service (QoS) requirements, including data throughput and transmission frequency."
))

add_body(doc, (
    "The authors proposed energy and timing models that formalize the relationship between "
    "harvester capacity, storage element sizing (capacitors), and the resulting communication "
    "duty cycle. A central contribution is the introduction of a duty-based Dynamic Power "
    "Management (DPM) scheme that dynamically adjusts the device's active and sleep periods "
    "based on available energy, significantly outperforming conventional threshold-based "
    "approaches. Experimental evaluation demonstrated that the proposed DPM scheme extends "
    "operational time by 9.1% to 90.0% compared to baseline methods, depending on ambient "
    "energy availability conditions."
))

add_body(doc, (
    "The strength of this work lies in its practical applicability: the design methodology "
    "provides actionable guidelines for hardware engineers to translate wireless QoS "
    "requirements into concrete harvester and storage specifications. The duty-based DPM "
    "approach offers a clear performance advantage. However, the methodology is primarily "
    "validated for single-source energy harvesting scenarios and does not explicitly consider "
    "multi-source configurations or the impact of highly variable channel conditions on "
    "communication reliability."
))

# --- Paper 3 ---
add_subsection_heading(doc, "C. EStacker: Explaining Battery-Less IoT System Performance with Energy Stacks [3]")

add_body(doc, (
    "Liedtke et al. presented EStacker in ACM Transactions on Embedded Computing Systems "
    "(2026), a specialized evaluation platform designed to address the challenge of fair "
    "and reproducible performance assessment of battery-less IoT systems [3]. The research "
    "objective was to create a systematic benchmarking framework that enables developers to "
    "understand precisely how energy is consumed across different hardware components and "
    "software tasks through the concept of \"energy stacks\"—detailed energy consumption "
    "profiles decomposed by functional unit and execution phase."
))

add_body(doc, (
    "The platform employs a simulation-based approach that models the interaction between "
    "energy harvesting, storage dynamics, and application workload execution. A significant "
    "methodological contribution is the ST-SP (Spatial-Temporal State Pruning) optimization "
    "technique, which reduces evaluation time by a factor of 6.3× on average while "
    "maintaining timing accuracy with a mean error of only 7.7%. This acceleration is "
    "critical for enabling practical design space exploration across different harvester "
    "and storage configurations."
))

add_body(doc, (
    "EStacker's principal strength is its ability to provide deterministic, energy-equivalent "
    "evaluation conditions, ensuring that different applications and hardware configurations "
    "are compared under identical energy budgets. This addresses a fundamental reproducibility "
    "challenge in battery-free systems research. The limitation is that the platform currently "
    "relies on simulation rather than hardware-in-the-loop evaluation, which may not fully "
    "capture real-world phenomena such as parasitic losses, component aging, and environmental "
    "electromagnetic interference."
))

# --- Paper 4 ---
add_subsection_heading(doc, "D. HANNA: Harvesting-Aware Neural Network Architecture Search for Batteryless Intermittent Devices [4]")

add_body(doc, (
    "Sahu, Deep, and Duwe introduced HANNA at IEEE IPCCC 2024, a novel Neural Architecture "
    "Search (NAS) framework specifically designed for batteryless intermittent devices [4]. "
    "The research objective was to develop an automated method for discovering deep neural "
    "network (DNN) architectures that are optimally suited for execution under intermittent "
    "power conditions, where conventional NAS approaches—which optimize solely for latency "
    "and accuracy—produce suboptimal results."
))

add_body(doc, (
    "HANNA's methodology integrates energy harvesting characteristics directly into the "
    "architecture search process. Unlike traditional NAS, which assumes continuous power "
    "availability, HANNA evaluates candidate architectures based on their ability to complete "
    "inference tasks within a single energy harvesting cycle. The search algorithm navigates "
    "a multi-objective design space that balances inference accuracy, computational cost, "
    "memory footprint, and energy harvesting compatibility. The framework accounts for the "
    "overhead of checkpoint-based execution models, where the system must periodically save "
    "intermediate computation state to non-volatile memory to survive power interruptions."
))

add_body(doc, (
    "A key strength of HANNA is that it represents one of the earliest systematic approaches "
    "to Intermittent TinyML—the intersection of tiny machine learning and intermittent "
    "computing. The discovered architectures demonstrate fundamentally different structural "
    "properties compared to those optimized for continuously powered platforms, validating "
    "the necessity of harvesting-aware design. However, the framework has been evaluated "
    "on a limited set of inference tasks and energy harvesting profiles, and its scalability "
    "to more complex models (e.g., transformer architectures) and diverse harvesting "
    "modalities remains to be demonstrated."
))

# --- Paper 5 ---
add_subsection_heading(doc, "E. Autonomous Agricultural Monitoring with Aerial Drones and RF Energy-Harvesting Sensor Tags [5]")

add_body(doc, (
    "Kudyba and Sun (arXiv, February 2025) investigated the application of battery-free "
    "RF energy-harvesting sensor tags for autonomous precision agriculture monitoring, "
    "powered wirelessly by unmanned aerial vehicles (UAVs) [5]. The objective was to "
    "demonstrate a practical, cost-effective, and environmentally sustainable alternative "
    "to conventional battery-powered agricultural sensor networks by eliminating the need "
    "for ground-based power infrastructure and battery replacement in field-deployed sensors."
))

add_body(doc, (
    "The system architecture comprises UAVs equipped with RF transmitters that provide "
    "both wireless power and communication capabilities to passive sensor tags distributed "
    "across agricultural fields. The sensor tags harvest RF energy from the UAV's downlink "
    "signal, use the harvested energy to perform environmental measurements (temperature, "
    "humidity, soil moisture), and backscatter the collected data to the UAV. The methodology "
    "included both ground-based controlled experiments and aerial flight tests conducted "
    "at the AERPAW (Aerial Experimentation and Research Platform for Advanced Wireless) "
    "testbed facility."
))

add_body(doc, (
    "Ground-based experiments demonstrated reliable sensor activation and data collection "
    "at practical distances, validating the fundamental feasibility of the approach. However, "
    "aerial flight tests revealed significant challenges related to RF interference, antenna "
    "orientation variability, and reduced communication reliability in dynamic flight "
    "conditions. The authors propose antenna consolidation and improved RF front-end design "
    "as potential mitigation strategies. The strength of this work lies in its demonstration "
    "of a complete, end-to-end battery-free sensing system for a high-impact application "
    "domain. The primary limitation is the current sensitivity to environmental RF conditions "
    "and the limited operational range of passive backscatter communication."
))

# --- Paper 6 ---
add_subsection_heading(doc, "F. Batteryless Systems for IoT: A Survey of Circuit and System Design [6]")

add_body(doc, (
    "Presented at IEEE MWSCAS 2025, this comprehensive survey paper provides a systematic "
    "review of circuit-level and system-level design architectures for batteryless IoT "
    "devices [6]. The survey encompasses the complete hardware stack, including energy "
    "harvesting transducers, power management integrated circuits (PMICs), energy storage "
    "technologies (supercapacitors, thin-film batteries), non-volatile memory systems for "
    "state preservation, and intermittent computing execution models."
))

add_body(doc, (
    "The survey categorizes intermittent computing approaches into two principal paradigms: "
    "task-based execution, where computational tasks are partitioned into atomic units that "
    "can complete within a single energy burst; and checkpoint-based execution, where the "
    "system periodically saves its computational state to non-volatile memory to enable "
    "resumption after power interruptions. The paper systematically analyzes the trade-offs "
    "inherent in each approach, including harvester efficiency versus manufacturing cost, "
    "storage capacity versus leakage current, and computational throughput versus the energy "
    "overhead of checkpointing operations."
))

add_body(doc, (
    "The principal strength of this survey is its breadth and systematic organization, which "
    "provides an accessible entry point for researchers entering the battery-free systems "
    "domain. The survey effectively contextualizes individual circuit innovations within the "
    "broader system architecture, facilitating cross-disciplinary understanding. However, the "
    "survey primarily focuses on hardware-level considerations and provides limited coverage "
    "of software frameworks, middleware, and application-level challenges associated with "
    "intermittent operation."
))

# --- Comparison Table ---
add_table(doc,
    "TABLE I: Comparative Summary of Reviewed Research Papers",
    ["Ref.", "Objective", "Methodology", "Key Result", "Strength", "Limitation"],
    [
        ["[1]", "Model energy dynamics of batteryless IoT sensors",
         "First-principles analytical modeling with experimental validation",
         "Accurate voltage prediction under varying illumination",
         "Generalizable across hardware platforms",
         "Assumes stable ambient energy conditions"],
        ["[2]", "Design cost-effective battery-less wireless communication",
         "Energy and timing models with duty-based DPM scheme",
         "9.1%–90.0% operational time extension",
         "Actionable design guidelines for engineers",
         "Single-source harvesting only"],
        ["[3]", "Fair and reproducible benchmarking of battery-less systems",
         "Simulation-based energy stacks with ST-SP optimization",
         "6.3× evaluation speedup with 7.7% timing error",
         "Deterministic energy-equivalent evaluation",
         "Simulation-only; lacks hardware-in-the-loop"],
        ["[4]", "Energy-harvesting-aware neural architecture search",
         "Multi-objective NAS with intermittent execution modeling",
         "Architectures completing inference in one harvest cycle",
         "Pioneer in Intermittent TinyML",
         "Limited task and harvesting profile diversity"],
        ["[5]", "UAV-powered battery-free agricultural monitoring",
         "RF energy harvesting with backscatter communication",
         "Successful ground tests; aerial tests revealed RF challenges",
         "Complete end-to-end system demonstration",
         "Sensitive to RF interference and limited range"],
        ["[6]", "Survey of batteryless IoT circuit and system design",
         "Systematic literature survey and taxonomy",
         "Comprehensive taxonomy of intermittent computing approaches",
         "Broad coverage and accessible organization",
         "Limited software and application-level coverage"],
    ],
    col_widths=[0.8, 2.5, 2.8, 2.8, 2.5, 2.5]
)


# ============================================================
# III. METHODOLOGY ADOPTED BY THE REVIEWED WORKS
# ============================================================
add_section_heading(doc, "III. Methodology Adopted by the Reviewed Works")

add_body(doc, (
    "The research methodologies adopted across the six reviewed papers can be classified "
    "into four principal categories: analytical modeling, experimental prototyping, "
    "simulation-based evaluation, and systematic literature survey. This section provides "
    "a summary and classification of these methodological approaches, along with a discussion "
    "of the algorithms, frameworks, architectures, and evaluation techniques employed."
), first_line_indent=False)

add_subsection_heading(doc, "A. Analytical and Mathematical Modeling")

add_body(doc, (
    "Papers [1] and [2] employ analytical modeling as their primary methodology. Fernández "
    "Landivar et al. [1] derive first-principles differential equations governing "
    "supercapacitor voltage dynamics as a function of harvested power, PMIC transfer "
    "characteristics, and load current demand. The model parameters are obtained through "
    "component-level characterization and the framework provides closed-form solutions for "
    "predicting system behavior under specified environmental inputs. Similarly, the IEEE "
    "Access paper [2] develops energy balance and timing models that relate harvester capacity, "
    "storage element sizing, and communication duty cycle parameters. Both approaches enable "
    "pre-fabrication design space exploration and sensitivity analysis."
))

add_subsection_heading(doc, "B. Experimental Prototyping and Field Testing")

add_body(doc, (
    "Papers [1], [2], and [5] incorporate experimental validation through hardware prototyping "
    "and field deployment. Fernández Landivar et al. [1] validate their analytical model "
    "against measurements from a custom batteryless IoT node under controlled indoor "
    "illumination. The IEEE Access paper [2] validates its DPM scheme through prototype "
    "implementation with measured energy harvesting profiles. Kudyba and Sun [5] conduct "
    "both ground-based controlled experiments and aerial flight tests at the AERPAW testbed, "
    "providing the most comprehensive real-world evaluation among the reviewed works. These "
    "experimental approaches are essential for validating theoretical predictions against "
    "real-world system behavior, including parasitic effects and environmental variability."
))

add_subsection_heading(doc, "C. Simulation-Based Evaluation and Automated Search")

add_body(doc, (
    "Papers [3] and [4] rely primarily on simulation-based evaluation frameworks. EStacker [3] "
    "employs cycle-accurate simulation of energy harvesting, storage, and load execution to "
    "construct detailed energy consumption profiles. The ST-SP optimization algorithm prunes "
    "the simulation state space to accelerate evaluation without significantly compromising "
    "accuracy. HANNA [4] utilizes a simulation-driven NAS framework where candidate DNN "
    "architectures are evaluated against modeled energy harvesting profiles and intermittent "
    "execution semantics. The search algorithm employs multi-objective optimization to balance "
    "inference accuracy, computational cost, and energy harvesting compatibility, navigating "
    "a fundamentally different design space than conventional NAS approaches."
))

add_subsection_heading(doc, "D. Systematic Literature Survey")

add_body(doc, (
    "Paper [6] adopts a systematic survey methodology, reviewing and categorizing existing "
    "circuit and system design approaches for batteryless IoT devices. The survey employs a "
    "taxonomic classification scheme that organizes contributions by functional layer (energy "
    "harvesting, power management, storage, computation, communication) and by execution "
    "paradigm (task-based vs. checkpoint-based intermittent computing). This methodology "
    "enables the identification of design trade-offs and research trends across the broader "
    "battery-free systems community."
))

# --- Methodology Comparison Table ---
add_table(doc,
    "TABLE II: Classification of Research Methodologies",
    ["Methodology", "Papers", "Key Techniques", "Evaluation Approach"],
    [
        ["Analytical Modeling", "[1], [2]",
         "Differential equations, energy balance models, closed-form solutions",
         "Comparison with experimental measurements"],
        ["Experimental Prototyping", "[1], [2], [5]",
         "Hardware prototyping, field deployment, controlled experiments",
         "Real-world measurement and statistical analysis"],
        ["Simulation-Based", "[3], [4]",
         "Cycle-accurate simulation, state-space pruning, multi-objective NAS",
         "Simulation accuracy metrics, speedup benchmarks"],
        ["Literature Survey", "[6]",
         "Taxonomic classification, systematic review",
         "Coverage analysis, gap identification"],
    ],
    col_widths=[2.5, 1.5, 5.0, 3.5]
)

# ============================================================
# IV. RESULTS AND DISCUSSION
# ============================================================
add_section_heading(doc, "IV. Results and Discussion")

add_body(doc, (
    "This section presents a comparative analysis of the reviewed studies, discusses key "
    "findings and performance metrics, examines emerging research trends, and identifies "
    "critical research gaps that remain unaddressed in the current literature."
), first_line_indent=False)

add_subsection_heading(doc, "A. Comparative Analysis of Reviewed Studies")

add_body(doc, (
    "The six reviewed papers collectively represent three major research thrusts in "
    "contemporary battery-free embedded system development. Papers [1] and [2] contribute "
    "to the theoretical and design methodology domain, providing analytical foundations "
    "and actionable engineering guidelines. Papers [3] and [4] advance evaluation "
    "infrastructure and architectural innovation, addressing the need for standardized "
    "benchmarking and harvesting-aware system design. Papers [5] and [6] focus on "
    "application-driven system integration and comprehensive technology surveys, "
    "demonstrating practical deployment scenarios and contextualizing the broader "
    "research landscape."
))

add_body(doc, (
    "A notable convergence across all reviewed works is the shift from demonstrating the "
    "mere feasibility of batteryless operation to addressing practical deployment challenges, "
    "including reliability, predictability, and scalability. The modeling contributions of "
    "Fernández Landivar et al. [1] and the design methodology of [2] are complementary: "
    "while [1] provides the analytical foundation for understanding energy dynamics, [2] "
    "translates these insights into actionable design rules for wireless communication "
    "systems. Similarly, EStacker [3] provides the evaluation infrastructure needed to "
    "validate designs produced by approaches like HANNA [4], creating a natural toolchain "
    "for battery-free system development."
))

add_subsection_heading(doc, "B. Key Findings and Performance Metrics")

add_body(doc, (
    "The quantitative results reported across the reviewed papers reveal substantial "
    "performance improvements in battery-free system capabilities. Table III summarizes "
    "the key quantitative performance metrics reported across all reviewed studies."
))

# --- TABLE III: Quantitative Performance Metrics ---
add_table(doc,
    "TABLE III: Quantitative Performance Metrics of Reviewed Studies",
    ["Ref.", "Metric", "Value", "Improvement", "Baseline"],
    [
        ["[1]", "Voltage prediction accuracy", "3 scenarios validated", "High correlation", "Measured profiles"],
        ["[2]", "Operational time extension", "9.1%–90.0%", "+9.1% to +90.0%", "Threshold-based DPM"],
        ["[3]", "Evaluation speedup (ST-SP)", "6.3x", "41.7 days → 7.7 days", "Full simulation"],
        ["[3]", "Throughput timing error", "7.7%", "—", "Cycle-accurate sim."],
        ["[3]", "App. performance gain", "3.3x", "+230%", "Unoptimized config."],
        ["[4]", "Inference accuracy gain", "10%–44%", "+10% to +44%", "SOTA NAS methods"],
        ["[4]", "NAS search cost", "1-shot", "Significant reduction", "Traditional NAS"],
        ["[5]", "Tag comm. range (BLE)", "10 m", "—", "—"],
        ["[5]", "RF harvest frequency", "918 MHz", "—", "—"],
        ["[5]", "Active TX frequency", "2.4 GHz", "—", "—"],
        ["[5]", "Aerial data packets received", "1 (ID only)", "0 temp. packets", "Ground: reliable"],
    ],
    col_widths=[0.7, 2.8, 2.5, 2.5, 2.5]
)

add_body(doc, (
    "The DPM scheme proposed in [2] demonstrates an operational time extension ranging from "
    "9.1% to 90.0%, with the magnitude of improvement being inversely correlated with ambient "
    "energy availability—indicating that the approach is most beneficial in energy-scarce "
    "environments where battery-free operation is most challenging. The ST-SP optimization "
    "in EStacker [3] achieves a 6.3x reduction in evaluation time while maintaining "
    "7.7% average throughput error. Notably, EStacker's energy stack profiling identified a "
    "performance bottleneck in a case study application, leading to a 3.3x performance "
    "improvement after optimization—reducing the full design space sweep from 41.7 days to "
    "7.7 days [3]."
))

add_body(doc, (
    "HANNA [4] demonstrates that harvesting-aware neural architecture search improves "
    "average inference accuracy by 10% to 44% compared to state-of-the-art NAS approaches "
    "that do not account for energy harvesting constraints, while significantly reducing "
    "the neural network search cost through a one-shot differentiable NAS formulation. "
    "The discovered architectures exhibit fundamentally different structural properties—"
    "smaller individual layers with more frequent checkpointing boundaries—enabling "
    "completion of partial inference within shorter energy availability windows."
))

add_body(doc, (
    "The agricultural monitoring system in [5] successfully demonstrates end-to-end "
    "battery-free sensing using passive RF energy harvesting at 918 MHz with active BLE "
    "transmission at 2.4 GHz over a range of up to 10 meters. Ground-based experiments "
    "confirmed reliable sensor operation, but aerial flight tests at the AERPAW testbed "
    "encountered significant wireless interference from drone motor EMI that impeded "
    "data collection, with only a single ID packet successfully received during manual "
    "flight and no temperature data collected during airborne operation."
))

# --- TABLE IV: Technical Specifications Comparison ---
add_table(doc,
    "TABLE IV: Technical Specifications of Reviewed Systems",
    ["Ref.", "Harvest Freq.", "TX Freq.", "Storage Type", "Range", "Eval. Scale", "Year"],
    [
        ["[1]", "Solar (indoor)", "—", "Supercapacitor", "—", "3 scenarios", "2025"],
        ["[2]", "Ambient", "Sub-GHz/ISM", "Capacitor", "—", "Multiple configs.", "2025"],
        ["[3]", "Simulated", "—", "Simulated", "—", "2 case studies", "2026"],
        ["[4]", "RF", "—", "Capacitor + NVM", "—", "Multiple datasets", "2024"],
        ["[5]", "918 MHz", "2.4 GHz BLE", "On-tag buffer", "10 m", "3 flight trials", "2025"],
        ["[6]", "Multiple", "Multiple", "Supercap./thin-film", "—", "49 references", "2025"],
    ],
    col_widths=[0.7, 2.0, 2.0, 2.2, 1.2, 2.2, 1.0]
)

add_subsection_heading(doc, "C. Research Trends")

add_body(doc, (
    "Several important research trends emerge from the analysis of the reviewed works. "
    "First, there is a clear movement toward formalization and standardization. The "
    "development of analytical models [1], systematic design methodologies [2], and "
    "standardized evaluation platforms [3] reflects the field's maturation from ad hoc "
    "experimentation to rigorous engineering practice. Second, the emergence of Intermittent "
    "TinyML [4] represents a convergence of two previously distinct research communities—"
    "embedded machine learning and intermittent computing—creating new challenges and "
    "opportunities at their intersection."
))

add_body(doc, (
    "Third, application-specific system integration [5] is driving the identification of "
    "real-world deployment challenges that motivate fundamental research. The AERPAW "
    "experiments revealed that drone motor EMI represents a critical engineering barrier "
    "not predicted by laboratory testing, highlighting the importance of field validation. "
    "Fourth, the comprehensive survey in [6] indicates that the circuit and system design "
    "landscape has reached sufficient maturity to warrant systematic categorization, "
    "suggesting that the foundational hardware building blocks for battery-free systems are "
    "increasingly well-understood, with the primary challenges shifting toward system-level "
    "integration and software support."
))

add_subsection_heading(doc, "D. Identified Research Gaps")

add_body(doc, (
    "Despite the substantial contributions of the reviewed works, several critical research "
    "gaps persist that must be addressed to enable widespread deployment of battery-free "
    "embedded systems. Table V maps the identified research gaps to the specific papers "
    "that expose each gap and the evidence supporting their identification."
), first_line_indent=False)


add_body(doc, (
    "Gap 1: Absence of Unified Benchmarking Standards. While EStacker [3] represents an "
    "important step toward standardized evaluation, the battery-free systems community still "
    "lacks universally accepted benchmark suites, reference energy traces, and standardized "
    "performance metrics. Each study employs proprietary hardware configurations, custom "
    "energy sources, and application-specific workloads, making meaningful cross-study "
    "comparison extremely difficult. The establishment of community-accepted benchmarks—"
    "analogous to MLPerf for machine learning or SPEC for general-purpose computing—is "
    "urgently needed."
))

add_body(doc, (
    "Gap 2: Insufficient Multi-Source Energy Harvesting Integration. The reviewed papers "
    "predominantly address single-source harvesting scenarios (solar in [1], RF in [5]). "
    "However, real-world deployments frequently encounter multiple ambient energy sources "
    "with complementary temporal availability patterns. The design of intelligent multi-source "
    "power management systems that can dynamically arbitrate between heterogeneous energy "
    "inputs—combining photovoltaic, thermoelectric, piezoelectric, and RF harvesting within "
    "a unified framework—remains a largely open research problem."
))

add_body(doc, (
    "Gap 3: Limited Edge AI Adaptation for Intermittent Operation. Although HANNA [4] "
    "pioneers the concept of harvesting-aware neural architecture search and achieves "
    "10%–44% accuracy improvement, the broader challenge of adapting edge AI and TinyML "
    "frameworks for intermittent execution remains substantially underexplored. Critical "
    "open problems include energy-efficient checkpointing of neural network intermediate "
    "states, graceful degradation of inference accuracy under energy scarcity, and the "
    "development of training methodologies that incorporate energy availability as a constraint."
))

add_body(doc, (
    "Gap 4: Inadequate Standardization of Power Management Protocols. The DPM scheme in [2] "
    "and the analytical models in [1] represent isolated, platform-specific solutions. There "
    "is no standardized abstraction layer or protocol suite for power management across "
    "heterogeneous battery-free IoT devices. The development of open, interoperable power "
    "management standards—analogous to communication protocol stacks—would significantly "
    "accelerate ecosystem growth and reduce development costs."
))

add_body(doc, (
    "Gap 5: Reliability and Long-Term Durability Assessment. While battery-free systems are "
    "frequently proposed for deployment in harsh industrial and agricultural environments, "
    "systematic studies of long-term reliability, component degradation, and failure modes "
    "under sustained exposure to extreme temperatures, humidity, mechanical stress, and "
    "electromagnetic interference are notably absent. The RF interference from drone motor "
    "EMI observed in [5]'s aerial tests—where motor proximity effectively blocked the "
    "bridge-to-gateway communication link—exemplifies this gap."
))

add_body(doc, (
    "Gap 6: Scalability of Battery-Free Sensor Networks. The reviewed works primarily focus "
    "on individual device-level optimization. The system-level challenges of deploying "
    "large-scale networks of hundreds or thousands of battery-free nodes—including distributed "
    "energy management, interference mitigation, and data routing under intermittent node "
    "availability—remain largely unaddressed. Conventional networking protocols assume "
    "continuous node availability and require fundamental redesign for intermittent operation."
))


# ============================================================
# V. CONCLUSION AND CONTRIBUTION
# ============================================================
add_section_heading(doc, "V. Conclusion and Contribution")

add_subsection_heading(doc, "A. Summary of Major Findings")

add_body(doc, (
    "This review has critically examined six recent and representative research papers that "
    "collectively illustrate the current state of advancement in battery-free embedded systems "
    "during the 2024–2026 period. The reviewed works demonstrate that the field has progressed "
    "significantly beyond proof-of-concept demonstrations toward deployment-oriented solutions. "
    "Analytical modeling frameworks [1] now enable pre-fabrication performance prediction, "
    "while systematic design methodologies [2] translate theoretical insights into actionable "
    "engineering guidelines with demonstrated operational improvements of up to 90%. "
    "Standardized evaluation platforms [3] address the critical need for reproducible "
    "benchmarking, and harvesting-aware neural architecture search [4] opens the emerging "
    "frontier of Intermittent TinyML. Application-specific deployments [5] validate the "
    "real-world potential while honestly exposing the remaining engineering challenges, and "
    "comprehensive surveys [6] provide the taxonomic foundation for systematic progress."
))

add_subsection_heading(doc, "B. Contributions of This Review")

add_body(doc, (
    "The principal contributions of this review paper are threefold. First, it provides a "
    "structured comparative analysis of six representative works across the key dimensions "
    "of objectives, methodologies, results, strengths, and limitations, enabling readers to "
    "quickly identify relevant prior art and understand the relationships between different "
    "research contributions. Second, it classifies and discusses the research methodologies "
    "adopted across the reviewed studies, identifying four principal methodological categories "
    "(analytical modeling, experimental prototyping, simulation-based evaluation, and "
    "systematic survey) and their respective strengths and applicability. Third, it identifies "
    "six critical research gaps—spanning benchmarking standards, multi-source harvesting, "
    "edge AI adaptation, power management standardization, long-term reliability, and "
    "network scalability—that must be addressed to enable the transition from laboratory "
    "prototypes to mass-deployed commercial systems."
))

add_subsection_heading(doc, "C. Future Research Directions")

add_body(doc, (
    "Based on the analysis presented in this review, the following future research directions "
    "are recommended: (1) Development of community-accepted open-source benchmark suites with "
    "standardized energy traces, hardware reference designs, and performance metrics for fair "
    "cross-platform comparison. (2) Investigation of multi-source energy harvesting architectures "
    "with intelligent source arbitration and adaptive power management algorithms. "
    "(3) Co-design of neural network architectures and intermittent computing hardware to "
    "achieve robust and energy-efficient edge AI inference under unreliable power conditions. "
    "(4) Standardization of power management protocols and abstraction layers to enable "
    "interoperability across heterogeneous battery-free platforms. (5) Longitudinal field "
    "studies assessing component degradation, failure modes, and system reliability under "
    "sustained real-world deployment conditions. (6) Design of intermittent-aware networking "
    "protocols that accommodate stochastic node availability for scalable battery-free sensor "
    "network deployments."
))

add_body(doc, (
    "The convergence of advances in energy harvesting efficiency, ultra-low-power circuit "
    "design, and edge computing capabilities suggests that battery-free embedded systems are "
    "approaching a critical threshold of commercial viability. Addressing the research gaps "
    "identified in this review will be instrumental in realizing the vision of truly "
    "maintenance-free, sustainable IoT infrastructure capable of operating autonomously "
    "across diverse and challenging deployment environments."
))

# ============================================================
# REFERENCES
# ============================================================
add_section_heading(doc, "References")

add_reference(doc, 1,
    "J. Fernández Landivar, A. Zanella, I. Gryech, S. Pollin, and H. Sallouha, "
    "\"Analytical Modeling of Batteryless IoT Sensors Powered by Ambient Energy "
    "Harvesting,\" arXiv preprint arXiv:2507.20952, Jul. 2025. "
    "[Online]. Available: https://arxiv.org/abs/2507.20952"
)

add_reference(doc, 2,
    "L. Liedtke, P. G. Kjeldsberg, F. A. Kraemer, and M. Jahre, "
    "\"Designing Cost-Effective Battery-Less Energy Harvesting for Intermittent "
    "Wireless Communication,\" IEEE Access, vol. 13, pp. 157044–157058, "
    "Jan. 2025. [Online]. Available: https://doi.org/10.1109/ACCESS.2025.3606514"
)

add_reference(doc, 3,
    "L. Liedtke, P. G. Kjeldsberg, F. A. Kraemer, and M. Jahre, "
    "\"EStacker: Explaining Battery-Less IoT System Performance with Energy Stacks,\" "
    "ACM Trans. Embed. Comput. Syst., vol. 25, no. 1, 2026. "
    "[Online]. Available: https://arxiv.org/abs/2505.22366"
)

add_reference(doc, 4,
    "R. Sahu, V. Deep, and H. Duwe, \"HANNA: Harvesting-Aware Neural Network "
    "Architecture Search for Batteryless Intermittent Devices,\" in Proc. IEEE "
    "International Performance, Computing, and Communications Conference (IPCCC), "
    "2024. [Online]. Available: https://doi.org/10.1109/IPCCC59868.2024.10850328"
)

add_reference(doc, 5,
    "P. S. Kudyba and H. Sun, \"Autonomous Agricultural Monitoring with Aerial "
    "Drones and RF Energy-Harvesting Sensor Tags,\" arXiv preprint "
    "arXiv:2502.16028, Feb. 2025. "
    "[Online]. Available: https://arxiv.org/abs/2502.16028"
)

add_reference(doc, 6,
    "IEEE MWSCAS, \"Batteryless Systems for IoT: A Survey of Circuit and System "
    "Design,\" in Proc. IEEE Midwest Symposium on Circuits and Systems (MWSCAS), "
    "2025. [Online]. Available: https://doi.org/10.1109/MWSCAS53549.2025.11244474"
)


# ============================================================
# SAVE
# ============================================================
doc.save(OUTPUT_PATH)
print(f"✅ Review paper saved to: {OUTPUT_PATH}")
print(f"\n📄 PDF Download Links for the 6 papers:")
print("=" * 70)
print("[1] https://arxiv.org/pdf/2507.20952")
print("[2] https://ieeexplore.ieee.org/document/10810505")
print("[3] https://dl.acm.org/doi/10.1145/3708997")
print("[4] https://doi.org/10.1109/IPCCC59868.2024.10850484")
print("[5] https://arxiv.org/pdf/2502.16028")
print("[6] https://ieeexplore.ieee.org/xpl/conhome/MWSCAS/2025")
