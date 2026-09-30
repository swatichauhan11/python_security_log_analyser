# Incident Timeline

## Investigation Overview

This timeline documents the authentication events observed in the controlled SSH authentication log used by the Python Security Log Analyzer.

The timestamps represent simulated test activity created for defensive security analysis.

---

## Authentication Timeline

| Time     | Source IP      | Username | Event            | Assessment                   |
| -------- | -------------- | -------- | ---------------- | ---------------------------- |
| 09:14:22 | 192.168.100.10 | swati    | Successful login | Normal authentication        |
| 09:18:03 | 192.168.100.50 | admin    | Failed login     | Suspicious pattern begins    |
| 09:18:07 | 192.168.100.50 | admin    | Failed login     | Repeated failure             |
| 09:18:11 | 192.168.100.50 | admin    | Failed login     | Repeated failure             |
| 09:18:15 | 192.168.100.50 | admin    | Failed login     | Repeated failure             |
| 09:18:19 | 192.168.100.50 | admin    | Failed login     | Repeated failure             |
| 09:18:24 | 192.168.100.50 | admin    | Failed login     | Detection threshold exceeded |
| 09:19:02 | 192.168.100.60 | testuser | Failed login     | Requires investigation       |
| 09:19:41 | 192.168.100.60 | testuser | Successful login | Requires correlation         |
| 09:22:18 | 192.168.100.70 | root     | Failed login     | Isolated event               |

---

## Key Event Sequence

The primary suspicious sequence occurred from:

```text id="o1jjl7"
192.168.100.50
```

targeting:

```text id="plc7g6"
admin
```

The source generated six failed authentication attempts:

```text id="y5q0xy"
09:18:03
09:18:07
09:18:11
09:18:15
09:18:19
09:18:24
```

The configured detection threshold was five failed attempts.

Therefore, the sixth failed attempt caused the detection rule to generate a potential brute-force alert.

---

## Investigation Sequence

```text id="i7mj7r"
09:18:03
First failed login
        ↓
09:18:07
Second failed login
        ↓
09:18:11
Third failed login
        ↓
09:18:15
Fourth failed login
        ↓
09:18:19
Fifth failed login
        ↓
09:18:24
Sixth failed login
        ↓
Threshold exceeded
        ↓
Potential brute-force alert
```

---

## Related Authentication Activity

A separate source, `192.168.100.60`, produced a failed login followed by a successful login.

This sequence was not automatically classified as malicious.

Instead, it was marked for further investigation because authentication success after a failed attempt can have both legitimate and suspicious explanations.

---

## Analyst Assessment

The repeated authentication attempts from `192.168.100.50` represent the primary suspicious pattern in the controlled dataset.

The Python analyzer correctly identified the repeated failures and generated a potential brute-force alert.

Because this is controlled test data, the result represents a **detection finding**, not confirmation of a real attack.

---

## Recommended Follow-Up

In a real SOC environment, an analyst could correlate this activity with:

* Additional authentication logs
* Account activity
* Endpoint telemetry
* Firewall logs
* Network telemetry
* Source IP reputation
* Other targeted usernames

Additional evidence would be required before taking containment or account-protection actions.
