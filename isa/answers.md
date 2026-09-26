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
