# ISA Exam — Generalized Outlines for Audits & Assessments

> Use these outlines as templates. Replace `<<Organization>>`, `<<N sites>>`, `<<N controls>>` with question-specific details.

---

## 1. IS Audit Report — ISO 27001:2022 (5/6/10 Controls)

> **Question Pattern:** "You have been appointed as an external IS Auditor for `<<Organization>>` with `<<N>>` sites, its own DC and DRC. Conduct an IS Audit focusing on `<<N>>` controls of ISO 27001:2022. Prepare a comprehensive report covering Control, Observation, Risk Rating, Recommendation."

**Standard:** ISO/IEC 27001:2022 — 93 Annex A controls grouped into 4 themes:
- A.5 — Organizational Controls (37 controls)
- A.6 — People Controls (8 controls)
- A.7 — Physical Controls (14 controls)
- A.8 — Technological Controls (34 controls)

### Report Structure

```
IS Audit Report
├── Organization: <<Organization>> with <<N>> sites, own DC and DRC
├── Audit Standard: ISO 27001:2022
├── Audit Type: External Information System Audit
├── Controls Evaluated: <<N>> (across all 4 Annex A themes)
│
├── Introduction
│   - ICT plays a vital role for <<Organization>> to enable its business processes
│   - IS Audit identifies existing risks from ICT services
│   - Based on ISO 27001:2022 Information Security Management Framework
│   - Preserves CIA by applying a risk management process
│   - Gives confidence to stakeholders that risks are adequately managed
│
├── Objective
│   - Evaluate effectiveness of ISMS by auditing <<N>> selected controls
│   - Identify risks and provide recommendations
│
├── Scope
│   - Head Office, DC, DRC, sample of branch sites
│   - Organizational, People, Physical, and Technological controls
│
├── A.1. Organizational Controls
│   ├── Control: Policies for Information Security (A.5.1)
│   └── Control: Information Security Roles and Responsibilities (A.5.2)
│
├── A.2. People Controls
│   └── Control: Information Security Awareness, Education and Training (A.6.3)
│
├── A.3. Physical Controls
│   ├── Control: Physical Security Perimeters (A.7.1)
│   └── Control: Securing Offices, Rooms and Facilities (A.7.3)
│
├── A.4. Technological Controls
│   ├── Control: Privileged Access Rights / Access Control (A.8.2)
│   ├── Control: Protection Against Malware (A.8.7)
│   ├── Control: Management of Technical Vulnerabilities (A.8.8)
│   ├── Control: Information Backup (A.8.13)
│   └── Control: Logging (A.8.15)
│
├── Summary of Findings (Table: #, Control, ISO Ref, Theme, Risk Rating)
│
├── Prioritized Recommendations
│   ├── Critical Priority (Immediate)
│   ├── High Priority (Within 3 Months)
│   └── Medium Priority (Within 6 Months)
│
└── (Optional) Regulatory Compliance Context
```

### Per-Control Format

For **each control**, write:

1. **Control** — ISO 27001:2022 control statement (copy verbatim from standard)
2. **Purpose** — Why this control exists
3. **Observation** — What was found during audit (specific gaps, evidence)
4. **Risk Rating** — HIGH / MEDIUM / LOW
5. **Recommendation** — Actionable remediation steps
6. **Management Response** — (Optional) Organization's planned action

### Control Selection Guide (Pick from each theme to cover all 4)

| Theme          | Common Controls for Exam                                      |
| -------------- | ------------------------------------------------------------- |
| Organizational | A.5.1 (Policies), A.5.2 (Roles), A.5.15 (Access Control)     |
| People         | A.6.3 (Awareness/Training)                                    |
| Physical       | A.7.1 (Physical Perimeters), A.7.3 (Securing Rooms)           |
| Technological  | A.8.2 (Privileged Access), A.8.7 (Malware), A.8.8 (Vuln Mgmt), A.8.13 (Backup), A.8.15 (Logging) |

### Typical Observations (Reusable)

| Control | Typical Observation |
| ------- | ------------------- |
| A.5.1   | Policy exists but not reviewed since creation; no topic-specific policies; staff unaware; no written acknowledgement |
| A.5.2   | No dedicated CISO; IT handles security ad-hoc; no roles at branches; no escalation matrix |
| A.6.3   | No structured training program; staff unaware of phishing/passwords; no records; shared credentials observed |
| A.7.1   | DC uses key-lock (no biometric/card); no visitor log; DRC shared corridors; CCTV retention 15 days |
| A.7.3   | No environmental sensors; standard fire extinguishers (not gas-based); no UPS records; DRC no generator |
| A.8.2   | No access control policy; terminated accounts active; shared accounts; weak password (6-char); no MFA; shared admin credentials |
| A.8.7   | Antivirus not centrally managed; outdated definitions at branches; no EDR; no USB restrictions |
| A.8.8   | No VAPT; ad-hoc patching; outdated OS; customer app not security-tested; no software inventory |
| A.8.13  | Daily backup but no policy; weekly DRC replication (7-day gap); no restoration test 12+ months; RTO/RPO not defined; no encryption |
| A.8.15  | No centralized log/SIEM; inconsistent retention (7-30 days); reactive review only; admin activities not logged; no tamper protection; no alerting |

---

## 2. Information Security Self-Assessment — ISO/IEC 27001:2022 (93 Controls)

> **Question Pattern:** "Your organization operates 100+ sites with DC and private cloud DRC. Undertake an Information Security Self-Assessment in alignment with ISO/IEC 27001:2022, focusing on the 93 Annex A controls."

**Standard:** ISO/IEC 27001:2022 — All 93 Annex A controls across 4 themes

### Report Structure

```
Information Security Self-Assessment Report
├── Organization: <<Organization>> with <<N>> sites, in-house DC, private cloud DRC
├── Standard: ISO/IEC 27001:2022
├── Assessment Focus: 93 Annex A Controls (4 Themes)
│
├── 1. Introduction
│   - Evaluates current security posture against 93 Annex A controls
│   - Systematically reviews existing security measures
│   - Identifies risks/gaps, supports continuous improvement of ISMS
│
├── 2. Objective
│   - Evaluate implementation status of 93 controls across 4 themes
│   - Identify gaps between current posture and ISO 27001:2022
│   - Assess risk levels for each gap
│   - Provide roadmap for continuous improvement
│
├── 3. Scope
│   - All sites, DC, DRC, all information assets, personnel, processes, technology
│
├── 4. Methodology
│   - Review Statement of Applicability (SoA) for each of 93 controls
│   - Documentation review — policies, procedures, records, evidence
│   - Interviews with process owners and key personnel
│   - Technical verification — system configs, access logs, vulnerability reports
│   - Rate each control: Fully Implemented / Partially Implemented / Not Implemented / Not Applicable
│
├── 5. Self-Assessment of Annex A Controls
│   ├── Theme A.5 — Organizational Controls (37 controls)
│   │   Table: #, Control, Ref, Status, Gap Identified, Risk
│   ├── Theme A.6 — People Controls (8 controls)
│   │   Table: #, Control, Ref, Status, Gap Identified, Risk
│   ├── Theme A.7 — Physical Controls (14 controls)
│   │   Table: #, Control, Ref, Status, Gap Identified, Risk
│   └── Theme A.8 — Technological Controls (34 controls)
│       Table: #, Control, Ref, Status, Gap Identified, Risk
│
├── 6. Self-Assessment Summary
│   Table: Theme, Total Controls, Fully Implemented, Partially Implemented, Not Implemented, Not Applicable
│
├── 7. Risk Summary
│   Table: Risk Level (HIGH/MEDIUM/LOW), Count
│
└── 8. Recommendations
    ├── Immediate Priority
    ├── Short-Term (3–6 Months)
    └── Medium-Term (6–12 Months)
```

### Key Difference from IS Audit
- Self-assessment is **internal**, done by the organization itself
- Uses **all 93 controls** (not a selection of 5-10)
- Status rating is 4-level: Fully / Partially / Not Implemented / Not Applicable
- References the **Statement of Applicability (SoA)**

---

## 3. Cybersecurity Maturity Assessment — NIST CSF

> **Question Pattern:** "A multinational organization with 300+ locations, DC and DRC, plans to undertake a Cybersecurity Maturity Assessment aligned with NIST CSF. Evaluate across core functions and document maturity level, gaps, and improvements."

### Determine Version from Question

| If question says...                  | Use                                                     |
| ------------------------------------ | ------------------------------------------------------- |
| NIST CSF v1.1 / five core functions  | **NIST CSF v1.1** — 5 functions: Identify, Protect, Detect, Respond, Recover |
| NIST CSF v2.0 / six core functions   | **NIST CSF v2.0** — 6 functions: **Govern**, Identify, Protect, Detect, Respond, Recover |
| Just "NIST CSF" (unspecified)        | Check question context; if "six functions" mentioned → v2.0 |

### NIST CSF Implementation Tiers (Maturity Levels — same for v1.1 and v2.0)

| Tier   | Name          | Description                                                              |
| ------ | ------------- | ------------------------------------------------------------------------ |
| Tier 1 | Partial       | Risk management is ad-hoc and reactive; not formalized                   |
| Tier 2 | Risk Informed | Risk management approved by management but not organization-wide         |
| Tier 3 | Repeatable    | Policies and procedures formally approved and implemented org-wide       |
| Tier 4 | Adaptive      | Continuously improved based on lessons learned and predictive indicators |

### Report Structure

```
<<Organization>> Cybersecurity Assessment
NIST Cybersecurity Framework Version <<1.1 or 2.0>>
Cybersecurity Maturity Assessment Report
│
├── Organization: <<Organization>> with <<N>> locations, DC and DRC
├── Framework: NIST CSF Version <<1.1 or 2.0>>
├── Assessment Scope: All <<5 or 6>> core functions
│
├── 1. Introduction
│   - Evaluates cybersecurity posture against NIST CSF
│   - Maps current practices to core functions using Implementation Tiers
│   (If v2.0: mention Govern as new sixth function for governance integration)
│
├── 2. Implementation Tiers table (Tier 1-4 with descriptions)
│
├── 3. Assessment by Core Function
│   │
│   ├── (v2.0 only) Function: GOVERN (GV)
│   │   Categories: GV.OC (Org Context), GV.RM (Risk Mgmt Strategy),
│   │   GV.RR (Roles/Responsibilities), GV.PO (Policy), GV.SC (Supply Chain RM)
│   │
│   ├── Function: IDENTIFY (ID)
│   │   Categories: ID.AM (Asset Mgmt), ID.BE (Business Env), ID.GV (Governance — v1.1),
│   │   ID.RA (Risk Assessment), ID.RM (Risk Mgmt Strategy), ID.SC (Supply Chain — v1.1)
│   │
│   ├── Function: PROTECT (PR)
│   │   Categories: PR.AC/PR.AA (Access Control), PR.AT (Awareness/Training),
│   │   PR.DS (Data Security), PR.IP (Info Protection Processes), PR.PT (Protective Tech)
│   │
│   ├── Function: DETECT (DE)
│   │   Categories: DE.AE (Anomalies/Events), DE.CM (Continuous Monitoring),
│   │   DE.DP (Detection Processes)
│   │
│   ├── Function: RESPOND (RS)
│   │   Categories: RS.RP (Response Planning), RS.CO (Communications),
│   │   RS.AN (Analysis), RS.MI (Mitigation), RS.IM (Improvements)
│   │
│   └── Function: RECOVER (RC)
│       Categories: RC.RP (Recovery Planning), RC.IM (Improvements),
│       RC.CO (Communications)
│
│   Per-subcategory table: Category, Subcategory, Description, Current Tier, Gap, Target Tier
│   After each function: "Function Maturity: Tier X (Name)"
│
├── 4. Overall Maturity Summary
│   Table: Function, Current Maturity, Target Maturity
│   "Overall Organization Maturity: Tier X–Y"
│
└── 5. Improvement Roadmap
    ├── Phase 1 — Immediate (0–3 Months)
    ├── Phase 2 — Short-Term (3–6 Months)
    └── Phase 3 — Medium-Term (6–12 Months)
```

### Minimum Subcategory Selection (ensure all functions covered)

Select **at least 5 subcategories** ensuring **at least 1 per function**. Example sets:

**NIST CSF v1.1 (5 functions):**
- ID.AM-1 (Asset inventory), ID.RA-1 (Vulnerability identification)
- PR.AC-1 (Identity/credentials), PR.AT-1 (Training), PR.DS-1 (Data-at-rest)
- DE.CM-1 (Network monitoring)
- RS.RP-1 (Response plan)
- RC.RP-1 (Recovery plan)

**NIST CSF v2.0 (6 functions):**
- GV.RR-01 (Roles/responsibilities), GV.PO-01 (Policy)
- ID.AM-01 (Asset inventory), ID.RA-01 (Vulnerability identification)
- PR.AA-01 (Identity/credentials), PR.AT-01 (Training)
- DE.CM-01 (Network monitoring)
- RS.MA-01 (Incident management)
- RC.RP-01 (Recovery plan)

---

## 4. Building Terms of Reference (ToR) for an IS Audit

> **Question Pattern:** "A leading organization with 100+ sites, DC and DRC intends to carry out an IS Audit. In alignment with NIST, ISO 27001:2022, and CIS, develop a comprehensive ToR."

**Standards:** ISO/IEC 27001:2022, NIST CSF, CIS Critical Security Controls, applicable regulations

### Report Structure

```
Terms of Reference (ToR) for Information Systems Audit
│
├── 1. Introduction
│   - Defines purpose, scope, authority, methodology for IS Audit
│
├── 2. Background
│   - Organization requires IS Audit to evaluate security posture
│   - Mandated alignment with NIST, ISO 27001:2022, CIS Controls
│
├── 3. Audit Objectives
│   - Evaluate ISMS effectiveness against ISO 27001:2022 (93 Annex A controls)
│   - Assess cybersecurity maturity against NIST CSF (5 functions)
│   - Evaluate technical controls against CIS Critical Security Controls
│   - Identify vulnerabilities, risks, and gaps
│   - Assess regulatory compliance
│   - Provide actionable recommendations
│
├── 4. Scope of Work
│   ├── 4.1 Infrastructure Scope
│   │   - All sites, DC, DRC, network infrastructure, end-user devices
│   └── 4.2 Audit Domains (Table: Domain, Framework Reference, Key Areas)
│       - Information Security Governance — ISO 27001 Clauses 4-10, CIS Control 1
│       - Asset Management — ISO A.5.9-A.5.14, NIST ID.AM, CIS Control 1-2
│       - Access Control — ISO A.5.15-A.5.18, A.8.2-A.8.5, NIST PR.AC, CIS Control 5-6
│       - Physical Security — ISO A.7.1-A.7.14, NIST PR.AC-2
│       - Network Security — ISO A.8.20-A.8.22, NIST PR.PT, CIS Control 12-13
│       - Vulnerability Management — ISO A.8.8, NIST ID.RA, CIS Control 7
│       - Incident Management — ISO A.5.24-A.5.28, NIST RS, CIS Control 17
│       - Business Continuity — ISO A.5.29-A.5.30, NIST RC, CIS Control 11
│       - Logging and Monitoring — ISO A.8.15-A.8.16, NIST DE.CM, CIS Control 8
│       - Data Protection — ISO A.8.10-A.8.12, NIST PR.DS, CIS Control 3
│
├── 5. Audit Criteria / Standards and Frameworks
│   - ISO/IEC 27001:2022 — 93 Annex A controls
│   - NIST CSF v1.1 — 5 functions, 23 categories, 108 subcategories
│   - CIS Critical Security Controls v8 — 18 controls
│   - Applicable regulations (Electronic Transactions Act 2008, Individual Privacy Act 2018, sector-specific)
│   - Organizational IT Policies
│
├── 6. Methodology
│   - Phase 1 — Planning
│   - Phase 2 — Information Gathering (documentation, interviews, evidence)
│   - Phase 3 — Assessment and Testing (compliance/maturity/technical)
│   - Phase 4 — Analysis (gap analysis, risk assessment, categorize: Major NC, Minor NC, OFI)
│   - Phase 5 — Reporting (draft → management response → final report with CAP)
│
├── 7. Deliverables (Table: #, Deliverable, Description)
│   1. Audit Plan
│   2. IS Audit Report
│   3. Gap Analysis Report
│   4. Risk Assessment Report
│   5. Executive Summary
│   6. Corrective Action Plan
│
├── 8. Audit Team Composition and Qualifications
│   - Lead Auditor (ISO 27001 LA, CISA certified)
│   - Technical Auditor (network/VAPT expertise)
│   - Compliance Auditor (regulatory/governance knowledge)
│   - Independence requirement
│
├── 9. Timeline and Schedule (Table: Phase, Activity, Duration)
│   Phase 1: Planning (Week 1)
│   Phase 2: Info Gathering (Week 2-3)
│   Phase 3: On-site Assessment (Week 4-5)
│   Phase 4: Analysis/Draft (Week 6)
│   Phase 5: Final Report (Week 7-8)
│
├── 10. Authority and Access
│   - Unrestricted access to all systems, documentation, facilities, personnel
│
├── 11. Confidentiality
│   - All findings confidential; NDA required
│
└── 12. Reporting and Communication
    - Weekly progress updates
    - Draft report within 5 business days of fieldwork
    - Management response within 10 business days
    - Final report within 20 business days
```

---

## 5. Ransomware Readiness Assessment — CISA CSET RRA

> **Question Pattern:** "An organization with 250+ sites, DC and DRC, plans to conduct a Ransomware Readiness Assessment using CISA CSET. How would you conduct this assessment and what weaknesses might be identified?"

**Tool:** CISA Cyber Security Evaluation Tool (CSET) — Ransomware Readiness Assessment (RRA) Module
**Maturity Tiers:** Basic, Intermediate, Advanced

### Report Structure

```
Ransomware Readiness Assessment Report
├── Organization: <<Organization>> with <<N>> sites, DC, DRC
├── Tool: CISA CSET — RRA Module
├── Maturity Levels: Basic, Intermediate, Advanced
│
├── 1. Introduction
│   - RRA evaluates preparedness against ransomware threats
│   - Structured evaluation across 10 goals at 3 maturity levels
│
├── 2. Assessment Methodology
│   - Step 1: Scoping — define boundaries (all sites, DC, DRC)
│   - Step 2: Tool Setup — install CISA CSET, select RRA module
│   - Step 3: Self-Assessment — answer RRA questions per goal at 3 tiers
│     (Naming: Goal [GG] : Level [B,I,A] . Question Number [Q##])
│   - Step 4: Analysis — review CSET-generated dashboards and reports
│   - Step 5: Reporting — document findings and remediation roadmap
│
├── 3. RRA Assessment — 10 Goals
│   │
│   │  Per Goal Table: Level (Basic/Intermediate/Advanced),
│   │  Question Area, Finding, Maturity (Met/Partial/Not Met)
│   │  + "Weakness:" summary after each goal
│   │
│   ├── Goal 1: Asset Management (AM)
│   │   B: Critical assets inventoried
│   │   I: Criticality documented and prioritized
│   │   A: Automated discovery and dependency mapping
│   │
│   ├── Goal 2: Robust Data Backup (DB)
│   │   B: Regular backups performed
│   │   I: Tested regularly; offline/air-gapped copies
│   │   A: Immutable backups; architecture resilient to ransomware
│   │
│   ├── Goal 3: Phishing Prevention and Awareness (PP)
│   │   B: Email filtering and spam protection
│   │   I: Phishing training; simulated exercises
│   │   A: Advanced email security; DMARC/DKIM/SPF
│   │
│   ├── Goal 4: User and Access Management (UM)
│   │   B: Unique user IDs managed
│   │   I: MFA enabled; least privilege enforced
│   │   A: Zero trust; continuous authentication
│   │
│   ├── Goal 5: Network Perimeter Monitoring (NM)
│   │   B: Firewalls and basic perimeter controls
│   │   I: IDS/IPS; network traffic monitored
│   │   A: Network behavior analysis; automated response
│   │
│   ├── Goal 6: Web Browser Management and DNS Filtering (BM)
│   │   B: Browsers kept updated
│   │   I: DNS filtering and web content filtering
│   │   A: Browser isolation; advanced web threat protection
│   │
│   ├── Goal 7: Application Integrity and Allowlisting (AI)
│   │   B: Only authorized software permitted
│   │   I: Allowlisting on critical systems
│   │   A: Application control across all endpoints; automated
│   │
│   ├── Goal 8: Incident Response (IR)
│   │   B: IRP exists with ransomware scenarios
│   │   I: IRP tested via tabletop; communication plan defined
│   │   A: Automated playbooks; threat intelligence integration
│   │
│   ├── Goal 9: Risk Management (RM)
│   │   B: Risk management includes ransomware as threat
│   │   I: Regular risk assessments include ransomware scenarios
│   │   A: Quantitative risk analysis; cyber insurance evaluated
│   │
│   └── Goal 10: Vulnerability Management (VM)
│       B: Regular vulnerability scanning
│       I: Patch management with defined timelines
│       A: Continuous monitoring; automated patching
│
├── 4. Overall RRA Maturity Summary
│   Table: Goal, Basic, Intermediate, Advanced (Met/Partial/Not Met)
│   "Overall Maturity: Basic (Partial)"
│
├── 5. Major Weaknesses Identified (numbered list)
│   1. No air-gapped/offline/immutable backups
│   2. No MFA or PAM
│   3. No ransomware-specific incident response plan
│   4. No application allowlisting
│   5. No network segmentation (flat network)
│   6. No vulnerability management/scanning
│   7. No phishing training
│   8. Ransomware not in risk register
│
└── 6. Recommendations
    - 3-2-1 backup strategy with air-gapped/immutable copy
    - Deploy MFA for all access
    - Develop ransomware-specific IRP with tabletop exercises
    - Implement application allowlisting
    - Network segmentation
    - Vulnerability scanning with patch SLAs
    - Phishing awareness training
    - Include ransomware in risk register; evaluate cyber insurance
```

---

## 6. VAPT Terms of Reference (ToR)

> **Question Pattern:** "A company with 100+ sites, DC and DRC, plans to conduct VAPT. Develop a detailed ToR."

**Standards:** OWASP Testing Guide, PTES, NIST SP 800-115, CVSS

### Report Structure

```
Terms of Reference (ToR) for VAPT
│
├── 1. Introduction — purpose, scope, methodology, deliverables
│
├── 2. Background — organization needs VAPT to identify vulnerabilities
│
├── 3. Objectives
│   - Identify known/unknown vulnerabilities
│   - Assess exploitability via penetration testing
│   - Evaluate DC/DRC security posture
│   - Assess effectiveness of existing controls
│   - Provide prioritized remediation plan
│   - Support compliance with ISO 27001 A.8.8
│
├── 4. Scope of Work
│   ├── 4.1 In-Scope
│   │   - Network infrastructure (all sites, DC, DRC)
│   │   - Servers (application, database, mail, DNS, web)
│   │   - Web applications (customer-facing and internal)
│   │   - Mobile applications (if applicable)
│   │   - Cloud infrastructure (DRC)
│   │   - Wireless networks
│   │   - Endpoints (sample)
│   └── 4.2 Out-of-Scope
│       - Third-party services not under org control
│       - Social engineering (unless explicitly requested)
│       - Physical security testing
│
├── 5. Methodology (OWASP, PTES, NIST SP 800-115, CVSS)
│   - Phase 1: Planning and Scoping
│   - Phase 2: Reconnaissance and Information Gathering
│   - Phase 3: Vulnerability Assessment (automated + manual verification)
│   - Phase 4: Penetration Testing (manual exploitation, lateral movement)
│   - Phase 5: Reporting (CVSS scores, PoC evidence, remediation)
│   - Phase 6: Retest (Optional — verify remediation)
│
├── 6. Rules of Engagement (RoE)
│   - Only within authorized scope/windows
│   - No DoS on production unless authorized
│   - Critical vulns reported immediately
│   - No data modification/exfiltration
│   - All activities logged
│
├── 7. Deliverables (Table)
│   1. Executive Summary
│   2. Detailed VAPT Report
│   3. Vulnerability Assessment Report
│   4. Penetration Testing Report
│   5. Remediation Guidance
│   6. Retest Report (if applicable)
│   7. Raw Data/Logs
│
├── 8. Team Qualifications
│   - Lead Pentester (CEH/OSCP/GPEN, 5+ years)
│   - Web Application Tester (OSCP/GWAPT, OWASP expertise)
│   - Network Security Tester
│   - All sign NDA and conflict of interest declarations
│
├── 9. Timeline (Table: Phase, Activity, Duration)
│
├── 10. Authority and Access
│
├── 11. Confidentiality (NDA, encrypted transmission)
│
└── 12. Reporting and Communication
    - Daily status during testing
    - Critical findings reported immediately
    - Draft report within 5 business days
    - Final report within 15 business days
```

---

## 7. Ransomware Readiness Assessment — Proposal

> **Question Pattern:** "As an expert, outline your approach to conducting a Ransomware Readiness Assessment for a company that has issued an RFP. Prepare a comprehensive proposal."

**Tool:** CISA CSET — RRA Module
**10 Domains × 3 Tiers (Basic, Intermediate, Advanced)**

### Proposal Structure

```
Ransomware Readiness Assessment — Proposal
│
├── 1. Introduction
│   - Outlines approach for RRA using CISA CSET RRA module
│   - Evaluates across 10 domains at 3 maturity tiers
│
├── 2. Objectives
│   - Evaluate ransomware preparedness using CISA RRA framework
│   - Identify gaps across 10 domains
│   - Determine maturity (Basic/Intermediate/Advanced) per domain
│   - Provide prioritized remediation roadmap
│
├── 3. Scope
│   - All sites, DC, DRC, critical systems, network, endpoints, cloud
│   - Policies, procedures, incident response capabilities
│
├── 4. Assessment Framework
│   - Tool: CISA CSET RRA Module
│   - 10 Domains (Table: #, Domain, Focus Area)
│     1. Asset Management (AM)
│     2. Robust Data Backup (DB)
│     3. Phishing Prevention and Awareness (PP)
│     4. User and Access Management (UM)
│     5. Network Perimeter Monitoring (NM)
│     6. Web Browser Mgmt and DNS Filtering (BM)
│     7. Application Integrity and Allowlisting (AI)
│     8. Incident Response (IR)
│     9. Risk Management (RM)
│     10. Vulnerability Management (VM)
│   - Maturity Tiers: Basic → Intermediate → Advanced
│
├── 5. Methodology
│   - Phase 1: Pre-Engagement and Scoping (Week 1) — discovery meeting, NDA
│   - Phase 2: Assessment and Evaluation (Week 2-3) — CSET tool, evidence review, interviews
│   - Phase 3: Validation and Testing (Week 3-4) — vuln scanning, tabletop exercise, backup restoration test
│   - Phase 4: Analysis and Reporting (Week 4-5) — CSET results, gap analysis, prioritization
│   - Phase 5: Reporting and Presentation (Week 5-6) — draft, present, final report
│
├── 6. Deliverables (Table)
│   1. RRA Maturity Assessment Report
│   2. Gap Analysis Report
│   3. Vulnerability Scan Report
│   4. Tabletop Exercise Report
│   5. Executive Summary
│   6. Remediation Roadmap
│
├── 7. Team Composition
│   - Lead Assessor (CISA/CISM, ransomware IR experience)
│   - Technical Assessor (network/endpoint/VAPT)
│   - GRC Assessor (risk/policy/compliance)
│
├── 8. Timeline (Table: Phase, Activity, Duration)
│
└── 9. Confidentiality (NDA, authorized stakeholders only)
```

---

## 8. Audit of Incident Response Plan — NIST SP 800-61

> **Question Pattern:** "You are assigned to evaluate the effectiveness of the Incident Response Plan at <<Organization>>. How would you conduct this audit?"

**Standard:** NIST SP 800-61 Rev.2 (Incident Handling Guide) — 4-Phase Lifecycle
**ISO Reference:** ISO 27001:2022 Controls A.5.24–A.5.28

### Audit Structure

```
IRP Audit Methodology — <<Organization>>
├── Audit Reference: NIST SP 800-61, ISO 27001:2022 (A.5.24–A.5.28), NIST CSF 2.0 (RS)
│
├── 1. Introduction
│   - Evaluate IRP effectiveness
│   - Determine if practical, aligned with best practices
│   - Adequately addresses risks, incident handling, recovery
│
├── 2. Audit Objectives
│   - Formal IRP exists and is documented
│   - Aligned with NIST SP 800-61 four-phase lifecycle and ISO 27001
│   - IRT/CSIRT is ready and capable
│   - IRP is tested, maintained, continuously improved
│   - Integrated with BCP/DRP
│
├── 3. Audit Methodology — NIST SP 800-61 Four-Phase Lifecycle
│   │
│   ├── Phase 1: Preparation
│   │   Step 1: Review IRP Policy and Documentation
│   │     - Formal policy exists, approved, defines authority/scope
│   │     - IRP defines: classification, escalation, roles, communication, evidence handling
│   │     - Covers relevant incident types for the organization
│   │   Step 2: Assess IRT/CSIRT Structure
│   │     - Formally established with defined membership
│   │     - Roles assigned: incident commander, technical lead, comms lead, legal
│   │     - Skills adequate; 24/7 or on-call availability
│   │   Step 3: Evaluate Training and Readiness
│   │     - IR training records for IRT and general staff
│   │     - Tabletop exercises conducted and documented
│   │     - Staff know how to report/escalate incidents
│   │   Step 4: Review Tools and Resources
│   │     - SIEM, forensic tools, secure communications, tracking system
│   │     - IRT has access to hardware, software, forensic kits
│   │
│   ├── Phase 2: Detection and Analysis
│   │   Step 5: Evaluate Detection Capabilities
│   │     - Monitoring tools: IDS/IPS, SIEM, endpoint protection, log management
│   │     - IoCs and alert thresholds defined
│   │     - Criteria for classifying events vs incidents (ISO A.5.25)
│   │   Step 6: Assess Triage and Analysis Process
│   │     - Alert analysis: who receives, how prioritized, decisions
│   │     - Severity levels defined (Low/Medium/High/Critical) with response timelines
│   │     - Sample incident records reviewed
│   │
│   ├── Phase 3: Containment, Eradication, and Recovery
│   │   Step 7: Review Containment Procedures
│   │     - Short-term and long-term containment strategies per incident type
│   │     - Evidence preservation (ISO A.5.28)
│   │     - System isolation procedures
│   │   Step 8: Evaluate Eradication and Recovery
│   │     - Root cause removal (malware, patching, credential reset)
│   │     - Recovery from clean backups
│   │     - Validation before returning to production
│   │     - Integration with BCP/DRP
│   │
│   └── Phase 4: Post-Incident Activity
│       Step 9: Assess Lessons Learned
│         - Post-incident reviews mandated (ISO A.5.27)
│         - Evidence of meetings: minutes, attendees, action items
│         - Findings used to update IRP and improve controls
│       Step 10: Evaluate Reporting and Communication
│         - Communication plan: internal (management), external (regulatory)
│         - Reporting timelines aligned with regulations
│         - Templates prepared (stakeholders, media, affected parties)
│
└── 4. Audit Deliverables
    - IRP Effectiveness Assessment Report mapped to NIST SP 800-61 phases
    - Gap analysis vs ISO 27001 A.5.24–A.5.28
    - Risk ratings per area
    - Recommendations with priorities
    - Recommend tabletop exercise
```

---

## 9. Audit of Business Continuity Plan (BCP)

> **Question Pattern:** "You are assigned to evaluate the effectiveness of the BCP at <<Organization>>. How would you conduct this audit?"

**Standards:** ISO 22301 (BCMS), ISO 27001:2022 (A.5.29, A.5.30), NIST CSF (RC function)

### Audit Structure

```
BCP Audit Methodology — <<Organization>>
│
├── 1. Introduction — evaluate BCP effectiveness
│
├── 2. Audit Objectives
│   - BCP exists, documented, approved
│   - Aligned with ISO 22301 / ISO 27001 (A.5.29, A.5.30)
│   - Covers all critical business functions
│   - RTO/RPO defined and achievable
│   - Tested and maintained
│
├── 3. Audit Steps
│   Step 1: Review BCP Policy and Plan Documentation
│     - Formal BCP policy approved by management
│     - Plan covers scope, critical functions, recovery strategies
│   Step 2: Evaluate Business Impact Analysis (BIA)
│     - BIA conducted; critical functions identified and prioritized
│     - RTO and RPO defined for each critical function
│     - Dependencies mapped (IT, people, suppliers)
│   Step 3: Review Recovery Strategies
│     - DRP for IT systems — DC/DRC failover
│     - Alternate work locations for personnel
│     - Communication plan during disruption
│   Step 4: Assess Testing and Exercises
│     - BCP/DRP tested (tabletop, walkthrough, full failover)
│     - Test results documented with lessons learned
│     - Frequency of testing (at least annually)
│   Step 5: Evaluate Roles and Responsibilities
│     - Crisis management team defined
│     - Roles clear: crisis commander, comms lead, IT lead
│   Step 6: Review Maintenance and Updates
│     - BCP reviewed and updated annually or after changes
│     - Distribution to key personnel verified
│   Step 7: Assess ICT Readiness (ISO A.5.30)
│     - ICT continuity plans aligned with BCP objectives
│     - DRC tested for failover; RTO/RPO validated
│
└── 4. Deliverables — Assessment report, gap analysis, recommendations
```

---

## 10. Risk Assessment of Information Assets

> **Question Pattern:** "As CRO of <<Organization>>, identify at least 5 information assets of the information processing facility. Perform risk assessment of all assets."

### Report Structure

```
Risk Assessment
├── Role: Chief Risk Officer (CRO) of <<Organization>>
│
├── 1. Identification of Information Assets
│   Table: #, Asset, Category, Description
│   (Pick 5 relevant to the organization type)
│
├── 2. Risk Assessment
│   For EACH asset, table with:
│   - Confidentiality: High/Medium/Low — reason
│   - Integrity: High/Medium/Low — reason
│   - Availability: High/Medium/Low — reason
│   - Threats: list specific threats
│   - (If asked) Threat Capability: High/Medium/Low — reason
│   - Vulnerabilities: list specific vulnerabilities
│   - Existing Controls: what's currently in place
│   - Likelihood: High/Medium/Low
│   - Impact: High/Medium/Low — consequences
│   - Risk Rating: HIGH/MEDIUM/LOW
│   - Recommendation: specific remediation
│
├── 3. Risk Assessment Summary
│   Table: #, Asset, C, I, A, Risk Rating
│
└── Closing: All assets require risk treatment tracked via Risk Register
```

### Asset Selection by Organization Type

| Organization Type      | Suggested Assets                                                                   |
| ---------------------- | ---------------------------------------------------------------------------------- |
| General company        | Core Database Server, Email System, Network Infrastructure, Backup Storage, Web App Server |
| Wallet/Fintech         | Transaction DB, Mobile App Backend (API), Payment Gateway, KYC System, Network     |
| Bank                   | Core Banking System, Internet/Mobile Banking, ATM System, Customer DB, Network     |
| Insurance              | Policy Management System, Customer DB, Claims System, Email, Network               |
| Airline                | Booking System, Passenger Data System, Flight Ops System, IVR/Telephony, Network   |
| Telecom                | Subscriber DB, Billing System, Network Infrastructure, CRM, Service Platform       |
| Stock Broker           | Trading Platform, Customer Portfolio DB, Payment Gateway, Market Data Feed, Network |

---

## 11. Information Security Policy Framework

> **Question Pattern:** "As CISO of <<Organization>>, design an Information Security Policy framework to mitigate IS risks to an acceptable level."

### Framework Structure

```
Information Security Policy Framework — <<Organization>>
│
├── 1. Policy Framework Structure
│   ├── Level 1 — Overarching Information Security Policy
│   │   - Organization's commitment to information security
│   │   - Approved by top management / Board
│   │   - Aligned with ISO 27001:2022, regulatory requirements, business objectives
│   │   - Scope of ISMS defined
│   │   - Reviewed annually or upon significant changes
│   │
│   ├── Level 2 — Topic-Specific Policies
│   │   - Access Control Policy (MFA, RBAC, PAM, access review)
│   │   - Acceptable Use Policy (IT assets, internet, email, removable media)
│   │   - Data Classification and Handling Policy (Public/Internal/Confidential/Restricted)
│   │   - Backup and Recovery Policy (RTO, RPO, frequency, encryption, testing)
│   │   - Incident Management Policy (categories, escalation, response, evidence, reporting)
│   │   - Password Policy (12-char min, complexity, rotation, no shared credentials)
│   │   - Remote Access and Teleworking Policy (VPN, MFA, endpoint security)
│   │   - Change Management Policy (approval, testing, documentation, rollback)
│   │   - Physical and Environmental Security Policy (DC/DRC access, CCTV, environmental)
│   │   - Supplier and Third-Party Security Policy (contracts, right to audit)
│   │   - (Sector-specific: e.g., Digital Banking Security Policy for banks)
│   │
│   └── Level 3 — Procedures and Guidelines
│       - SOPs for implementing each policy
│       - Technical guidelines (hardening, secure coding, network config)
│       - Checklists (audit, incident response, BCP)
│
├── 2. Policy Development Process
│   - Conduct Risk Assessment → identify risks → determine controls
│   - Map to ISO 27001:2022 Annex A (93 controls, 4 themes)
│   - Align with regulatory requirements (sector-specific)
│   - Draft with stakeholder input (IT, HR, Legal, Operations)
│   - Top management approval
│   - Communicate to all personnel; obtain written acknowledgement
│
├── 3. Policy Implementation and Enforcement
│   - Security awareness training
│   - Compliance checks via IS Audits
│   - Disciplinary procedures for violations
│   - Technical controls to enforce (DLP, MFA, endpoint protection, SIEM)
│
├── 4. Policy Review and Maintenance
│   - Annual review minimum
│   - Additional reviews on significant changes/incidents/regulatory updates
│   - Version control and review history
│   - Communicate updates to all personnel
│
└── 5. Regulatory Alignment
    - ISO/IEC 27001:2022
    - Electronic Transactions Act, 2063 (2008)
    - Individual Privacy Act, 2075 (2018)
    - NIST Cybersecurity Framework
    - Sector-specific (NRB IT Guidelines for banks, NTA for telecom, CAAN for aviation, etc.)
    - (PCI DSS if card payments involved)
```

---

## 12. Tasks and Knowledge Areas of a Professional IS Auditor

> **Question Pattern:** "Describe the key responsibilities/tasks an IS Auditor must perform and the key knowledge areas/domains they must acquire."

**Reference:** ISACA CISA — 5 Domains

### Outline

```
IS Auditor — Tasks and Knowledge Areas
│
├── Critical Tasks (5 Tasks)
│   ├── Task 1: IS Audit Planning
│   │   - Define objectives, scope, criteria (ISO 27001, COBIT 2019, NIST CSF)
│   │   - Develop audit plan and program with resources/timelines
│   │   - Preliminary risk assessment to prioritize audit areas
│   │   - Identify stakeholders and communication channels
│   │
│   ├── Task 2: Executing the Audit
│   │   - Gather evidence: documentation review, interviews, observation, technical verification
│   │   - Compliance testing (controls exist and are followed)
│   │   - Substantive testing (data accuracy and completeness)
│   │   - CAATs, sampling techniques, audit questionnaires
│   │
│   ├── Task 3: Assessing IT Governance and Management
│   │   - Evaluate IT governance (COBIT 2019 framework)
│   │   - Assess IT strategy alignment with business objectives
│   │   - Review IT policies, procedures, organizational structure
│   │   - Evaluate IT resource management and performance monitoring
│   │
│   ├── Task 4: Evaluating Information Systems and Controls
│   │   - Logical and physical access controls
│   │   - Network security, system configs, vulnerability management
│   │   - Change, problem, incident management processes
│   │   - BCP/DRP effectiveness
│   │   - Data backup and recovery procedures
│   │
│   └── Task 5: Reporting and Follow-Up
│       - Document findings with evidence, risk ratings, recommendations
│       - Classify: Major NC, Minor NC, Opportunity for Improvement (OFI)
│       - Present to management and stakeholders
│       - Track corrective action plans; verify in follow-up audits
│
└── Key Knowledge Domains (CISA 5 Domains)
    ├── Domain 1: IS Auditing Process
    │   - ISACA Standards, Guidelines, Code of Ethics
    │   - Audit methodologies (risk-based, compliance, substantive)
    │   - ISO 27001, NIST CSF, COBIT 2019, CIS Controls
    │
    ├── Domain 2: Governance and Management of IT
    │   - COBIT 2019 (EDM, APO, BAI, DSS, MEA domains)
    │   - IT strategy, policies, organizational structures
    │   - IT risk management and assessment
    │   - Regulatory requirements (ETA 2008, Privacy Act 2018)
    │
    ├── Domain 3: IS Acquisition, Development and Implementation
    │   - SDLC and Secure SDLC (SecSDLC)
    │   - Change management and configuration management
    │   - Project management practices
    │
    ├── Domain 4: IS Operations and Business Resilience
    │   - IT service management (incident, problem, change management)
    │   - BCP, DRP, BIA
    │   - Backup and recovery — RTO, RPO
    │   - Data center operations, cloud computing
    │
    └── Domain 5: Protection of Information Assets
        - Access control models, authentication, encryption
        - Network security (firewalls, IDS/IPS, VPN, segmentation)
        - VAPT
        - SIEM, logging, monitoring
        - Data classification, privacy, protection
```

---

## 13. Importance of IS Audit with Example

> **Question Pattern:** "Discuss the importance of conducting IS Audit and illustrate with a suitable example."

### Outline

```
Importance of IS Audit
│
├── 1. Key Importance Points
│   - Identifying Security Risks and Vulnerabilities (proactive mitigation)
│   - Ensuring Regulatory Compliance (ETA 2008, Privacy Act 2018, sector regulations)
│   - Protecting CIA Triad (Confidentiality, Integrity, Availability)
│   - Improving IT Governance (COBIT 2019, IT-business alignment)
│   - Evaluating Business Continuity Readiness (BCP, DRP, RTO/RPO)
│   - Building Stakeholder Confidence (Board, regulators, customers)
│   - Driving Continuous Improvement (recommendations → corrective actions)
│
└── 2. Example: IS Audit of <<Organization>> (e.g., Yeti Airlines)
    - Organization context and scope
    - Summary of controls audited (use table: #, Control, ISO Ref, Risk)
    - Key findings: what gaps were found
    - Impact: what actions the organization initiated based on audit
    - Conclusion: IS Audit is a critical mechanism for identifying and remediating weaknesses
```

---

## 14. 4P Framework for Cybersecurity Risk

> **Question Pattern:** "As Chief Compliance Officer, describe how the 4P framework can be applied to identify and mitigate cybersecurity risks."

### Outline

```
4P Framework — People, Process, Policy, Platform (Technology)
│
├── 1. People
│   - Cybersecurity awareness training (annual minimum)
│   - Define IS roles (CISO, security focal points)
│   - Background screening for sensitive roles
│   - Security culture (phishing simulations, incident reporting, disciplinary procedures)
│   - Adequate cybersecurity staffing
│
├── 2. Process
│   - Risk Assessment and Treatment (ISO 27001:2022)
│   - Incident Response Process (detection → containment → eradication → recovery → lessons learned)
│   - Change and Problem Management
│   - Periodic VAPT
│   - BIA, BCP, DRP
│   - User access lifecycle (provision → review → de-provision)
│
├── 3. Policy
│   - Information Security Policy (approved, annual review)
│   - Topic-specific policies (Acceptable Use, Access Control, Data Classification, Backup, Remote Access, Password, Incident Management)
│   - Regulatory alignment (ETA 2008, Privacy Act 2018, sector-specific)
│   - Communicate and obtain acknowledgement
│   - Compliance monitoring and audit
│
├── 4. Platform (Technology)
│   - EDR/Antivirus (centralized, all endpoints)
│   - MFA for critical systems
│   - SIEM (log management, correlation, alerting)
│   - Network segmentation, Firewall, IDS/IPS, DLP
│   - Encryption (at rest and in transit)
│   - PAM (privileged access management)
│   - Patch management (defined timelines)
│
└── Application
    Map risks against People/Process/Policy/Platform →
    Assess CIA impact → Prioritize by risk rating →
    Track via Risk Register with owners and timelines
```

---

## 15. Problem and Change Management in IS Audit

> **Question Pattern:** "Explain the importance of Problem/Change Management in an audit and describe key activities an IS Auditor should perform."

**Standards:** ITIL, ISO 20000, ISO 27001:2022 (A.8.32 — Change Management)

### Outline

```
Problem and Change Management
│
├── Problem Management
│   ├── Importance
│   │   - Minimizes service disruptions (root cause elimination)
│   │   - Reduces incident recurrence
│   │   - Improves service quality
│   │   - Supports regulatory compliance
│   │   - Builds Known Error Database (KEDB)
│   │
│   └── IS Auditor Activities
│       1. Review Problem Management Policy and Procedures
│       2. Evaluate Problem Identification Process (reactive + proactive)
│       3. Assess Root Cause Analysis (RCA) — 5-Why, Fishbone, Fault Tree
│       4. Review Known Error Database (KEDB)
│       5. Evaluate Problem Resolution and Closure
│       6. Assess Problem Management KPIs
│
├── Change Management
│   ├── Importance
│   │   - Prevents unauthorized changes
│   │   - Ensures service stability (testing, rollback plans)
│   │   - Maintains audit trail
│   │   - Supports compliance (ISO 27001 A.8.32)
│   │   - Reduces security risks
│   │
│   └── IS Auditor Activities
│       1. Review Change Management Policy and Procedures
│          (Standard, Normal, Emergency categories; CAB composition)
│       2. Evaluate Change Request and Logging Process
│       3. Assess Change Authorization (CAB approval; emergency fast-track)
│       4. Review Testing and Validation (non-production testing, sign-off)
│       5. Evaluate Implementation and Rollback (maintenance windows, PIR)
│       6. Assess Change Management KPIs
│          (success rate, failed changes, unauthorized changes, emergency ratio)
```

---

## 16. Secure SDLC (SecSDLC) Audit

> **Question Pattern:** "As an IT auditor, explain how you would audit the SecSDLC process to ensure security is integrated throughout."

**Reference:** ISO 27001:2022 (A.8.25–A.8.31), OWASP, NIST SSDF

### Outline

```
SecSDLC Audit
│
├── Importance of Security by Design
│   - Vulnerabilities introduced in design/coding are costly to fix later
│   - "Shift left" security — integrate from requirements phase
│   - Reduces application-level attacks (OWASP Top 10)
│   - Supports compliance with ISO 27001 A.8.25 (Secure Development Life Cycle)
│
└── Audit of Each SDLC Phase
    1. Requirements Phase — security requirements defined (A.8.26)
    2. Design Phase — threat modeling, secure architecture principles (A.8.27)
    3. Development Phase — secure coding standards (A.8.28), code review
    4. Testing Phase — security testing: SAST, DAST, pentest (A.8.29)
    5. Deployment Phase — secure deployment procedures, change management
    6. Maintenance Phase — vulnerability management, patching
    7. Environment Separation — dev/test/prod separation (A.8.31)
    8. Outsourced Development — security requirements in contracts (A.8.30)
```

---

## 17. Short Notes Templates

### IT Governance with COBIT
- COBIT 2019 by ISACA — governance and management of enterprise I&T
- Core Principles: Meeting Stakeholder Needs, End-to-End, Single Integrated Framework, Holistic Approach, Separating Governance from Management
- 5 Domains (40 objectives): EDM (Governance) + APO, BAI, DSS, MEA (Management)
- Capability Maturity: Level 0 (Incomplete) to Level 5 (Optimizing)
- Design Factors for tailoring
- IS Auditors use COBIT to evaluate IT governance alignment with business

### Licensing Issues in IS Audit
- License types: Proprietary, Open Source, SaaS/Subscription, Volume, OEM
- Key issues: Piracy, Under-licensing, Over-licensing, No license tracking (SAM), Expired licenses, Open source compliance
- Auditor role: verify inventory, compare installed vs. entitled, check procurement, detect unauthorized software, review renewal tracking

### Audit Questionnaire
- Structured set of questions for systematic information gathering
- Types: General IT Controls, Application Controls, Compliance, Self-Assessment
- Structure: organized by domain; each question has expected response, actual response, evidence, status, remarks
- Role: used in planning/execution; responses corroborated with evidence; findings feed into audit report

### Audit Sampling
- Selecting a subset of data/transactions to evaluate controls
- Types: Statistical sampling (random, systematic) and Non-statistical (judgmental)
- Purpose: efficient audit coverage when 100% testing is impractical
- Key factors: sample size, selection method, confidence level, tolerable error rate
- Results extrapolated to the full population

### Governance of Enterprise I&T
- IT Governance ensures IT supports and enables business objectives
- Frameworks: COBIT 2019, ISO 38500, ITIL
- Key areas: strategic alignment, value delivery, risk management, resource management, performance measurement
- IS Auditor evaluates: IT strategy alignment, governance structures, policy compliance, risk management effectiveness

---

## 18. Asset Identification — Cooperative Bank / Organization

> **Question Pattern:** "Identify Information Assets, Software Assets, Physical Assets, and Service Assets required for <<Organization>>."

### Outline

```
Asset Identification — <<Organization>>
│
├── Information Assets
│   - Customer/User Database (personal data, KYC, account details)
│   - Transaction Records (financial transactions)
│   - Core Business Data (ledger, records, reports)
│   - Audit Logs and Trails
│   - Policies and Procedures
│   - Employee Records
│   - Credentials/Authentication Data
│   - Regulatory Reports
│
├── Software Assets
│   - Core Business Application/System
│   - Customer-facing Applications (mobile, web portal)
│   - Database Management System (Oracle/SQL Server)
│   - Operating Systems (server and desktop)
│   - Endpoint Protection/Antivirus
│   - Email System
│   - SIEM/Log Management
│   - Backup Software
│   - (Sector-specific: ATM/POS software, trading platform, etc.)
│
├── Physical Assets
│   - Servers (application, database, web at DC/DRC)
│   - Network Equipment (routers, switches, firewalls, load balancers)
│   - Storage Systems (SAN/NAS)
│   - UPS and Power Systems
│   - CCTV and Surveillance
│   - Access Control Systems (biometric/card)
│   - Workstations and Laptops
│   - Environmental Controls (AC, fire suppression, sensors)
│   - Cabling Infrastructure
│   - (Sector-specific: ATMs, POS terminals, etc.)
│
└── Service Assets
    - Internet Connectivity (ISP, primary + redundant)
    - WAN/MPLS Connectivity
    - SMS Gateway Service
    - Payment Gateway Service
    - Cloud DRC Service
    - IT Support and Maintenance (AMC)
    - Security Operations (SOC)
    - Call Center / Customer Support
```
