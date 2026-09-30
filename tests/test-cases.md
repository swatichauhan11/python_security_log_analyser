# Test Cases

## Purpose

These test cases define how the Python Security Log Analyzer will be validated.

The goal is to verify that the analyzer can distinguish between normal authentication activity, isolated failures, and repeated suspicious authentication attempts.

---

## Test Case 1 — Successful Login

**Scenario:** A user successfully authenticates through SSH.

**Expected Result:** No security alert should be generated.

**Log Example:**

```text
Accepted password for swati from 192.168.100.10
```

**Expected Classification:**

```text
NORMAL
```

---

## Test Case 2 — Single Failed Login

**Scenario:** A single failed authentication attempt occurs.

**Expected Result:** The event should be recorded, but should not automatically be classified as a brute-force attack.

**Log Example:**

```text
Failed password for root from 192.168.100.70
```

**Expected Classification:**

```text
FAILED AUTHENTICATION
```

---

## Test Case 3 — Repeated Failed Logins

**Scenario:** Multiple failed authentication attempts originate from the same source IP within a short period.

**Expected Result:** The analyzer should identify the repeated activity and generate a potential brute-force alert.

**Source IP:**

```text
192.168.100.50
```

**Expected Classification:**

```text
POTENTIAL BRUTE-FORCE ACTIVITY
```

---

## Test Case 4 — Failed Login Followed by Successful Login

**Scenario:** Multiple authentication events occur, including a failed attempt followed by a successful login.

**Expected Result:** The analyzer should preserve both events so the sequence can be investigated rather than treating the successful login as automatically benign.

**Source IP:**

```text
192.168.100.60
```

**Expected Classification:**

```text
REQUIRES INVESTIGATION
```

---

## Test Case 5 — Different Source IPs

**Scenario:** Failed authentication attempts originate from different IP addresses.

**Expected Result:** Attempts from different sources should not be incorrectly combined into one brute-force event.

**Expected Classification:**

```text
SEPARATE EVENTS
```

---

## Validation Criteria

The analyzer will be considered functional when it can:

* Parse authentication events correctly.
* Identify failed authentication attempts.
* Extract source IP addresses.
* Count repeated failures.
* Apply the configured detection threshold.
* Generate an alert when the threshold is exceeded.
* Avoid treating every individual failed login as a brute-force attack.
* Provide output that can be used for further investigation.
