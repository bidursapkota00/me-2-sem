# ISA Exam Answers

---

## 1. 4P Framework for Cybersecurity Risk Identification and Mitigation [10]

> **Q.** As the Chief Compliance Officer of a leading organization, describe how you would leverage the 4P Framework to proactively identify and mitigate cybersecurity risks across the enterprise. [10]

As the Chief Compliance Officer, I would leverage the **4P Framework — People, Process, Policy, and Technology (Platform)** — to proactively identify and mitigate cybersecurity risks across the enterprise.

### 1.1 People

- Conduct cybersecurity awareness training for all employees at planned intervals (at least annually).
- Define information security roles and responsibilities — appoint CISO, security focal points per department.
- Implement background screening for employees handling sensitive information.
- Establish a security culture through phishing simulations, incident reporting awareness, and disciplinary procedures for policy violations.
- Ensure adequate staffing of skilled cybersecurity professionals (SOC analysts, incident responders).

### 1.2 Process

- Establish a formal Risk Assessment and Risk Treatment process aligned with ISO 27001:2022.
- Implement Incident Response Process — detection, containment, eradication, recovery, lessons learned.
- Define Change Management and Problem Management processes for IT systems.
- Conduct periodic Vulnerability Assessment and Penetration Testing (VAPT).
- Perform Business Impact Analysis (BIA) and maintain Business Continuity Plan (BCP) and Disaster Recovery Plan (DRP).
- Establish user access lifecycle management — provisioning, periodic review, de-provisioning.

### 1.3 Policy

- Develop and maintain an Information Security Policy approved by top management, reviewed annually.
- Create topic-specific policies: Acceptable Use Policy, Access Control Policy, Data Classification Policy, Backup Policy, Remote Access Policy, Password Policy, Incident Management Policy.
- Ensure policies align with regulatory requirements (Electronic Transactions Act 2008, Individual Privacy Act 2018, NRB IT Guidelines as applicable).
- Communicate policies to all personnel and obtain written acknowledgement.
- Establish compliance monitoring and audit mechanisms to verify policy adherence.

### 1.4 Platform (Technology)

- Deploy centralized Endpoint Detection and Response (EDR) and antivirus across all endpoints.
- Implement Multi-Factor Authentication (MFA) for all critical systems.
- Deploy a SIEM solution for centralized log management, correlation, and alerting.
- Implement network segmentation, firewall, IDS/IPS, and DLP solutions.
- Enforce encryption for data at rest and in transit.
- Implement Privileged Access Management (PAM) for administrative accounts.
- Maintain patch management program with defined timelines for applying security patches.

### Application of 4P Framework

By mapping identified cybersecurity risks against People, Process, Policy, and Platform dimensions, each risk is assessed for its impact on Confidentiality, Integrity, and Availability (CIA). Remediation actions are prioritized based on risk rating (Critical, High, Medium, Low) and tracked through a risk register with defined owners and timelines.

---

## 2. Risk Assessment of Information Assets of an Information Processing Facility [10]

> **Q.** You are hired as a Chief Risk Officer (CRO) of a company. Identify and list at least 5 Information assets of the Information Processing Facility. Perform the necessary and appropriate Risk Assessment of all the assets. [10]

As the Chief Risk Officer (CRO), I identify the following **5 Information Assets** of the Information Processing Facility and perform a Risk Assessment.

### 2.1 Identification of Information Assets

| #   | Asset                  | Category             | Description                                                          |
| --- | ---------------------- | -------------------- | -------------------------------------------------------------------- |
| 1   | Core Database Server   | Hardware/Information | Stores customer records, financial transactions, operational data    |
| 2   | Email System           | Software/Information | Corporate email server handling internal and external communications |
| 3   | Network Infrastructure | Hardware             | Routers, switches, firewalls, LAN/WAN connectivity                   |
| 4   | Backup Storage System  | Hardware/Information | Backup tapes/NAS/SAN storing copies of critical data                 |
| 5   | Web Application Server | Software/Information | Customer-facing portal/application server                            |

### 2.2 Risk Assessment

**Risk Assessment Methodology:** Each asset is evaluated based on CIA (Confidentiality, Integrity, Availability), Threat, Vulnerability, Existing Controls, Likelihood, Impact, and Risk Rating.

#### Asset 1: Core Database Server

| Parameter             | Assessment                                                                                                             |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Confidentiality**   | High — contains sensitive customer and financial data                                                                  |
| **Integrity**         | High — any unauthorized modification impacts business decisions                                                        |
| **Availability**      | High — downtime directly halts business operations                                                                     |
| **Threats**           | SQL injection, unauthorized access, ransomware, hardware failure, insider threat                                       |
| **Vulnerabilities**   | Unpatched database software, weak access controls, lack of encryption at rest                                          |
| **Existing Controls** | Antivirus installed, basic firewall, daily backup                                                                      |
| **Likelihood**        | High                                                                                                                   |
| **Impact**            | High — financial loss, regulatory penalty, reputational damage                                                         |
| **Risk Rating**       | **HIGH**                                                                                                               |
| **Recommendation**    | Implement database encryption, enforce strong access controls with PAM, regular patching, database activity monitoring |

#### Asset 2: Email System

| Parameter             | Assessment                                                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Confidentiality**   | High — emails contain sensitive business communications                                                                 |
| **Integrity**         | Medium — email spoofing and tampering possible                                                                          |
| **Availability**      | High — email disruption affects daily operations                                                                        |
| **Threats**           | Phishing attacks, email spoofing, malware via attachments, account compromise                                           |
| **Vulnerabilities**   | No MFA enabled, no advanced threat protection, weak password policy                                                     |
| **Existing Controls** | Basic spam filter, antivirus scanning                                                                                   |
| **Likelihood**        | High                                                                                                                    |
| **Impact**            | High — data breach, credential theft, business disruption                                                               |
| **Risk Rating**       | **HIGH**                                                                                                                |
| **Recommendation**    | Implement MFA, deploy advanced email security with sandboxing, enforce SPF/DKIM/DMARC, user phishing awareness training |

#### Asset 3: Network Infrastructure

| Parameter             | Assessment                                                                                                                                                      |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Confidentiality**   | Medium — network carries sensitive data in transit                                                                                                              |
| **Integrity**         | High — compromised network enables MITM attacks                                                                                                                 |
| **Availability**      | High — network outage halts all operations                                                                                                                      |
| **Threats**           | DDoS attacks, unauthorized access, MITM, misconfiguration                                                                                                       |
| **Vulnerabilities**   | Default credentials on devices, lack of network segmentation, outdated firmware                                                                                 |
| **Existing Controls** | Firewall deployed, basic ACLs                                                                                                                                   |
| **Likelihood**        | Medium                                                                                                                                                          |
| **Impact**            | High — complete operational disruption                                                                                                                          |
| **Risk Rating**       | **HIGH**                                                                                                                                                        |
| **Recommendation**    | Implement network segmentation, update firmware regularly, deploy IDS/IPS, enforce secure configuration baselines, conduct periodic network vulnerability scans |

#### Asset 4: Backup Storage System

| Parameter             | Assessment                                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Confidentiality**   | High — backup contains copies of all critical data                                                                              |
| **Integrity**         | High — corrupted backup renders recovery impossible                                                                             |
| **Availability**      | High — unavailable backup during disaster means data loss                                                                       |
| **Threats**           | Ransomware encrypting backups, physical theft, media degradation, unauthorized access                                           |
| **Vulnerabilities**   | Backups not encrypted, no off-site copy, restoration not tested regularly                                                       |
| **Existing Controls** | Daily backup schedule, on-site storage                                                                                          |
| **Likelihood**        | Medium                                                                                                                          |
| **Impact**            | High — permanent data loss, inability to recover from disaster                                                                  |
| **Risk Rating**       | **HIGH**                                                                                                                        |
| **Recommendation**    | Encrypt backups at rest and in transit, maintain off-site/cloud copies, conduct quarterly restoration tests, define RTO and RPO |

#### Asset 5: Web Application Server

| Parameter             | Assessment                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Confidentiality**   | High — processes customer data and credentials                                                                                                    |
| **Integrity**         | High — defacement or data manipulation affects trust                                                                                              |
| **Availability**      | High — downtime means revenue loss                                                                                                                |
| **Threats**           | Web application attacks (OWASP Top 10), DDoS, data breach, code injection                                                                         |
| **Vulnerabilities**   | No WAF deployed, no regular VAPT, outdated application framework                                                                                  |
| **Existing Controls** | SSL/TLS enabled, basic firewall                                                                                                                   |
| **Likelihood**        | High                                                                                                                                              |
| **Impact**            | High — financial loss, regulatory penalty, customer data exposure                                                                                 |
| **Risk Rating**       | **HIGH**                                                                                                                                          |
| **Recommendation**    | Deploy WAF, conduct regular VAPT (at least quarterly), implement secure SDLC, apply patches promptly, implement rate limiting and DDoS protection |

### 2.3 Risk Assessment Summary

| #   | Asset                  | C      | I      | A    | Risk Rating |
| --- | ---------------------- | ------ | ------ | ---- | ----------- |
| 1   | Core Database Server   | High   | High   | High | HIGH        |
| 2   | Email System           | High   | Medium | High | HIGH        |
| 3   | Network Infrastructure | Medium | High   | High | HIGH        |
| 4   | Backup Storage System  | High   | High   | High | HIGH        |
| 5   | Web Application Server | High   | High   | High | HIGH        |

All identified assets require immediate risk treatment through implementation of recommended controls, tracked via a Risk Register with assigned owners and remediation timelines.

---

## 3. IS Audit Report Based on ISO 27001:2022 (5 Controls) [10]

> **Q.** You have been appointed as an external Information System Auditor for a well-known organization with 100 sites, its own Data Center, and a Disaster Recovery Center. Your task is to conduct an IS Audit focusing on five controls of the ISO 27001:2022 Standard. Identify relevant audit metrics, compile a detailed IS Audit Report based on your findings, and provide recommendations to address the identified Information Security risks. [10]

### IS Audit Report

**Organization:** A well-known organization with 100 sites, own Data Center (DC) and Disaster Recovery Center (DRC)
**Audit Standard:** ISO 27001:2022
**Audit Type:** External Information System Audit

### Introduction

Information and Communication Technologies (ICT) play a vital role for the organization to enable its entire business process across its 100 sites, Data Center (DC), and Disaster Recovery Center (DRC). An IS Audit enables the organization to identify existing risks exposed from ICT services. This report presents the detailed activities conducted based on the Information Security Management Framework (ISO 27001:2022). It aids in preserving the Confidentiality, Integrity and Availability (CIA) of information by applying a risk management process and gives confidence to interested stakeholders that risks are adequately managed.

### Objective

To evaluate the effectiveness of the Information Security Management System (ISMS) by auditing 5 selected controls from ISO 27001:2022 Annex A, identify risks, and provide recommendations.

### Scope

The audit covers the organization's Head Office, Data Center, Disaster Recovery Center, and a sample of branch sites. The audit evaluates organizational, people, physical, and technological controls.

### Audit Metrics

- Number of non-conformities identified (Major/Minor)
- Percentage of controls compliant vs non-compliant
- Risk ratings per control (High, Medium, Low)
- Time since last policy review
- Percentage of employees who completed security awareness training
- Mean time to apply critical patches

---

### Control 1: Policies for Information Security (A.5.1) — Organizational Control

**Control:** Information security policy and topic-specific policies should be defined, approved by management, published, communicated to and acknowledged by relevant personnel, and reviewed at planned intervals.

**Purpose:** To ensure continuing suitability, adequacy, effectiveness of management direction and support for information security in accordance with business, legal, statutory, regulatory and contractual requirements.

**Observation:** The organization has an Information Security Policy (Version 1.0, 2022); however, it has not been reviewed or updated since initial release. No topic-specific policies (acceptable use, data classification, remote access) were formally documented. Staff awareness of the policy was limited at branch sites. No evidence of written acknowledgement by employees.

**Risk Rating:** HIGH

**Recommendation:** Review and update the Information Security Policy to align with ISO 27001:2022. Develop topic-specific policies. Communicate to all employees and obtain signed acknowledgement. Establish an annual review cycle with additional reviews triggered by significant organizational changes.

**Management Response:** The Information Security Policy shall be reviewed and updated within the next fiscal quarter. A working committee will be formed to draft topic-specific policies covering acceptable use, data classification, and remote access.

---

### Control 2: Information Security Awareness, Education and Training (A.6.3) — People Control

**Control:** Personnel should receive appropriate information security awareness, education and training and regular updates of the organization's information security policy and procedures.

**Purpose:** To ensure personnel and relevant interested parties are aware of and fulfill their information security responsibilities.

**Observation:** No structured information security awareness and training program exists. Employees across branch sites were unaware of basic cybersecurity practices (phishing identification, password management). No training records were available. Shared login credentials were observed at multiple sites.

**Risk Rating:** HIGH

**Recommendation:** Establish a comprehensive security awareness training program conducted annually. Cover phishing, social engineering, password hygiene, data handling, and incident reporting. Maintain training records. Conduct periodic simulated phishing exercises to measure effectiveness.

**Management Response:** A comprehensive information security awareness training program will be initiated in the upcoming quarter. Mandatory annual training sessions will be implemented for all employees, and records will be maintained by the HR department.

---

### Control 3: Physical Security Perimeters (A.7.1) — Physical Control

**Control:** Security perimeters should be defined and used to protect areas that contain information and other associated assets.

**Purpose:** To prevent unauthorized physical access, damage and interference to the organization's information and other associated assets.

**Observation:** The Data Center uses a basic key-lock mechanism without electronic access control (biometric/card-based). No visitor log is maintained. The DRC has shared access corridors without a dedicated security perimeter. CCTV retention is limited to 15 days. Branch offices have minimal physical security for IT equipment.

**Risk Rating:** HIGH

**Recommendation:** Implement electronic access control (biometric or smart card) for DC and DRC. Deploy a visitor management system with logging. Enhance CCTV with minimum 90-day retention. Establish a dedicated security perimeter for DRC. Define minimum physical security standards for all branch sites.

**Management Response:** Budget has been allocated for upgrading physical security measures. Electronic access control systems and enhanced CCTV coverage for the Data Center and Disaster Recovery Center will be deployed within six months.

---

### Control 4: Access Control (A.5.15) — Organizational Control

**Control:** Access to information and other associated assets should be restricted in accordance with the established topic-specific policy on access control.

**Purpose:** To ensure authorized access and to prevent unauthorized access to information and other associated assets.

**Observation:** No formal access control policy documented. User account provisioning and de-provisioning is unstructured — terminated employees' accounts remain active. Shared accounts observed in critical systems. Password policy is weak (6-character minimum, no complexity, no expiry). No MFA implemented. Privileged access uses shared admin credentials.

**Risk Rating:** HIGH

**Recommendation:** Develop and implement a formal access control policy. Establish user lifecycle management with HR integration. Eliminate shared accounts. Enforce 12-character passwords with complexity and rotation. Implement MFA for all critical systems. Deploy a PAM solution. Conduct quarterly user access reviews.

**Management Response:** An access control policy is currently being drafted. Stronger password policies will be enforced and shared accounts will be eliminated immediately. Implementation of PAM and MFA for critical systems is planned for the next fiscal year.

---

### Control 5: Information Backup (A.8.13) — Technological Control

**Control:** Backup copies of information, software and systems should be maintained and regularly tested in accordance with the agreed topic-specific policy on backup.

**Purpose:** To enable recovery of information and other associated assets following data loss or disruption.

**Observation:** Daily backups of critical databases are performed; however, no formal backup policy exists defining scope, frequency, retention, and recovery procedures. Off-site replication to DRC is weekly, creating a 7-day data loss window. Backup restoration tests have not been conducted in over 12 months. RTO and RPO are not formally defined. Backup encryption is not implemented.

**Risk Rating:** HIGH

**Recommendation:** Develop a formal backup policy defining RTO, RPO, frequency, and retention. Increase DRC replication to daily. Conduct quarterly backup restoration tests. Encrypt all backup data at rest and in transit. Integrate backup strategy with the BCP.

**Management Response:** The IT department will draft a formal backup policy defining RTO and RPO within three months. Backup infrastructure will be upgraded to support daily automated replication to the DRC and backup encryption will be implemented.

---

### Audit Findings

| #   | Control                           | ISO Ref | Risk Rating |
| --- | --------------------------------- | ------- | ----------- |
| 1   | Policies for Information Security | A.5.1   | HIGH        |
| 2   | Security Awareness and Training   | A.6.3   | HIGH        |
| 3   | Physical Security Perimeter       | A.7.1   | HIGH        |
| 4   | Access Control                    | A.5.15  | HIGH        |
| 5   | Information Backup                | A.8.13  | HIGH        |

### Audit Conclusions and Recommendations

The organization's information security posture requires significant improvement. Immediate priority should be given to implementing MFA, formalizing access controls, establishing a security awareness program, and strengthening backup and recovery mechanisms. A formal Risk Treatment Plan with defined owners and timelines should be established to track remediation of all identified gaps.

---

## 4. Information Security Policy Framework [10]

> **Q.** As the newly appointed Chief Information Security Officer (CISO) of an organization, design an Information Security Policy framework aimed at effectively mitigating Information Security risks to an acceptable level for the organization. [10]

As the newly appointed CISO, I would design the following Information Security Policy framework to mitigate information security risks to an acceptable level.

### 4.1 Policy Framework Structure

The framework follows a hierarchical structure:

**Level 1 — Overarching Information Security Policy**

- Defines the organization's commitment to information security.
- Approved by top management / Board of Directors.
- Aligned with ISO 27001:2022, business objectives, and applicable regulations.
- States the scope of the ISMS.
- Reviewed annually or upon significant organizational changes.

**Level 2 — Topic-Specific Policies**

- **Access Control Policy** — defines access provisioning, authentication requirements (MFA), RBAC, privileged access management, periodic access review.
- **Acceptable Use Policy** — governs acceptable use of IT assets, internet, email, removable media.
- **Data Classification and Handling Policy** — defines classification levels (Public, Internal, Confidential, Restricted) and handling procedures for each.
- **Backup and Recovery Policy** — defines RTO, RPO, backup frequency, retention, encryption, and restoration testing schedule.
- **Incident Management Policy** — defines incident categories, escalation matrix, response procedures, evidence preservation, and reporting requirements.
- **Password Policy** — minimum length (12 chars), complexity, rotation, prohibition of shared credentials.
- **Remote Access and Teleworking Policy** — VPN requirements, MFA, endpoint security for remote workers.
- **Change Management Policy** — formal approval, testing, documentation, and rollback procedures for system changes.
- **Physical and Environmental Security Policy** — access controls for DC/DRC, visitor management, CCTV, environmental monitoring.
- **Supplier and Third-Party Security Policy** — security requirements in supplier contracts, right to audit, data processing agreements.

**Level 3 — Procedures and Guidelines**

- Standard Operating Procedures (SOPs) for implementing each policy.
- Technical guidelines (e.g., server hardening guide, secure coding guidelines, network configuration standards).
- Checklists for audit, incident response, and business continuity.

### 4.2 Policy Development Process

- Conduct a Risk Assessment to identify information security risks and determine required controls.
- Map controls to ISO 27001:2022 Annex A (93 controls across 4 themes: Organizational, People, Physical, Technological).
- Draft policies with input from relevant stakeholders (IT, HR, Legal, Operations).
- Obtain top management approval for all policies.
- Communicate and distribute policies to all relevant personnel.
- Obtain written acknowledgement from all employees.

### 4.3 Policy Implementation and Enforcement

- Conduct security awareness training to ensure understanding of policies.
- Integrate policy compliance checks into regular IS Audits.
- Define disciplinary procedures for policy violations.
- Implement technical controls (DLP, MFA, endpoint protection) to enforce policy requirements.

### 4.4 Policy Review and Maintenance

- Review all policies at least annually.
- Trigger additional reviews upon significant changes (regulatory updates, major incidents, organizational restructuring).
- Maintain version control and document review history.
- Communicate updates to all relevant personnel.

### 4.5 Regulatory Alignment

- Electronic Transactions Act, 2063 (2008)
- Individual Privacy Act, 2075 (2018)
- NRB IT Guidelines / Sector-specific regulations (as applicable)
- ISO/IEC 27001:2022
- NIST Cybersecurity Framework

---

## 5. Tasks and Knowledge Areas of a Professional Information System Auditor [10]

> **Q.** To become a professional Information System Auditor, it is essential to possess a comprehensive understanding of the tasks and knowledge areas required for the role. Identify and elaborate on the critical tasks an Information System Auditor must perform and the key knowledge statements they must acquire to effectively audit, assess, and ensure the integrity, confidentiality, and availability of information systems. [10]

### 5.1 Critical Tasks of an IS Auditor

**Task 1: Planning the IS Audit**

- Define audit objectives, scope, and criteria based on standards (ISO 27001, COBIT, NIST).
- Develop the audit plan and audit program.
- Identify key stakeholders and audit resources.
- Conduct preliminary risk assessment to prioritize audit areas.

**Task 2: Executing the Audit**

- Gather audit evidence through documentation review, interviews, observation, and technical verification.
- Evaluate IT governance, management, and operational controls.
- Perform compliance testing (verify controls exist and are followed) and substantive testing (verify data accuracy and completeness).
- Use audit tools and techniques — CAATs (Computer Assisted Audit Techniques), sampling techniques, audit questionnaires.

**Task 3: Assessing IT Governance and Management**

- Evaluate IT governance structures (COBIT framework).
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
- Classify findings (Major Non-Conformity, Minor Non-Conformity, Opportunity for Improvement).
- Present findings to management and stakeholders.
- Track corrective action plans and verify implementation in follow-up audits.

### 5.2 Key Knowledge Statements

**KS 1: Information Systems Auditing Process**

- Knowledge of ISACA IS Audit Standards, Guidelines, and Code of Ethics.
- Understanding of ISO 27001, NIST CSF, COBIT, CIS Controls.
- Knowledge of regulatory requirements (Electronic Transactions Act, Privacy Act, sector-specific regulations).

**KS 2: Governance and Management of IT**

- Understanding of IT governance frameworks (COBIT 2019).
- Knowledge of IT strategy, policies, and organizational structures.
- Understanding of IT risk management processes and risk assessment methodologies.

**KS 3: Information Systems Acquisition, Development and Implementation**

- Knowledge of SDLC and Secure SDLC (SecSDLC).
- Understanding of change management and configuration management.
- Knowledge of project management practices for IT projects.

**KS 4: Information Systems Operations and Business Resilience**

- Knowledge of IT service management (incident, problem, change management).
- Understanding of BCP, DRP, and Business Impact Analysis.
- Knowledge of backup and recovery strategies, RTO, RPO.
- Understanding of data center operations and environmental controls.

**KS 5: Protection of Information Assets**

- Knowledge of access control models, authentication mechanisms, encryption.
- Understanding of network security (firewalls, IDS/IPS, VPN, segmentation).
- Knowledge of vulnerability assessment and penetration testing (VAPT).
- Understanding of security monitoring, logging, and SIEM.
- Knowledge of data classification, data privacy, and data protection principles.

---

## 6. Importance of IS Audit with Example [10]

> **Q.** Discuss the importance of conducting an Information System Audit within an organization, and illustrate its impact with a suitable example. [10]

### 6.1 Importance of Information System Audit

**Identifying Security Risks and Vulnerabilities**
IS Audit identifies gaps in the organization's information security controls — unpatched systems, weak access controls, inadequate backup procedures — enabling proactive risk mitigation before exploitation by threat actors.

**Ensuring Regulatory Compliance**
Organizations are subject to legal and regulatory requirements (Electronic Transactions Act 2008, Individual Privacy Act 2018, NRB IT Guidelines, sector-specific regulations). IS Audit verifies compliance and helps avoid legal penalties and sanctions.

**Protecting CIA Triad**
IS Audit evaluates whether controls adequately preserve the Confidentiality, Integrity, and Availability of information assets, which are fundamental to business operations and stakeholder trust.

**Improving IT Governance**
IS Audit assesses whether IT governance structures align IT strategy with business objectives, ensuring efficient use of IT resources and effective risk management through frameworks like COBIT and ISO 27001.

**Evaluating Business Continuity Readiness**
IS Audit reviews the adequacy of BCP, DRP, and incident response plans, ensuring the organization can recover from disruptions within acceptable timeframes (RTO/RPO).

**Building Stakeholder Confidence**
Audit findings and assurance reports provide confidence to the Board, management, customers, regulators, and other stakeholders that information security risks are adequately managed.

**Driving Continuous Improvement**
IS Audit provides recommendations and tracks corrective actions, fostering a culture of continuous improvement in information security practices.

### 6.2 Example: IS Audit of Yeti Airlines Pvt. Ltd.

Yeti Airlines Pvt. Ltd., a domestic airline operating across multiple sites in Nepal, underwent an IS Audit based on ISO 27001:2022. The audit evaluated **10 controls** across all 4 themes. The scope covered Head Office, Data Center (DC), Disaster Recovery Center (DRC), and branch sites.

#### A.1. Organizational Controls

**A.5.1 — Policies for Information Security**
Information Security Policy (v1.0, 2021) exists but has not been reviewed or updated since release. No topic-specific policies (acceptable use, data classification, remote access) documented. Staff awareness limited at branch sites; no written acknowledgement obtained. **Risk: HIGH.**

**A.5.2 — Information Security Roles and Responsibilities**
No designated CISO or equivalent; IT Manager handles security in an ad-hoc manner with no clear role delineation. No security focal points at branch offices. No formal escalation matrix for security incidents. **Risk: HIGH.**

#### A.2. People Controls

**A.6.3 — Information Security Awareness, Education and Training**
No structured cybersecurity awareness or training program. Staff unaware of phishing identification, password management. No training records available. Shared login credentials observed at multiple stations. **Risk: HIGH.**

#### A.3. Physical Controls

**A.7.1 — Physical Security Perimeters**
DC uses basic key-lock mechanism; no electronic access control (biometric/card). No visitor log maintained. DRC has shared access corridors without a dedicated security perimeter. CCTV retention only 15 days. **Risk: HIGH.**

**A.7.3 — Securing Offices, Rooms and Facilities**
Server room lacks environmental monitoring sensors (temperature, humidity, water leak). Fire suppression relies on standard extinguishers, not gas-based system. UPS capacity and maintenance records unavailable. DRC has no diesel generator backup. **Risk: MEDIUM.**

#### A.4. Technological Controls

**A.8.2 — Privileged Access Rights**
No formal access control policy. Terminated employees' accounts remain active. Shared accounts in booking system. Password policy: 6-char minimum, no complexity, no expiry. No MFA. Shared admin/root credentials for privileged access. **Risk: HIGH.**

**A.8.7 — Protection Against Malware**
Antivirus deployed but not centrally managed. Several branch workstations running outdated definitions (30+ days). No EDR. USB restrictions not enforced. No advanced email threat protection or sandboxing. **Risk: MEDIUM.**

**A.8.8 — Management of Technical Vulnerabilities**
No formal vulnerability management program. No periodic VAPT conducted. Customer-facing booking portal never security-assessed. Patch management is ad-hoc; servers running outdated OS with known vulnerabilities. No software inventory maintained. **Risk: HIGH.**

**A.8.13 — Information Backup**
Daily backups performed but no formal backup policy. Off-site DRC replication only weekly (7-day data loss window). Restoration not tested in 12+ months. RTO/RPO not defined. Backup encryption not implemented. **Risk: HIGH.**

**A.8.15 — Logging**
No centralized log management or SIEM. Log retention inconsistent (7–30 days). Logs reviewed only reactively. Admin activities not separately logged. No alerting for failed logins, privilege escalation, or after-hours access. Logs not tamper-protected. **Risk: HIGH.**

#### Summary of Findings

| #   | Control                                 | ISO Ref | Theme          | Risk   |
| --- | --------------------------------------- | ------- | -------------- | ------ |
| 1   | Policies for Information Security       | A.5.1   | Organizational | HIGH   |
| 2   | IS Roles and Responsibilities           | A.5.2   | Organizational | HIGH   |
| 3   | Security Awareness and Training         | A.6.3   | People         | HIGH   |
| 4   | Physical Security Perimeters            | A.7.1   | Physical       | HIGH   |
| 5   | Securing Offices, Rooms and Facilities  | A.7.3   | Physical       | MEDIUM |
| 6   | Privileged Access Rights                | A.8.2   | Technological  | HIGH   |
| 7   | Protection Against Malware              | A.8.7   | Technological  | MEDIUM |
| 8   | Management of Technical Vulnerabilities | A.8.8   | Technological  | HIGH   |
| 9   | Information Backup                      | A.8.13  | Technological  | HIGH   |
| 10  | Logging                                 | A.8.15  | Technological  | HIGH   |

**Overall:** 8 out of 10 controls rated HIGH risk, 2 rated MEDIUM.

#### Impact of IS Audit

The audit exposed critical gaps across all domains — lack of formal policies, absent access controls, no VAPT, untested backups, and no centralized logging. Based on recommendations, Yeti Airlines initiated:

- Appointment of a dedicated Information Security Manager.
- Implementation of MFA and elimination of shared accounts.
- Engagement of a third-party firm for VAPT of booking portal.
- Upgrade of DC/DRC physical security with biometric access controls.
- Development of a formal backup policy with defined RTO/RPO and daily DRC replication.
- Acquisition of a centralized SIEM solution.

This demonstrates that IS Audit serves as a critical mechanism for identifying and addressing information security weaknesses that could otherwise lead to significant financial, operational, and reputational damage.

---

## 7. Information Security Self-Assessment (ISO/IEC 27001:2022) [10]

> **Q.** Consider a scenario where your organization operates a network of over 100 sites, supported by an in-house Data Center (DC) and a private cloud-based Disaster Recovery Center (DRC). The organization is planning to undertake an Information Security Self-Assessment to evaluate its current security posture, in alignment with ISO/IEC 27001:2022, focusing on the 93 Annex A controls. [10]

### Information Security Self-Assessment Report

**Organization:** An organization with 100+ sites, in-house DC, private cloud-based DRC
**Standard:** ISO/IEC 27001:2022
**Assessment Focus:** 93 Annex A Controls (4 Themes)

### 1. Introduction

This Information Security Self-Assessment evaluates the organization's current security posture against the 93 Annex A controls of ISO/IEC 27001:2022. The assessment systematically reviews existing security measures, identifies potential risks or gaps, and supports continuous improvement of the ISMS.

### 2. Objective

- Evaluate the implementation status of the 93 Annex A controls across 4 themes.
- Identify gaps between current security posture and ISO/IEC 27001:2022 requirements.
- Assess risk levels for each identified gap.
- Provide a roadmap for continuous improvement of the ISMS.

### 3. Scope

The assessment covers all 100+ sites, the in-house Data Center (DC), and the private cloud-based Disaster Recovery Center (DRC), including all information assets, personnel, processes, and technology infrastructure.

### 4. Methodology

- Review of the Statement of Applicability (SoA) to determine applicability of each of the 93 controls.
- Documentation review — policies, procedures, records, and evidence.
- Interviews with process owners and key personnel.
- Technical verification — system configurations, access logs, vulnerability reports.
- Rate each control as: Fully Implemented, Partially Implemented, Not Implemented, or Not Applicable.

### 5. Self-Assessment of Annex A Controls (93 Controls, 4 Themes)

#### Theme A.5 — Organizational Controls (37 controls)

| #   | Control                                                                | Ref    | Status                | Gap Identified                                                                 | Risk   |
| --- | ---------------------------------------------------------------------- | ------ | --------------------- | ------------------------------------------------------------------------------ | ------ |
| 1   | Policies for Information Security                                      | A.5.1  | Partially Implemented | Policy exists but not reviewed since creation; no topic-specific policies      | HIGH   |
| 2   | Information Security Roles and Responsibilities                        | A.5.2  | Partially Implemented | No dedicated CISO; roles not formally assigned at branch sites                 | HIGH   |
| 3   | Segregation of Duties                                                  | A.5.3  | Not Implemented       | No formal segregation of conflicting duties in IT operations                   | MEDIUM |
| 4   | Management Responsibilities                                            | A.5.4  | Partially Implemented | Management commitment exists but not formally documented                       | MEDIUM |
| 5   | Contact with Authorities                                               | A.5.5  | Partially Implemented | No formal procedure for contacting regulatory authorities during incidents     | LOW    |
| 6   | Contact with Special Interest Groups                                   | A.5.6  | Not Implemented       | No membership in security forums or threat intelligence sharing groups         | LOW    |
| 7   | Threat Intelligence                                                    | A.5.7  | Not Implemented       | No threat intelligence feeds or analysis capability                            | HIGH   |
| 8   | Information Security in Project Management                             | A.5.8  | Not Implemented       | Security requirements not integrated into project lifecycle                    | MEDIUM |
| 9   | Inventory of Information and Other Associated Assets                   | A.5.9  | Partially Implemented | Asset register exists but incomplete; no classification applied                | HIGH   |
| 10  | Acceptable Use of Information and Other Associated Assets              | A.5.10 | Not Implemented       | No acceptable use policy documented                                            | MEDIUM |
| 11  | Return of Assets                                                       | A.5.11 | Partially Implemented | No formal process for asset return upon termination                            | MEDIUM |
| 12  | Classification of Information                                          | A.5.12 | Not Implemented       | No data classification scheme defined                                          | HIGH   |
| 13  | Labelling of Information                                               | A.5.13 | Not Implemented       | No labelling procedures for classified information                             | MEDIUM |
| 14  | Information Transfer                                                   | A.5.14 | Partially Implemented | Encryption used for some transfers; no formal transfer policy                  | MEDIUM |
| 15  | Access Control                                                         | A.5.15 | Partially Implemented | No formal access control policy; weak password policy; no MFA                  | HIGH   |
| 16  | Identity Management                                                    | A.5.16 | Partially Implemented | User accounts managed but no centralized identity management                   | MEDIUM |
| 17  | Authentication Information                                             | A.5.17 | Partially Implemented | Passwords used but weak policy; no MFA                                         | HIGH   |
| 18  | Access Rights                                                          | A.5.18 | Partially Implemented | No periodic access review; terminated users not promptly disabled              | HIGH   |
| 19  | Information Security in Supplier Relationships                         | A.5.19 | Not Implemented       | No security clauses in supplier contracts                                      | HIGH   |
| 20  | Addressing Information Security Within Supplier Agreements             | A.5.20 | Not Implemented       | No formal supplier security requirements                                       | HIGH   |
| 21  | Managing Information Security in the ICT Supply Chain                  | A.5.21 | Not Implemented       | No ICT supply chain risk management                                            | MEDIUM |
| 22  | Monitoring, Review and Change Management of Supplier Services          | A.5.22 | Not Implemented       | No periodic review of supplier security compliance                             | MEDIUM |
| 23  | Information Security for Use of Cloud Services                         | A.5.23 | Partially Implemented | DRC on private cloud but no formal cloud security policy                       | HIGH   |
| 24  | Information Security Incident Management Planning and Preparation      | A.5.24 | Partially Implemented | Basic incident handling exists; no formal incident response plan               | HIGH   |
| 25  | Assessment and Decision on Information Security Events                 | A.5.25 | Not Implemented       | No criteria defined for classifying security events                            | MEDIUM |
| 26  | Response to Information Security Incidents                             | A.5.26 | Partially Implemented | Ad-hoc response; no documented response procedures                             | HIGH   |
| 27  | Learning from Information Security Incidents                           | A.5.27 | Not Implemented       | No post-incident review process                                                | MEDIUM |
| 28  | Collection of Evidence                                                 | A.5.28 | Not Implemented       | No evidence collection procedures for digital forensics                        | MEDIUM |
| 29  | Information Security During Disruption                                 | A.5.29 | Partially Implemented | Basic DR exists via DRC; no formal BCP                                         | HIGH   |
| 30  | ICT Readiness for Business Continuity                                  | A.5.30 | Partially Implemented | DRC operational but ICT readiness not tested; RTO/RPO not defined              | HIGH   |
| 31  | Legal, Statutory, Regulatory and Contractual Requirements              | A.5.31 | Partially Implemented | Some awareness of ETA 2008 and Privacy Act 2018; no formal compliance register | MEDIUM |
| 32  | Intellectual Property Rights                                           | A.5.32 | Partially Implemented | Software licensing tracked but not comprehensive                               | LOW    |
| 33  | Protection of Records                                                  | A.5.33 | Partially Implemented | Records maintained but no formal retention and disposal policy                 | MEDIUM |
| 34  | Privacy and Protection of PII                                          | A.5.34 | Partially Implemented | Basic PII handling but not aligned with Privacy Act 2018                       | HIGH   |
| 35  | Independent Review of Information Security                             | A.5.35 | Not Implemented       | No independent review or audit conducted previously                            | HIGH   |
| 36  | Compliance with Policies, Rules and Standards for Information Security | A.5.36 | Not Implemented       | No compliance monitoring mechanism                                             | MEDIUM |
| 37  | Documented Operating Procedures                                        | A.5.37 | Partially Implemented | Some SOPs exist but not comprehensive                                          | MEDIUM |

#### Theme A.6 — People Controls (8 controls)

| #   | Control                                                    | Ref   | Status                | Gap Identified                                                                             | Risk   |
| --- | ---------------------------------------------------------- | ----- | --------------------- | ------------------------------------------------------------------------------------------ | ------ |
| 1   | Screening                                                  | A.6.1 | Partially Implemented | Background checks performed for senior roles only; not for all employees                   | MEDIUM |
| 2   | Terms and Conditions of Employment                         | A.6.2 | Partially Implemented | Employment contracts include basic confidentiality clause; no detailed IS responsibilities | MEDIUM |
| 3   | Information Security Awareness, Education and Training     | A.6.3 | Not Implemented       | No structured awareness or training program; no records                                    | HIGH   |
| 4   | Disciplinary Process                                       | A.6.4 | Partially Implemented | General disciplinary process exists; no IS-specific disciplinary procedure                 | MEDIUM |
| 5   | Responsibilities After Termination or Change of Employment | A.6.5 | Partially Implemented | No formal process for revoking access and returning assets upon termination                | HIGH   |
| 6   | Confidentiality or Non-Disclosure Agreements               | A.6.6 | Partially Implemented | NDAs signed for some roles; not standardized                                               | MEDIUM |
| 7   | Remote Working                                             | A.6.7 | Partially Implemented | VPN used but no remote working security policy; no endpoint security enforcement           | HIGH   |
| 8   | Information Security Event Reporting                       | A.6.8 | Not Implemented       | No mechanism for employees to report security events                                       | HIGH   |

#### Theme A.7 — Physical Controls (14 controls)

| #   | Control                                               | Ref    | Status                | Gap Identified                                                                     | Risk   |
| --- | ----------------------------------------------------- | ------ | --------------------- | ---------------------------------------------------------------------------------- | ------ |
| 1   | Physical Security Perimeters                          | A.7.1  | Partially Implemented | DC has basic lock; no biometric/card access; DRC lacks dedicated perimeter         | HIGH   |
| 2   | Physical Entry                                        | A.7.2  | Partially Implemented | No visitor management system; no electronic entry logs                             | HIGH   |
| 3   | Securing Offices, Rooms and Facilities                | A.7.3  | Partially Implemented | No environmental monitoring; no gas-based fire suppression in server room          | MEDIUM |
| 4   | Physical Security Monitoring                          | A.7.4  | Partially Implemented | CCTV exists but retention only 15 days; no 24/7 monitoring                         | MEDIUM |
| 5   | Protecting Against Physical and Environmental Threats | A.7.5  | Partially Implemented | Basic fire extinguishers; no flood/water leak detection; no seismic considerations | MEDIUM |
| 6   | Working in Secure Areas                               | A.7.6  | Not Implemented       | No specific procedures for working in secure areas (DC/DRC)                        | MEDIUM |
| 7   | Clear Desk and Clear Screen                           | A.7.7  | Not Implemented       | No clear desk/screen policy enforced                                               | LOW    |
| 8   | Equipment Siting and Protection                       | A.7.8  | Partially Implemented | Equipment in DC properly sited; branch sites lack proper siting                    | MEDIUM |
| 9   | Security of Assets Off-Premises                       | A.7.9  | Not Implemented       | No policy for off-premises asset security (laptops, mobile devices)                | HIGH   |
| 10  | Storage Media                                         | A.7.10 | Partially Implemented | No formal media handling or disposal procedures                                    | MEDIUM |
| 11  | Supporting Utilities                                  | A.7.11 | Partially Implemented | UPS at DC; DRC lacks generator backup                                              | HIGH   |
| 12  | Cabling Security                                      | A.7.12 | Partially Implemented | Raised floor in DC but poor cable management                                       | LOW    |
| 13  | Equipment Maintenance                                 | A.7.13 | Partially Implemented | Maintenance performed but records not systematically maintained                    | MEDIUM |
| 14  | Secure Disposal or Re-Use of Equipment                | A.7.14 | Not Implemented       | No formal secure disposal or data wiping procedures                                | HIGH   |

#### Theme A.8 — Technological Controls (34 controls)

| #   | Control                                                     | Ref    | Status                | Gap Identified                                                            | Risk   |
| --- | ----------------------------------------------------------- | ------ | --------------------- | ------------------------------------------------------------------------- | ------ |
| 1   | User Endpoint Devices                                       | A.8.1  | Partially Implemented | Antivirus on most; no centralized endpoint management; no MDM             | HIGH   |
| 2   | Privileged Access Rights                                    | A.8.2  | Not Implemented       | Shared admin credentials; no PAM; no privilege monitoring                 | HIGH   |
| 3   | Information Access Restriction                              | A.8.3  | Partially Implemented | Basic file permissions; no DLP; no granular access controls               | MEDIUM |
| 4   | Access to Source Code                                       | A.8.4  | Partially Implemented | Source code in repository; no formal access restriction policy            | MEDIUM |
| 5   | Secure Authentication                                       | A.8.5  | Partially Implemented | Password-based only; no MFA; weak password policy                         | HIGH   |
| 6   | Capacity Management                                         | A.8.6  | Partially Implemented | Basic monitoring; no proactive capacity planning                          | MEDIUM |
| 7   | Protection Against Malware                                  | A.8.7  | Partially Implemented | Antivirus not centrally managed; outdated definitions at branches; no EDR | MEDIUM |
| 8   | Management of Technical Vulnerabilities                     | A.8.8  | Not Implemented       | No VAPT; ad-hoc patching; no vulnerability tracking                       | HIGH   |
| 9   | Configuration Management                                    | A.8.9  | Not Implemented       | No standardized configuration baselines                                   | HIGH   |
| 10  | Information Deletion                                        | A.8.10 | Not Implemented       | No formal data deletion or sanitization procedures                        | MEDIUM |
| 11  | Data Masking                                                | A.8.11 | Not Implemented       | No data masking applied in non-production environments                    | MEDIUM |
| 12  | Data Leakage Prevention                                     | A.8.12 | Not Implemented       | No DLP solution deployed                                                  | HIGH   |
| 13  | Information Backup                                          | A.8.13 | Partially Implemented | Daily backup but no policy; weekly off-site; no restoration testing       | HIGH   |
| 14  | Redundancy of Information Processing Facilities             | A.8.14 | Partially Implemented | DRC exists but failover not tested; no defined RTO/RPO                    | HIGH   |
| 15  | Logging                                                     | A.8.15 | Partially Implemented | Logs generated but no SIEM; inconsistent retention; no alerting           | HIGH   |
| 16  | Monitoring Activities                                       | A.8.16 | Not Implemented       | No real-time security monitoring or SOC capability                        | HIGH   |
| 17  | Clock Synchronization                                       | A.8.17 | Partially Implemented | NTP configured on some servers; not standardized across all systems       | LOW    |
| 18  | Use of Privileged Utility Programs                          | A.8.18 | Not Implemented       | No restrictions on use of privileged utilities                            | MEDIUM |
| 19  | Installation of Software on Operational Systems             | A.8.19 | Not Implemented       | No software installation policy; users can install arbitrary software     | MEDIUM |
| 20  | Networks Security                                           | A.8.20 | Partially Implemented | Firewall deployed; no IDS/IPS; limited network segmentation               | HIGH   |
| 21  | Security of Network Services                                | A.8.21 | Partially Implemented | ISP SLAs exist; no security-specific service level requirements           | MEDIUM |
| 22  | Segregation of Networks                                     | A.8.22 | Not Implemented       | Flat network; no segmentation between business units or DC zones          | HIGH   |
| 23  | Web Filtering                                               | A.8.23 | Partially Implemented | Basic URL filtering; no advanced web security gateway                     | MEDIUM |
| 24  | Use of Cryptography                                         | A.8.24 | Partially Implemented | SSL/TLS on web; no encryption at rest; no crypto key management           | HIGH   |
| 25  | Secure Development Life Cycle                               | A.8.25 | Not Implemented       | No secure SDLC process; no code review or security testing                | HIGH   |
| 26  | Application Security Requirements                           | A.8.26 | Not Implemented       | Security requirements not defined in application specifications           | HIGH   |
| 27  | Secure System Architecture and Engineering Principles       | A.8.27 | Not Implemented       | No documented secure architecture principles                              | MEDIUM |
| 28  | Secure Coding                                               | A.8.28 | Not Implemented       | No secure coding standards or guidelines                                  | HIGH   |
| 29  | Security Testing in Development and Acceptance              | A.8.29 | Not Implemented       | No security testing before deployment                                     | HIGH   |
| 30  | Outsourced Development                                      | A.8.30 | Not Implemented       | No security requirements for outsourced development                       | MEDIUM |
| 31  | Separation of Development, Test and Production Environments | A.8.31 | Partially Implemented | Separate environments exist but access controls between them are weak     | MEDIUM |
| 32  | Change Management                                           | A.8.32 | Partially Implemented | Ad-hoc change process; no formal CAB or approval workflow                 | HIGH   |
| 33  | Test Information                                            | A.8.33 | Not Implemented       | Production data used in testing without masking                           | HIGH   |
| 34  | Protection of Information Systems During Audit Testing      | A.8.34 | Not Implemented       | No safeguards for audit testing activities                                | LOW    |

### 6. Self-Assessment Summary

| Theme                | Total Controls | Fully Implemented | Partially Implemented | Not Implemented | Not Applicable |
| -------------------- | -------------- | ----------------- | --------------------- | --------------- | -------------- |
| A.5 — Organizational | 37             | 0                 | 24                    | 13              | 0              |
| A.6 — People         | 8              | 0                 | 5                     | 3               | 0              |
| A.7 — Physical       | 14             | 0                 | 9                     | 5               | 0              |
| A.8 — Technological  | 34             | 0                 | 16                    | 18              | 0              |
| **Total**            | **93**         | **0**             | **54**                | **39**          | **0**          |

### 7. Risk Summary

| Risk Level | Count |
| ---------- | ----- |
| HIGH       | 42    |
| MEDIUM     | 38    |
| LOW        | 13    |

### 8. Recommendations

**Immediate Priority**

- Appoint a dedicated CISO and define IS roles across all sites.
- Develop and approve an Information Security Policy with topic-specific policies.
- Implement MFA for all critical systems and eliminate shared accounts.
- Deploy centralized SIEM for log management and monitoring.
- Establish a formal vulnerability management and patch management program.

**Short-Term (3–6 Months)**

- Implement electronic access controls (biometric/card) at DC and DRC.
- Develop BCP and define RTO/RPO; test DR failover quarterly.
- Establish security awareness training program for all personnel.
- Implement DLP, EDR, and network segmentation.
- Develop supplier security requirements and include in contracts.

**Medium-Term (6–12 Months)**

- Implement secure SDLC and application security testing.
- Deploy encryption at rest for sensitive data stores.
- Establish threat intelligence capability.
- Conduct annual independent review of the ISMS.
- Achieve full compliance with all 93 Annex A controls as applicable per SoA.

---

## 8. Cybersecurity Maturity Assessment — NIST CSF v1.1 [10]

> **Q.** A well-established multinational organization operating across more than 300 locations, supported by a centralized DC and DRC, plans to undertake a Cybersecurity Maturity Assessment aligned with the NIST Cybersecurity Framework (CSF) v1.1. Evaluate the organization's current cybersecurity posture across the five core functions—Identify, Protect, Detect, Respond, and Recover—and document the maturity level, gaps, and improvement opportunities. [10]

### <<Organization>> Cyber Security Assessment

### NIST Cyber Security Framework Version 1.1

### Cybersecurity Maturity Assessment Report

**Organization:** A multinational organization with 300+ locations, centralized DC and DRC
**Framework:** NIST Cybersecurity Framework (CSF) Version 1.1
**Assessment Scope:** All 5 core functions, 23 categories, selected subcategories

### 1. Introduction

This Cybersecurity Maturity Assessment evaluates the organization's cybersecurity posture against the NIST Cybersecurity Framework v1.1. The assessment maps current practices to the five core functions and uses the NIST Implementation Tiers to determine maturity.

### 2. NIST CSF v1.1 Implementation Tiers (Maturity Levels)

| Tier   | Name          | Description                                                                            |
| ------ | ------------- | -------------------------------------------------------------------------------------- |
| Tier 1 | Partial       | Risk management is ad-hoc and reactive; not formalized                                 |
| Tier 2 | Risk Informed | Risk management approved by management but not organization-wide                       |
| Tier 3 | Repeatable    | Policies and procedures formally approved and implemented organization-wide            |
| Tier 4 | Adaptive      | Practices are continuously improved based on lessons learned and predictive indicators |

### 3. Assessment by Core Function

#### Function 1: IDENTIFY (ID)

| Category                             | Subcategory | Description                                                                                                | Current Tier | Gap                                                                                 | Target Tier |
| ------------------------------------ | ----------- | ---------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------------------------- | ----------- |
| Asset Management (ID.AM)             | ID.AM-1     | Physical devices and systems are inventoried                                                               | Tier 2       | Asset inventory exists but incomplete across all 300+ sites; no automated discovery | Tier 3      |
| Asset Management (ID.AM)             | ID.AM-2     | Software platforms and applications are inventoried                                                        | Tier 1       | No centralized software inventory; no license tracking system                       | Tier 3      |
| Business Environment (ID.BE)         | ID.BE-3     | Priorities for organizational mission, objectives, and activities are established and communicated         | Tier 2       | Business priorities defined at HQ; not cascaded to all locations                    | Tier 3      |
| Governance (ID.GV)                   | ID.GV-1     | Organizational cybersecurity policy is established and communicated                                        | Tier 2       | Policy exists but outdated; not communicated to all 300+ sites                      | Tier 3      |
| Risk Assessment (ID.RA)              | ID.RA-1     | Asset vulnerabilities are identified and documented                                                        | Tier 1       | No formal vulnerability assessment or scanning program                              | Tier 3      |
| Risk Management Strategy (ID.RM)     | ID.RM-1     | Risk management processes are established, managed, and agreed to by organizational stakeholders           | Tier 2       | Risk register exists at HQ; not extended to branch operations                       | Tier 3      |
| Supply Chain Risk Management (ID.SC) | ID.SC-1     | Cyber supply chain risk management processes are identified, established, assessed, managed, and agreed to | Tier 1       | No supply chain risk management program                                             | Tier 3      |

**Function Maturity: Tier 1–2 (Partial to Risk Informed)**

#### Function 2: PROTECT (PR)

| Category                                                | Subcategory | Description                                                                                                                 | Current Tier | Gap                                                                                   | Target Tier |
| ------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------- | ----------- |
| Identity Management and Access Control (PR.AC)          | PR.AC-1     | Identities and credentials are issued, managed, verified, revoked, and audited for authorized devices, users and processes  | Tier 2       | User lifecycle management exists but inconsistent; no MFA; no periodic access reviews | Tier 3      |
| Identity Management and Access Control (PR.AC)          | PR.AC-4     | Access permissions and authorizations are managed, incorporating the principles of least privilege and separation of duties | Tier 1       | Shared admin credentials; no RBAC; no PAM                                             | Tier 3      |
| Awareness and Training (PR.AT)                          | PR.AT-1     | All users are informed and trained                                                                                          | Tier 1       | No structured cybersecurity training program; no training records                     | Tier 3      |
| Data Security (PR.DS)                                   | PR.DS-1     | Data-at-rest is protected                                                                                                   | Tier 1       | No encryption at rest for sensitive data; backups unencrypted                         | Tier 3      |
| Data Security (PR.DS)                                   | PR.DS-2     | Data-in-transit is protected                                                                                                | Tier 2       | SSL/TLS used for web; internal traffic largely unencrypted                            | Tier 3      |
| Information Protection Processes and Procedures (PR.IP) | PR.IP-4     | Backups of information are conducted, maintained, and tested                                                                | Tier 2       | Daily backups exist; no restoration testing; no defined RTO/RPO                       | Tier 3      |
| Protective Technology (PR.PT)                           | PR.PT-1     | Audit/log records are determined, documented, implemented, and reviewed                                                     | Tier 1       | Logs generated but not centralized; no review process; no SIEM                        | Tier 3      |

**Function Maturity: Tier 1–2 (Partial to Risk Informed)**

#### Function 3: DETECT (DE)

| Category                               | Subcategory | Description                                                                         | Current Tier | Gap                                                  | Target Tier |
| -------------------------------------- | ----------- | ----------------------------------------------------------------------------------- | ------------ | ---------------------------------------------------- | ----------- |
| Anomalies and Events (DE.AE)           | DE.AE-1     | A baseline of network operations and expected data flows is established and managed | Tier 1       | No network baseline defined; no anomaly detection    | Tier 3      |
| Security Continuous Monitoring (DE.CM) | DE.CM-1     | The network is monitored to detect potential cybersecurity events                   | Tier 1       | No real-time network monitoring; no IDS/IPS          | Tier 3      |
| Security Continuous Monitoring (DE.CM) | DE.CM-4     | Malicious code is detected                                                          | Tier 2       | Antivirus deployed but not centrally managed; no EDR | Tier 3      |
| Detection Processes (DE.DP)            | DE.DP-1     | Roles and responsibilities for detection are well defined                           | Tier 1       | No SOC; detection responsibilities not assigned      | Tier 3      |

**Function Maturity: Tier 1 (Partial)**

#### Function 4: RESPOND (RS)

| Category                  | Subcategory | Description                                                                  | Current Tier | Gap                                                                 | Target Tier |
| ------------------------- | ----------- | ---------------------------------------------------------------------------- | ------------ | ------------------------------------------------------------------- | ----------- |
| Response Planning (RS.RP) | RS.RP-1     | Response plan is executed during or after an incident                        | Tier 1       | No formal incident response plan; ad-hoc response                   | Tier 3      |
| Communications (RS.CO)    | RS.CO-1     | Personnel know their roles and order of operations when a response is needed | Tier 1       | No escalation matrix; no communication plan for incidents           | Tier 3      |
| Analysis (RS.AN)          | RS.AN-1     | Notifications from detection systems are investigated                        | Tier 1       | No detection systems generating alerts; reactive investigation only | Tier 3      |
| Mitigation (RS.MI)        | RS.MI-1     | Incidents are contained                                                      | Tier 1       | No documented containment procedures                                | Tier 3      |
| Improvements (RS.IM)      | RS.IM-1     | Response plans incorporate lessons learned                                   | Tier 1       | No post-incident review process                                     | Tier 3      |

**Function Maturity: Tier 1 (Partial)**

#### Function 5: RECOVER (RC)

| Category                  | Subcategory | Description                                                        | Current Tier | Gap                                                      | Target Tier |
| ------------------------- | ----------- | ------------------------------------------------------------------ | ------------ | -------------------------------------------------------- | ----------- |
| Recovery Planning (RC.RP) | RC.RP-1     | Recovery plan is executed during or after a cybersecurity incident | Tier 2       | DRC exists; no formal recovery plan; failover not tested | Tier 3      |
| Improvements (RC.IM)      | RC.IM-1     | Recovery plans incorporate lessons learned                         | Tier 1       | No post-recovery review process                          | Tier 3      |
| Communications (RC.CO)    | RC.CO-1     | Public relations are managed                                       | Tier 1       | No crisis communication plan for cyber incidents         | Tier 3      |

**Function Maturity: Tier 1–2 (Partial to Risk Informed)**

### 4. Overall Maturity Summary

| Function | Current Maturity                    | Target Maturity     |
| -------- | ----------------------------------- | ------------------- |
| Identify | Tier 2 (Risk Informed)              | Tier 3 (Repeatable) |
| Protect  | Tier 1–2 (Partial to Risk Informed) | Tier 3 (Repeatable) |
| Detect   | Tier 1 (Partial)                    | Tier 3 (Repeatable) |
| Respond  | Tier 1 (Partial)                    | Tier 3 (Repeatable) |
| Recover  | Tier 1–2 (Partial to Risk Informed) | Tier 3 (Repeatable) |

**Overall Organization Maturity: Tier 1–2 (Partial to Risk Informed)**

### 5. Improvement Roadmap

**Phase 1 — Immediate (0–3 Months)**

- Develop and communicate an organizational cybersecurity policy across all 300+ locations.
- Implement MFA and PAM for critical systems.
- Deploy centralized SIEM and establish basic monitoring capability.
- Develop a formal Incident Response Plan with escalation matrix.

**Phase 2 — Short-Term (3–6 Months)**

- Establish a vulnerability management program with regular scanning.
- Implement cybersecurity awareness training for all personnel.
- Define RTO/RPO and test DR failover procedures.
- Deploy IDS/IPS and network monitoring tools.
- Develop supply chain risk management program.

**Phase 3 — Medium-Term (6–12 Months)**

- Implement data encryption at rest and enhanced data-in-transit protections.
- Establish SOC or managed security services for 24/7 monitoring.
- Conduct tabletop exercises for incident response and recovery.
- Achieve Tier 3 (Repeatable) maturity across all five functions.

---

## 9. Building Terms of Reference (ToR) for an IS Audit [10]

> **Q.** A leading organization operating more than 100 sites, supported by an in-house DC and a private cloud-based DRC, intends to carry out an IS Audit. In alignment with NIST, ISO/IEC 27001:2022, and CIS, as well as applicable IT policies, bylaws, and regulatory guidelines, develop a comprehensive Terms of Reference (ToR) for the IS Audit. [10]

### Terms of Reference (ToR) for Information Systems Audit

### 1. Introduction

This Terms of Reference (ToR) defines the purpose, scope, authority, and methodology for conducting an Information Systems (IS) Audit for the organization operating 100+ sites with an in-house Data Center (DC) and a private cloud-based Disaster Recovery Center (DRC).

### 2. Background

The organization requires an IS Audit to evaluate its information security posture, assess compliance with applicable standards and regulations, and identify risks and gaps in its ICT infrastructure. The audit is mandated to align with internationally recognized frameworks including NIST Cybersecurity Framework, ISO/IEC 27001:2022, and CIS Controls.

### 3. Audit Objectives

- Evaluate the effectiveness of the organization's ISMS against ISO/IEC 27001:2022 (93 Annex A controls).
- Assess cybersecurity maturity against the NIST Cybersecurity Framework (5 core functions: Identify, Protect, Detect, Respond, Recover).
- Evaluate technical security controls against CIS Critical Security Controls.
- Identify vulnerabilities, risks, and gaps in the ICT infrastructure.
- Assess compliance with applicable regulatory requirements and IT policies.
- Provide actionable recommendations for risk mitigation and continuous improvement.

### 4. Scope of Work

**4.1 Infrastructure Scope**

- All 100+ operational sites.
- In-house Data Center (DC) — servers, storage, network infrastructure.
- Private cloud-based Disaster Recovery Center (DRC).
- Network infrastructure — LAN, WAN, VPN, internet connectivity.
- End-user devices — workstations, laptops, mobile devices.

**4.2 Audit Domains**

| Domain                          | Framework Reference                                         | Key Areas                                               |
| ------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------- |
| Information Security Governance | ISO 27001 Clauses 4–10, CIS Control 1                       | Policies, roles, management commitment, risk management |
| Asset Management                | ISO A.5.9–A.5.14, NIST ID.AM, CIS Control 1–2               | Asset inventory, classification, acceptable use         |
| Access Control                  | ISO A.5.15–A.5.18, A.8.2–A.8.5, NIST PR.AC, CIS Control 5–6 | User management, MFA, PAM, access reviews               |
| Physical Security               | ISO A.7.1–A.7.14, NIST PR.AC-2                              | DC/DRC physical controls, environmental controls        |
| Network Security                | ISO A.8.20–A.8.22, NIST PR.PT, CIS Control 12–13            | Firewall, IDS/IPS, segmentation, wireless security      |
| Vulnerability Management        | ISO A.8.8, NIST ID.RA, CIS Control 7                        | VAPT, patch management, vulnerability tracking          |
| Incident Management             | ISO A.5.24–A.5.28, NIST RS, CIS Control 17                  | Incident response plan, escalation, evidence collection |
| Business Continuity             | ISO A.5.29–A.5.30, NIST RC, CIS Control 11                  | BCP, DRP, RTO/RPO, failover testing                     |
| Logging and Monitoring          | ISO A.8.15–A.8.16, NIST DE.CM, CIS Control 8                | SIEM, log retention, alerting, monitoring               |
| Data Protection                 | ISO A.8.10–A.8.12, NIST PR.DS, CIS Control 3                | Encryption, DLP, data masking, backup                   |

### 5. Audit Criteria / Standards and Frameworks

- **ISO/IEC 27001:2022** — ISMS requirements and 93 Annex A controls.
- **NIST Cybersecurity Framework v1.1** — 5 functions, 23 categories, 108 subcategories.
- **CIS Critical Security Controls v8** — 18 controls with implementation groups.
- **Applicable Regulatory Requirements** — Electronic Transactions Act 2008, Individual Privacy Act 2018, sector-specific regulations and IT bylaws.
- **Organizational IT Policies** — Internal policies, procedures, and standards.

### 6. Methodology

- **Phase 1 — Planning:** Define audit plan, schedule, resource allocation, and communication with stakeholders.
- **Phase 2 — Information Gathering:** Documentation review (policies, procedures, network diagrams, asset registers), interviews with key personnel, and technical evidence collection.
- **Phase 3 — Assessment and Testing:** Compliance testing against ISO 27001 controls, maturity assessment against NIST CSF tiers, technical verification of CIS Controls (system configurations, access logs, vulnerability scan results).
- **Phase 4 — Analysis:** Gap analysis, risk assessment, and categorization of findings (Major NC, Minor NC, OFI).
- **Phase 5 — Reporting:** Draft report, management response, final report with corrective action plan.

### 7. Deliverables

| #   | Deliverable            | Description                                                               |
| --- | ---------------------- | ------------------------------------------------------------------------- |
| 1   | Audit Plan             | Detailed audit schedule, resource allocation, and checklist               |
| 2   | IS Audit Report        | Findings per control with observations, risk ratings, and recommendations |
| 3   | Gap Analysis Report    | Mapping of current state vs. ISO 27001, NIST CSF, and CIS requirements    |
| 4   | Risk Assessment Report | Identified risks with likelihood, impact, and risk ratings                |
| 5   | Executive Summary      | High-level summary of findings for senior management                      |
| 6   | Corrective Action Plan | Recommended remediation actions with priorities and timelines             |

### 8. Audit Team Composition and Qualifications

- Lead Auditor — ISO 27001 Lead Auditor certified, CISA certified.
- Technical Auditor — Expertise in network security, system administration, VAPT.
- Compliance Auditor — Knowledge of regulatory requirements and IT governance frameworks.
- All auditors must maintain independence from the areas being audited.

### 9. Timeline and Schedule

| Phase   | Activity                                       | Duration |
| ------- | ---------------------------------------------- | -------- |
| Phase 1 | Planning and Kick-off                          | Week 1   |
| Phase 2 | Information Gathering and Documentation Review | Week 2–3 |
| Phase 3 | On-site Assessment (DC, DRC, sample sites)     | Week 4–5 |
| Phase 4 | Analysis and Draft Report                      | Week 6   |
| Phase 5 | Management Response and Final Report           | Week 7–8 |

### 10. Authority and Access

- The audit team shall have unrestricted access to all information systems, documentation, facilities, and personnel relevant to the audit scope.
- The organization shall provide necessary access to DC, DRC, and branch sites as per the audit schedule.
- Audit evidence shall be handled in accordance with confidentiality requirements.

### 11. Confidentiality

- All audit findings, reports, and evidence shall be treated as confidential.
- Information shall only be shared with authorized stakeholders.
- The audit team shall sign Non-Disclosure Agreements (NDAs) prior to commencement.

### 12. Reporting and Communication

- Weekly progress updates to the audit sponsor during the engagement.
- Draft report submitted within 5 business days of fieldwork completion.
- Management response due within 10 business days of draft report.
- Final report issued within 20 business days of fieldwork completion.

---

## 10. Ransomware Readiness Assessment — CISA CSET [10]

> **Q.** An organization operating over 250 sites, supported by an in-house DC and a private cloud-based DRC, plans to conduct a Ransomware Readiness Assessment using the CISA Cyber Security Evaluation Tool (CSET). How would you conduct this ransomware readiness assessment, and what major weaknesses might be identified? [10]

### Ransomware Readiness Assessment Report

**Organization:** An organization with 250+ sites, in-house DC, private cloud-based DRC
**Tool:** CISA Cyber Security Evaluation Tool (CSET) — Ransomware Readiness Assessment (RRA) Module
**Maturity Levels:** Basic, Intermediate, Advanced

### 1. Introduction

This Ransomware Readiness Assessment (RRA) evaluates the organization's preparedness against ransomware threats using the CISA CSET tool. The RRA module is a self-assessment that guides organizations through a structured evaluation across 10 goals and three maturity levels (Basic, Intermediate, Advanced).

### 2. Assessment Methodology

**Step 1 — Scoping:** Define assessment boundaries covering all 250+ sites, DC, DRC, and all information processing facilities.

**Step 2 — Tool Setup:** Install and configure CISA CSET desktop application. Select the Ransomware Readiness Assessment (RRA) module.

**Step 3 — Self-Assessment Execution:** Answer the RRA questions across the 10 goals at three maturity tiers (Basic, Intermediate, Advanced). Each question follows the naming convention: Goal [GG] : Level [B,I,A] . Question Number [Q##].

**Step 4 — Analysis:** Review the CSET-generated analysis dashboard, including summary and detailed reports with graphs showing compliance levels per goal.

**Step 5 — Reporting:** Document findings, identified weaknesses, and develop a remediation roadmap.

### 3. RRA Assessment — 10 Goals

#### Goal 1: Asset Management (AM)

| Level        | Question Area                                              | Finding                                                               | Maturity |
| ------------ | ---------------------------------------------------------- | --------------------------------------------------------------------- | -------- |
| Basic        | Critical assets and systems are identified and inventoried | Asset inventory exists for DC but not comprehensive across 250+ sites | Partial  |
| Intermediate | Asset criticality is documented and prioritized            | No formal criticality classification                                  | Not Met  |
| Advanced     | Automated asset discovery and dependency mapping           | No automated tools deployed                                           | Not Met  |

**Weakness:** Incomplete asset inventory across 250+ sites; no criticality ranking; unknown shadow IT assets.

#### Goal 2: Robust Data Backup (DB)

| Level        | Question Area                                                                       | Finding                                                      | Maturity |
| ------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------- |
| Basic        | Regular backups of critical data are performed                                      | Daily backups at DC; weekly replication to DRC               | Partial  |
| Intermediate | Backups are tested regularly for restoration; backups are stored offline/air-gapped | No regular restoration testing; no offline/air-gapped copies | Not Met  |
| Advanced     | Immutable backups; backup architecture resilient to ransomware propagation          | No immutable backup; backup network not isolated             | Not Met  |

**Weakness:** No air-gapped/offline backups; backups accessible from the same network (can be encrypted by ransomware); no restoration testing; no immutable storage.

#### Goal 3: Phishing Prevention and Awareness (PP)

| Level        | Question Area                                                                 | Finding                                                 | Maturity |
| ------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------- | -------- |
| Basic        | Email filtering and spam protection is in place                               | Basic spam filter deployed                              | Met      |
| Intermediate | Phishing awareness training conducted regularly; simulated phishing exercises | No structured training program; no phishing simulations | Not Met  |
| Advanced     | Advanced email security with sandboxing; DMARC/DKIM/SPF fully implemented     | No sandboxing; DMARC not implemented                    | Not Met  |

**Weakness:** No employee phishing awareness training; no simulated phishing exercises; lack of advanced email threat protection.

#### Goal 4: User and Access Management (UM)

| Level        | Question Area                                                        | Finding                                        | Maturity |
| ------------ | -------------------------------------------------------------------- | ---------------------------------------------- | -------- |
| Basic        | User accounts are managed with unique IDs                            | Some shared accounts exist in critical systems | Partial  |
| Intermediate | MFA enabled for critical and remote access; least privilege enforced | No MFA; no PAM; weak password policy           | Not Met  |
| Advanced     | Zero trust architecture; continuous authentication                   | Not implemented                                | Not Met  |

**Weakness:** Shared admin credentials; no MFA; weak password policy (6-char, no complexity); no privileged access management; terminated user accounts not promptly disabled.

#### Goal 5: Network Perimeter Monitoring (NM)

| Level        | Question Area                                             | Finding                           | Maturity |
| ------------ | --------------------------------------------------------- | --------------------------------- | -------- |
| Basic        | Firewalls and basic perimeter controls are in place       | Perimeter firewall deployed       | Met      |
| Intermediate | IDS/IPS deployed; network traffic monitored for anomalies | No IDS/IPS; no network monitoring | Not Met  |
| Advanced     | Network behavior analysis; automated threat response      | Not implemented                   | Not Met  |

**Weakness:** No IDS/IPS; no network anomaly detection; no real-time traffic monitoring; flat network enables lateral movement.

#### Goal 6: Web Browser Management and DNS Filtering (BM)

| Level        | Question Area                                                | Finding                                                        | Maturity |
| ------------ | ------------------------------------------------------------ | -------------------------------------------------------------- | -------- |
| Basic        | Web browsers are kept updated                                | Browsers updated via manual process; inconsistent across sites | Partial  |
| Intermediate | DNS filtering and web content filtering deployed             | Basic URL filtering; no DNS-level protection                   | Partial  |
| Advanced     | Browser isolation technology; advanced web threat protection | Not implemented                                                | Not Met  |

**Weakness:** No DNS filtering; inconsistent browser patching across 250+ sites; no browser isolation.

#### Goal 7: Application Integrity and Allowlisting (AI)

| Level        | Question Area                                                       | Finding                                                              | Maturity |
| ------------ | ------------------------------------------------------------------- | -------------------------------------------------------------------- | -------- |
| Basic        | Only authorized software is permitted on systems                    | No software restriction policy; users can install arbitrary software | Not Met  |
| Intermediate | Application allowlisting enforced on critical systems               | Not implemented                                                      | Not Met  |
| Advanced     | Application control across all endpoints with automated enforcement | Not implemented                                                      | Not Met  |

**Weakness:** No application allowlisting; no software restriction policies; users can install unauthorized software increasing malware infection risk.

#### Goal 8: Incident Response (IR)

| Level        | Question Area                                                               | Finding                                                             | Maturity |
| ------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------- |
| Basic        | An incident response plan exists and includes ransomware scenarios          | No formal incident response plan; no ransomware-specific procedures | Not Met  |
| Intermediate | IR plan is tested through tabletop exercises; communication plan defined    | No testing or exercises conducted                                   | Not Met  |
| Advanced     | Automated incident response playbooks; integration with threat intelligence | Not implemented                                                     | Not Met  |

**Weakness:** No incident response plan; no ransomware-specific response procedures; no escalation matrix; no tabletop exercises conducted.

#### Goal 9: Risk Management (RM)

| Level        | Question Area                                                        | Finding                                             | Maturity |
| ------------ | -------------------------------------------------------------------- | --------------------------------------------------- | -------- |
| Basic        | Organizational risk management includes ransomware as a threat       | Ransomware not explicitly included in risk register | Not Met  |
| Intermediate | Regular risk assessments include ransomware scenarios                | No ransomware-specific risk assessment              | Not Met  |
| Advanced     | Quantitative risk analysis for ransomware; cyber insurance evaluated | Not implemented                                     | Not Met  |

**Weakness:** Ransomware not identified as a specific threat in risk assessments; no ransomware-specific risk treatment plan; no cyber insurance evaluation.

#### Goal 10: Vulnerability Management (VM)

| Level        | Question Area                                           | Finding                               | Maturity |
| ------------ | ------------------------------------------------------- | ------------------------------------- | -------- |
| Basic        | Regular vulnerability scanning is performed             | No vulnerability scanning program     | Not Met  |
| Intermediate | Patch management process with defined timelines         | Ad-hoc patching; no defined timelines | Not Met  |
| Advanced     | Continuous vulnerability monitoring; automated patching | Not implemented                       | Not Met  |

**Weakness:** No vulnerability scanning; ad-hoc patching; servers running outdated OS with known exploitable vulnerabilities.

### 4. Overall RRA Maturity Summary

| Goal                         | Basic   | Intermediate | Advanced |
| ---------------------------- | ------- | ------------ | -------- |
| Asset Management             | Partial | Not Met      | Not Met  |
| Robust Data Backup           | Partial | Not Met      | Not Met  |
| Phishing Prevention          | Met     | Not Met      | Not Met  |
| User and Access Management   | Partial | Not Met      | Not Met  |
| Network Perimeter Monitoring | Met     | Not Met      | Not Met  |
| Web Browser/DNS Filtering    | Partial | Partial      | Not Met  |
| Application Allowlisting     | Not Met | Not Met      | Not Met  |
| Incident Response            | Not Met | Not Met      | Not Met  |
| Risk Management              | Not Met | Not Met      | Not Met  |
| Vulnerability Management     | Not Met | Not Met      | Not Met  |

**Overall Maturity: Basic (Partial) — The organization meets only a few Basic-level practices.**

### 5. Major Weaknesses Identified

1. **No air-gapped/offline/immutable backups** — Backups accessible on the same network; ransomware can encrypt both primary data and backups.
2. **No MFA or PAM** — Compromised credentials provide direct access to critical systems without additional verification.
3. **No incident response plan for ransomware** — Organization has no documented procedure for containment, eradication, or recovery from a ransomware attack.
4. **No application allowlisting** — Any software can execute on endpoints, enabling ransomware payloads.
5. **No network segmentation** — Flat network allows ransomware lateral movement from any compromised endpoint to DC/DRC systems.
6. **No vulnerability management** — Unpatched systems with known vulnerabilities provide entry points for ransomware.
7. **No phishing training** — Employees unable to recognize ransomware delivery via phishing emails.
8. **Ransomware not in risk register** — No organizational awareness or planning for ransomware as a specific threat.

### 6. Recommendations

- Implement 3-2-1 backup strategy with at least one air-gapped/immutable copy; test restoration quarterly.
- Deploy MFA for all user and administrative access.
- Develop and test a ransomware-specific incident response plan with tabletop exercises.
- Implement application allowlisting on critical systems and endpoints.
- Segment the network to isolate critical systems, DC, and DRC.
- Establish vulnerability scanning and patch management with defined SLAs.
- Conduct phishing awareness training and simulations for all employees.
- Include ransomware in the organizational risk register and evaluate cyber insurance.

---

## 11. Conducting an Information System Audit — ISO 27001:2022 (10 Controls) [10]

> **Q.** A well-established organization with over 200 sites, operating its own DC and DRC, is planning to conduct an IS Audit aligned with ISO 27001:2022 (consider 10 controls). Prepare a comprehensive report covering: Control, Observation, Risk Rating, Recommendation. [10]

### Information System Audit Report

**Organization:** A well-established organization with 200+ sites, own DC and DRC
**Audit Standard:** ISO 27001:2022
**Audit Type:** Information System Audit
**Controls Evaluated:** 10 (across all 4 Annex A themes)

### Introduction

This IS Audit evaluates the organization's information security posture against 10 selected controls from ISO 27001:2022 Annex A. The audit covers the Head Office, Data Center (DC), Disaster Recovery Center (DRC), and a sample of branch sites across 200+ locations.

### Objective

To assess the design and operating effectiveness of 10 ISO 27001:2022 Annex A controls, identify risks, and provide recommendations for improvement.

### Scope

Head Office, Data Center (DC), Disaster Recovery Center (DRC), and representative sample of branch sites. Organizational, People, Physical, and Technological controls evaluated.

---

### A.1. Organizational Controls

#### Control 1: Policies for Information Security (A.5.1)

**Control:** Information security policy and topic-specific policies should be defined, approved by management, published, communicated to and acknowledged by relevant personnel and relevant interested parties, and reviewed at planned intervals and if significant changes occur.

**Observation:** Information Security Policy (v1.0) exists but has not been reviewed or updated since initial publication. No topic-specific policies (acceptable use, data classification, remote access, backup) are formally documented. Policy has not been communicated to all 200+ sites. No written acknowledgement from employees obtained.

**Risk Rating:** HIGH

**Recommendation:** Update the Information Security Policy to align with ISO 27001:2022 and current organizational context. Develop topic-specific policies covering acceptable use, access control, data classification, backup, incident management, and remote access. Communicate to all personnel across 200+ sites and obtain signed acknowledgement. Establish annual review cycle.

---

#### Control 2: Information Security Roles and Responsibilities (A.5.2)

**Control:** Information security roles and responsibilities should be defined and allocated according to the organization's needs.

**Observation:** No dedicated CISO or Information Security Manager position exists. IT department handles security in an ad-hoc manner. Security responsibilities at branch offices are not formally assigned. No escalation matrix for security incidents from branch sites to Head Office.

**Risk Rating:** HIGH

**Recommendation:** Create a dedicated CISO or Information Security Manager role with direct reporting to senior management. Define and document IS roles at all levels. Designate security focal points at major branch clusters. Develop and communicate an incident escalation matrix.

---

### A.2. People Controls

#### Control 3: Information Security Awareness, Education and Training (A.6.3)

**Control:** Personnel of the organization and relevant interested parties should receive appropriate information security awareness, education and training and regular updates of the organization's information security policy, topic-specific policies and procedures, as relevant for their job function.

**Observation:** No structured cybersecurity awareness and training program exists. Staff across branch sites are unaware of basic cybersecurity practices (phishing, password management, social engineering). No training records maintained. Shared login credentials observed at multiple sites.

**Risk Rating:** HIGH

**Recommendation:** Establish a comprehensive security awareness training program conducted at least annually for all employees. Cover phishing, social engineering, password hygiene, data handling, and incident reporting. Maintain training records. Conduct periodic simulated phishing exercises.

---

### A.3. Physical Controls

#### Control 4: Physical Security Perimeters (A.7.1)

**Control:** Security perimeters should be defined and used to protect areas that contain information and other associated assets.

**Observation:** DC uses basic key-lock mechanism without electronic access control (biometric/card-based). No visitor log maintained for DC area. DRC has shared access corridors without a dedicated security perimeter. CCTV coverage limited with retention of only 15 days. Branch offices have minimal physical security for IT equipment.

**Risk Rating:** HIGH

**Recommendation:** Implement electronic access control (biometric or smart card) at DC and DRC. Deploy visitor management system with logging. Enhance CCTV with minimum 90-day retention. Establish dedicated security perimeter for DRC. Define minimum physical security standards for all branch sites.

---

#### Control 5: Securing Offices, Rooms and Facilities (A.7.3)

**Control:** Physical security for offices, rooms and facilities should be designed and implemented.

**Observation:** Server room lacks environmental monitoring sensors (temperature, humidity, water leak detection). Fire suppression relies on standard extinguishers rather than gas-based system. UPS capacity and maintenance records not available. DRC has no diesel generator backup for redundant power supply.

**Risk Rating:** MEDIUM

**Recommendation:** Install environmental monitoring with real-time alerting in DC and DRC. Deploy gas-based fire suppression (FM-200 or Novec 1230) in server room. Implement proper cable management. Review and document UPS capacity with regular testing. Equip DRC with diesel generator backup.

---

### A.4. Technological Controls

#### Control 6: Access Control (A.8.2)

**Control:** Access to information and other associated assets should be restricted in accordance with the established topic-specific policy on access control.

**Observation:** No formal access control policy documented. User provisioning and de-provisioning is unstructured — terminated employees' accounts found active. Shared accounts observed in critical systems. Password policy weak (6-character minimum, no complexity, no expiry). No MFA implemented for any system. Privileged access uses shared admin/root credentials.

**Risk Rating:** HIGH

**Recommendation:** Develop and implement a formal access control policy. Establish user lifecycle management with HR integration. Eliminate shared accounts. Enforce 12-character minimum passwords with complexity and rotation. Implement MFA for all critical systems. Deploy PAM solution. Conduct quarterly user access reviews.

---

#### Control 7: Protection Against Malware (A.8.7)

**Control:** Protection against malware should be implemented and supported by appropriate user awareness.

**Observation:** Antivirus deployed on most workstations but not centrally managed. Several branch workstations running outdated virus definitions (30+ days old). No EDR solution deployed. USB port restrictions not enforced. Email gateway filtering is basic with no sandboxing or advanced threat protection. No regular malware scan schedule for servers.

**Risk Rating:** MEDIUM

**Recommendation:** Implement centrally managed endpoint protection with EDR capabilities across all endpoints including branches. Enforce USB restrictions via group policy. Enhance email security with sandboxing and URL filtering. Schedule regular malware scans on all servers.

---

#### Control 8: Management of Technical Vulnerabilities (A.8.8)

**Control:** Information about technical vulnerabilities of information systems in use should be obtained, the organization's exposure to such vulnerabilities should be evaluated and appropriate measures should be taken.

**Observation:** No formal vulnerability management program. No periodic vulnerability assessments or penetration testing conducted. Patch management is ad-hoc with no defined timelines. Servers running outdated OS with known vulnerabilities. Customer-facing application never security-assessed. No software inventory to track patch status.

**Risk Rating:** HIGH

**Recommendation:** Establish a formal vulnerability management program with quarterly vulnerability assessments and annual penetration testing. Define patch management timelines: critical patches within 72 hours, high within 2 weeks, routine within 30 days. Maintain a comprehensive IT asset and software inventory. Subscribe to vulnerability advisory services.

---

#### Control 9: Information Backup (A.8.13)

**Control:** Backup copies of information, software and systems should be maintained and regularly tested in accordance with the agreed topic-specific policy on backup.

**Observation:** Daily backups of critical databases performed. No formal backup policy defining scope, frequency, retention, and recovery procedures. Off-site replication to DRC is weekly, creating a 7-day potential data loss window. Backup restoration not tested in over 12 months. RTO and RPO not formally defined. Backup encryption not implemented.

**Risk Rating:** HIGH

**Recommendation:** Develop a formal backup policy defining RTO, RPO, backup frequency, retention, and restoration procedures. Increase DRC replication to daily minimum. Conduct quarterly backup restoration tests. Encrypt all backup data at rest and in transit. Integrate backup strategy with BCP.

---

#### Control 10: Logging (A.8.15)

**Control:** Logs that record activities, exceptions, faults and other relevant events should be produced, stored, protected and analysed.

**Observation:** System logs generated on individual servers and network devices but no centralized log management or SIEM. Log retention inconsistent (7–30 days). No log review process — examined only reactively. Administrator activities not separately logged. Logs not protected against tampering. No alerting for failed logins, privilege escalation, or after-hours access.

**Risk Rating:** HIGH

**Recommendation:** Implement centralized SIEM platform to aggregate and correlate logs. Establish minimum 1-year log retention for security-relevant logs. Configure automated alerting for critical security events. Protect logs against tampering with write-once storage. Log administrator activities separately. Conduct weekly log reviews.

---

### Summary of Findings

| #   | Control                                 | ISO Ref | Theme          | Risk Rating |
| --- | --------------------------------------- | ------- | -------------- | ----------- |
| 1   | Policies for Information Security       | A.5.1   | Organizational | HIGH        |
| 2   | IS Roles and Responsibilities           | A.5.2   | Organizational | HIGH        |
| 3   | Security Awareness and Training         | A.6.3   | People         | HIGH        |
| 4   | Physical Security Perimeters            | A.7.1   | Physical       | HIGH        |
| 5   | Securing Offices, Rooms and Facilities  | A.7.3   | Physical       | MEDIUM      |
| 6   | Access Control                          | A.8.2   | Technological  | HIGH        |
| 7   | Protection Against Malware              | A.8.7   | Technological  | MEDIUM      |
| 8   | Management of Technical Vulnerabilities | A.8.8   | Technological  | HIGH        |
| 9   | Information Backup                      | A.8.13  | Technological  | HIGH        |
| 10  | Logging                                 | A.8.15  | Technological  | HIGH        |

**Overall Assessment:** 8 out of 10 controls rated HIGH risk, 2 rated MEDIUM risk. The organization's information security posture requires significant improvement across organizational, people, physical, and technological domains.

### Prioritized Recommendations

**Critical Priority (Immediate)**

- Implement MFA for all critical systems.
- Eliminate shared accounts and implement individual user accounts.
- Conduct immediate VAPT of customer-facing applications and IT infrastructure.
- Deploy centralized SIEM for real-time monitoring and alerting.
- Define RTO/RPO and increase DRC backup replication to daily.

**High Priority (Within 3 Months)**

- Update Information Security Policy and develop topic-specific policies.
- Appoint a dedicated CISO/Information Security Manager.
- Implement electronic access controls at DC and DRC.
- Deploy centrally managed endpoint protection with EDR.
- Establish formal vulnerability and patch management program.
- Develop and test BCP.

**Medium Priority (Within 6 Months)**

- Conduct cybersecurity awareness training for all employees across all sites.
- Install environmental monitoring and gas-based fire suppression in DC/DRC.
- Implement PAM for administrative accounts.
- Establish security focal points at major branch sites.
- Conduct comprehensive risk assessment for all IT assets.
