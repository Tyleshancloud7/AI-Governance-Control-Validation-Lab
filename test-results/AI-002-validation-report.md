# AI-002: Approved AI Tools Control Validation Report

## 1. Assessment Information

- **Organization:** Meridian Health Solutions (Fictional)
- **Assessment ID:** AI-002
- **Related Risk:** AI-001 – Unauthorized AI Usage and Sensitive Data Disclosure
- **Control Objective:** Ensure employees use only organization-approved AI applications.
- **Test Environment:** Local macOS environment
- **Programming Language:** Python 3.14.3
- **Assessment Type:** Simulated control validation using synthetic data
- **Status:** Test completed; exceptions identified

## 2. Objective

Evaluate whether a predefined list of employee AI application activities complies with the organization's approved AI tools list.

The test compares each application against an established allowlist and flags applications that are not approved.

## 3. Testing Methodology

A Python script was developed to:

1. Define a fictional list of approved AI applications.
2. Evaluate five synthetic employee application activities.
3. Compare each application against the approved list.
4. Flag applications not found on the approved list.
5. Generate a summary of approved and flagged activities.

## 4. Test Results

| Employee | AI Application | Result |
|---|---|---|
| Employee 001 | Microsoft Copilot | Approved |
| Employee 002 | ChatGPT Enterprise | Approved |
| Employee 003 | UnknownAI Chat | Flagged |
| Employee 004 | Google Gemini Enterprise | Approved |
| Employee 005 | Personal ChatGPT Account | Flagged |

## 5. Results Summary

- Total activities tested: 5
- Approved activities: 3
- Flagged activities: 2
- Exceptions identified: 2

**Overall Result:** Exceptions identified – further investigation required.

## 6. Findings

Two synthetic employee activities involved applications that were not included in the organization's approved AI tools list.

Potential concerns include:

- Use of unapproved AI applications.
- Possible exposure of confidential organizational information.
- Lack of enforcement of AI application usage requirements.
- Insufficient visibility into employee AI application activity.

These are potential risks, not confirmed security incidents.

## 7. Recommended Remediation

1. Establish and publish an organization-approved AI application inventory.
2. Implement an AI acceptable-use policy.
3. Evaluate technical restrictions for unauthorized AI applications.
4. Assign ownership for investigating and resolving exceptions.
5. Establish recurring reviews of AI application usage.

## 8. Limitations

- All employee activity was fictional and synthetic.
- The approved application list was created for demonstration purposes.
- The script does not inspect actual network traffic, endpoints, or employee accounts.
- The test does not verify whether the listed applications are contractually or technically approved.
- No production enforcement mechanism was implemented.

## 9. Conclusion

The prototype successfully identified two exceptions within the five synthetic activities tested.

The results demonstrate how an organization can use a defined application inventory and repeatable testing logic to identify potential AI governance policy violations.

This test demonstrates a proof of concept. It does not establish that an enterprise AI application control is implemented or operating effectively.

**Evidence Artifact:** `test-results/approved_ai_tools_test.py`

**Validation Report:** `test-results/AI-002-validation-report.md`