# Meridian Health Solutions
# AI Governance Risk Register

## Risk Register Overview

**Organization:** Meridian Health Solutions (Fictional)  
**Assessment Type:** AI Governance and Security Risk Assessment  
**Framework:** NIST AI RMF and NIST SP 800-53 Rev. 5  
**Assessment Status:** Initial Assessment  
**Risk Scoring:** Likelihood × Impact (1–25)

---

## Risk AI-001: Unauthorized AI Data Disclosure

| Field | Assessment |
|---|---|
| Risk ID | AI-001 |
| Risk Category | Data Privacy / AI Governance |
| Risk Title | Unauthorized disclosure of sensitive information through generative AI |
| Threat Scenario | An employee enters confidential customer or healthcare-related information into an unapproved generative AI application. |
| Vulnerability | Lack of formal AI usage policies, employee awareness, and technical restrictions on unauthorized AI applications. |
| Affected Assets | Customer information, employee records, confidential business information |
| Likelihood | 4 - Likely |
| Impact | 5 - Severe |
| Inherent Risk Score | 20/25 |
| Initial Risk Rating | High |
| Proposed Control | Establish an approved AI usage policy, restrict unauthorized AI applications, and implement data loss prevention safeguards. |
| Risk Owner | Information Security / GRC |
| Treatment Strategy | Mitigate |
| Assessment Status | Open - Pending Control Validation |

### Risk Rationale

Employees may use generative AI tools without understanding how submitted information is processed, retained, or shared.

Without documented policies, employee awareness, and technical safeguards, sensitive organizational information could be exposed through unauthorized AI usage.

The initial likelihood rating of 4 reflects the potential for employees to use AI applications without adequate guidance.

The impact rating of 5 reflects the potential consequences of exposing sensitive customer or healthcare-related information.

### Recommended Remediation

1. Develop and approve an organizational AI acceptable-use policy.
2. Establish an inventory of approved AI applications.
3. Implement technical safeguards to restrict unauthorized AI applications.
4. Develop employee AI security awareness training.
5. Implement monitoring and data loss prevention controls.
6. Conduct periodic AI governance control assessments.

### Validation Objective

Determine whether organizational controls effectively prevent employees from submitting sensitive information to unauthorized AI applications.

**Validation Status:** Not Tested  
**Evidence Status:** Pending

---

## Risk Scoring Methodology

| Score | Likelihood | Impact |
|---|---|---|
| 1 | Rare | Negligible |
| 2 | Unlikely | Minor |
| 3 | Possible | Moderate |
| 4 | Likely | Major |
| 5 | Almost Certain | Severe |

**Risk Score = Likelihood × Impact**

These ratings are illustrative assessment criteria established for this lab, not official NIST scoring requirements.
##  Evidence and Validation Updates

### Test DLP-001: Sensitive Data Leakage Detection
- **Test outcome:** 3 of 3 synthetic test cases matched expected results.
- **Finding:** The prototype flagged a synthetic email address and payment-card-like number.
- **Evidence:** `test-results/DLP-001-validation-report.md`
- **Status:** Prototype test successful; enterprise DLP effectiveness not verified.

### Test AI-002: Approved AI Application Usage
- **Test outcome:** 3 approved activities and 2 flagged activities.
- **Finding:** Two synthetic employee activities involved AI applications absent from the approved tools list.
- **Evidence:** `test-results/AI-002-validation-report.md`
- **Status:** Prototype test successful; actual employee activity and enforcement not verified.

### Updated Risk Assessment
- **Risk ID:** AI-001
- **Risk status:** Open
- **Treatment:** Mitigate
- **Evidence status:** Two prototype tests completed.
- **Residual risk:** Not assessed.
- **Next action:** Define enterprise control owners, establish an approved AI application inventory, and determine how actual usage will be monitored and enforced.