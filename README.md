# AI Governance Control Validation Lab

## Project Overview

This project demonstrates the development of an AI governance and security control validation program for a fictional healthcare technology company, Meridian Health Solutions.

The lab focuses on identifying AI-related security and privacy risks, mapping applicable security controls, developing validation procedures, conducting controlled tests using synthetic data, and documenting findings and remediation recommendations.

## Business Scenario

Meridian Health Solutions is a fictional healthcare technology company with approximately 250 employees.

The organization uses generative AI tools to support business operations but lacks a formal AI governance and control validation program.

Key risks include:
- Unauthorized use of AI applications.
- Exposure of sensitive information through AI prompts.
- Inadequate access controls.
- Insufficient AI vendor risk assessments.
- Limited monitoring and oversight of AI usage.

## Project Objectives

- Develop an AI governance risk register.
- Map AI-related risks to applicable security controls.
- Develop control validation procedures.
- Execute controlled security tests using synthetic data.
- Document test results and supporting evidence.
- Identify control gaps and recommend remediation.

## Frameworks and References

- NIST AI Risk Management Framework (AI RMF).
- NIST SP 800-53 Revision 5.
- NIST Privacy Framework.
- ISO/IEC 42001.

## Technical Testing

Two Python-based validation prototypes were developed:

**1. AI Data Leakage Detection**
- Evaluates synthetic text for email and payment-card-like patterns.
- Executes three test cases.
- All three test cases passed.
- Demonstrates basic pattern-based detection.

**2. Approved AI Tools Validation**
- Compares synthetic AI application activity against a fictional approved-tools list.
- Identifies activity involving unapproved applications.
- Demonstrates a basic approach to AI usage oversight.

## Project Deliverables

| Deliverable | Description |
|---|---|
| Risk Register | AI-related risks and risk scoring |
| Control Matrix | Candidate mappings to NIST SP 800-53 |
| Evidence Register | Supporting evidence documentation |
| Validation Reports | Test procedures, results, and observations |
| Assessment Report | Findings and remediation recommendations |
| Python Scripts | Local validation prototypes |

## Key Findings

- No formal AI acceptable-use policy was established in the fictional scenario.
- No verified enterprise AI application inventory was available.
- Technical enforcement of approved AI tools was not established.
- Sensitive data detection capabilities were limited to basic pattern matching.

## Project Status

**Phase 1: Completed — AI Governance Prototype Assessment**

- Business scenario and project scope defined.
- AI governance risk register developed.
- Candidate security control mappings documented.
- Synthetic-data validation prototypes executed.
- Test results and evidence documented.
- Governance assessment report completed.
- Remediation recommendations developed.

## Limitations

This is a portfolio demonstration using a fictional organization and synthetic data.

The Python scripts are local prototypes, not production DLP or enterprise AI monitoring solutions. Testing does not establish that enterprise controls are implemented or effective.

Control mappings are candidate mappings and require organizational context before implementation.

## Author

Tylesha Alexander  
Cybersecurity | Governance, Risk & Compliance | AI Security Governance

GitHub: [Tyleshancloud7](https://github.com/Tyleshancloud7)


