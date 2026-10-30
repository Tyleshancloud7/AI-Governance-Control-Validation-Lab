import re

# AI GOVERNANCE CONTROL VALIDATION LAB
# Test ID: DLP-001
# Objective: Detect potential sensitive information before AI submission.

def detect_sensitive_information(text):

    findings = []

    # Detect email address patterns
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    # Detect 13-19 digit payment-card-like sequences
    card_pattern = r"\b(?:\d[ -]*?){13,19}\b"

    if re.search(email_pattern, text):
        findings.append("Potential email address detected")

    if re.search(card_pattern, text):
        findings.append("Potential payment card number detected")

    return findings


# Synthetic test scenarios
test_cases = [
    {
        "id": "TEST-001",
        "description": "Normal business question",
        "input": "How can we improve our employee onboarding process?",
        "expected": "PASS"
    },
    {
        "id": "TEST-002",
        "description": "Synthetic email exposure",
        "input": "Contact the fictional customer at customer@example.com",
        "expected": "FLAGGED"
    },
    {
        "id": "TEST-003",
        "description": "Synthetic payment card exposure",
        "input": "Payment reference 4111 1111 1111 1111",
        "expected": "FLAGGED"
    }
]


# Execute validation tests
print("\nAI DATA LEAKAGE CONTROL VALIDATION")
print("=" * 45)

passed = 0
failed = 0

for test in test_cases:

    findings = detect_sensitive_information(test["input"])

    actual = "FLAGGED" if findings else "PASS"

    result = "PASS" if actual == test["expected"] else "FAIL"

    print(f"\nTest ID: {test['id']}")
    print(f"Description: {test['description']}")
    print(f"Expected: {test['expected']}")
    print(f"Actual: {actual}")
    print(f"Validation Result: {result}")

    if findings:
        print(f"Findings: {', '.join(findings)}")

    if result == "PASS":
        passed += 1
    else:
        failed += 1


print("\n" + "=" * 45)
print("VALIDATION SUMMARY")
print(f"Total Tests: {len(test_cases)}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Test Success Rate: {(passed / len(test_cases)) * 100:.1f}%")