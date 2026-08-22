import re

with open("generate_review_paper_es.py", "r") as f:
    content = f.read()

replacements = [
    # Remaining Problem Statement
    (
        r'"These challenges collectively impede.*?evolving field\."',
        '"These problem make it hard to use battery-free system in real world. "\n    "So we need to read new paper and find what is missing. This help us know "\n    "what to do next."'
    ),
    # Research Objectives
    (
        r'"The primary objective of this review.*?as follows:"',
        '"This paper want to look at 6 new research from 2024 to 2026. We want to do this:"'
    ),
    (
        r'"\(1\) To critically review.*?each selected paper\."',
        '"(1) Read and summarize what each paper do and find."'
    ),
    (
        r'"\(2\) To perform a comparative.*?reported outcomes\."',
        '"(2) Compare how they do research and their result."'
    ),
    (
        r'"\(3\) To identify and discuss.*?reviewed studies\."',
        '"(3) Find out what math and tool they use."'
    ),
    (
        r'"\(4\) To identify critical research gaps.*?current literature\."',
        '"(4) See what big problem is still not fixed."'
    ),
    (
        r'"\(5\) To propose future research directions.*?IoT systems\."',
        '"(5) Suggest what people should research next."'
    ),
    # Methodology (lines 496-515 or similar)
    (
        r'"The principal strength of this survey.*?software and application-level focus\."',
        '"Survey is good because it put everything in order. It help new people "\n    "understand battery-free system fast. But survey only talk about hardware "\n    "and circuits. It don\'t talk much about software."'
    ),
    (
        r'"The research methodologies adopted across.*?evaluation techniques employed\."',
        '"The 6 paper use 4 main way to do research: math model, real prototype, "\n    "computer simulation, and survey. Here we look at how they do it."'
    ),
    # Future Research
    (
        r'"Based on the analysis presented in this review, the following future research directions\n\s*are recommended: \(1\) Development of community-accepted open-source benchmark suites with\n\s*standardized energy traces, hardware reference designs, and performance metrics for fair\n\s*cross-platform comparison. \(2\) Investigation of multi-source energy harvesting architectures\n\s*with intelligent source arbitration and adaptive power management algorithms. \n\s*\(3\) Co-design of neural network architectures and intermittent computing hardware to\n\s*achieve robust and energy-efficient edge AI inference under unreliable power conditions. \n\s*\(4\) Standardization of power management protocols and abstraction layers to enable\n\s*interoperability across heterogeneous battery-free platforms. \(5\) Longitudinal field\n\s*studies assessing component degradation, failure modes, and system reliability under\n\s*sustained real-world deployment conditions. \(6\) Design of intermittent-aware networking\n\s*protocols that accommodate stochastic node availability for scalable battery-free sensor\n\s*network deployments\."',
        '"For future research, we suggest: (1) Make standard benchmark test. "\n    "(2) Study how to mix many energy source. (3) Design AI and hardware together "\n    "for unstable power. (4) Make standard power protocol. (5) Test device in "\n    "real harsh environment for long time. (6) Make new network rule for device that sleep often."'
    ),
    # Conclusion ending
    (
        r'"The convergence of advances in energy harvesting efficiency, ultra-low-power circuit\n\s*design, and edge computing capabilities suggests that battery-free embedded systems are\n\s*approaching a critical threshold of commercial viability. Addressing the research gaps\n\s*identified in this review will be instrumental in realizing the vision of truly\n\s*maintenance-free, sustainable IoT infrastructure capable of operating autonomously\n\s*without human intervention\."',
        '"Better energy harvest, low power circuit, and edge compute show battery-free "\n    "system will be commercial soon. If we solve the research gap, we can make "\n    "IoT infrastructure that is very green and work forever without human touch."'
    ),
    # Let's catch any other missed ones
    (
        r'"Paper \[6\] adopts a systematic survey methodology.*?battery-free systems community\."',
        '"Paper [6] is survey paper. It read many old paper and put them in groups. "\n    "It group by hardware part and execution type. This help see what is "\n    "good and bad, and show what researcher do now."'
    ),
]

for pat, repl in replacements:
    content = re.sub(pat, repl, content, flags=re.DOTALL)

with open("generate_review_paper_es.py", "w") as f:
    f.write(content)
