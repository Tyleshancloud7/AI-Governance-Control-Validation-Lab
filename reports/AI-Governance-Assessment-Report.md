# AI Governance Assessment Report

**Organization:** Meridian Health Solutions (Fictional)  
**Assessment Type:** AI Governance and Security Control Assessment  
**Assessment Date:** October 30, 2026  
**Prepared By:** AI Governance Assessment Team  
**Classification:** Portfolio Demonstration – Synthetic Data Only

---

## 1. Executive Summary

Meridian Health Solutions is a fictional healthcare technology organization with approximately 250 employees. The organization uses generative artificial intelligence tools to support business operations but has not established a formal AI governance program.

This assessment evaluates potential risks associated with generative AI usage, with particular attention to sensitive data disclosure and unauthorized AI application usage.

A prototype AI governance control validation lab was developed to demonstrate how an organization can identify AI-related risks, map candidate security controls, perform repeatable technical tests, and document supporting evidence.

Two prototype validation activities were completed:

- **DLP-001 – Sensitive Data Leakage Detection:** Three synthetic test cases were evaluated. All three produced their expected results.
- **AI-002 – Approved AI Tools Validation:** Five synthetic employee activities were evaluated. Three matched the approved application list, while two were flagged as exceptions.

The results demonstrate the prototype's ability to identify predefined conditions in synthetic data. They do not establish that Meridian has implemented effective enterprise security controls.

The assessment recommends establishing an AI acceptable-use policy, maintaining an approved AI application inventory, evaluating technical enforcement mechanisms, and implementing ongoing AI risk monitoring.

## 2. Organizational Background

### 2.1 Organization Profile

Meridian Health Solutions is a fictional healthcare technology company with approximately 250 employees.

The organization uses generative AI applications to support productivity, research, communication, and business operations.

Because the organization operates in
## 3. Risk Assessment Methodology

### 3.1 Risk Identification

Risks were identified by considering potential threats associated with employee use of generative AI applications.

The assessment focused on:
- Unauthorized disclosure of sensitive information.
- Use of unapproved AI applications.
- Insufficient AI usage oversight.
- Inadequate access restrictions.
- Limited visibility into AI-related activity.

### 3.2 Risk Scoring

A qualitative 5-point scoring model was used.

**Likelihood**

| Score | Description |
|---|---|
| 1 | Rare |
| 2 | Unlikely |
| 3 | Possible |
| 4 | Likely |
| 5 | Almost Certain |

**Impact**

| Score | Description |
|---|---|
| 1 | Negligible |
| 2 | Minor |
| 3 | Moderate |
| 4 | Major |
| 5 | Severe |

**Inherent Risk Calculation**

Inherent Risk = Likelihood × Impact

For this demonstration, the following illustrative ranges are used:

| Score | Risk Level |
|---|---|
| 1–4 | Low |
| 5–9 | Moderate |
| 10–16 | High |
| 17–25 | Severe |

These scoring thresholds are project-defined and are not a formula prescribed by NIST.

### 3.3 Identified Risk: AI-001

**Risk Title:** Unauthorized Disclosure of Sensitive Information Through Generative AI

**Risk Scenario:** An employee submits confidential customer or healthcare-related information to an unapproved generative AI application.

**Threat Sources:** Employees, compromised accounts, or unauthorized third parties.

**Potential Vulnerabilities:**
- Absence of a formal AI acceptable-use policy.
- Insufficient employee awareness.
- Lack of technical restrictions on unauthorized AI applications.
- Inadequate monitoring of AI-related activity.

**Likelihood:** 4 – Likely

**Impact:** 5 – Severe

**Inherent Risk Score:** 20/25

**Risk Level:** Severe

**Risk Treatment:** Mitigate

**Risk Status:** Open

### 3.4 Risk Scoring Interpretation

The likelihood score of 4 is an initial assessment hypothesis based on the possibility of employees using AI applications without sufficient guidance.

The impact score of 5 reflects the potential consequences of exposing sensitive healthcare-related or customer information.

These scores are illustrative and have not been confirmed through enterprise interviews, incident data, or operational testing.

Residual risk has not yet been assessed because enterprise control implementation and effectiveness have not been established.
## 4. Security Control Assessment

### 4.1 Framework Alignment

The assessment uses the following frameworks as reference points:

- NIST AI Risk Management Framework (AI RMF).
- NIST SP 800-53 Revision 5.
- NIST Privacy Framework.
- ISO/IEC 42001.

The control mappings below are preliminary candidate mappings. Final applicability must be determined based on the organization's actual systems, architecture, policies, and control implementation.

### 4.2 NIST SP 800-53 Control Mapping

| Control | Control Name | Assessment Relevance |
|---|---|---|
| AC-2 | Account Management | Supports management of user accounts and authorized access. |
| AC-3 | Access Enforcement | Supports enforcement of approved access restrictions. |
| AC-6 | Least Privilege | Limits user access to authorized business needs. |
| AU-2 | Event Logging | Supports identification of events that should be logged. |
| AU-6 | Audit Record Review, Analysis, and Reporting | Supports review and analysis of audit records. |
| SI-4 | System Monitoring | Supports monitoring and detection of potentially unauthorized activity. |
| SC-7 | Boundary Protection | Supports monitoring and control of communications at system boundaries. |

### 4.3 Control Validation Observations

**AC-3 – Access Enforcement**
- Related evidence: AI-002.
- Observation: The prototype flagged two applications absent from the approved list.
- Gap: No actual access restriction or enforcement mechanism was implemented.
- Assessment: Prototype logic demonstrated; enterprise control effectiveness not verified.

**SI-4 – System Monitoring**
- Related evidence: AI-002.
- Observation: The script identified two exceptions in five synthetic activities.
- Gap: No continuous monitoring or actual employee activity collection exists.
- Assessment: Prototype exception detection demonstrated; operational monitoring not verified.

**SC-7 – Boundary Protection**
- Related evidence: DLP-001.
- Observation: The prototype identified predefined sensitive-data patterns in synthetic text.
- Gap: No network traffic inspection or boundary enforcement was implemented.
- Assessment: Limited local prototype testing completed; enterprise control effectiveness not verified.

**AC-6 – Least Privilege**
- Related evidence: AI-001 risk register.
- Observation: Unauthorized AI usage represents a potential governance concern.
- Gap: User permissions and access privileges were not tested.
- Assessment: Not tested.

### 4.4 Overall Control Assessment

The project demonstrates preliminary control mapping and prototype-level testing.

The tests provide evidence of how selected security objectives can be evaluated through repeatable procedures.

However, the results do not establish that the organization has implemented or effectively operates the mapped NIST controls.
## 5. Technical Control Testing Results

### 5.1 DLP-001 – Sensitive Data Leakage Detection

**Objective:** Determine whether the prototype can identify predefined sensitive-data patterns in submitted text.

**Testing Method:** A Python script using pattern matching was executed against three synthetic test cases.

**Results:**

| Test Case | Input Scenario | Expected Result | Actual Result |
|---|---|---|---|
| TEST-001 | Normal business question | Pass | Pass |
| TEST-002 | Synthetic email address | Flagged | Flagged |
| TEST-003 | Payment-card-like number | Flagged | Flagged |

**Summary:**
- Total test cases: 3
- Successful expected-result matches: 3
- Failed test cases: 0
- Prototype test success rate: 100%

**Finding:** The prototype successfully identified the predefined email and payment-card-like patterns.

**Limitation:** This test does not establish production DLP effectiveness or detect every form of sensitive information.

### 5.2 AI-002 – Approved AI Tools Validation

**Objective:** Determine whether the prototype can identify AI applications that are absent from a predefined approved application list.

**Testing Method:** A Python script compared five synthetic employee application activities against a fictional approved AI tools inventory.

**Results:**

| Test Case | Application | Result |
|---|---|---|
| Employee 001 | Microsoft Copilot | Approved |
| Employee 002 | ChatGPT Enterprise | Approved |
| Employee 003 | UnknownAI Chat | Flagged |
| Employee 004 | Google Gemini Enterprise | Approved |
| Employee 005 | Personal ChatGPT Account | Flagged |

**Summary:**
- Total activities tested: 5
- Approved activities: 3
- Flagged activities: 2
- Exceptions identified: 2

**Finding:** Two synthetic activities involved applications absent from the approved inventory.

**Limitation:** The script does not inspect actual network traffic, employee devices, or enterprise application logs.

### 5.3 Technical Testing Conclusion

Both prototype tests produced their expected results against the predefined synthetic test cases.

The tests demonstrate basic pattern detection and approved-application inventory comparison.

These results represent successful prototype execution, not proof of enterprise control implementation or operating effectiveness.
## 6. Findings and Remediation Plan

### 6.1 Finding F-001: Lack of Formal AI Acceptable-Use Policy

**Related Risk:** AI-001  
**Risk Level:** Severe  
**Observation:** The fictional organization does not have a documented AI acceptable-use policy.

**Potential Impact:**
Employees may submit confidential or sensitive information to unauthorized AI applications without understanding the associated risks.

**Recommended Remediation:**
- Develop and approve an AI acceptable-use policy.
- Define permitted and prohibited AI activities.
- Establish data classification and handling requirements.
- Provide employee AI security awareness training.

**Suggested Owner:** Information Security / GRC  
**Priority:** High  
**Status:** Open

### 6.2 Finding F-002: No Verified Approved AI Application Inventory

**Related Risk:** AI-001  
**Observation:** The prototype identified two synthetic activities involving applications absent from the fictional approved AI tools list.

**Potential Impact:**
Unauthorized applications may introduce privacy, security, and third-party risk.

**Recommended Remediation:**
- Establish an approved AI application inventory.
- Evaluate vendors before authorization.
- Document business owners and permitted use cases.
- Establish a recurring application review process.

**Suggested Owner:** IT Security / Vendor Risk Management  
**Priority:** High  
**Status:** Open

### 6.3 Finding F-003: No Verified Technical AI Usage Enforcement

**Related Risk:** AI-001  
**Observation:** The prototype identified exceptions but did not enforce restrictions.

**Potential Impact:**
Employees may continue using unauthorized applications without detection or intervention.

**Recommended Remediation:**
- Evaluate secure web gateway or cloud access security broker capabilities.
- Evaluate endpoint and data loss prevention controls.
- Define monitoring and escalation procedures.
- Test enforcement mechanisms in a controlled environment.

**Suggested Owner:** Security Engineering / IT  
**Priority:** High  
**Status:** Open

### 6.4 Finding F-004: Limited Sensitive Data Detection

**Related Risk:** AI-001  
**Observation:** The local prototype detects only selected email and payment-card-like patterns.
## 7. AI Governance Recommendations

Based on the simulated assessment, the following actions are recommended for Meridian Health Solutions.

### 7.1 Establish an AI Governance Program
- Assign an executive sponsor for AI governance.
- Establish an AI governance committee.
- Define roles and responsibilities for AI risk management.
- Maintain an inventory of AI applications and use cases.

### 7.2 Implement AI Security Policies
- Develop an AI acceptable-use policy.
- Establish data classification and handling requirements.
- Define restrictions for confidential and regulated information.
- Establish procedures for reviewing new AI applications.

### 7.3 Strengthen Technical Safeguards
- Evaluate enterprise data loss prevention solutions.
- Implement appropriate access restrictions.
- Evaluate monitoring capabilities for AI application usage.
- Establish processes for detecting and escalating unauthorized activity.

### 7.4 Improve Third-Party AI Risk Management
- Evaluate AI vendors before procurement.
- Review data retention and privacy practices.
- Assess vendor security documentation.
- Establish ongoing third-party risk reviews.

### 7.5 Establish Continuous Monitoring
- Conduct periodic AI application inventory reviews.
- Review security events and exceptions.
- Track remediation activities.
- Reassess AI risks when applications, vendors, or business processes change.

## 8. Conclusion

This assessment demonstrates a practical approach to identifying and evaluating generative AI governance risks within a fictional healthcare technology organization.

Two Python-based prototype tests were developed and executed successfully against predefined synthetic test cases.

The assessment identified potential governance gaps involving sensitive data disclosure, unauthorized AI application usage, technical enforcement, and monitoring.

The project demonstrates how risk registers, security control mappings, technical testing, evidence management, and remediation planning can support an AI governance program.

Further work is required to evaluate enterprise technologies, establish organizational policies, assign control ownership, and verify operating effectiveness.

**Final Assessment Status:** Prototype assessment completed. Enterprise control effectiveness not established.

## 9. Supporting Project Evidence

| Artifact | Location |
|---|---|
| Risk Register | risk-register/risk-register.md |
| NIST Control Matrix | controls/ai-control-matrix.md |
| DLP Python Test | test-results/ai_data_leakage_test.py |
| DLP Validation Report | test-results/DLP-001-validation-report.md |
| Approved AI Tools Test | test-results/approved_ai_tools_test.py |
| AI Tools Validation Report | test-results/AI-002-validation-report.md |
| Evidence Register | evidence/evidence-register.md |

---

**End of Assessment Report**

Prepared for portfolio demonstration purposes. All organizational data and test records are synthetic.

