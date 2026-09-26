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

| Theme          | Common Controls for Exam                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------ |
| Organizational | A.5.1 (Policies), A.5.2 (Roles), A.5.15 (Access Control)                                         |
| People         | A.6.3 (Awareness/Training)                                                                       |
| Physical       | A.7.1 (Physical Perimeters), A.7.3 (Securing Rooms)                                              |
| Technological  | A.8.2 (Privileged Access), A.8.7 (Malware), A.8.8 (Vuln Mgmt), A.8.13 (Backup), A.8.15 (Logging) |

### Typical Observations (Reusable)

| Control | Typical Observation                                                                                                                               |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| A.5.1   | Policy exists but not reviewed since creation; no topic-specific policies; staff unaware; no written acknowledgement                              |
| A.5.2   | No dedicated CISO; IT handles security ad-hoc; no roles at branches; no escalation matrix                                                         |
| A.6.3   | No structured training program; staff unaware of phishing/passwords; no records; shared credentials observed                                      |
| A.7.1   | DC uses key-lock (no biometric/card); no visitor log; DRC shared corridors; CCTV retention 15 days                                                |
| A.7.3   | No environmental sensors; standard fire extinguishers (not gas-based); no UPS records; DRC no generator                                           |
| A.8.2   | No access control policy; terminated accounts active; shared accounts; weak password (6-char); no MFA; shared admin credentials                   |
| A.8.7   | Antivirus not centrally managed; outdated definitions at branches; no EDR; no USB restrictions                                                    |
| A.8.8   | No VAPT; ad-hoc patching; outdated OS; customer app not security-tested; no software inventory                                                    |
| A.8.13  | Daily backup but no policy; weekly DRC replication (7-day gap); no restoration test 12+ months; RTO/RPO not defined; no encryption                |
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

| If question says...                 | Use                                                                                      |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| NIST CSF v1.1 / five core functions | **NIST CSF v1.1** — 5 functions: Identify, Protect, Detect, Respond, Recover             |
| NIST CSF v2.0 / six core functions  | **NIST CSF v2.0** — 6 functions: **Govern**, Identify, Protect, Detect, Respond, Recover |
| Just "NIST CSF" (unspecified)       | Check question context; if "six functions" mentioned → v2.0                              |

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

| Organization Type | Suggested Assets                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------ |
| General company   | Core Database Server, Email System, Network Infrastructure, Backup Storage, Web App Server |
| Wallet/Fintech    | Transaction DB, Mobile App Backend (API), Payment Gateway, KYC System, Network             |
| Bank              | Core Banking System, Internet/Mobile Banking, ATM System, Customer DB, Network             |
| Insurance         | Policy Management System, Customer DB, Claims System, Email, Network                       |
| Airline           | Booking System, Passenger Data System, Flight Ops System, IVR/Telephony, Network           |
| Telecom           | Subscriber DB, Billing System, Network Infrastructure, CRM, Service Platform               |
| Stock Broker      | Trading Platform, Customer Portfolio DB, Payment Gateway, Market Data Feed, Network        |

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

---

# ISA Exam — Generalized Outlines for Audit & Assessment Proposals

> These are **proposal** outlines — used when responding to RFP/RFQ or when the question says "prepare a comprehensive proposal." Adapt `<<Organization>>`, `<<N sites>>`, etc. to the question context.

> **Key Difference from Reports/Assessments (outlines1.md):** A proposal is written **before** the engagement begins. It describes _how_ you will conduct the work, not the findings. It includes commercial/logistical elements like team qualifications, timeline, deliverables, and confidentiality — but **no observations or findings**.

---

## 1. Proposal for Conducting an Information System Audit (ISO 27001:2022)

> **Question Pattern:** "Prepare a comprehensive proposal for conducting an IS Audit for <<Organization>> with <<N>> sites, DC and DRC, focusing on <<N>> controls of ISO 27001:2022."
> **Syllabus Reference:** Unit 4 (Conducting an IS Audit), Workshop #4 & #5
> **Standards:** ISO/IEC 27001:2022, ISO 19011 (Guidelines for Auditing Management Systems)

### Proposal Structure

```
Proposal for Information System Audit
│
├── 1. Cover Page
│   - Proposal Title: Proposal for Information System Audit
│   - Submitted To: <<Organization>>
│   - Submitted By: <<Audit Firm Name>>
│   - Date of Submission
│   - Reference: RFP/RFQ Number (if applicable)
│   - Document Version and Classification: Confidential
│
├── 2. Introduction
│   - ICT plays a vital role for <<Organization>> to enable its business processes
│   - IS Audit systematically evaluates security posture of information systems
│   - This proposal outlines approach to conduct IS Audit aligned with ISO 27001:2022
│   - Audit will evaluate <<N>> Annex A controls across 4 themes
│   - Preserves CIA by applying a risk management process
│   - Gives confidence to stakeholders that risks are adequately managed
│
├── 3. Understanding of the Organization
│   - <<Organization>> operates <<N>> sites with own DC and DRC
│   - Nature of business and critical business processes
│   - Regulatory environment (Electronic Transactions Act 2008, Individual Privacy Act 2018,
│     sector-specific regulations)
│   - Key IT systems and infrastructure supporting operations
│
├── 4. Audit Objectives
│   - Evaluate effectiveness of ISMS against ISO 27001:2022
│   - Audit <<N>> selected Annex A controls across all 4 themes
│   - Identify vulnerabilities, risks, and gaps in current security posture
│   - Assess compliance with applicable regulatory requirements
│   - Provide actionable recommendations with risk-based prioritization
│   - Support continuous improvement of the ISMS
│
├── 5. Scope of Work
│   ├── 5.1 Infrastructure Scope
│   │   - Head Office, Data Center (DC), Disaster Recovery Center (DRC)
│   │   - Sample of branch/remote sites
│   │   - Network infrastructure, servers, endpoints, applications
│   │
│   ├── 5.2 Controls to be Audited (Table: #, Control, ISO Reference, Theme)
│   │   Select <<N>> controls covering all 4 Annex A themes:
│   │   - Organizational: A.5.1 (Policies), A.5.2 (Roles)
│   │   - People: A.6.3 (Awareness/Training)
│   │   - Physical: A.7.1 (Physical Perimeters), A.7.3 (Securing Rooms)
│   │   - Technological: A.8.2 (Access Control), A.8.7 (Malware), A.8.8 (Vuln Mgmt),
│   │     A.8.13 (Backup), A.8.15 (Logging)
│   │
│   └── 5.3 Exclusions
│       - Any explicitly excluded areas (third-party systems not under org control, etc.)
│
├── 6. Audit Criteria / Standards and Frameworks
│   - ISO/IEC 27001:2022 — 93 Annex A controls (4 themes)
│   - ISO 19011 — Guidelines for Auditing Management Systems
│   - Applicable regulations (ETA 2008, Privacy Act 2018, sector-specific)
│   - Organizational IT policies and procedures
│
├── 7. Audit Methodology
│   ├── Phase 1 — Planning and Preparation (Week 1)
│   │   - Kick-off meeting with management
│   │   - Review existing documentation (policies, SoA, risk register)
│   │   - Develop detailed audit plan and checklist
│   │   - Identify key personnel for interviews
│   │
│   ├── Phase 2 — Information Gathering (Week 2)
│   │   - Document review: policies, procedures, records, evidence
│   │   - Interviews with process owners and key personnel
│   │   - Site visits: Head Office, DC, DRC, sample branches
│   │
│   ├── Phase 3 — Assessment and Testing (Week 3–4)
│   │   - Compliance testing: verify controls exist and are followed
│   │   - Substantive testing: data accuracy and completeness
│   │   - Technical verification: system configs, access logs, vulnerability reports
│   │   - Use of CAATs, sampling techniques, audit questionnaires
│   │
│   ├── Phase 4 — Analysis and Evaluation (Week 5)
│   │   - Gap analysis against ISO 27001:2022
│   │   - Risk assessment of identified gaps
│   │   - Categorize findings: Major NC, Minor NC, OFI
│   │   - Develop risk ratings (HIGH / MEDIUM / LOW) per control
│   │
│   └── Phase 5 — Reporting (Week 6–7)
│       - Draft report submitted for factual verification
│       - Management response within 10 business days
│       - Final report with agreed Corrective Action Plan (CAP)
│
├── 8. Deliverables (Table: #, Deliverable, Description)
│   1. Audit Plan — Detailed plan with schedule, scope, methodology
│   2. IS Audit Report — Comprehensive report with per-control findings
│      (Control, Observation, Risk Rating, Recommendation)
│   3. Gap Analysis Report — Gaps identified against ISO 27001:2022
│   4. Risk Assessment Report — Risk ratings and prioritization
│   5. Executive Summary — High-level summary for management/Board
│   6. Corrective Action Plan (CAP) — Agreed remediation with timelines
│
├── 9. Audit Team Composition and Qualifications (Table: Role, Qualification, Responsibility)
│   - Lead Auditor: ISO 27001 Lead Auditor (LA) certified, CISA, 7+ years IS Audit experience
│   - Technical Auditor: Network/infrastructure expertise, VAPT skills, CEH/OSCP
│   - Compliance Auditor: Regulatory/governance knowledge, GRC experience
│   - All team members independent of the organization (no conflict of interest)
│
├── 10. Timeline and Schedule (Table: Phase, Activity, Duration, Week)
│   Phase 1: Planning and Preparation          — Week 1
│   Phase 2: Information Gathering              — Week 2
│   Phase 3: Assessment and Testing             — Week 3–4
│   Phase 4: Analysis and Evaluation            — Week 5
│   Phase 5: Draft Report                       — Week 6
│   Phase 6: Management Response & Final Report — Week 7
│   Total Duration: 7 Weeks
│
├── 11. Per-Control Reporting Format
│   For each of the <<N>> controls, the audit report will cover:
│   1. Control — ISO 27001:2022 control statement
│   2. Purpose — Why this control exists
│   3. Observation — Findings during audit (specific gaps, evidence)
│   4. Risk Rating — HIGH / MEDIUM / LOW
│   5. Recommendation — Actionable remediation steps
│   6. Management Response — Organization's planned action
│
├── 12. Authority and Access Requirements
│   - Unrestricted access to all systems, documentation, facilities, personnel
│   - Cooperation from all departments during audit
│   - Availability of key personnel for interviews
│
├── 13. Confidentiality and Terms
│   - All findings treated as strictly confidential
│   - NDA to be executed before engagement commencement
│   - Report shared only with authorized stakeholders
│
└── 14. Reporting and Communication
    - Weekly progress updates during engagement
    - Draft report within 5 business days of completing fieldwork
    - Management response within 10 business days
    - Final report within 20 business days of engagement completion
```

### Why This Differs from the Audit Report (Outline #1)

| Aspect       | Proposal (This Outline)                    | Audit Report (Outline #1)            |
| ------------ | ------------------------------------------ | ------------------------------------ |
| Written      | **Before** audit begins                    | **After** audit is completed         |
| Contains     | Approach, methodology, team, timeline      | Observations, findings, risk ratings |
| Observations | ❌ None — audit hasn't happened yet        | ✅ Per-control observations          |
| Deliverables | Listed as promised outputs                 | Actual content of the deliverable    |
| Audience     | Client evaluating proposals (RFP response) | Client receiving audit results       |

---

## 2. Proposal for Information Security Self-Assessment (ISO 27001:2022 — 93 Controls)

> **Question Pattern:** "Prepare a proposal for conducting Information Security Self-Assessment aligned with ISO/IEC 27001:2022 focusing on 93 Annex A controls."
> **Syllabus Reference:** Unit 1 (ISO 27001), Workshop #1
> **Standard:** ISO/IEC 27001:2022 — All 93 Annex A controls

### Proposal Structure

```
Proposal for Information Security Self-Assessment
│
├── 1. Cover Page
│   - Title, Submitted To/By, Date, Reference
│
├── 2. Introduction
│   - Organization operates <<N>> sites with in-house DC and private cloud DRC
│   - Self-assessment evaluates current security posture against ISO 27001:2022
│   - Systematically reviews existing security measures across 93 Annex A controls
│   - Identifies risks/gaps and supports continuous improvement of ISMS
│   - Self-assessment is an INTERNAL exercise (vs. external audit)
│
├── 3. Objectives
│   - Evaluate implementation status of all 93 Annex A controls across 4 themes
│   - Identify gaps between current posture and ISO 27001:2022 requirements
│   - Assess risk level for each identified gap
│   - Determine readiness for external certification audit
│   - Provide a roadmap for continuous ISMS improvement
│
├── 4. Scope
│   - All <<N>> sites, Data Center, Disaster Recovery Center
│   - All information assets, personnel, processes, and technology
│   - All 4 Annex A themes:
│     - A.5 Organizational Controls (37 controls)
│     - A.6 People Controls (8 controls)
│     - A.7 Physical Controls (14 controls)
│     - A.8 Technological Controls (34 controls)
│
├── 5. Assessment Framework
│   - Standard: ISO/IEC 27001:2022
│   - Control Set: 93 Annex A controls (4 themes)
│   - Rating Scale per control:
│     - Fully Implemented
│     - Partially Implemented
│     - Not Implemented
│     - Not Applicable
│   - Reference: Statement of Applicability (SoA)
│
├── 6. Methodology
│   ├── Phase 1 — Preparation (Week 1)
│   │   - Form internal assessment team
│   │   - Review Statement of Applicability (SoA)
│   │   - Develop assessment checklist for all 93 controls
│   │
│   ├── Phase 2 — Documentation Review (Week 2–3)
│   │   - Review policies, procedures, records, evidence
│   │   - Verify documented controls against SoA
│   │
│   ├── Phase 3 — Assessment Execution (Week 3–5)
│   │   - Interviews with process owners and key personnel
│   │   - Technical verification: system configs, access logs, vulnerability reports
│   │   - Rate each control: Fully / Partially / Not Implemented / Not Applicable
│   │   - Document gaps identified per control
│   │
│   ├── Phase 4 — Analysis (Week 5–6)
│   │   - Compile assessment results per theme
│   │   - Calculate implementation percentages
│   │   - Risk assessment for identified gaps
│   │
│   └── Phase 5 — Reporting (Week 6–7)
│       - Self-assessment report with per-theme tables
│       - Gap analysis with risk ratings
│       - Improvement roadmap with priorities
│
├── 7. Deliverables (Table: #, Deliverable, Description)
│   1. Self-Assessment Report — Status of all 93 controls across 4 themes
│   2. Gap Analysis Report — Gaps identified with risk ratings
│   3. Risk Summary — Count of HIGH/MEDIUM/LOW risks
│   4. Implementation Status Dashboard — Theme-wise summary
│      (Total, Fully Implemented, Partially, Not Implemented, N/A)
│   5. Improvement Roadmap — Prioritized recommendations
│   6. Executive Summary — High-level summary for management
│
├── 8. Assessment Team
│   - Assessment Lead (internal ISMS Manager or designated officer)
│   - IT Security representative
│   - Operations/Business representative
│   - HR representative (for People controls)
│   - Facilities representative (for Physical controls)
│   - (Optional) External consultant for guidance
│
├── 9. Timeline (Table: Phase, Activity, Duration)
│   Phase 1: Preparation                — Week 1
│   Phase 2: Documentation Review       — Week 2–3
│   Phase 3: Assessment Execution       — Week 3–5
│   Phase 4: Analysis                   — Week 5–6
│   Phase 5: Reporting                  — Week 6–7
│   Total Duration: 7 Weeks
│
└── 10. Key Difference from External IS Audit
    - Self-assessment is INTERNAL — conducted by the organization itself
    - Covers ALL 93 controls (not a selection of 5–10)
    - Uses 4-level status rating (not observation-based)
    - References the Statement of Applicability (SoA)
    - Purpose is readiness evaluation, not certification
```

---

## 3. Proposal for Cybersecurity Maturity Assessment (NIST CSF)

> **Question Pattern:** "Prepare a comprehensive proposal for conducting a Cybersecurity Maturity Assessment aligned with NIST CSF for <<Organization>> with <<N>> locations."
> **Syllabus Reference:** Unit 1 (NIST CSF), Workshop #2
> **Framework:** NIST CSF v1.1 (5 functions) or v2.0 (6 functions) — determine from question

### Determine Version from Question

| If question says...                 | Use                                                                                      |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| NIST CSF v1.1 / five core functions | **NIST CSF v1.1** — 5 functions: Identify, Protect, Detect, Respond, Recover             |
| NIST CSF v2.0 / six core functions  | **NIST CSF v2.0** — 6 functions: **Govern**, Identify, Protect, Detect, Respond, Recover |
| Just "NIST CSF" (unspecified)       | Default to v1.1 unless "six functions" mentioned                                         |

### Proposal Structure

```
Proposal for Cybersecurity Maturity Assessment
│
├── 1. Cover Page
│   - Title, Submitted To/By, Date, Framework Version
│
├── 2. Introduction
│   - <<Organization>> operates <<N>> locations with DC and DRC
│   - Cybersecurity maturity assessment evaluates security posture against NIST CSF
│   - Maps current practices to <<5 or 6>> core functions
│   - Uses Implementation Tiers (Tier 1–4) to measure maturity
│   (If v2.0: mention Govern as new sixth function for governance integration)
│
├── 3. Objectives
│   - Evaluate cybersecurity maturity across all <<5 or 6>> core functions
│   - Determine current Implementation Tier per function
│   - Identify gaps between current state and target maturity
│   - Provide improvement roadmap to achieve target maturity
│   - Support alignment with industry best practices and regulations
│
├── 4. Scope
│   - All <<N>> locations, DC, DRC
│   - All core functions of NIST CSF:
│     (v2.0) Govern, Identify, Protect, Detect, Respond, Recover
│     (v1.1) Identify, Protect, Detect, Respond, Recover
│   - All associated categories and subcategories
│   - IT infrastructure, personnel, processes, and governance
│
├── 5. Assessment Framework
│   - Framework: NIST CSF Version <<1.1 or 2.0>>
│   - Core Functions: <<5 or 6>>
│   - Implementation Tiers (Table):
│     Tier 1 — Partial: Ad-hoc, reactive, not formalized
│     Tier 2 — Risk Informed: Approved by management, not org-wide
│     Tier 3 — Repeatable: Formally approved, implemented org-wide
│     Tier 4 — Adaptive: Continuously improved, predictive indicators
│   - Subcategory Selection: At least 5 subcategories covering all functions
│
├── 6. Subcategory Selection Plan
│   Table: Function, Category, Subcategory ID, Description
│
│   NIST CSF v1.1 (5 functions):
│   - ID.AM-1 (Asset inventory), ID.RA-1 (Vulnerability identification)
│   - PR.AC-1 (Identity/credentials), PR.AT-1 (Training)
│   - DE.CM-1 (Network monitoring)
│   - RS.RP-1 (Response plan)
│   - RC.RP-1 (Recovery plan)
│
│   NIST CSF v2.0 (6 functions):
│   - GV.RR-01 (Roles/responsibilities), GV.PO-01 (Policy)
│   - ID.AM-01 (Asset inventory), ID.RA-01 (Vulnerability identification)
│   - PR.AA-01 (Identity/credentials), PR.AT-01 (Training)
│   - DE.CM-01 (Network monitoring)
│   - RS.MA-01 (Incident management)
│   - RC.RP-01 (Recovery plan)
│
├── 7. Methodology
│   ├── Phase 1 — Planning (Week 1)
│   │   - Kick-off meeting, define scope boundaries
│   │   - Select subcategories for evaluation
│   │   - Develop assessment questionnaire
│   │
│   ├── Phase 2 — Data Collection (Week 2–3)
│   │   - Documentation review: policies, procedures, architecture diagrams
│   │   - Interviews with process owners, IT staff, management
│   │   - Technical review: system configs, monitoring tools, logs
│   │   - Site visits: DC, DRC, sample locations
│   │
│   ├── Phase 3 — Assessment (Week 3–4)
│   │   - Rate each subcategory against Implementation Tiers
│   │   - Identify gaps per subcategory
│   │   - Determine current vs. target maturity per function
│   │
│   ├── Phase 4 — Analysis (Week 4–5)
│   │   - Compile function-level maturity scores
│   │   - Overall organizational maturity determination
│   │   - Gap analysis and prioritization
│   │
│   └── Phase 5 — Reporting (Week 5–6)
│       - Draft report with maturity assessment results
│       - Improvement roadmap with phased priorities
│       - Final report after management review
│
├── 8. Per-Subcategory Reporting Format
│   For each subcategory assessed:
│   - Category and Subcategory Reference
│   - Description
│   - Current Tier (1–4)
│   - Gap Identified
│   - Target Tier
│   - Recommendation
│   After each function: "Function Maturity: Tier X (Name)"
│
├── 9. Deliverables (Table: #, Deliverable, Description)
│   1. Cybersecurity Maturity Assessment Report
│   2. Per-Function Maturity Scorecards
│   3. Gap Analysis Report
│   4. Improvement Roadmap (phased: Immediate, Short-Term, Medium-Term)
│   5. Executive Summary
│
├── 10. Team Composition
│   - Lead Assessor (CISA/CISM, NIST CSF expertise, 5+ years)
│   - Technical Assessor (network/infrastructure/security tools expertise)
│   - GRC Assessor (governance, risk, compliance)
│
├── 11. Timeline (Table: Phase, Activity, Duration)
│   Phase 1: Planning              — Week 1
│   Phase 2: Data Collection       — Week 2–3
│   Phase 3: Assessment            — Week 3–4
│   Phase 4: Analysis              — Week 4–5
│   Phase 5: Reporting             — Week 5–6
│   Total Duration: 6 Weeks
│
└── 12. Confidentiality
    - NDA before engagement
    - All findings confidential
    - Report shared with authorized stakeholders only
```

---

## 4. Proposal for Building Terms of Reference (ToR) for an IS Audit

> **Question Pattern:** "Develop a comprehensive ToR for IS Audit for <<Organization>> with <<N>> sites, aligned with NIST, ISO 27001:2022, and CIS."
> **Syllabus Reference:** Unit 4 (Audit Program/Plan), Workshop #3
> **Standards:** ISO/IEC 27001:2022, NIST CSF, CIS Critical Security Controls

### Note

> The ToR itself IS the proposal/pre-engagement document. Outline #4 in outlines1.md already covers the ToR structure comprehensively. The "proposal" for a ToR is essentially the ToR itself. Below is how to frame it as a proposal response.

### Proposal Structure

```
Proposal: Terms of Reference (ToR) for Information Systems Audit
│
├── 1. Cover Page
│   - Title: Proposal for Development of Terms of Reference for IS Audit
│   - Submitted To: <<Organization>>
│   - Submitted By: <<Audit Firm>>
│   - Date
│
├── 2. Introduction
│   - <<Organization>> operates <<N>> sites with DC and DRC
│   - Organization requires IS Audit to evaluate security posture
│   - ToR defines purpose, scope, authority, and methodology for the IS Audit
│   - Mandated alignment with NIST, ISO 27001:2022, CIS Controls
│
├── 3. Audit Objectives
│   - Evaluate ISMS effectiveness against ISO 27001:2022 (93 Annex A controls)
│   - Assess cybersecurity maturity against NIST CSF (5 functions)
│   - Evaluate technical controls against CIS Critical Security Controls v8 (18 controls)
│   - Identify vulnerabilities, risks, and gaps
│   - Assess regulatory compliance
│   - Provide actionable recommendations
│
├── 4. Scope of Work
│   ├── 4.1 Infrastructure Scope
│   │   - All sites, DC, DRC, network infrastructure, end-user devices
│   │
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
│   - Applicable regulations (ETA 2008, Privacy Act 2018, sector-specific)
│   - Organizational IT Policies
│
├── 6. Methodology
│   - Phase 1 — Planning (define objectives, scope, audit plan)
│   - Phase 2 — Information Gathering (documentation, interviews, evidence)
│   - Phase 3 — Assessment and Testing (compliance, maturity, technical testing)
│   - Phase 4 — Analysis (gap analysis, risk assessment; Major NC, Minor NC, OFI)
│   - Phase 5 — Reporting (draft → management response → final report with CAP)
│
├── 7. Deliverables (Table: #, Deliverable, Description)
│   1. Audit Plan
│   2. IS Audit Report
│   3. Gap Analysis Report
│   4. Risk Assessment Report
│   5. Executive Summary
│   6. Corrective Action Plan (CAP)
│
├── 8. Audit Team Composition and Qualifications
│   - Lead Auditor (ISO 27001 LA, CISA certified)
│   - Technical Auditor (network/VAPT expertise)
│   - Compliance Auditor (regulatory/governance knowledge)
│   - Independence requirement (no conflict of interest)
│
├── 9. Timeline and Schedule (Table: Phase, Activity, Duration)
│   Phase 1: Planning             — Week 1
│   Phase 2: Info Gathering       — Week 2–3
│   Phase 3: On-site Assessment   — Week 4–5
│   Phase 4: Analysis/Draft       — Week 6
│   Phase 5: Final Report         — Week 7–8
│   Total Duration: 8 Weeks
│
├── 10. Authority and Access
│   - Unrestricted access to all systems, documentation, facilities, personnel
│
├── 11. Confidentiality
│   - All findings confidential; NDA required
│
└── 12. Reporting and Communication
    - Weekly progress updates
    - Draft report within 5 business days of fieldwork completion
    - Management response within 10 business days
    - Final report within 20 business days
```

---

## 5. Proposal for Cybersecurity Assessment (NIST CSF)

> **Question Pattern:** "Prepare a proposal for Cybersecurity Assessment for <<Organization>> using NIST CSF."
> **Syllabus Reference:** Unit 1 (NIST CSF), Workshop #2
> **Note:** A "Cybersecurity Assessment" is similar to a "Cybersecurity Maturity Assessment" but may be broader — covering compliance evaluation in addition to maturity. When the question says just "Cybersecurity Assessment" without specifying maturity, include both compliance checking and maturity rating.

### Proposal Structure

```
Proposal for Cybersecurity Assessment
│
├── 1. Cover Page
│   - Title: Proposal for Cybersecurity Assessment
│   - Framework: NIST CSF Version <<1.1 or 2.0>>
│   - Submitted To/By, Date
│
├── 2. Introduction
│   - <<Organization>> with <<N>> locations, DC and DRC
│   - Cybersecurity assessment evaluates organization's cybersecurity posture
│   - Aligned with NIST Cybersecurity Framework
│   - Covers <<5 or 6>> core functions with Implementation Tiers (Tier 1–4)
│   - Identifies current state, gaps, and improvement opportunities
│
├── 3. Objectives
│   - Comprehensively assess cybersecurity posture against NIST CSF
│   - Evaluate current practices across all core functions
│   - Determine Implementation Tier per function and overall
│   - Identify cybersecurity risks, vulnerabilities, and gaps
│   - Assess alignment with applicable regulations
│   - Develop improvement roadmap
│
├── 4. Scope
│   - All <<N>> locations, DC, DRC
│   - All NIST CSF core functions:
│     (v1.1) Identify, Protect, Detect, Respond, Recover
│     (v2.0) Govern, Identify, Protect, Detect, Respond, Recover
│   - IT infrastructure, OT systems (if applicable), cloud services
│   - Governance structures, policies, incident response capabilities
│
├── 5. Assessment Framework
│   ├── NIST CSF Version <<1.1 or 2.0>>
│   ├── Implementation Tiers (Tier 1–4) — same table as Outline #3
│   └── Core Functions and Categories:
│       (v2.0 only) GOVERN: GV.OC, GV.RM, GV.RR, GV.PO, GV.SC
│       IDENTIFY: ID.AM, ID.BE, ID.GV (v1.1), ID.RA, ID.RM, ID.SC (v1.1)
│       PROTECT: PR.AC/PR.AA, PR.AT, PR.DS, PR.IP, PR.PT
│       DETECT: DE.AE, DE.CM, DE.DP
│       RESPOND: RS.RP, RS.CO, RS.AN, RS.MI, RS.IM
│       RECOVER: RC.RP, RC.IM, RC.CO
│
├── 6. Methodology
│   ├── Phase 1 — Planning and Scoping (Week 1)
│   │   - Discovery meeting, define scope boundaries
│   │   - NDA execution, access arrangements
│   │   - Select subcategories for evaluation (minimum 5, covering all functions)
│   │
│   ├── Phase 2 — Information Gathering (Week 2–3)
│   │   - Documentation review: policies, procedures, network diagrams, asset registers
│   │   - Interviews with CISO, IT team, operations, management
│   │   - Technical review: configurations, monitoring tools, access controls
│   │   - Site visits: DC, DRC, sample locations
│   │
│   ├── Phase 3 — Assessment and Evaluation (Week 3–4)
│   │   - Rate each subcategory against Implementation Tiers
│   │   - Identify gaps and vulnerabilities per function
│   │   - Compliance check against regulations
│   │
│   ├── Phase 4 — Analysis (Week 4–5)
│   │   - Function-level and overall maturity determination
│   │   - Gap analysis, risk prioritization
│   │
│   └── Phase 5 — Reporting and Presentation (Week 5–6)
│       - Draft assessment report
│       - Presentation to management
│       - Final report with improvement roadmap
│
├── 7. Deliverables
│   1. Cybersecurity Assessment Report (per-function maturity)
│   2. Gap Analysis Report
│   3. Risk Assessment Summary
│   4. Improvement Roadmap (Phase 1: 0–3 months, Phase 2: 3–6 months, Phase 3: 6–12 months)
│   5. Executive Summary
│
├── 8. Team Composition
│   - Lead Assessor (CISA/CISM, NIST CSF expertise)
│   - Technical Assessor (network, infrastructure, security tools)
│   - GRC Assessor (governance, risk, compliance)
│
├── 9. Timeline (Table: Phase, Activity, Duration)
│   Total Duration: 6 Weeks
│
└── 10. Confidentiality
    - NDA, authorized stakeholders only
```

---

## 6. Proposal for Ransomware Readiness Assessment (CISA CSET RRA)

> **Question Pattern:** "As an expert, outline your approach to conducting a Ransomware Readiness Assessment for a company that has issued an RFP. Prepare a comprehensive proposal."
> **Syllabus Reference:** Unit 1 (Frameworks), Unit 5 (BCP/DRP)
> **Tool:** CISA CSET — RRA Module
> **Note:** Outline #7 in outlines1.md already has this proposal structure. Below is the complete expanded version.

### Proposal Structure

```
Proposal for Ransomware Readiness Assessment
│
├── 1. Cover Page
│   - Title: Proposal for Ransomware Readiness Assessment
│   - Tool: CISA Cyber Security Evaluation Tool (CSET) — RRA Module
│   - Submitted To/By, Date
│
├── 2. Introduction
│   - Ransomware is among the most significant cybersecurity threats
│   - This proposal outlines approach for RRA using CISA CSET RRA module
│   - Evaluates organization across 10 assessment domains at 3 maturity tiers
│   - Identifies weaknesses and provides prioritized remediation roadmap
│
├── 3. Objectives
│   - Evaluate ransomware preparedness using CISA RRA framework
│   - Identify gaps across all 10 assessment domains
│   - Determine maturity level (Basic / Intermediate / Advanced) per domain
│   - Identify major weaknesses in information systems and processing facilities
│   - Provide prioritized remediation roadmap
│
├── 4. Scope
│   - All <<N>> sites, DC, DRC
│   - Critical systems, network infrastructure, endpoints, cloud services
│   - Policies, procedures, incident response capabilities
│   - Backup and recovery infrastructure
│
├── 5. Assessment Framework
│   - Tool: CISA CSET — Ransomware Readiness Assessment (RRA) Module
│   - 10 Assessment Domains (Table: #, Domain, Code, Focus Area):
│     1.  Asset Management (AM) — Critical asset inventory and management
│     2.  Robust Data Backup (DB) — Backup strategy and resilience
│     3.  Phishing Prevention and Awareness (PP) — Email security and training
│     4.  User and Access Management (UM) — Identity, MFA, least privilege
│     5.  Network Perimeter Monitoring (NM) — Network defense and monitoring
│     6.  Web Browser Mgmt and DNS Filtering (BM) — Browser and DNS controls
│     7.  Application Integrity and Allowlisting (AI) — Application control
│     8.  Incident Response (IR) — Ransomware-specific IRP
│     9.  Risk Management (RM) — Ransomware in risk framework
│     10. Vulnerability Management (VM) — Scanning and patching
│   - Maturity Tiers:
│     Basic — Foundational practices in place
│     Intermediate — Documented, tested, regularly maintained
│     Advanced — Automated, continuously improved, proactive
│   - Question Naming Convention: Goal [GG] : Level [B,I,A] . Question [Q##]
│
├── 6. Methodology
│   ├── Phase 1 — Pre-Engagement and Scoping (Week 1)
│   │   - Discovery meeting with management
│   │   - NDA execution
│   │   - Define scope boundaries and key contacts
│   │   - Request preliminary documentation (policies, network diagrams, backup procedures)
│   │
│   ├── Phase 2 — Assessment and Evaluation (Week 2–3)
│   │   - Install and configure CISA CSET, select RRA module
│   │   - Conduct structured assessment against 10 domains × 3 tiers
│   │   - Evidence review: backup logs, access control configs, IRP documents
│   │   - Interviews with IT, security, operations personnel
│   │   - Review CSET-generated dashboards and reports
│   │
│   ├── Phase 3 — Validation and Testing (Week 3–4)
│   │   - Vulnerability scanning of critical systems
│   │   - Tabletop exercise (ransomware scenario simulation)
│   │   - Backup restoration test (verify recoverability)
│   │   - Verify network segmentation and lateral movement resistance
│   │
│   ├── Phase 4 — Analysis and Reporting (Week 4–5)
│   │   - Compile CSET results per domain and tier
│   │   - Gap analysis and weakness identification
│   │   - Risk prioritization
│   │   - Develop remediation roadmap
│   │
│   └── Phase 5 — Reporting and Presentation (Week 5–6)
│       - Draft report
│       - Presentation to management
│       - Final report with agreed remediation plan
│
├── 7. Per-Domain Reporting Format
│   For each of the 10 domains:
│   Table: Level (Basic/Intermediate/Advanced),
│          Question Area, Finding, Maturity (Met/Partial/Not Met)
│   + "Weakness:" summary after each domain
│
├── 8. Deliverables (Table: #, Deliverable, Description)
│   1. RRA Maturity Assessment Report — Per-domain maturity with gaps
│   2. Gap Analysis Report — Detailed gaps per domain and tier
│   3. Vulnerability Scan Report — Technical vulnerabilities identified
│   4. Tabletop Exercise Report — Results of ransomware scenario simulation
│   5. Executive Summary — High-level findings for management/Board
│   6. Remediation Roadmap — Prioritized actions (Immediate/Short/Medium-term)
│
├── 9. Team Composition
│   - Lead Assessor (CISA/CISM certified, ransomware IR experience)
│   - Technical Assessor (network/endpoint security, VAPT expertise)
│   - GRC Assessor (risk, policy, compliance)
│
├── 10. Timeline (Table: Phase, Activity, Duration)
│    Phase 1: Pre-Engagement and Scoping    — Week 1
│    Phase 2: Assessment and Evaluation      — Week 2–3
│    Phase 3: Validation and Testing         — Week 3–4
│    Phase 4: Analysis and Reporting         — Week 4–5
│    Phase 5: Reporting and Presentation     — Week 5–6
│    Total Duration: 6 Weeks
│
└── 11. Confidentiality
    - NDA before engagement commencement
    - All findings shared with authorized stakeholders only
    - Encrypted transmission of all reports and data
```

### Common Weaknesses to Expect (Reusable for any organization)

| #   | Weakness                                                   | Domain |
| --- | ---------------------------------------------------------- | ------ |
| 1   | No air-gapped/offline/immutable backups                    | DB     |
| 2   | No MFA or Privileged Access Management (PAM)               | UM     |
| 3   | No ransomware-specific incident response plan              | IR     |
| 4   | No application allowlisting                                | AI     |
| 5   | No network segmentation (flat network)                     | NM     |
| 6   | No regular vulnerability scanning or patch management SLAs | VM     |
| 7   | No phishing awareness training or simulations              | PP     |
| 8   | Ransomware not included in risk register                   | RM     |
| 9   | No DNS filtering or browser isolation                      | BM     |
| 10  | No automated asset discovery or dependency mapping         | AM     |

---

## 7. Proposal for VAPT Engagement

> **Question Pattern:** "Develop a detailed ToR/proposal for conducting VAPT for <<Organization>> with <<N>> sites, DC and DRC."
> **Syllabus Reference:** Unit 6 (VAPT, OWASP, Security Testing)
> **Standards:** OWASP Testing Guide, PTES, NIST SP 800-115, CVSS

### Proposal Structure

```
Proposal for Vulnerability Assessment and Penetration Testing (VAPT)
│
├── 1. Cover Page
│   - Title, Submitted To/By, Date
│
├── 2. Introduction
│   - <<Organization>> operates <<N>> sites with DC and DRC
│   - VAPT identifies known/unknown vulnerabilities and assesses exploitability
│   - Evaluates effectiveness of existing security controls
│   - Aligned with OWASP, PTES, NIST SP 800-115
│
├── 3. Objectives
│   - Identify known and unknown vulnerabilities across infrastructure
│   - Assess exploitability through controlled penetration testing
│   - Evaluate DC/DRC security posture
│   - Assess effectiveness of existing security controls
│   - Provide prioritized remediation plan using CVSS scoring
│   - Support compliance with ISO 27001:2022 A.8.8 (Technical Vulnerabilities)
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
│   │
│   └── 4.2 Out-of-Scope
│       - Third-party services not under organization's control
│       - Social engineering (unless explicitly requested)
│       - Physical security testing
│
├── 5. Methodology (OWASP, PTES, NIST SP 800-115, CVSS)
│   ├── Phase 1: Planning and Scoping (Week 1)
│   │   - Define scope, objectives, RoE, testing windows
│   │   - Obtain written authorization
│   │
│   ├── Phase 2: Reconnaissance and Information Gathering (Week 1–2)
│   │   - Passive reconnaissance (OSINT, DNS enumeration)
│   │   - Active reconnaissance (network scanning, service enumeration)
│   │
│   ├── Phase 3: Vulnerability Assessment (Week 2–3)
│   │   - Automated scanning (Nessus, Qualys, OpenVAS)
│   │   - Manual verification of findings
│   │   - Web application testing per OWASP Testing Guide
│   │
│   ├── Phase 4: Penetration Testing (Week 3–4)
│   │   - Manual exploitation of confirmed vulnerabilities
│   │   - Lateral movement assessment
│   │   - Privilege escalation testing
│   │   - Data access validation
│   │
│   ├── Phase 5: Reporting (Week 4–5)
│   │   - CVSS v3.1 scoring for each vulnerability
│   │   - Proof of Concept (PoC) evidence
│   │   - Prioritized remediation guidance
│   │
│   └── Phase 6: Retest (Optional — Week 6+)
│       - Verify remediation of critical/high findings
│       - Issue retest report
│
├── 6. Rules of Engagement (RoE)
│   - Testing only within authorized scope and windows
│   - No Denial of Service on production unless authorized
│   - Critical vulnerabilities reported immediately (within 24 hours)
│   - No data modification or exfiltration of real data
│   - All activities logged and timestamped
│   - Emergency contact for testing issues
│
├── 7. Deliverables (Table: #, Deliverable, Description)
│   1. Executive Summary — High-level overview for management
│   2. Detailed VAPT Report — Full technical findings
│   3. Vulnerability Assessment Report — All identified vulnerabilities with CVSS scores
│   4. Penetration Testing Report — Exploitation results with PoC
│   5. Remediation Guidance — Prioritized fix recommendations
│   6. Retest Report (if applicable)
│   7. Raw Data/Logs — Scan outputs and testing logs
│
├── 8. Team Qualifications
│   - Lead Pentester (CEH/OSCP/GPEN, 5+ years penetration testing)
│   - Web Application Tester (OSCP/GWAPT, OWASP expertise)
│   - Network Security Tester (infrastructure, wireless expertise)
│   - All team members sign NDA and conflict of interest declarations
│
├── 9. Timeline (Table: Phase, Activity, Duration)
│   Phase 1: Planning and Scoping           — Week 1
│   Phase 2: Reconnaissance                 — Week 1–2
│   Phase 3: Vulnerability Assessment       — Week 2–3
│   Phase 4: Penetration Testing            — Week 3–4
│   Phase 5: Reporting                      — Week 4–5
│   Phase 6: Retest (Optional)              — Week 6+
│   Total Duration: 5–6 Weeks
│
├── 10. Authority and Access
│   - Written authorization before any testing
│   - Access credentials for authenticated testing
│   - Network access to in-scope systems
│
├── 11. Confidentiality
│   - NDA executed before engagement
│   - Encrypted transmission of reports
│   - All test data securely destroyed after engagement
│
└── 12. Reporting and Communication
    - Daily status during active testing
    - Critical findings reported immediately (within 24 hours)
    - Draft report within 5 business days of testing completion
    - Final report within 15 business days
```

---

## Quick Reference: Proposal vs. Report/Assessment

| Element               | Proposal (Pre-Engagement)        | Report/Assessment (Post-Engagement) |
| --------------------- | -------------------------------- | ----------------------------------- |
| Cover Page            | ✅ Always include                | ✅ Always include                   |
| Introduction          | How we will approach the work    | What we did and why                 |
| Objectives            | What we plan to achieve          | What we set out to evaluate         |
| Scope                 | What we will cover               | What we covered                     |
| Methodology           | Phases we will follow            | Phases we followed                  |
| Observations/Findings | ❌ Not included                  | ✅ Detailed per-control/subcategory |
| Risk Ratings          | ❌ Not included                  | ✅ Per finding                      |
| Recommendations       | ❌ Not included (only in report) | ✅ Prioritized per finding          |
| Team Composition      | ✅ With qualifications           | Optional / in appendix              |
| Timeline              | ✅ Detailed schedule             | Actual dates in report header       |
| Deliverables          | ✅ List of promised outputs      | ✅ The actual outputs               |
| Confidentiality       | ✅ Always include                | ✅ Always include                   |
| Authority & Access    | ✅ What we need from the client  | N/A (already provided)              |

---
