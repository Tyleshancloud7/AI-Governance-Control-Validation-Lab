# Meridian Health Solutions
# AI Governance Security Control Matrix

## 1. Purpose

This control matrix maps identified AI governance risks to relevant NIST SP 800-53 Rev. 5 security controls.

The objective is to identify safeguards, define validation procedures, and establish the evidence required to evaluate control effectiveness.

## 2. Control Mapping

| Control ID | Control Name | Security Objective | Related Risk |
|---|---|---|---|
| AC-2 | Account Management | Manage and authorize user accounts accessing approved AI applications. | AI-001 |
| AC-3 | Access Enforcement | Enforce approved access permissions and restrict unauthorized resources. | AI-001 |
| SI-4 | System Monitoring | Monitor systems for unauthorized access and suspicious AI-related activity. | AI-001 |
| AC-6 | Least Privilege | Limit user access to only the privileges necessary for assigned responsibilities. | AI-001 |
| AU-2 | Event Logging | Identify the events that must be logged for security monitoring and accountability. | AI-001 |
| AU-6 | Audit Record Review, Analysis, and Reporting | Review and analyze audit records for suspicious or unauthorized activity. | AI-001 |
| SC-7 | Boundary Protection | Monitor and control communications at external and internal system boundaries. | AI-001 |
| PM-30 | Supply Chain Risk Management Strategy | Establish an organization-wide strategy for managing supply chain risks, including relevant AI service providers. | AI-001 |

## 3. Control Validation Plan

### AC-2: Account Management

**Validation Objective:** Determine whether only authorized users have accounts and access to approved AI applications.

**Validation Procedure:**
1. Obtain the approved AI application inventory.
2. Obtain a list of authorized users.
3. Compare application access against approved user records.
4. Identify unauthorized or inactive accounts.
5. Document exceptions.

**Expected Evidence:**
- Approved user access list.
- Application inventory.
- Access review records.
- Account approval documentation.

### AC-3: Access Enforcement

**Validation Objective:** Determine whether technical restrictions prevent unauthorized access to prohibited AI applications.

**Validation Procedure:**
1. Identify approved and prohibited AI applications.
2. Review technical access restrictions.
3. Conduct authorized tests against a simulated prohibited application.
4. Record whether access is permitted or denied.
5. Document findings.

**Expected Evidence:**
- Application access policy.
- Firewall or web-filter configuration.
- Test execution records.
- Access-denial logs.

### SI-4: System Monitoring

**Validation Objective:** Determine whether suspicious AI-related activity is detected and investigated.

**Validation Procedure:**
1. Review applicable monitoring requirements.
2. Generate a controlled test event.
3. Review security monitoring records.
4. Determine whether the event was detected.
5. Document alerting and response results.

**Expected Evidence:**
- Monitoring configuration.
- Test event records.
- Security alerts.
- Investigation documentation.

## 4. Control Assessment Status

| Control | Implementation Status | Validation Status |
|---|---|---|
| AC-2 | Not Verified | Not Tested |
| AC-3 | Not Verified | Not Tested |
| SI-4 | Not Verified | Not Tested |
| AC-6 | Not Verified | Not Tested |
| AU-2 | Not Verified | Not Tested |
| AU-6 | Not Verified | Not Tested |
| SC-7 | Not Verified | Not Tested |
| PM-30 | Not Verified | Not Tested |

## 5. Assessment Notes

Control mappings are preliminary and must be evaluated against the organization's actual environment, system boundaries, control implementation, and applicable requirements.

No control should be marked effective without supporting evidence and completed validation procedures.

**Assessment Status:** Initial Control Mapping  
**Related Risk:** AI-001  
**Next Phase:** Control Validation Testing
## Control Validation Evidence Updates

### AC-3 – Access Enforcement
- **Control objective:** Enforce approved access restrictions.
- **Related test:** AI-002
- **Evidence:** `test-results/AI-002-validation-report.md`
- **Prototype result:** Two synthetic AI application activities were flagged because they were absent from the approved tools list.
- **Assessment:** The prototype demonstrates allowlist comparison logic. Actual access enforcement has not been implemented or verified.
- **Status:** Partially demonstrated through prototype testing.

### SI-4 – System Monitoring
- **Control objective:** Monitor systems and identify potentially unauthorized activity.
- **Related test:** AI-002
- **Evidence:** `test-results/AI-002-validation-report.md`
- **Prototype result:** The script identified two exceptions in five synthetic activities.
- **Assessment:** Demonstrates basic exception identification using supplied data. Continuous monitoring and actual employee activity collection have not been implemented.
- **Status:** Prototype demonstrated; operational monitoring not verified.

### AC-6 – Least Privilege
- **Control objective:** Restrict access to what users need to perform assigned tasks.
- **Related risk:** AI-001
- **Evidence:** Risk register and AI-002 findings.
- **Assessment:** The tests identify a potential governance concern but do not demonstrate user permissions or least-privilege enforcement.
- **Status:** Not tested.

### SC-7 – Boundary Protection
- **Control objective:** Monitor and control communications at external and internal system boundaries.
- **Related test:** DLP-001
- **Evidence:** `test-results/DLP-001-validation-report.md`
- **Assessment:** The local prototype detects selected sensitive-data patterns in supplied text. It does not inspect or restrict actual network traffic.
- **Status:** Not implemented or operationally validated.

## Overall Control Assessment

The lab currently demonstrates prototype-level testing for sensitive-data pattern detection and approved AI application inventory comparison.

No enterprise security control is claimed to be fully implemented or operating effectively.

Further testing will require an actual technical environment, defined control owners, approved policies, and verifiable evidence.