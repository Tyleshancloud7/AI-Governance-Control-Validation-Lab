
"""
AI Governance Lab - Approved AI Tools Validation Test

Fictional organization: Meridian Health Solutions

Purpose:
Identify AI applications that are not on the organization's
approved AI tools list.

This is a simulated governance control test using synthetic data.
It does not monitor actual employee activity or network traffic.
"""

# Fictional list of organization-approved AI tools
approved_ai_tools = [
    "Microsoft Copilot",
    "ChatGPT Enterprise",
    "Google Gemini Enterprise"
]

# Synthetic employee AI application usage
employee_ai_usage = [
    {"employee": "Employee 001", "tool": "Microsoft Copilot"},
    {"employee": "Employee 002", "tool": "ChatGPT Enterprise"},
    {"employee": "Employee 003", "tool": "UnknownAI Chat"},
    {"employee": "Employee 004", "tool": "Google Gemini Enterprise"},
    {"employee": "Employee 005", "tool": "Personal ChatGPT Account"}
]

print("MERIDIAN HEALTH SOLUTIONS")
print("APPROVED AI TOOLS CONTROL TEST")
print("-" * 45)

approved_count = 0
flagged_count = 0

for activity in employee_ai_usage:
    employee = activity["employee"]
    tool = activity["tool"]

    if tool in approved_ai_tools:
        status = "APPROVED"
        approved_count += 1
    else:
        status = "FLAGGED - NOT ON APPROVED LIST"
        flagged_count += 1

    print(f"{employee}: {tool} --> {status}")

print("-" * 45)
print(f"Total activities tested: {len(employee_ai_usage)}")
print(f"Approved activities: {approved_count}")
print(f"Flagged activities: {flagged_count}")

print("\nCONTROL TEST RESULT:")
if flagged_count > 0:
    print("EXCEPTIONS IDENTIFIED - Further investigation required.")
else:
    print("NO EXCEPTIONS IDENTIFIED - No unauthorized tools detected in this sample.")
