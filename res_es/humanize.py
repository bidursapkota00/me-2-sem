import re

with open("generate_review_paper_es.py", "r") as f:
    content = f.read()

replacements = [
    # Introduction
    (
        r'"The rapid proliferation.*?"\n\s*"domains.*?infeasible \[6\]\."',
        '"Many IoT devices are everywhere now. Like farm, factory, nature check, "\n    "and health. So we need sensor that live long time without help. But big "\n    "problem for many IoT is battery. Normal battery cost much money because "\n    "we must change them. Also they make bad trash for environment. And it is "\n    "very hard to change battery if sensor is very far place [6]."'
    ),
    (
        r'"Battery-free embedded systems offer.*?interruptions \[3\], \[6\]\."',
        '"Battery-free system is good choice. It takes energy from outside like "\n    "sun, radio wave, heat and shaking. These system use supercapacitor or "\n    "small cell to keep energy. They use it to do compute and talk sometimes. "\n    "This way is called intermittent computing. It have hard problem because "\n    "system must not make mistake and keep data safe when power go off suddenly [3], [6]."'
    ),
    (
        r'"The period from 2024 to 2026.*?technology \[1\], \[5\]\."',
        '"From 2024 to 2026, research in battery-free system change a lot. Before, "\n    "people just try to make it work. Now people try to solve real problem. "\n    "Like how to guess performance, make cheap hardware, test it good, and "\n    "put AI on it. Also new thing like drone sensor for farm show this tech "\n    "is very useful now [1], [5]."'
    ),
    # Problem Statement
    (
        r'"Despite the conceptual appeal.*?scalability \[2\], \[4\]\."',
        '"Even if battery-free sound very good, many problem make it hard to use "\n    "everywhere. First, we have no standard way to test them, so hard to compare "\n    "different system. Second, use many different energy source together is still "\n    "very new. Third, use AI and neural network when power is not stable is very "\n    "hard. Fourth, no standard power rule make it hard to connect different hardware [2], [4]."'
    ),
    # Research Objectives
    (
        r'"The primary objective.*?identify unresolved research gaps\."',
        '"This review want to look at 6 new paper about battery-free system from "\n    "2024 to 2026. We look at what they want to do, how they do it, and what "\n    "they find. We compare their strong and weak points. Also we find what "\n    "problem is still not solved so future research can fix them."'
    ),
    # Related Works
    (
        r'"Fernández Landivar et al\. \[1\].*?pre-fabrication design\."',
        '"Fernández Landivar and friends [1] make math model for batteryless IoT "\n    "node. They use supercapacitor and solar power. Model show how voltage "\n    "change when light change. They test it inside room with different light. "\n    "Model is good to guess how system work before building it."'
    ),
    (
        r'"A complementary approach is presented in \[2\].*?without oversizing components\."',
        '"Another paper [2] make new way to manage power. They change when sensor "\n    "send data base on how much energy it have. This is Dynamic Power Management "\n    "(DPM). It help sensor work 9.1% to 90% longer. This mean sensor can work "\n    "good even if energy is small, so we no need very big capacitor."'
    ),
    (
        r'"To address the challenge.*?execution phase\."',
        '"Testing battery-less system is hard, so paper [3] make EStacker. It is "\n    "tool to check performance. It show exactly how energy is used by different "\n    "hardware and software part. They call this \\"energy stacks\\". It help "\n    "developer see where energy go."'
    ),
    (
        r'"Sahu, Deep, and Duwe \[4\].*?produce suboptimal results\."',
        '"Sahu and friends [4] make HANNA. It is search tool to find best neural "\n    "network for device with no battery. Normal AI search only care about speed "\n    "and accuracy, but this not work for intermittent power. HANNA find AI that "\n    "work best when power come and go."'
    ),
    (
        r'"A key strength of HANNA.*?different platforms\."',
        '"HANNA is very strong because it mix tiny AI with intermittent computing. "\n    "The AI it find look different from normal AI. But it only test on some dataset. "\n    "We need to check if it work good on many different hardware."'
    ),
    (
        r'"Moving toward application-specific.*?agricultural fields\."',
        '"Paper [5] put sensor on farm using drone. Sensor have no battery, it "\n    "take energy from drone radio wave. Then sensor send temperature data to "\n    "drone. Ground test work very good. But when drone fly, drone motor make "\n    "too much noise so sensor cannot talk good. This show real world is hard."'
    ),
    # Methodology
    (
        r'"Papers \[1\] and \[2\] employ analytical modeling.*?sensitivity analysis\."',
        '"Paper [1] and [2] use math model. Paper [1] write math equation for "\n    "supercapacitor and power. They test part by part to get math numbers. "\n    "Paper [2] use math to balance energy and time for communication. Both "\n    "help test design before make real hardware."'
    ),
    (
        r'"Papers \[1\], \[2\], and \[5\] incorporate experimental.*?environmental variability\."',
        '"Paper [1], [2], and [5] make real hardware to test. Paper [1] test "\n    "IoT node with room light. Paper [2] test power manage with real energy "\n    "profile. Paper [5] test farm sensor with drone in real field. Real test "\n    "is very important to see if math model is correct in real world."'
    ),
    (
        r'"Papers \[3\] and \[4\] rely primarily.*?conventional NAS approaches\."',
        '"Paper [3] and [4] use computer simulation. EStacker [3] simulate time "\n    "and energy very detail. It use smart way to cut simulation time. "\n    "HANNA [4] simulate AI on intermittent power. It use optimization to "\n    "balance accuracy and energy cost."'
    ),
    (
        r'"Paper \[6\] adopts a systematic survey.*?systems community\."',
        '"Paper [6] is survey paper. It read many old paper and put them in groups. "\n    "It group by hardware part and execution type. This help see what is "\n    "good and bad, and show what researcher do now."'
    ),
    # Results and Discussion
    (
        r'"The six reviewed papers collectively.*?research landscape\."',
        '"The 6 paper show 3 main research area. Paper [1] and [2] do math and "\n    "design rule. Paper [3] and [4] make test tool and AI architecture. "\n    "Paper [5] and [6] do real farm application and big survey review. "\n    "All are important for battery-free system."'
    ),
    (
        r'"A notable convergence across.*?battery-free system development\."',
        '"All paper show that researcher now care about real use, not just show "\n    "it work. Math from [1] and rule from [2] help each other. EStacker [3] "\n    "can test AI from HANNA [4]. They all connect together to make battery-free "\n    "system better."'
    ),
    (
        r'"The quantitative results reported.*?all reviewed studies\."',
        '"The number result in paper show big improvement. Table III show main "\n    "performance number for all paper."'
    ),
    (
        r'"The DPM scheme proposed in \[2\].*?7\.7 days \[3\]\."',
        '"Power method in [2] make system work 9.1% to 90% longer time. It help "\n    "most when energy is very low. EStacker [3] make test 6.3x faster but "\n    "error is only 7.7%. It also find problem in app and make it 3.3x better, "\n    "so test time go from 41.7 day to 7.7 day."'
    ),
    (
        r'"HANNA \[4\] demonstrates that.*?availability windows\."',
        '"HANNA [4] improve AI accuracy by 10% to 44% compare to old AI. It also "\n    "make search cost lower. The AI it find is different. It have smaller "\n    "layer and save state more time. So it can finish job in short power time."'
    ),
    (
        r'"The agricultural monitoring system.*?airborne operation\."',
        '"Farm system in [5] use 918 MHz radio to harvest energy. It use 2.4 GHz "\n    "to send data up to 10 meter. Ground test is good. But drone test fail "\n    "because drone motor make interference. They get 1 ID packet but no temp data."'
    ),
    (
        r'"Several important research trends.*?their intersection\."',
        '"Many trend show in these paper. First, people want standard and math. "\n    "Model [1], design [2], and test [3] show researcher want formal way. "\n    "Second, Intermittent TinyML [4] is new. It mix AI and battery-free computing."'
    ),
    (
        r'"Third, application-specific.*?software support\."',
        '"Third, real application like [5] show problem we don\'t see in lab, like "\n    "drone motor noise. Fourth, survey [6] show hardware is very mature now. "\n    "People understand hardware well, so now big problem is software and system integration."'
    ),
    (
        r'"Despite the substantial contributions.*?their identification\."',
        '"Even with good result, many big research gap still exist. We must fix "\n    "them to use battery-free system everywhere."'
    ),
    (
        r'"Gap 1: Absence of Unified.*?urgently needed\."',
        '"Gap 1: No standard test benchmark. EStacker [3] is good start but not "\n    "everyone use it. Every paper use different hardware and energy to test. "\n    "So very hard to compare paper. We need standard test like MLPerf for battery-free."'
    ),
    (
        r'"Gap 2: Insufficient Multi-Source.*?open research problem\."',
        '"Gap 2: Not enough multi-source energy. Paper only use one energy like "\n    "solar [1] or radio [5]. But real world have many energy source same time. "\n    "We need smart system to mix solar, heat, and radio together."'
    ),
    (
        r'"Gap 3: Limited Edge AI.*?as a constraint\."',
        '"Gap 3: Edge AI for intermittent power is small. HANNA [4] is good and "\n    "get 10%-44% better accuracy. But we still need know how to save AI state "\n    "cheaply, and how to train AI when energy is low."'
    ),
    (
        r'"Gap 4: Inadequate Standardization.*?reduce development costs\."',
        '"Gap 4: No standard power rule. Paper [1] and [2] only work for their "\n    "own platform. We no have standard protocol for power like we have for "\n    "network. If we have standard, ecosystem will grow fast."'
    ),
    (
        r'"Gap 5: Reliability and Long-Term.*?exemplifies this gap\."',
        '"Gap 5: We no know long-term reliability. People want use battery-free "\n    "in harsh farm or factory. But no paper study if it break after many month "\n    "in hot, cold, or noise. Drone noise problem in [5] is good example of this."'
    ),
    (
        r'"Gap 6: Scalability of Battery-Free.*?intermittent operation\."',
        '"Gap 6: Network scalability is bad. Paper only optimize one device. "\n    "We no know how to manage 1000 device network when power go on and off. "\n    "Normal network rule assume device always on, so we must redesign network rule."'
    ),
    # Conclusion
    (
        r'"This review has critically examined.*?systematic progress\."',
        '"This review read 6 new paper about battery-free system from 2024 to 2026. "\n    "Paper show field move from just proof to real use. Math model [1] and "\n    "design rule [2] improve time up to 90%. EStacker [3] make standard test, "\n    "and HANNA [4] open TinyML area. Farm test [5] show real challenge, and survey [6] give foundation."'
    ),
    (
        r'"The principal contributions of.*?commercial systems\."',
        '"This review have 3 main contribution. First, it compare 6 paper objective, "\n    "method, and result. Second, it group methodology into 4 type: math, "\n    "prototype, simulation, and survey. Third, it find 6 big research gap like "\n    "benchmark, energy mix, AI, power rule, reliability, and network scale."'
    ),
    (
        r'"Based on the analysis presented.*?sensor network deployments\."',
        '"For future research, we suggest: (1) Make standard benchmark test. "\n    "(2) Study how to mix many energy source. (3) Design AI and hardware together "\n    "for unstable power. (4) Make standard power protocol. (5) Test device in "\n    "real harsh environment for long time. (6) Make new network rule for device that sleep often."'
    ),
    (
        r'"The convergence of advances.*?without human intervention\."',
        '"Better energy harvest, low power circuit, and edge compute show battery-free "\n    "system will be commercial soon. If we solve the research gap, we can make "\n    "IoT infrastructure that is very green and work forever without human touch."'
    ),
]

for pat, repl in replacements:
    content = re.sub(pat, repl, content, flags=re.DOTALL)

with open("generate_review_paper_es.py", "w") as f:
    f.write(content)
