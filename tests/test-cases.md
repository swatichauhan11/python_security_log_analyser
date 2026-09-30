# Test Cases

## Purpose

These test cases verify that the Python Security Log Analyzer correctly parses SSH authentication events and identifies repeated failed login attempts.

The tests use controlled authentication data from `sample_auth.log`.

---

## Test Case 1 — Successful Login Detection

**Input:**

```text
Accepted password for swati from 192.168.100.10
```

**Expected result:**

The event should be identified as:

```text
SUCCESSFUL_LOGIN
```

The analyzer should extract:

* Username: `swati`
* Source IP: `192.168.100.10`

**Expected outcome:** PASS

---

## Test Case 2 — Failed Login Detection

**Input:**

```text
Failed password for invalid user admin from 192.168.100.50
```

**Expected result:**

The event should be identified as:

```text
FAILED_LOGIN
```

The analyzer should extract:

* Username: `admin`
* Source IP: `192.168.100.50`

**Expected outcome:** PASS

---

## Test Case 3 — Failed Login Counting

The sample log contains eight failed authentication attempts.

**Expected result:**

```text
Failed authentication attempts: 8
```

**Expected outcome:** PASS

---

## Test Case 4 — Successful Login Counting

The sample log contains two successful authentication events.

**Expected result:**

```text
Successful logins: 2
```

**Expected outcome:** PASS

---

## Test Case 5 — Source IP Aggregation

Failed authentication attempts should be grouped by source IP.

**Expected result:**

```text
192.168.100.50: 6 failed attempt(s)
192.168.100.60: 1 failed attempt(s)
192.168.100.70: 1 failed attempt(s)
```

**Expected outcome:** PASS

---

## Test Case 6 — Brute-Force Detection

The configured detection threshold is:

```text
5 failed attempts
```

Source IP `192.168.100.50` generates six failed authentication attempts.

**Expected result:**

```text
[ALERT] Potential brute-force activity from 192.168.100.50
```

**Expected outcome:** PASS

---

## Test Case 7 — Isolated Failure

Source IP `192.168.100.70` generates one failed authentication attempt.

**Expected result:**

No brute-force alert should be generated for this source.

**Expected outcome:** PASS

---

## Test Case 8 — Failed Login Followed by Successful Login

Source IP `192.168.100.60` produces:

```text
09:19:02 → Failed login
09:19:41 → Successful login
```

**Expected result:**

Both events should be detected and recorded.

The sequence should be identified as requiring further investigation rather than automatically classified as malicious.

**Expected outcome:** PASS

---

## Test Case 9 — Missing Log File

Run the analyzer with a nonexistent file:

```bash
python3 analyzer.py nonexistent.log
```

**Expected result:**

```text
[ERROR] Log file not found: nonexistent.log
```

The program should exit without crashing.

**Expected outcome:** PASS

---

## Test Case 10 — Invalid Command Usage

Run the analyzer without providing a log file:

```bash
python3 analyzer.py
```

**Expected result:**

```text
Usage: python3 analyzer.py <log_file>
```

**Expected outcome:** PASS

---

## Test Summary

| Test Case | Function Tested               | Expected Result |
| --------- | ----------------------------- | --------------- |
| 1         | Successful login parsing      | PASS            |
| 2         | Failed login parsing          | PASS            |
| 3         | Failed login counting         | PASS            |
| 4         | Successful login counting     | PASS            |
| 5         | Source IP aggregation         | PASS            |
| 6         | Brute-force detection         | PASS            |
| 7         | Isolated failure handling     | PASS            |
| 8         | Failure → success correlation | PASS            |
| 9         | Missing file handling         | PASS            |
| 10        | Invalid command handling      | PASS            |

> **Note:** These are expected test outcomes based on the current implementation and controlled input. They should be marked as verified only after the commands are actually executed.

