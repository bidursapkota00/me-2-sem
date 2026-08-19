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

def add_body_with_highlight(doc, normal_text, highlight_text, after_text=""):
    """Add paragraph with bold text for research gaps."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Cm(0.5)

    if normal_text:
        run1 = p.add_run(normal_text)
        run1.font.size = Pt(10)
        run1.font.name = 'Times New Roman'

    run2 = p.add_run(highlight_text)
    run2.font.size = Pt(10)
    run2.font.name = 'Times New Roman'
    run2.bold = True

    if after_text:
        run3 = p.add_run(after_text)
        run3.font.size = Pt(10)
        run3.font.name = 'Times New Roman'
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

def add_table_paper_summary(doc):
    """Add a summary table of the 6 reviewed papers."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run("TABLE I: Summary of Reviewed Research Papers")
    run.bold = True
    run.font.size = Pt(8)
    run.font.name = 'Times New Roman'

    table = doc.add_table(rows=7, cols=4)
    table.style = 'Table Grid'

    headers = ["Ref.", "Paper Title", "Key Contribution", "Year"]
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = header
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.bold = True
                run.font.size = Pt(7)
                run.font.name = 'Times New Roman'

    data = [
        ["[1]", "Analytical Modeling of Batteryless IoT Sensors Powered by Ambient Energy Harvesting",
         "Mathematical framework for energy dynamics modeling of batteryless IoT nodes with power management", "2025"],
        ["[2]", "Designing Cost-Effective Battery-Less Energy Harvesting for Intermittent Wireless Communication",
         "Duty-based DPM scheme extending operation time by 9.1%–90.0%", "2025"],
        ["[3]", "EStacker: Explaining Battery-Less IoT System Performance with Energy Stacks",
         "Fair evaluation platform with 6.3× speedup via ST-SP optimization", "2026"],
        ["[4]", "HANNA: Harvesting-Aware Neural Network Architecture Search for Batteryless Intermittent Devices",
         "Energy-harvesting-aware NAS for adaptive DNN inference on batteryless devices", "2024"],
        ["[5]", "Autonomous Agricultural Monitoring with Aerial Drones and RF Energy-Harvesting Sensor Tags",
         "UAV-powered battery-free precision agriculture sensor system", "2025"],
        ["[6]", "Batteryless Systems for IoT: A Survey of Circuit and System Design (MWSCAS 2025)",
         "Comprehensive circuit-level survey of intermittent computing architectures", "2025"],
    ]

    for row_idx, row_data in enumerate(data, 1):
        for col_idx, value in enumerate(row_data):
            cell = table.rows[row_idx].cells[col_idx]
            cell.text = value
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(7)
                    run.font.name = 'Times New Roman'

    # Set column widths
    for row in table.rows:
        row.cells[0].width = Cm(1.0)
        row.cells[1].width = Cm(5.5)
        row.cells[2].width = Cm(6.5)
        row.cells[3].width = Cm(1.2)

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
    "Battery-free embedded systems that get power from ambient energy is getting "
    "really popular for sustainable IoT. Between 2025 and 2026, lots of cool stuff happened, "
    "moving from just ideas to actual working things. This paper looks at six important "
    "research papers about making battery-free systems better. They talk about math models for "
    "energy, cheap ways to do wireless communication, platforms to test performance, AI that "
    "knows about energy harvesting, drones powering sensors for farming, and surveys of circuit "
    "designs. We look at each paper and find some big problems that still need fixing, like not "
    "having standard tests, trouble using multiple energy sources at once, AI not working well "
    "when power stops, and no standard rules for managing power. We think future research needs "
    "to focus on making things work together better, designing AI and hardware together, and "
    "making sure these systems are reliable so we can actually use them without maintenance."
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
                     "IoT, TinyML, Power Management, Wireless Sensor Networks, Research Gaps")
run_val.italic = True
run_val.font.size = Pt(9)
run_val.font.name = 'Times New Roman'

# ============================================================
# I. INTRODUCTION
# ============================================================
add_section_heading(doc, "I. Introduction")

add_body(doc, (
    "Having lots of IoT devices in farming, factories, and health stuff is cool but "
    "there is a big problem: batteries. Batteries are annoying because they cost money to replace, "
    "are bad for the environment, and don't last long in tough places. Also changing them in huge "
    "sensor networks is just too much work. Because of this, many people are researching "
    "battery-free systems that can grab energy from the sun, radio waves, heat, or moving around."
))

add_body(doc, (
    "The years 2025 to 2026 was a big turning point. Researchers moved from just proving it's "
    "possible to actually making it reliable and ready for the real world. Some big steps include "
    "fancy math models to guess how sensors act in different weather [1], cheap ways to build "
    "them to save energy for wireless talk [2], and standard testing platforms to fairly compare "
    "different battery-less systems [3]. Also, people started mixing energy harvesting with edge "
    "AI, which created Intermittent TinyML. This means designing neural networks that can work "
    "even when the power keeps turning on and off [4]."
))

add_body(doc, (
    "There are also new cool uses, like drones powering sensors with RF signals for farming [5]. "
    "Plus, big surveys have listed all the new circuit designs making this possible [6]. All this "
    "shows that battery-free systems are not just science projects anymore, but real tech we can use."
))

add_body(doc, (
    "This review looks deep into six really important papers from 2024 to 2026. We look at how "
    "they did it, what's new, and their test results. We also point out some big holes in the "
    "research that still need filling, and give ideas for what to do next. The rest of the paper "
    "goes like this: Section II talks about the papers, Section III compares them, Section IV "
    "shows the gaps, Section V talks about the future, and Section VI wraps it all up."
))

# ============================================================
# II. LITERATURE REVIEW
# ============================================================
add_section_heading(doc, "II. Literature Review")

# --- Paper 1 ---
add_subsection_heading(doc, "A. Analytical Modeling of Batteryless IoT Sensors Powered by Ambient Energy Harvesting")

add_body(doc, (
    "Fernández Landivar and their team (arXiv:2507.20952, July 2025) made a big math "
    "framework to figure out how energy moves in batteryless IoT nodes [1]. The model looks "
    "at how it gets energy and how it uses it, including power management stuff that other "
    "papers usually forget. They modeled the Energy Harvesting Unit (EHU), which has the "
    "harvester, power manager, and supercapacitor, along with the Circuit Load (CL). This helps "
    "guess exactly how the device acts, like how the voltage changes in different environments."
))

add_body(doc, (
    "A really good thing about this work is you can use it for lots of things. The math "
    "isn't just for one specific hardware. They tested their model with a real batteryless IoT "
    "node under different lighting and showed that their guesses matched the real voltage very well. "
    "This model helps design smart power units to get the most energy even when the environment "
    "changes, giving engineers a handy tool to check performance before actually building it."
))

# --- Paper 2 ---
add_subsection_heading(doc, "B. Designing Cost-Effective Battery-Less Energy Harvesting for Intermittent Wireless Communication")

add_body(doc, (
    "In IEEE Access (Jan 2025), this paper talks about a cheap way to design battery-less "
    "IoT devices that need to reliably send wireless data even when power comes and goes [2]. "
    "They made models for energy and timing to figure out the best size for energy harvesters "
    "and storage, like capacitors. This helps designers find the best setup to meet wireless "
    "needs without using normal batteries."
))

add_body(doc, (
    "The coolest part is a duty-based Dynamic Power Management (DPM) thing that works way "
    "better than older threshold methods. Tests showed this DPM scheme makes devices run 9.1% "
    "to 90.0% longer depending on the weather. The power setup is made to improve Quality of "
    "Service (QoS), like how fast and often data is sent. This work connects paper theories with "
    "real world needs, giving engineers a step-by-step guide to build these wireless systems "
    "so they work exactly how you expect."
))

# --- Paper 3 ---
add_subsection_heading(doc, "C. EStacker: Explaining Battery-Less IoT System Performance with Energy Stacks")

add_body(doc, (
    "Liedtke and guys show EStacker in ACM Transactions on Embedded Computing Systems "
    "(2026), which is a special platform to test battery-less IoT systems [3]. EStacker tries "
    "to fix the hard problem of testing things fairly and repeatably by making 'energy stacks', "
    "which are detailed lists of how much energy the app uses on different hardware and tasks. "
    "This deep dive lets developers see exactly where the energy goes, helping them fix specific "
    "hardware and software parts."
))

add_body(doc, (
    "A big deal here is the ST-SP optimization trick, which cuts testing time by 6.3 times on "
    "average while keeping the timing mostly accurate (error is just 7.7%). This speed is super "
    "important because trying out different sizes for harvesters and storage normally takes "
    "forever. EStacker makes sure every app and setup is tested with the exact same energy, "
    "setting up a good base for standard tests in the battery-less community."
))

# --- Paper 4 ---
add_subsection_heading(doc, "D. HANNA: Harvesting-Aware Neural Network Architecture Search")

add_body(doc, (
    "Sahu, Deep, and Duwe brought HANNA to IPCCC 2024. It is a Neural Architecture Search "
    "(NAS) method that actually cares about energy harvesting, made just for batteryless devices "
    "that turn on and off [4]. Normal NAS usually just looks at speed and accuracy, but HANNA "
    "also looks at the energy environment while searching. This makes deep neural networks "
    "(DNN) that fit perfectly in these stopping-and-starting environments."
))

add_body(doc, (
    "The big idea is that the best neural networks for batteryless devices are totally "
    "different from ones with constant power. They have to deal with power dying, saving "
    "progress, and unpredictable energy. HANNA's search method quickly looks through this "
    "messy space and finds networks that can finish a job with just one cycle of harvested energy. "
    "This work is one of the first real steps into Intermittent TinyML, where machine learning "
    "is tweaked to handle the weird limits of energy-harvesting systems."
))

# --- Paper 5 ---
add_subsection_heading(doc, "E. Autonomous Agricultural Monitoring with Aerial Drones and RF Energy-Harvesting Sensor Tags")

add_body(doc, (
    "Kudyba and Sun (arXiv:2502.16028, Feb 2025) look at a cheap and green way to do "
    "farming by throwing away battery sensors and using battery-less RF energy-harvesting "
    "tags that get power from drones flying around [5]. The setup uses drones carrying special "
    "wireless gear that shoots out RF signals. The tags catch this energy to measure things like "
    "temp and humidity, and then send the data back to the drone. This means you can collect "
    "data without needing any power lines on the ground."
))

add_body(doc, (
    "The guys did tests at AERPAW, a drone research place. Tests on the ground worked great, "
    "but flying tests showed some issues with wireless interference messing up data collection. "
    "They think combining the receiver parts to cut weight and interference could make it stronger. "
    "This work shows a really cool use for battery-free systems in farming, pointing out both "
    "the awesome potential and the hard engineering problems of using RF sensors everywhere."
))

# --- Paper 6 ---
add_subsection_heading(doc, "F. Batteryless Systems for IoT: A Survey of Circuit and System Design")

add_body(doc, (
    "At MWSCAS 2025, this big survey paper listed all the new circuit and system designs "
    "pushing battery-less IoT forward [6]. The survey talks about everything, from energy "
    "catchers, power management chips (PMICs), storage things like supercapacitors, memory "
    "that doesn't lose data when power dies, and how intermittent computing actually runs."
))

add_body(doc, (
    "The paper groups intermittent computing into two types: task-based (where jobs are "
    "small enough to finish in one energy burst) and checkpoint-based (where the program keeps "
    "saving its spot). The survey points out important trade-offs, like harvester efficiency vs "
    "cost, storage size vs leaking power, and getting work done vs the energy it takes. It "
    "basically gives a map for newbies entering battery-free system design."
))

# ============================================================
# III. COMPARATIVE ANALYSIS
# ============================================================
add_section_heading(doc, "III. Comparative Analysis")

add_table_paper_summary(doc)

add_body(doc, (
    "The six reviewed papers collectively represent three major research thrusts in "
    "contemporary battery-free embedded system development: (1) theoretical modeling and "
    "design methodology (Papers [1] and [2]), (2) evaluation, benchmarking, and architecture "
    "innovation (Papers [3] and [4]), and (3) application-driven system integration and "
    "comprehensive technology surveys (Papers [5] and [6]). A notable convergence across "
    "all works is the shift from demonstrating the mere feasibility of batteryless operation "
    "to addressing practical deployment challenges including reliability, predictability, "
    "and scalability."
))

add_body(doc, (
    "The modeling contributions of Fernández Landivar et al. [1] and the design methodology "
    "of the IEEE Access paper [2] are complementary: while [1] provides the analytical "
    "foundation for understanding energy dynamics, [2] translates these insights into "
    "actionable design rules for wireless communication systems. Similarly, EStacker [3] "
    "provides the evaluation infrastructure needed to validate designs produced by approaches "
    "like HANNA [4], creating a natural toolchain for battery-free system development. "
    "The application-focused work of Kudyba and Sun [5] demonstrates real-world deployment "
    "challenges that motivate the theoretical and systems-level innovations in the other papers, "
    "while the MWSCAS survey [6] provides the comprehensive technology landscape that "
    "contextualizes all contributions."
))

# ============================================================
# IV. RESEARCH GAPS (HIGHLIGHTED)
# ============================================================
add_section_heading(doc, "IV. Identified Research Gaps")

add_body(doc, (
    "Even though lots of good stuff happened in these papers, there are still some "
    "big holes we need to look at right now. Here are the main ones:"
), first_line_indent=False)

# Gap 1
add_subsection_heading(doc, "A. Lack of Unified Benchmarking and Evaluation Standards")
add_body_with_highlight(doc,
    "While EStacker [3] is a good start for testing, ",
    "we still don't have a normal test or dataset everyone agrees on to compare different "
    "battery-free boards, energy sources, and apps.",
    " Right now, everyone tests with their own secret setups and weird weather, so you can't "
    "really compare paper A to paper B. We badly need the community to make standard setups, "
    "energy records, and normal scores (like energy per task or speed) so everyone is on the same page."
)

# Gap 2
add_subsection_heading(doc, "B. Insufficient Multi-Source Energy Harvesting Integration")
add_body_with_highlight(doc,
    "Most papers just look at one energy thing (like sun in [1], or RF in [5]), but ",
    "nobody is really making good ways to mix and manage a bunch of energy things at the same "
    "time (like sun, RF, heat, moving) in one single power manager.",
    " The real world has crazy weather and changing energy. Mixing harvesters that can smoothly "
    "swap or combine sources to stay alive is a super important thing we are missing if we want "
    "devices to truly run forever."
)

# Gap 3
add_subsection_heading(doc, "C. Limited Edge AI and TinyML Adaptation for Intermittent Operation")
add_body_with_highlight(doc,
    "HANNA [4] is a great first step for intermittent TinyML, but ",
    "using deep learning and AI on devices that keep losing power is still super new and not "
    "developed enough.",
    " Big problems are how to save AI progress without wasting energy, making models that don't "
    "break when power dies halfway, and training them to know about energy. New things like "
    "compute-in-memory look cool but they don't work with intermittent systems yet."
)

# Gap 4
add_subsection_heading(doc, "D. Inadequate Standardization of Power Management Protocols")
add_body_with_highlight(doc,
    "The DPM thing in [2] and math in [1] are neat, but they are kind of on their own, and ",
    "there is no standard rules or software layer to manage power across all different kinds "
    "of battery-free IoT devices.",
    " Without standards, every single device needs its own special power code, which makes it "
    "hard to mix devices and makes building them expensive. A open power software, kind of like "
    "internet protocols, that handles harvesting and saving power would make things grow super fast."
)

# Gap 5
add_subsection_heading(doc, "E. Reliability and Long-Term Durability in Harsh Environments")
add_body_with_highlight(doc,
    "People always say battery-free systems are great for tough factories or farms, but ",
    "nobody actually researches how long they last, how they break down, or if they are safe "
    "when stuck in crazy heat, water, shaking, or bad radio noise for a long time.",
    " The RF noise problem in [5]'s flying tests shows exactly this. We really need tests that "
    "run for months or years, and official safety rules for battery-free things if industries "
    "are ever going to trust them."
)

# Gap 6
add_subsection_heading(doc, "F. Scalability of Battery-Free Wireless Sensor Networks")
add_body_with_highlight(doc,
    "Most papers just look at making one device better, but ",
    "the big problems of putting hundreds of battery-free nodes together in huge networks, "
    "like managing energy everywhere, stopping noise, and sending data when things turn off "
    "randomly, are mostly ignored.",
    " As we move from single tests to huge real deployments, we need network rules that know "
    "devices will randomly die and wake up. Normal network rules assume things have power all "
    "the time and they break when power drops."
)

# ============================================================
# V. DISCUSSION AND FUTURE DIRECTIONS
# ============================================================
add_section_heading(doc, "V. Discussion and Future Directions")

add_body(doc, (
    "Looking at battery-free stuff in 2025-2026, the field is finally growing up. Mixing math "
    "models [1], design rules [2], standard tests [3], AI designs [4], cool drone uses [5], "
    "and big circuit surveys [6] shows we have the basic Lego blocks to make huge battery-free "
    "IoT things. But, putting it all together is still a huge pain."
))

add_body(doc, (
    "Some good ideas for the future are: (1) Make a big open-source testing world with standard "
    "energy traces and boards; (2) Look into harvesting many energy types that switch smartly "
    "based on the weather; (3) Build AI and hardware together to be accurate and save energy "
    "even when power dies; (4) Make normal power management software so you can just plug and "
    "play different harvesters; (5) Do long field tests to see how things break in the real "
    "world; and (6) Make network rules that expect things to lose power, so huge networks don't crash."
))

add_body(doc, (
    "Also, big companies really want maintenance-free IoT now because of green rules and "
    "because changing batteries in a million devices is crazy. Because solar, chips, and power "
    "managers got so good in 2025-2026, it looks like battery-free systems are finally ready "
    "to leave the lab and become real things you can buy."
))

# ============================================================
# VI. CONCLUSION
# ============================================================
add_section_heading(doc, "VI. Conclusion")

add_body(doc, (
    "This review looked at six really important papers that show the best of battery-free "
    "embedded systems in 2025-2026. From Fernández Landivar's math [1], to cheap wireless "
    "designs [2], EStacker's testing platform [3], HANNA's AI search [4], drone farming [5], "
    "and the MWSCAS circuit survey [6], these works show a massive jump from just science "
    "projects to stuff that is actually ready to use."
))

add_body(doc, (
    "But, we still have big problems, especially with no testing standards, trouble using "
    "multiple energy things, AI not working well with power loss, no normal power rules, no "
    "long-term testing, and networks that don't scale. Fixing these holes is super important "
    "if we want to make IoT systems that really run forever without maintenance. We hope this "
    "paper helps people working on battery-free stuff, especially computer folks trying to "
    "add to this fast-moving area."
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
