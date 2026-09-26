# ISA Exam Answers

---

## 1. Tasks and Knowledge Areas of a Professional IS Auditor

> **Q.** Explain the essential responsibilities and knowledge areas required to become a professional Information System Auditor. Identify and elaborate on the critical tasks that an Information System Auditor must perform and the key knowledge domains they must acquire to effectively audit, assess, and ensure the integrity, confidentiality, and availability of information systems.

To become a professional IS Auditor, one must possess comprehensive understanding of the tasks to perform and knowledge domains to master, as defined by ISACA's CISA framework which structures the profession into five domains.

### 1.1 Critical Tasks of an IS Auditor

**Task 1: IS Audit Planning**
- Define audit objectives, scope, and criteria based on standards (ISO 27001:2022, COBIT 2019, NIST CSF).
- Develop the audit plan and audit program with resource allocation and timelines.
- Conduct preliminary risk assessment to prioritize audit areas.
- Identify key stakeholders and establish communication channels.

**Task 2: Executing the Audit**
- Gather audit evidence through documentation review, interviews, observation, and technical verification.
- Perform compliance testing (verify controls exist and are followed) and substantive testing (verify data accuracy and completeness).
- Use CAATs (Computer Assisted Audit Techniques), sampling techniques, and audit questionnaires.
- Evaluate IT general controls and application controls.

**Task 3: Assessing IT Governance and Management**
- Evaluate IT governance structures using COBIT 2019 framework.
- Assess alignment of IT strategy with business objectives.
- Review IT policies, procedures, and organizational structure.
- Evaluate IT resource management and performance monitoring.

**Task 4: Evaluating Information Systems and Controls**
- Assess logical and physical access controls.
- Evaluate network security, system configurations, and vulnerability management.
- Review change management, problem management, and incident management processes.
- Assess BCP/DRP effectiveness and test results.
- Evaluate data backup and recovery procedures.

**Task 5: Reporting and Follow-Up**
- Document audit findings with evidence, risk ratings, and recommendations.
- Classify findings as Major Non-Conformity, Minor Non-Conformity, or Opportunity for Improvement (OFI).
- Present findings to management and stakeholders.
- Track corrective action plans and verify implementation in follow-up audits.

### 1.2 Key Knowledge Domains (CISA Five Domains)

**Domain 1: Information Systems Auditing Process**
- ISACA IS Audit Standards, Guidelines, and Code of Professional Ethics.
- Audit methodologies — risk-based auditing, compliance auditing, substantive testing.
- Knowledge of ISO 27001, NIST CSF, COBIT 2019, CIS Controls.
- Evidence collection, evaluation, and documentation standards.

**Domain 2: Governance and Management of IT**
- IT governance frameworks (COBIT 2019 — EDM, APO, BAI, DSS, MEA domains).
- IT strategy, policies, and organizational structures.
- IT risk management processes and risk assessment methodologies.
- Regulatory requirements (Electronic Transactions Act 2008, Individual Privacy Act 2018).

**Domain 3: Information Systems Acquisition, Development and Implementation**
- SDLC and Secure SDLC (SecSDLC) processes.
- Change management and configuration management.
- Project management practices for IT projects.
- Application controls and testing methodologies.

**Domain 4: Information Systems Operations and Business Resilience**
- IT service management (incident, problem, change management).
- BCP, DRP, and Business Impact Analysis (BIA).
- Backup and recovery strategies — RTO, RPO.
- Data center operations, environmental controls, and cloud computing.

**Domain 5: Protection of Information Assets**
- Access control models, authentication mechanisms, encryption.
- Network security — firewalls, IDS/IPS, VPN, segmentation.
- Vulnerability assessment and penetration testing (VAPT).
- Security monitoring, logging, and SIEM.
- Data classification, data privacy, and data protection principles.

---

## 2. Cybersecurity Maturity Assessment — NIST CSF 2.0

> **Q.** Conduct a cybersecurity maturity assessment for a multinational company that operates its own data center and a cloud-based disaster recovery center, using the NIST Cybersecurity Framework as a guiding reference. Select at least five relevant subcategories, ensuring that all six core functions of the framework are covered.

### <<Organization>> Cybersecurity Assessment

### NIST Cybersecurity Framework Version 2.0

### Cybersecurity Maturity Assessment Report

**Organization:** A multinational company with own Data Center (DC) and cloud-based Disaster Recovery Center (DRC)
**Framework:** NIST Cybersecurity Framework (CSF) Version 2.0
**Assessment Scope:** All 6 core functions — Govern, Identify, Protect, Detect, Respond, Recover

### 1. Introduction

This Cybersecurity Maturity Assessment evaluates the organization's cybersecurity posture against the NIST Cybersecurity Framework v2.0. The CSF 2.0 introduced a sixth function — **Govern** — to integrate cybersecurity governance into enterprise risk management. The assessment evaluates selected subcategories across all six functions using NIST Implementation Tiers.

### 2. NIST CSF 2.0 Implementation Tiers (Maturity Levels)

| Tier   | Name          | Description                                                                            |
| ------ | ------------- | -------------------------------------------------------------------------------------- |
| Tier 1 | Partial       | Risk management is ad-hoc and reactive; not formalized                                 |
| Tier 2 | Risk Informed | Risk management approved by management but not organization-wide                       |
| Tier 3 | Repeatable    | Policies and procedures formally approved and implemented organization-wide            |
| Tier 4 | Adaptive      | Practices are continuously improved based on lessons learned and predictive indicators |

### 3. Assessment by Core Function

#### Function 1: GOVERN (GV)

| Category | Subcategory | Description | Current Tier | Gap | Target Tier |
| --- | --- | --- | --- | --- | --- |
| Organizational Context (GV.OC) | GV.OC-01 | The organizational mission is understood and informs cybersecurity risk management | Tier 2 | Mission documented but cybersecurity not formally linked to business objectives | Tier 3 |
| Risk Management Strategy (GV.RM) | GV.RM-01 | Risk management objectives are established and used to support operational decisions | Tier 2 | Risk register exists at HQ but not extended to all locations or cloud DRC | Tier 3 |
| Roles, Responsibilities, and Authorities (GV.RR) | GV.RR-01 | Organizational leadership establishes and communicates cybersecurity roles and responsibilities | Tier 1 | No dedicated CISO; IT Manager handles security ad-hoc; no roles defined for DRC | Tier 3 |
| Policy (GV.PO) | GV.PO-01 | Cybersecurity policy based on organizational context and strategy is established | Tier 2 | Information Security Policy exists but outdated; no topic-specific policies | Tier 3 |
| Cybersecurity Supply Chain Risk Management (GV.SC) | GV.SC-01 | A cybersecurity supply chain risk management program is established | Tier 1 | No supply chain risk management; DRC cloud provider not formally assessed | Tier 3 |

**Function Maturity: Tier 1–2 (Partial to Risk Informed)**

#### Function 2: IDENTIFY (ID)

| Category | Subcategory | Description | Current Tier | Gap | Target Tier |
| --- | --- | --- | --- | --- | --- |
| Asset Management (ID.AM) | ID.AM-01 | Inventories of hardware managed by the organization are maintained | Tier 2 | Asset inventory exists for DC but not comprehensive; cloud DRC assets not tracked | Tier 3 |
| Risk Assessment (ID.RA) | ID.RA-01 | Vulnerabilities in assets are identified, validated, and recorded | Tier 1 | No formal vulnerability scanning or assessment program | Tier 3 |

**Function Maturity: Tier 1–2 (Partial to Risk Informed)**

#### Function 3: PROTECT (PR)

| Category | Subcategory | Description | Current Tier | Gap | Target Tier |
| --- | --- | --- | --- | --- | --- |
| Identity Management, Authentication, and Access Control (PR.AA) | PR.AA-01 | Identities and credentials for authorized users, services, and hardware are managed | Tier 2 | User lifecycle management inconsistent; no MFA; shared admin credentials | Tier 3 |
| Awareness and Training (PR.AT) | PR.AT-01 | Personnel are provided cybersecurity awareness and training | Tier 1 | No structured cybersecurity training; no training records | Tier 3 |
| Data Security (PR.DS) | PR.DS-01 | The confidentiality, integrity, and availability of data-at-rest are protected | Tier 1 | No encryption at rest; backups unencrypted; cloud DRC data not encrypted | Tier 3 |
| Platform Security (PR.PS) | PR.PS-01 | The hardware, software, and services of physical and virtual platforms are managed | Tier 2 | Patch management ad-hoc; no configuration baselines | Tier 3 |

**Function Maturity: Tier 1–2 (Partial to Risk Informed)**

#### Function 4: DETECT (DE)

| Category | Subcategory | Description | Current Tier | Gap | Target Tier |
| --- | --- | --- | --- | --- | --- |
| Continuous Monitoring (DE.CM) | DE.CM-01 | Networks and network services are monitored to find potentially adverse events | Tier 1 | No IDS/IPS; no SIEM; no real-time network monitoring | Tier 3 |
| Adverse Event Analysis (DE.AE) | DE.AE-02 | Potentially adverse events are analyzed to better understand associated activities | Tier 1 | Logs only reviewed reactively; no correlation or anomaly detection | Tier 3 |

**Function Maturity: Tier 1 (Partial)**

#### Function 5: RESPOND (RS)

| Category | Subcategory | Description | Current Tier | Gap | Target Tier |
| --- | --- | --- | --- | --- | --- |
| Incident Management (RS.MA) | RS.MA-01 | The incident response plan is executed in coordination with relevant third parties | Tier 1 | No formal incident response plan; ad-hoc response; no escalation matrix | Tier 3 |
| Incident Analysis (RS.AN) | RS.AN-03 | Analysis is performed to determine what has taken place during an incident | Tier 1 | No forensic analysis capability; no evidence collection procedures | Tier 3 |

**Function Maturity: Tier 1 (Partial)**

#### Function 6: RECOVER (RC)

| Category | Subcategory | Description | Current Tier | Gap | Target Tier |
| --- | --- | --- | --- | --- | --- |
| Incident Recovery Plan Execution (RC.RP) | RC.RP-01 | The recovery portion of the incident response plan is executed | Tier 2 | Cloud DRC exists but failover not tested; RTO/RPO not defined | Tier 3 |
| Incident Recovery Communication (RC.CO) | RC.CO-03 | Recovery activities and progress are communicated to designated stakeholders | Tier 1 | No crisis communication plan for cyber incidents | Tier 3 |

**Function Maturity: Tier 1–2 (Partial to Risk Informed)**

### 4. Overall Maturity Summary

| Function | Current Maturity | Target Maturity |
| --- | --- | --- |
| Govern | Tier 1–2 (Partial to Risk Informed) | Tier 3 (Repeatable) |
| Identify | Tier 1–2 (Partial to Risk Informed) | Tier 3 (Repeatable) |
| Protect | Tier 1–2 (Partial to Risk Informed) | Tier 3 (Repeatable) |
| Detect | Tier 1 (Partial) | Tier 3 (Repeatable) |
| Respond | Tier 1 (Partial) | Tier 3 (Repeatable) |
| Recover | Tier 1–2 (Partial to Risk Informed) | Tier 3 (Repeatable) |

**Overall Organization Maturity: Tier 1–2 (Partial to Risk Informed)**

### 5. Improvement Roadmap

**Phase 1 — Immediate (0–3 Months)**
- Appoint a dedicated CISO and define cybersecurity roles and responsibilities (GV.RR).
- Update cybersecurity policy and develop topic-specific policies (GV.PO).
- Implement MFA and PAM for critical systems (PR.AA).
- Deploy centralized SIEM and establish monitoring capability (DE.CM).
- Develop a formal Incident Response Plan with escalation matrix (RS.MA).

**Phase 2 — Short-Term (3–6 Months)**
- Establish vulnerability management program with regular scanning (ID.RA).
- Implement cybersecurity awareness training for all personnel (PR.AT).
- Define RTO/RPO and test DR failover procedures at cloud DRC (RC.RP).
- Implement encryption at rest for sensitive data and backups (PR.DS).
- Develop supply chain risk management for cloud DRC provider (GV.SC).

**Phase 3 — Medium-Term (6–12 Months)**
- Deploy IDS/IPS and network anomaly detection (DE.CM).
- Establish crisis communication plan for cyber incidents (RC.CO).
- Conduct tabletop exercises for incident response and recovery.
- Achieve Tier 3 (Repeatable) maturity across all six functions.

---

## 3. Information Security Policy Framework — Himalayan Bank

> **Q.** As the newly appointed Chief Information Security Officer (CISO) of Himalayan Bank, you have been tasked with designing an Information Security Policy framework that effectively mitigates security risks to an acceptable level while ensuring compliance with regulatory requirements, adherence to industry best practices, and alignment with the bank's strategic objectives. How would you approach this task?

As the newly appointed CISO of Himalayan Bank, I would design the following Information Security Policy framework aligned with ISO 27001:2022, NRB IT Guidelines, and the bank's strategic objectives.

### 3.1 Policy Framework Structure

**Level 1 — Overarching Information Security Policy**
- Defines the bank's commitment to information security.
- Approved by the Board of Directors / IT Management Committee.
- Aligned with ISO 27001:2022, NRB Unified Directives (IT Guidelines), and the bank's strategic objectives.
- States the scope of the ISMS covering Head Office, branches, DC, DRC, and digital banking channels.
- Reviewed annually or upon significant organizational/regulatory changes.

**Level 2 — Topic-Specific Policies**
- **Access Control Policy** — access provisioning, MFA, RBAC, PAM, periodic access review for core banking system and digital channels.
- **Acceptable Use Policy** — governs acceptable use of IT assets, internet, email, removable media.
- **Data Classification and Handling Policy** — classification levels (Public, Internal, Confidential, Restricted) for customer data, financial records.
- **Backup and Recovery Policy** — RTO, RPO, backup frequency, retention, encryption, restoration testing for core banking data.
- **Incident Management Policy** — incident categories, escalation matrix, response procedures, evidence preservation, NRB reporting requirements.
- **Password Policy** — minimum 12 characters, complexity, rotation, prohibition of shared credentials.
- **Remote Access and Teleworking Policy** — VPN requirements, MFA, endpoint security for remote banking staff.
- **Change Management Policy** — formal approval, testing, documentation, rollback for core banking system changes.
- **Physical and Environmental Security Policy** — access controls for DC/DRC, visitor management, CCTV, environmental monitoring.
- **Supplier and Third-Party Security Policy** — security requirements for banking software vendors, payment processors, ATM service providers.
- **Digital Banking Security Policy** — security controls for mobile banking, internet banking, and payment gateways.

**Level 3 — Procedures and Guidelines**
- SOPs for implementing each policy (e.g., user provisioning SOP, incident handling SOP).
- Technical guidelines (server hardening, secure coding for banking applications, network configuration standards).
- Checklists for audit, incident response, and business continuity.

### 3.2 Policy Development Process

- Conduct a Risk Assessment to identify information security risks across banking operations.
- Map controls to ISO 27001:2022 Annex A (93 controls across 4 themes).
- Align with NRB Unified Directives and IT Guidelines for banking sector.
- Draft policies with input from relevant departments (IT, Operations, Compliance, Legal, Treasury).
- Obtain Board/IT Management Committee approval.
- Communicate and distribute to all branches and obtain written acknowledgement.

### 3.3 Policy Implementation and Enforcement

- Conduct security awareness training across all branches for all employees.
- Integrate policy compliance checks into regular IS Audits.
- Define disciplinary procedures for policy violations.
- Implement technical controls (DLP, MFA, endpoint protection, SIEM) to enforce policy requirements.

### 3.4 Policy Review and Maintenance

- Review all policies at least annually.
- Trigger additional reviews upon NRB directive updates, major incidents, organizational restructuring.
- Maintain version control and document review history.
- Communicate updates to all branches and relevant personnel.

### 3.5 Regulatory Alignment

- NRB Unified Directives — IT Guidelines for banks and financial institutions.
- Electronic Transactions Act, 2063 (2008).
- Individual Privacy Act, 2075 (2018).
- ISO/IEC 27001:2022.
- NIST Cybersecurity Framework.
- PCI DSS (for card payment processing systems).

---

## 4. Problem and Change Management in IS Audit — Nepal Telecom

> **Q.** Consider the IS Audit Activity in Nepal Telecom. Explain the importance of Problem and Change Management in an audit and describe the key activities an Information System (IS) Auditor should perform to assess the effectiveness of the Problem and Change Management process.

### 4.1 Importance of Problem Management in IS Audit

Problem Management is the process of identifying the root cause of recurring incidents and eliminating them to prevent future occurrences. In the context of Nepal Telecom, which operates critical telecommunications infrastructure serving millions of subscribers:

- **Minimizes service disruptions** — identifying root causes of recurring network outages, billing errors, or system failures reduces downtime for telecom services.
- **Reduces incident recurrence** — permanent fixes prevent repeated incidents affecting customer experience and SLA compliance.
- **Improves service quality** — proactive problem management identifies weaknesses in infrastructure before they cause incidents.
- **Supports regulatory compliance** — NTA (Nepal Telecommunications Authority) requires service availability standards that demand effective problem resolution.
- **Builds Known Error Database (KEDB)** — documented workarounds enable faster incident resolution by the service desk.

### 4.2 Importance of Change Management in IS Audit

Change Management ensures that all changes to IT systems are recorded, evaluated, authorized, prioritized, planned, tested, implemented, documented, and reviewed in a controlled manner. For Nepal Telecom:

- **Prevents unauthorized changes** — uncontrolled changes to network configurations, billing systems, or subscriber databases can cause widespread service disruption.
- **Ensures service stability** — structured change process with testing and rollback plans minimizes risk of failed changes impacting telecom services.
- **Maintains audit trail** — documented change records provide evidence for regulatory audits and accountability.
- **Supports compliance** — NTA regulations and ISO 27001 (A.8.32) require formal change management processes.
- **Reduces security risks** — uncontrolled changes can introduce vulnerabilities into critical telecom infrastructure.

### 4.3 Key Activities of an IS Auditor — Problem Management Assessment

**Activity 1: Review Problem Management Policy and Procedures**
- Verify that a formal Problem Management policy exists defining roles, responsibilities, escalation paths, and KPIs.
- Check alignment with ITIL framework and ISO 20000 standards.

**Activity 2: Evaluate Problem Identification Process**
- Assess whether problems are identified both reactively (from recurring incidents) and proactively (trend analysis, infrastructure review).
- Verify linkage between Incident Management and Problem Management — major incidents should automatically trigger problem records.

**Activity 3: Assess Root Cause Analysis (RCA)**
- Review a sample of problem records for evidence of documented root cause analysis.
- Verify that RCA techniques (5-Why, Fishbone, Fault Tree) are applied consistently.

**Activity 4: Review Known Error Database (KEDB)**
- Verify that known errors and workarounds are documented in a centralized knowledge base.
- Check that the KEDB is accessible to the service desk for faster incident resolution.

**Activity 5: Evaluate Problem Resolution and Closure**
- Verify that permanent fixes are submitted through the Change Management process (RFC).
- Check that problems are formally closed only after successful implementation of the permanent fix.
- Review problem closure rate and average resolution time as KPIs.

**Activity 6: Assess Problem Management KPIs**
- Review metrics: number of problems logged, reduction in recurring incidents, time to root cause, time to resolution, success rate of permanent fixes.

### 4.4 Key Activities of an IS Auditor — Change Management Assessment

**Activity 1: Review Change Management Policy and Procedures**
- Verify that a formal Change Management policy exists defining change categories (Standard, Normal, Emergency), approval workflows, and CAB (Change Advisory Board) composition.
- Check alignment with ITIL and ISO 27001 (A.8.32 — Change Management).

**Activity 2: Evaluate Change Request and Logging Process**
- Review that all changes are formally logged with unique IDs in an ITSM tool.
- Verify that change requests include description, reason, risk assessment, rollback plan, and testing requirements.

**Activity 3: Assess Change Authorization**
- Verify that changes are authorized by the CAB or designated authority before implementation.
- Check that emergency changes follow a separate fast-track authorization process with post-implementation review.
- Audit a sample of changes for evidence of proper authorization.

**Activity 4: Review Testing and Validation**
- Verify that changes are tested in a non-production environment before deployment to production.
- Check for evidence of test results and sign-off before go-live.

**Activity 5: Evaluate Implementation and Rollback**
- Review that changes are implemented within the approved maintenance windows.
- Verify that rollback plans are documented and tested for each change.
- Check post-implementation review (PIR) records to confirm changes achieved intended outcomes.

**Activity 6: Assess Change Management KPIs**
- Review metrics: number of changes (by category), change success rate, number of failed changes, number of unauthorized changes detected, emergency change ratio.

---

## 5. Risk Assessment of Information Assets — Wallet Company

> **Q.** As the newly appointed Chief Risk Officer (CRO) of a leading wallet company, identify and list at least five critical information assets within the organization's information processing facility. Conduct a thorough risk assessment for each asset, incorporating Confidentiality, Integrity, and Availability (CIA) considerations, threat capability analysis, vulnerability assessment, evaluation of existing controls, and impact analysis.

As the Chief Risk Officer (CRO) of a leading wallet company, I identify the following 5 critical Information Assets and perform a comprehensive Risk Assessment.

### 5.1 Identification of Information Assets

| # | Asset | Category | Description |
| --- | --- | --- | --- |
| 1 | Transaction Database Server | Hardware/Information | Stores all wallet transactions, user balances, KYC data, and financial records |
| 2 | Mobile Application Backend (API Server) | Software/Information | Processes all mobile wallet transactions, fund transfers, and payment requests |
| 3 | Payment Gateway Integration System | Software/Information | Interfaces with banks, PSPs, and NRB payment systems for fund settlement |
| 4 | User Authentication and KYC System | Software/Information | Stores user credentials, KYC documents, biometric data, and manages authentication |
| 5 | Network Infrastructure (DC/DRC) | Hardware | Core routers, switches, firewalls, load balancers connecting DC, DRC, and external networks |

### 5.2 Risk Assessment

#### Asset 1: Transaction Database Server

| Parameter | Assessment |
| --- | --- |
| **Confidentiality** | High — contains sensitive financial data, user balances, transaction history |
| **Integrity** | High — unauthorized modification of balances or transactions causes direct financial loss |
| **Availability** | High — downtime halts all wallet transactions and customer operations |
| **Threats** | SQL injection, ransomware, insider threat, unauthorized access, hardware failure |
| **Threat Capability** | High — financially motivated attackers target fintech/wallet platforms |
| **Vulnerabilities** | Unpatched database software, weak access controls, lack of encryption at rest, shared DBA credentials |
| **Existing Controls** | Antivirus installed, basic firewall, daily backup, SSL/TLS for transit |
| **Likelihood** | High |
| **Impact** | High — financial loss, regulatory penalty from NRB, loss of customer trust, legal liability |
| **Risk Rating** | **HIGH** |
| **Recommendation** | Implement database encryption at rest, enforce strong access controls with PAM, regular patching, database activity monitoring, implement row-level security |

#### Asset 2: Mobile Application Backend (API Server)

| Parameter | Assessment |
| --- | --- |
| **Confidentiality** | High — APIs process user credentials, OTPs, and financial transaction data |
| **Integrity** | High — compromised APIs can allow unauthorized fund transfers |
| **Availability** | High — API downtime renders mobile wallet unusable for all customers |
| **Threats** | API abuse, injection attacks (OWASP Top 10), DDoS, credential stuffing, session hijacking |
| **Threat Capability** | High — APIs are publicly exposed and actively targeted |
| **Vulnerabilities** | No rate limiting, insufficient input validation, outdated API framework, no WAF |
| **Existing Controls** | SSL/TLS, basic firewall, token-based authentication |
| **Likelihood** | High |
| **Impact** | High — unauthorized transactions, data breach, service disruption, NRB regulatory action |
| **Risk Rating** | **HIGH** |
| **Recommendation** | Deploy WAF, implement API rate limiting, conduct regular VAPT (quarterly), implement OAuth 2.0 with MFA, deploy DDoS protection |

#### Asset 3: Payment Gateway Integration System

| Parameter | Assessment |
| --- | --- |
| **Confidentiality** | High — handles bank account details, settlement data, inter-bank transaction information |
| **Integrity** | High — tampered settlement data causes financial discrepancies |
| **Availability** | High — downtime prevents fund loading, transfers, and merchant payments |
| **Threats** | MITM attacks on bank integrations, transaction tampering, system compromise, partner-side breach |
| **Threat Capability** | High — payment systems are high-value targets |
| **Vulnerabilities** | Unencrypted internal API calls, lack of transaction integrity checks, no real-time fraud detection |
| **Existing Controls** | TLS for external connections, basic reconciliation process |
| **Likelihood** | Medium |
| **Impact** | High — financial loss, regulatory penalty, disruption of payment services |
| **Risk Rating** | **HIGH** |
| **Recommendation** | Implement end-to-end encryption for all payment APIs, deploy real-time fraud detection, implement transaction signing and integrity verification, conduct regular reconciliation audits |

#### Asset 4: User Authentication and KYC System

| Parameter | Assessment |
| --- | --- |
| **Confidentiality** | High — contains PII, KYC documents (citizenship, photos), biometric data |
| **Integrity** | High — tampered KYC data enables identity fraud and money laundering |
| **Availability** | High — unavailability prevents new user onboarding and transaction authentication |
| **Threats** | Identity theft, data breach, social engineering, credential compromise, insider threat |
| **Threat Capability** | High — KYC data has high black-market value |
| **Vulnerabilities** | KYC documents stored unencrypted, weak password policy, no MFA for internal admin access, PII not masked in logs |
| **Existing Controls** | Password-based login, basic access restrictions |
| **Likelihood** | High |
| **Impact** | High — violation of Individual Privacy Act 2018, regulatory penalty, massive reputational damage |
| **Risk Rating** | **HIGH** |
| **Recommendation** | Encrypt KYC data at rest and in transit, implement MFA for all user and admin access, deploy data masking in non-production environments, implement access logging and monitoring, comply with Individual Privacy Act 2018 |

#### Asset 5: Network Infrastructure (DC/DRC)

| Parameter | Assessment |
| --- | --- |
| **Confidentiality** | High — network carries all financial transaction data |
| **Integrity** | High — compromised network enables MITM attacks on transactions |
| **Availability** | High — network outage halts all wallet services |
| **Threats** | DDoS, unauthorized access, network misconfiguration, MITM, lateral movement |
| **Threat Capability** | High — network is the backbone of all wallet operations |
| **Vulnerabilities** | Flat network topology, default credentials on some devices, no IDS/IPS, outdated firmware |
| **Existing Controls** | Perimeter firewall, basic ACLs, VPN for DRC connectivity |
| **Likelihood** | Medium |
| **Impact** | High — complete operational disruption for all wallet users |
| **Risk Rating** | **HIGH** |
| **Recommendation** | Implement network segmentation (separate transaction processing, user data, management zones), deploy IDS/IPS, update firmware, enforce secure configuration baselines, conduct periodic network VAPT |

### 5.3 Risk Assessment Summary

| # | Asset | C | I | A | Risk Rating |
| --- | --- | --- | --- | --- | --- |
| 1 | Transaction Database Server | High | High | High | HIGH |
| 2 | Mobile App Backend (API Server) | High | High | High | HIGH |
| 3 | Payment Gateway Integration | High | High | High | HIGH |
| 4 | User Authentication & KYC System | High | High | High | HIGH |
| 5 | Network Infrastructure (DC/DRC) | High | High | High | HIGH |

All identified assets require immediate risk treatment through implementation of recommended controls, tracked via a Risk Register with assigned owners and remediation timelines.

---

## 6. IS Audit Report — ISO 27001:2022 (Six Controls)

> **Q.** You have been appointed as an external Information System Auditor for a renowned company with 250 sites, its own Data Center, and a Disaster Recovery Center. Your task is to perform an IS audit focusing on Six controls from the ISO 27001:2022 standard. Prepare a comprehensive report that includes the control, your observations, risk ratings, and key findings with recommendations.

### Information System Audit Report

**Organization:** A renowned company with 250 sites, own Data Center (DC) and Disaster Recovery Center (DRC)
**Audit Standard:** ISO 27001:2022
**Audit Type:** External Information System Audit
**Controls Evaluated:** 6 (across all 4 Annex A themes)

### Introduction

Information and Communication Technologies (ICT) play a vital role for the organization to enable its business processes across 250 sites, DC, and DRC. This IS Audit evaluates the organization's information security posture against 6 selected controls from ISO 27001:2022 Annex A. It aids in preserving the Confidentiality, Integrity and Availability (CIA) of information by applying a risk management process and gives confidence to stakeholders that risks are adequately managed.

### Objective

To assess the design and operating effectiveness of 6 ISO 27001:2022 Annex A controls, identify risks, and provide actionable recommendations.

### Scope

Head Office, Data Center (DC), Disaster Recovery Center (DRC), and a representative sample of branch sites across 250 locations. Controls evaluated span all four Annex A themes: Organizational, People, Physical, and Technological.

---

### A.1. Organizational Controls

#### Control 1: Policies for Information Security (A.5.1)

**Control:** Information security policy and topic-specific policies should be defined, approved by management, published, communicated to and acknowledged by relevant personnel and relevant interested parties, and reviewed at planned intervals and if significant changes occur.

**Purpose:** To ensure continuing suitability, adequacy, effectiveness of management direction and support for information security in accordance with business, legal, statutory, regulatory and contractual requirements.

**Observation:** The organization has an Information Security Policy (Version 1.0); however, the policy has not been reviewed or updated since its initial release. No topic-specific policies (acceptable use, data classification, remote access, backup, incident management) are formally documented. Staff awareness of the existing policy was limited, particularly at remote branch sites. No evidence of written acknowledgement by employees was found.

**Risk Rating:** HIGH

**Recommendation:** Immediately review and update the Information Security Policy to align with ISO 27001:2022 and the current organizational context. Develop topic-specific policies covering acceptable use, access control, data classification, backup, incident management, and remote access. Communicate to all personnel across 250 sites and obtain signed acknowledgement. Establish an annual review cycle with additional reviews triggered by significant changes.

---

### A.2. People Controls

#### Control 2: Information Security Awareness, Education and Training (A.6.3)

**Control:** Personnel of the organization and relevant interested parties should receive appropriate information security awareness, education and training and regular updates of the organization's information security policy, topic-specific policies and procedures, as relevant for their job function.

**Purpose:** To ensure personnel and relevant interested parties are aware of and fulfill their information security responsibilities.

**Observation:** No structured information security awareness and training program exists. Employees across branch sites are unaware of basic cybersecurity practices (phishing identification, password management, social engineering). No training records were available for review. Shared login credentials were observed at multiple sites for convenience.

**Risk Rating:** HIGH

**Recommendation:** Establish a comprehensive security awareness training program conducted at least annually for all employees across 250 sites. Cover phishing, social engineering, password hygiene, data handling, and incident reporting. Maintain training records. Conduct periodic simulated phishing exercises. Provide specialized training for IT staff on secure administration and incident response.

---

### A.3. Physical Controls

#### Control 3: Physical Security Perimeters (A.7.1)

**Control:** Security perimeters should be defined and used to protect areas that contain information and other associated assets.

**Purpose:** To prevent unauthorized physical access, damage and interference to the organization's information and other associated assets.

**Observation:** The Data Center uses a basic key-lock mechanism without electronic access control (biometric/card-based). No visitor log is maintained for the DC area. The DRC has shared access corridors without a dedicated security perimeter. CCTV coverage at the DC entrance is limited, with footage retained for only 15 days. Multiple branch sites have minimal physical security for IT equipment and networking infrastructure.

**Risk Rating:** HIGH

**Recommendation:** Implement electronic access control systems (biometric or smart card) for DC and DRC. Deploy a visitor management system with proper logging. Enhance CCTV with minimum 90-day retention. Establish a dedicated security perimeter for DRC with independent access controls. Conduct physical security assessments at all branch sites and establish minimum security standards.

---

### A.4. Technological Controls

#### Control 4: Access Control (A.8.2)

**Control:** Access to information and other associated assets should be restricted in accordance with the established topic-specific policy on access control.

**Purpose:** To ensure authorized access and to prevent unauthorized access to information and other associated assets.

**Observation:** No formal access control policy has been documented. User account management lacks a structured provisioning and de-provisioning process — terminated employees' accounts were found active. Shared accounts observed in critical systems at multiple sites. Password policy is weak (6-character minimum, no complexity, no expiry). No MFA implemented for any system. Privileged access uses shared admin/root credentials without PAM.

**Risk Rating:** HIGH

**Recommendation:** Develop and implement a formal access control policy. Establish user lifecycle management with HR integration for timely account deactivation upon separation. Eliminate shared accounts. Enforce 12-character passwords with complexity and rotation. Implement MFA for all critical systems. Deploy PAM solution. Conduct quarterly user access reviews.

---

#### Control 5: Management of Technical Vulnerabilities (A.8.8)

**Control:** Information about technical vulnerabilities of information systems in use should be obtained, the organization's exposure to such vulnerabilities should be evaluated and appropriate measures should be taken.

**Purpose:** To prevent exploitation of technical vulnerabilities.

**Observation:** No formal vulnerability management program exists. No periodic vulnerability assessments or penetration testing conducted on IT infrastructure or applications. Patch management is ad-hoc with no defined timelines — several servers running outdated OS with known vulnerabilities. Customer-facing application has not been security-assessed. No software inventory maintained to track versions and patch status.

**Risk Rating:** HIGH

**Recommendation:** Establish a formal vulnerability management program with quarterly vulnerability assessments and annual penetration testing. Define patch management timelines: critical patches within 72 hours, high within 2 weeks, routine within 30 days. Maintain comprehensive IT asset and software inventory. Subscribe to vulnerability advisory services (e.g., CERT, vendor advisories).

---

#### Control 6: Information Backup (A.8.13)

**Control:** Backup copies of information, software and systems should be maintained and regularly tested in accordance with the agreed topic-specific policy on backup.

**Purpose:** To enable recovery of information and other associated assets following data loss or disruption.

**Observation:** Daily backups of critical databases are performed. No formal backup policy exists defining scope, frequency, retention periods, and recovery procedures. Off-site replication to DRC is weekly, creating a 7-day potential data loss window. Backup restoration tests have not been performed in over 12 months. RTO and RPO have not been formally defined. Backup encryption is not implemented.

**Risk Rating:** HIGH

**Recommendation:** Develop a formal backup policy defining RTO, RPO, frequency, retention, and restoration procedures. Increase DRC replication to daily minimum. Conduct quarterly backup restoration tests and document results. Encrypt all backup data at rest and in transit. Integrate backup strategy with BCP.

---

### Summary of Findings

| # | Control | ISO Ref | Theme | Risk Rating |
| --- | --- | --- | --- | --- |
| 1 | Policies for Information Security | A.5.1 | Organizational | HIGH |
| 2 | Security Awareness and Training | A.6.3 | People | HIGH |
| 3 | Physical Security Perimeters | A.7.1 | Physical | HIGH |
| 4 | Access Control | A.8.2 | Technological | HIGH |
| 5 | Management of Technical Vulnerabilities | A.8.8 | Technological | HIGH |
| 6 | Information Backup | A.8.13 | Technological | HIGH |

**Overall Assessment:** All 6 controls rated HIGH risk. The organization's information security posture requires significant improvement across organizational, people, physical, and technological domains.

### Prioritized Recommendations

**Critical Priority (Immediate)**
- Implement MFA for all critical systems and eliminate shared accounts.
- Conduct immediate VAPT of customer-facing applications and IT infrastructure.
- Define RTO/RPO and increase DRC backup replication to daily.

**High Priority (Within 3 Months)**
- Update Information Security Policy and develop topic-specific policies.
- Implement electronic access controls at DC and DRC.
- Establish formal vulnerability and patch management program.
- Deploy PAM for administrative accounts.

**Medium Priority (Within 6 Months)**
- Conduct cybersecurity awareness training for all employees across 250 sites.
- Establish quarterly backup restoration testing.
- Implement comprehensive IT asset inventory.

---

## 7. Audit of Incident Response Plan — Pokhara University

> **Q.** Elaborate on the methodology you would employ to audit the effectiveness of the Incident Response Plan at the Pokhara University in Pokhara. Describe the steps you would take to evaluate the plan, ensuring it aligns with industry best practices and adequately addresses potential risks, incident handling, and recovery scenarios.

### Incident Response Plan (IRP) Audit Methodology — Pokhara University

**Organization:** Pokhara University, Pokhara
**Audit Reference:** NIST SP 800-61 (Incident Handling Guide), ISO 27001:2022 (A.5.24–A.5.28), NIST CSF 2.0 (RS function)

### 1. Introduction

This audit evaluates the effectiveness of Pokhara University's Incident Response Plan to determine whether it is practical, aligned with industry best practices (NIST SP 800-61), and capable of effectively addressing potential risks, managing incidents, and supporting recovery and continuity efforts for the university's academic and administrative information systems.

### 2. Audit Objectives

- Assess whether a formal Incident Response Plan (IRP) exists and is documented.
- Evaluate alignment of the IRP with NIST SP 800-61 four-phase lifecycle and ISO 27001:2022 controls.
- Determine the readiness and capability of the Incident Response Team (IRT/CSIRT).
- Verify that the IRP is tested, maintained, and continuously improved.
- Assess integration with the university's BCP/DRP.

### 3. Audit Methodology — NIST SP 800-61 Four-Phase Lifecycle

#### Phase 1: Preparation

**Step 1: Review IRP Policy and Documentation**
- Verify that a formal Incident Response Policy exists, is approved by university management, and defines the authority and scope of the IR program.
- Review the written IRP document for completeness — does it define incident classification, escalation criteria, roles, communication plan, and evidence handling procedures?
- Check that the IRP covers incident types relevant to the university: data breach of student/faculty records, ransomware, email compromise, website defacement, unauthorized access to academic systems.

**Step 2: Assess Incident Response Team (IRT) Structure**
- Verify that a CSIRT/IRT is formally established with defined membership.
- Check that roles are clearly assigned: incident commander, technical lead, communications lead, legal coordinator.
- Assess whether the IRT has adequate skills and is available for 24/7 response or has on-call arrangements.

**Step 3: Evaluate Training and Readiness**
- Review records of IR training provided to IRT members and general staff.
- Check whether tabletop exercises or simulations have been conducted and how frequently.
- Verify that the university's IT staff know how to report and escalate security incidents.

**Step 4: Review Tools and Resources**
- Assess availability and configuration of IR tools: SIEM, forensic tools, secure communication channels, incident tracking system.
- Verify that the IRT has access to necessary resources (hardware, software, forensic kits).

#### Phase 2: Detection and Analysis

**Step 5: Evaluate Detection Capabilities**
- Review monitoring tools deployed — IDS/IPS, SIEM, endpoint protection, log management.
- Assess whether the university has defined indicators of compromise (IoCs) and alert thresholds.
- Verify that the IRP defines criteria for classifying security events vs. incidents (per ISO 27001 A.5.25).

**Step 6: Assess Triage and Analysis Process**
- Review the process for analyzing alerts — who receives them, how they are prioritized, and how decisions are made.
- Check that incident severity levels are defined (e.g., Low, Medium, High, Critical) with response timelines.
- Review sample incident records for evidence of proper analysis and documentation.

#### Phase 3: Containment, Eradication, and Recovery

**Step 7: Review Containment Procedures**
- Verify that the IRP defines short-term and long-term containment strategies for different incident types.
- Check that containment actions preserve evidence for forensic analysis (per ISO 27001 A.5.28 — Collection of Evidence).
- Assess procedures for isolating affected systems (network isolation, account lockout).

**Step 8: Evaluate Eradication and Recovery Procedures**
- Review procedures for removing the root cause (malware removal, vulnerability patching, credential reset).
- Check that recovery procedures define steps for restoring systems from clean backups.
- Verify that restored systems are validated before returning to production.
- Assess integration with the university's BCP/DRP for recovery scenarios.

#### Phase 4: Post-Incident Activity

**Step 9: Assess Lessons Learned Process**
- Verify that the IRP mandates post-incident reviews (per ISO 27001 A.5.27 — Learning from Information Security Incidents).
- Review evidence of lessons learned meetings — minutes, attendees, action items.
- Check that findings from past incidents are used to update the IRP and improve controls.

**Step 10: Evaluate Reporting and Communication**
- Review the IRP's communication plan — internal reporting to university management, external reporting to regulatory authorities.
- Verify that reporting timelines are defined and aligned with regulatory requirements.
- Check that communication templates (for stakeholders, media, students/faculty) are prepared.

### 4. Audit Deliverables

- IRP Effectiveness Assessment Report with findings mapped to NIST SP 800-61 phases.
- Gap analysis against ISO 27001:2022 controls A.5.24–A.5.28.
- Risk ratings for each audit area (HIGH, MEDIUM, LOW).
- Recommendations for improvement with priorities and timelines.
- Recommendation to conduct a tabletop exercise to test the IRP in a simulated scenario.

---

## 8. Ransomware Readiness Assessment — Proposal

> **Q.** As an expert, outline your approach to conducting a Ransomware Readiness Assessment for a well-known company that has issued an RFP for this purpose. Describe in detail how you would plan, execute, and report on this assessment, and prepare a comprehensive proposal for carrying out the engagement.

### Ransomware Readiness Assessment — Proposal

### 1. Introduction

This proposal outlines the approach for conducting a Ransomware Readiness Assessment (RRA) for the organization using the CISA Cyber Security Evaluation Tool (CSET) — Ransomware Readiness Assessment module. The assessment evaluates the organization's preparedness against ransomware threats across 10 core domains at three maturity tiers (Basic, Intermediate, Advanced).

### 2. Objectives

- Evaluate the organization's current ransomware preparedness posture using the CISA RRA framework.
- Identify gaps and weaknesses across 10 assessment domains.
- Determine maturity level (Basic, Intermediate, Advanced) for each domain.
- Provide a prioritized remediation roadmap to strengthen ransomware resilience.

### 3. Scope

- All operational sites, Data Center (DC), and Disaster Recovery Center (DRC).
- All critical information systems, network infrastructure, endpoints, and cloud services.
- IT policies, procedures, and incident response capabilities related to ransomware.

### 4. Assessment Framework

**Tool:** CISA Cyber Security Evaluation Tool (CSET) — Ransomware Readiness Assessment (RRA) Module

**10 RRA Assessment Domains:**

| # | Domain | Focus Area |
| --- | --- | --- |
| 1 | Asset Management (AM) | Asset inventory, criticality classification, dependency mapping |
| 2 | Robust Data Backup (DB) | Backup practices, offline/air-gapped copies, restoration testing, immutable backups |
| 3 | Phishing Prevention and Awareness (PP) | Email filtering, phishing training, simulations, advanced email security |
| 4 | User and Access Management (UM) | Unique IDs, MFA, PAM, least privilege, zero trust |
| 5 | Network Perimeter Monitoring (NM) | Firewalls, IDS/IPS, network anomaly detection, automated response |
| 6 | Web Browser Management and DNS Filtering (BM) | Browser patching, DNS filtering, browser isolation |
| 7 | Application Integrity and Allowlisting (AI) | Software restriction, application allowlisting, automated enforcement |
| 8 | Incident Response (IR) | Ransomware-specific IRP, tabletop exercises, automated playbooks |
| 9 | Risk Management (RM) | Ransomware in risk register, risk assessments, cyber insurance |
| 10 | Vulnerability Management (VM) | Vulnerability scanning, patch management, continuous monitoring |

**Maturity Tiers:** Basic → Intermediate → Advanced

### 5. Methodology

**Phase 1: Pre-Engagement and Scoping (Week 1)**
- Conduct discovery meeting with key stakeholders (CISO, IT, Risk, Operations).
- Collect organizational context — infrastructure architecture, existing security tools, compliance requirements.
- Define assessment boundaries and finalize scope.
- Sign NDA and engagement letter.

**Phase 2: Assessment and Evaluation (Week 2–3)**
- Install and configure CISA CSET tool with the RRA module.
- Conduct evidence-based review across all 10 domains at all three maturity tiers.
- Review documentation — policies, procedures, network diagrams, backup configurations, incident response plans.
- Conduct interviews with process owners and technical staff.
- Perform technical validation — verify backup configurations, access control settings, endpoint protection status, network segmentation.

**Phase 3: Validation and Testing (Week 3–4)**
- Perform targeted vulnerability scanning to validate ransomware attack surface.
- Conduct a tabletop exercise simulating a ransomware incident to test the IRP's effectiveness.
- Verify backup restoration capability with a controlled restoration test.

**Phase 4: Analysis and Reporting (Week 4–5)**
- Analyze CSET-generated assessment results — maturity scores per domain.
- Perform gap analysis mapping current state to target state for each domain.
- Categorize findings by severity and priority.
- Develop prioritized remediation roadmap.

**Phase 5: Reporting and Presentation (Week 5–6)**
- Submit draft report for management review and factual verification.
- Present findings to executive management and technical teams.
- Issue final report with agreed corrective action plan.

### 6. Deliverables

| # | Deliverable | Description |
| --- | --- | --- |
| 1 | RRA Maturity Assessment Report | Maturity scores per domain (Basic/Intermediate/Advanced) with evidence |
| 2 | Gap Analysis Report | Gaps identified per domain against CISA RRA framework |
| 3 | Vulnerability Scan Report | Technical vulnerability findings relevant to ransomware attack surface |
| 4 | Tabletop Exercise Report | Findings from ransomware incident simulation exercise |
| 5 | Executive Summary | High-level summary of ransomware risk posture for C-suite and Board |
| 6 | Remediation Roadmap | Prioritized recommendations with timelines mapped to Basic/Intermediate/Advanced tiers |

### 7. Team Composition

- Lead Assessor — CISA/CISM certified, ransomware incident response experience.
- Technical Assessor — Network security, endpoint security, and VAPT expertise.
- GRC Assessor — Risk management, policy review, and compliance expertise.

### 8. Timeline

| Phase | Activity | Duration |
| --- | --- | --- |
| Phase 1 | Pre-Engagement and Scoping | Week 1 |
| Phase 2 | Assessment and Evaluation | Week 2–3 |
| Phase 3 | Validation and Testing | Week 3–4 |
| Phase 4 | Analysis and Reporting | Week 4–5 |
| Phase 5 | Final Report and Presentation | Week 5–6 |

### 9. Confidentiality

All assessment findings, reports, and evidence shall be treated as confidential. Information shall only be shared with authorized stakeholders. The assessment team shall sign NDAs prior to commencement.

---

## 9. VAPT Terms of Reference (ToR)

> **Q.** A well-established company with a network spanning over 100 sites, supported by its own Data Center (DC) and a private Cloud-based Disaster Recovery Center (DRC), is planning to conduct a Vulnerability Assessment and Penetration Testing (VAPT) exercise. You have been assigned the task of developing a detailed Terms of Reference (ToR) for the VAPT activity.

### Terms of Reference (ToR) for Vulnerability Assessment and Penetration Testing (VAPT)

### 1. Introduction

This Terms of Reference (ToR) defines the purpose, scope, methodology, and deliverables for conducting a Vulnerability Assessment and Penetration Testing (VAPT) exercise for the organization operating 100+ sites with an in-house Data Center (DC) and a private cloud-based Disaster Recovery Center (DRC).

### 2. Background

The organization requires a comprehensive VAPT to identify security vulnerabilities in its IT infrastructure, applications, and network systems, assess their exploitability, and provide recommendations for remediation to strengthen the overall security posture.

### 3. Objectives

- Identify known and unknown vulnerabilities across network infrastructure, servers, applications, and endpoints.
- Assess the exploitability of identified vulnerabilities through controlled penetration testing.
- Evaluate the security posture of the Data Center (DC) and Disaster Recovery Center (DRC).
- Assess the effectiveness of existing security controls (firewalls, IDS/IPS, access controls).
- Provide a prioritized remediation plan based on risk ratings.
- Support compliance with ISO 27001:2022 (A.8.8 — Management of Technical Vulnerabilities) and applicable regulations.

### 4. Scope of Work

**4.1 In-Scope Assets**

- **Network Infrastructure:** All routers, switches, firewalls, load balancers, VPN gateways across 100+ sites, DC, and DRC. IP ranges and subnets to be provided during scoping.
- **Servers:** All production servers at DC and DRC — application servers, database servers, mail servers, DNS servers, web servers.
- **Web Applications:** All customer-facing and internal web applications (URLs to be provided).
- **Mobile Applications:** iOS and Android mobile applications (if applicable).
- **Cloud Infrastructure:** Private cloud DRC environment — virtual machines, storage, networking components.
- **Wireless Networks:** Wireless access points at Head Office and major branch sites.
- **Endpoints:** A sample of workstations and laptops at selected sites.

**4.2 Out-of-Scope**
- Third-party hosted services not under the organization's control.
- Social engineering testing (unless explicitly requested separately).
- Physical security testing.

### 5. Methodology

The VAPT shall follow industry-recognized frameworks and standards:
- **OWASP Testing Guide** — for web and mobile application testing.
- **PTES (Penetration Testing Execution Standard)** — for overall penetration testing methodology.
- **NIST SP 800-115** — Technical Guide to Information Security Testing and Assessment.
- **CVSS (Common Vulnerability Scoring System)** — for vulnerability severity rating.

**Phase 1: Planning and Scoping**
- Finalize scope, target assets, IP ranges, and testing schedule.
- Obtain written authorization (Rules of Engagement) and sign NDA.
- Define testing windows and escalation procedures.
- Identify points of contact for both parties.

**Phase 2: Reconnaissance and Information Gathering**
- Passive reconnaissance — OSINT, DNS enumeration, WHOIS.
- Active reconnaissance — network scanning, service discovery, OS fingerprinting.

**Phase 3: Vulnerability Assessment**
- Automated vulnerability scanning using industry tools (Nessus, Qualys, OpenVAS).
- Manual verification to eliminate false positives.
- Identification and documentation of vulnerabilities with CVSS scoring.

**Phase 4: Penetration Testing**
- Manual exploitation of identified vulnerabilities to demonstrate impact.
- Network penetration testing — external and internal.
- Web application penetration testing — OWASP Top 10 (injection, broken authentication, XSS, CSRF, SSRF, etc.).
- Privilege escalation and lateral movement assessment.
- Post-exploitation — assess data exfiltration potential and business impact.

**Phase 5: Reporting**
- Document all findings with evidence (screenshots, request/response captures, PoC).
- Assign CVSS scores and risk ratings (Critical, High, Medium, Low, Informational).
- Provide actionable remediation recommendations for each finding.

**Phase 6: Retest (Optional)**
- Verify remediation of identified vulnerabilities after the organization applies fixes.
- Issue a retest report confirming closure of findings.

### 6. Rules of Engagement (RoE)

- Testing shall be conducted only within the authorized scope and testing windows.
- No Denial of Service (DoS/DDoS) testing on production systems unless explicitly authorized.
- Any critical vulnerability discovered during testing shall be immediately reported to the designated point of contact.
- Testing team shall not modify, delete, or exfiltrate actual production data.
- All testing activities shall be logged and traceable.

### 7. Deliverables

| # | Deliverable | Description |
| --- | --- | --- |
| 1 | Executive Summary | Non-technical overview of security posture for senior management |
| 2 | Detailed VAPT Report | Each vulnerability with description, CVSS score, PoC evidence, business impact, remediation |
| 3 | Vulnerability Assessment Report | Automated scan results with false positive validation |
| 4 | Penetration Testing Report | Manual exploitation findings with attack narratives |
| 5 | Remediation Guidance | Prioritized remediation steps for IT/development teams |
| 6 | Retest Report | Verification of remediation (if retest phase is included) |
| 7 | Raw Data/Logs | Scan outputs and tool logs as appendices for audit records |

### 8. Team Qualifications

- Lead Penetration Tester — CEH/OSCP/GPEN certified with minimum 5 years experience.
- Web Application Tester — OSCP/GWAPT certified with OWASP expertise.
- Network Security Tester — expertise in network penetration testing and infrastructure security.
- All testers shall maintain professional certifications and sign NDAs and conflict of interest declarations.

### 9. Timeline

| Phase | Activity | Duration |
| --- | --- | --- |
| Phase 1 | Planning and Scoping | Week 1 |
| Phase 2 | Reconnaissance | Week 2 |
| Phase 3 | Vulnerability Assessment | Week 2–3 |
| Phase 4 | Penetration Testing | Week 3–5 |
| Phase 5 | Reporting | Week 6 |
| Phase 6 | Retest (Optional) | Week 8–9 |

### 10. Authority and Access

- The VAPT team shall have authorized access to all in-scope systems, networks, and applications.
- The organization shall provide necessary credentials for authenticated testing (grey-box/white-box testing as required).
- A designated POC shall be available during testing hours for issue escalation.

### 11. Confidentiality

- All findings, reports, and evidence are confidential and shall be shared only with authorized stakeholders.
- The VAPT team shall sign NDAs prior to engagement commencement.
- Reports shall be transmitted via encrypted channels only.

### 12. Reporting and Communication

- Daily status updates during active testing phase.
- Critical findings reported immediately upon discovery.
- Draft report within 5 business days of testing completion.
- Management response within 10 business days.
- Final report within 15 business days of testing completion.

---

## 10. Short Notes: IT Governance with COBIT

> **Q.** Short notes on: IT Governance with COBIT

**COBIT (Control Objectives for Information and Related Technologies)** is a framework developed by ISACA for the governance and management of enterprise information and technology (I&T). The latest version, COBIT 2019, provides a comprehensive structure for aligning IT with business objectives.

### Core Principles of COBIT 2019
- **Meeting Stakeholder Needs** — balancing competing interests to create value.
- **Covering the Enterprise End-to-End** — integrating IT governance into enterprise governance.
- **Applying a Single Integrated Framework** — a unified governance approach.
- **Enabling a Holistic Approach** — addressing processes, structures, culture, and technology.
- **Separating Governance from Management** — distinct functions with different purposes.

### Five Domains (40 Governance and Management Objectives)

**Governance Domain:**
- **Evaluate, Direct, and Monitor (EDM)** — strategic direction, stakeholder value, performance monitoring.

**Management Domains:**
- **Align, Plan, and Organize (APO)** — IT strategy, architecture, risk management, resource planning.
- **Build, Acquire, and Implement (BAI)** — solution development, change management, asset management.
- **Deliver, Service, and Support (DSS)** — service delivery, incident management, problem management, security management.
- **Monitor, Evaluate, and Assess (MEA)** — performance monitoring, internal controls, compliance assessment.

### Performance Management
COBIT 2019 uses **Capability Maturity Model** levels (0–5) to measure process maturity:
- Level 0: Incomplete — Level 1: Performed — Level 2: Managed — Level 3: Established — Level 4: Predictable — Level 5: Optimizing.

### Design Factors
COBIT 2019 allows tailoring through design factors: enterprise strategy, IT goals, risk profile, IT-related issues, threat landscape, compliance requirements, role of IT, sourcing model, IT implementation methods, and technology adoption strategy.

### Relevance to IS Audit
IS Auditors use COBIT to evaluate whether IT governance structures effectively align IT strategy with business objectives, manage IT risks, and optimize IT resource utilization. COBIT provides the control objectives and maturity benchmarks against which auditors assess IT governance effectiveness.

---

## 11. Short Notes: Licensing Issues in IS Audit

> **Q.** Short notes on: Licensing Issues in IS Audit

Licensing issues are a critical area in IS Audit, covered under Unit 2 of the syllabus (2.9 Licensing Issues, ICT Procurement Practices). An IS Auditor evaluates whether the organization complies with software licensing agreements and manages licenses effectively.

### Types of Software Licenses
- **Proprietary/Commercial License** — purchased per user, per device, or enterprise-wide (e.g., Microsoft, Oracle).
- **Open Source License** — free to use with varying restrictions (GPL, MIT, Apache).
- **Subscription/SaaS License** — recurring payment for cloud-based software.
- **Volume License** — bulk licensing for large organizations at discounted rates.
- **OEM License** — bundled with hardware; non-transferable.

### Key Licensing Issues in IS Audit
- **Software Piracy/Unlicensed Software** — using software without valid licenses violates copyright law (Electronic Transactions Act 2008) and exposes the organization to legal penalties.
- **Under-Licensing** — fewer licenses than actual installations; compliance risk during vendor audits.
- **Over-Licensing** — paying for more licenses than required; wasteful expenditure.
- **License Tracking** — absence of a centralized Software Asset Management (SAM) system to track installations, entitlements, and renewals.
- **Expired Licenses** — continued use of software after license expiry; security risk from lack of updates/patches.
- **Open Source Compliance** — failure to comply with open source license terms (e.g., GPL requirement to release modified source code).

### IS Auditor's Role
- Verify the existence of a software asset inventory/register.
- Compare installed software against license entitlements to identify gaps.
- Review software procurement procedures for compliance.
- Check for unauthorized or pirated software installations.
- Assess controls preventing unauthorized software installation (e.g., application allowlisting, group policy).
- Review license renewal tracking and expiry alerts.

---

## 12. Short Notes: Audit Questionnaire

> **Q.** Short notes on: Audit Questionnaire

An Audit Questionnaire is a structured set of questions used by IS Auditors during the audit process to systematically gather information about the organization's IT controls, practices, and compliance status. It is covered under Unit 4 (4.8 Audit Questionnaire; Audit Documentation; Audit Report).

### Purpose
- Standardize information gathering across audit engagements.
- Ensure comprehensive coverage of all audit areas.
- Provide documented evidence of audit inquiries and responses.
- Facilitate consistency when multiple auditors are involved.

### Types
- **General IT Controls Questionnaire** — covering IT governance, policies, organizational structure.
- **Application Controls Questionnaire** — specific to application-level controls (input, processing, output).
- **Compliance Questionnaire** — assessing compliance with specific standards (ISO 27001, NIST, COBIT).
- **Self-Assessment Questionnaire** — completed by the auditee before the audit for preliminary assessment.

### Structure
- Organized by audit domain or control area (e.g., access control, change management, backup).
- Each question has: Question text, Expected response/criteria, Actual response, Evidence reference, Status (Compliant/Non-Compliant/Partial), Auditor remarks.

### Example Questions
- Does a formal Information Security Policy exist, and when was it last reviewed?
- Is Multi-Factor Authentication (MFA) implemented for critical systems?
- Are backups tested for restoration at regular intervals?
- Is there a formal change management process with CAB approval?
- Are vulnerability assessments conducted periodically?

### Role in IS Audit
- Used during the planning and execution phases to guide interviews and evidence collection.
- Responses are corroborated with documentary evidence and technical verification.
- Findings from questionnaires feed into the audit report.

---

## 13. Importance of IS Audit with Example

> **Q.** Discuss the importance of conducting IS audit within an organization and illustrates its impact with a suitable example.

### 13.1 Importance of Information System Audit

**Identifying Security Risks and Vulnerabilities**
IS Audit identifies gaps in information security controls — unpatched systems, weak access controls, inadequate backup procedures — enabling proactive risk mitigation before exploitation.

**Ensuring Regulatory Compliance**
Organizations must comply with legal and regulatory requirements (Electronic Transactions Act 2008, Individual Privacy Act 2018, NRB IT Guidelines). IS Audit verifies compliance and prevents legal penalties.

**Protecting the CIA Triad**
IS Audit evaluates whether controls adequately preserve Confidentiality, Integrity, and Availability of information assets, fundamental to business operations and stakeholder trust.

**Improving IT Governance**
IS Audit assesses whether IT governance structures (per COBIT 2019) align IT strategy with business objectives, ensuring efficient use of IT resources and effective risk management.

**Evaluating Business Continuity Readiness**
IS Audit reviews BCP, DRP, and incident response plans, ensuring the organization can recover within acceptable timeframes (RTO/RPO).

**Building Stakeholder Confidence**
Audit findings provide assurance to the Board, management, customers, and regulators that information security risks are adequately managed.

**Driving Continuous Improvement**
IS Audit recommendations and corrective action tracking foster continuous improvement in information security practices.

### 13.2 Example: IS Audit of Yeti Airlines Pvt. Ltd.

Yeti Airlines, a domestic airline operating across multiple sites in Nepal, underwent an IS Audit based on ISO 27001:2022 evaluating 10 controls across 4 themes.

**Audit Findings:**

| # | Control | ISO Ref | Risk |
| --- | --- | --- | --- |
| 1 | Policies for Information Security | A.5.1 | HIGH |
| 2 | IS Roles and Responsibilities | A.5.2 | HIGH |
| 3 | Security Awareness and Training | A.6.3 | HIGH |
| 4 | Physical Security Perimeters | A.7.1 | HIGH |
| 5 | Securing Offices, Rooms and Facilities | A.7.3 | MEDIUM |
| 6 | Access Control | A.8.2 | HIGH |
| 7 | Protection Against Malware | A.8.7 | MEDIUM |
| 8 | Management of Technical Vulnerabilities | A.8.8 | HIGH |
| 9 | Information Backup | A.8.13 | HIGH |
| 10 | Logging | A.8.15 | HIGH |

8 of 10 controls rated HIGH, 2 rated MEDIUM.

**Impact:** The audit exposed critical gaps — lack of formal policies, absent access controls, no VAPT, untested backups, no centralized logging. Based on recommendations, Yeti Airlines initiated appointment of a Security Manager, MFA implementation, third-party VAPT engagement, DC/DRC physical security upgrades, backup policy with defined RTO/RPO, and SIEM acquisition. This demonstrates IS Audit as a critical mechanism for identifying and remediating information security weaknesses.

---

## 14. 4P Framework for Cybersecurity Risk

> **Q.** As a chief compliance officer of a leading organization, describe how the 4P framework can be applied to identify and mitigate cybersecurity risk?

As the Chief Compliance Officer, I would apply the **4P Framework — People, Process, Policy, and Platform (Technology)** — to identify and mitigate cybersecurity risks.

### 14.1 People

- Conduct cybersecurity awareness training for all employees at planned intervals (at least annually).
- Define information security roles and responsibilities — appoint CISO, security focal points per department.
- Implement background screening for employees handling sensitive information.
- Establish a security culture through phishing simulations, incident reporting awareness, and disciplinary procedures for violations.
- Ensure adequate staffing of skilled cybersecurity professionals (SOC analysts, incident responders).

### 14.2 Process

- Establish a formal Risk Assessment and Risk Treatment process aligned with ISO 27001:2022.
- Implement Incident Response Process — detection, containment, eradication, recovery, lessons learned.
- Define Change Management and Problem Management processes for IT systems.
- Conduct periodic VAPT.
- Perform BIA and maintain BCP and DRP.
- Establish user access lifecycle management — provisioning, periodic review, de-provisioning.

### 14.3 Policy

- Develop and maintain an Information Security Policy approved by top management, reviewed annually.
- Create topic-specific policies: Acceptable Use, Access Control, Data Classification, Backup, Remote Access, Password, Incident Management.
- Ensure policies align with regulatory requirements (Electronic Transactions Act 2008, Individual Privacy Act 2018, sector-specific regulations).
- Communicate policies to all personnel and obtain written acknowledgement.
- Establish compliance monitoring and audit mechanisms.

### 14.4 Platform (Technology)

- Deploy centralized EDR and antivirus across all endpoints.
- Implement MFA for all critical systems.
- Deploy SIEM for centralized log management, correlation, and alerting.
- Implement network segmentation, firewall, IDS/IPS, and DLP.
- Enforce encryption for data at rest and in transit.
- Implement PAM for administrative accounts.
- Maintain patch management program with defined timelines.

### Application

By mapping cybersecurity risks against People, Process, Policy, and Platform dimensions, each risk is assessed for its impact on CIA. Remediation actions are prioritized based on risk rating (Critical, High, Medium, Low) and tracked through a risk register with defined owners and timelines.

---

## 15. Asset Identification — Cooperative Bank

> **Q.** A Cooperative Bank operates with one Head Office and 150 Branch Offices, providing Core Banking Services along with multiple delivery channels such as Mobile Banking and Internet Banking. Identify the Information Assets, Software Assets, Physical Assets, and Service Assets required to support the bank's operations.

### 15.1 Information Assets

| # | Asset | Description |
| --- | --- | --- |
| 1 | Customer Database | Customer personal data, KYC documents, account details |
| 2 | Transaction Records | All financial transaction data (deposits, withdrawals, transfers, loans) |
| 3 | Core Banking Data | Ledger data, interest calculations, balance sheets, P&L records |
| 4 | Audit Logs and Trails | System logs, transaction logs, user activity logs |
| 5 | Policies and Procedures | Information Security Policy, IT policies, SOPs, operational manuals |
| 6 | Employee Records | HR data, payroll, staff credentials, background check records |
| 7 | Digital Banking Credentials | Mobile banking PINs, internet banking passwords, OTP records |
| 8 | Regulatory Reports | NRB reports, compliance records, audit reports |

### 15.2 Software Assets

| # | Asset | Description |
| --- | --- | --- |
| 1 | Core Banking System (CBS) | Primary banking application for all financial operations |
| 2 | Mobile Banking Application | Customer-facing mobile app for banking transactions |
| 3 | Internet Banking Portal | Web-based banking platform for customers |
| 4 | ATM/POS Software | Software for ATM and point-of-sale terminals |
| 5 | Database Management System | Oracle/SQL Server for core banking database |
| 6 | Operating Systems | Server OS (Windows Server/Linux) and desktop OS |
| 7 | Antivirus/Endpoint Protection | Endpoint security software across all branches |
| 8 | Email System | Corporate email server for internal and external communication |
| 9 | SIEM/Log Management | Security monitoring and log management platform |
| 10 | Backup Software | Automated backup solution for data protection |

### 15.3 Physical Assets

| # | Asset | Description |
| --- | --- | --- |
| 1 | Servers | Application servers, database servers, web servers at DC/DRC |
| 2 | Network Equipment | Routers, switches, firewalls, load balancers at HO and 150 branches |
| 3 | Storage Systems | SAN/NAS for data storage at DC and DRC |
| 4 | UPS and Power Systems | Uninterruptible power supply at DC, DRC, and branches |
| 5 | CCTV and Surveillance | Security cameras at HO, branches, DC, and DRC |
| 6 | Access Control Systems | Biometric/card-based access control at DC, DRC, vault areas |
| 7 | Workstations and Laptops | Desktop computers at HO and 150 branches |
| 8 | ATM Machines | Automated Teller Machines deployed across branch locations |
| 9 | Environmental Controls | Air conditioning, fire suppression, humidity sensors at DC/DRC |
| 10 | Cabling Infrastructure | Structured cabling (LAN cables, fiber optic) at all locations |

### 15.4 Service Assets

| # | Asset | Description |
| --- | --- | --- |
| 1 | Internet Connectivity (ISP) | Primary and redundant internet links for HO and all branches |
| 2 | WAN/MPLS Connectivity | Wide area network connecting HO and 150 branches |
| 3 | SMS Gateway Service | OTP delivery, transaction alerts, marketing messages |
| 4 | Payment Gateway Service | Integration with NPI/NCHL/SWIFT for fund transfers |
| 5 | Cloud DRC Service | Private cloud-based disaster recovery service (if applicable) |
| 6 | IT Support and Maintenance | AMC with hardware/software vendors for support |
| 7 | Security Operations (SOC) | Managed or in-house security monitoring service |
| 8 | Call Center Service | Customer support for mobile banking and internet banking |
