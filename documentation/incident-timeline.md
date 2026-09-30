# Incident Timeline

## Overview

This timeline records the authentication events identified during analysis of the controlled sample log.

The timestamps below represent simulated test activity and are used to demonstrate the investigation workflow.

---

## Timeline

| Time     | Source IP      | User     | Event            | Initial Assessment            |
| -------- | -------------- | -------- | ---------------- | ----------------------------- |
| 09:14:22 | 192.168.100.10 | swati    | Successful login | Normal                        |
| 09:18:03 | 192.168.100.50 | admin    | Failed login     | Suspicious pattern begins     |
| 09:18:07 | 192.168.100.50 | admin    | Failed login     | Repeated failure              |
| 09:18:11 | 192.168.100.50 | admin    | Failed login     | Repeated failure              |
| 09:18:15 | 192.168.100.50 | admin    | Failed login     | Repeated failure              |
| 09:18:19 | 192.168.100.50 | admin    | Failed login     | Repeated failure              |
| 09:18:24 | 192.168.100.50 | admin    | Failed login     | Detection threshold candidate |
| 09:19:02 | 192.168.100.60 | testuser | Failed login     | Requires review               |
| 09:19:41 | 192.168.100.60 | testuser | Successful login | Requires correlation          |
| 09:22:18 | 192.168.100.70 | root     | Failed login     | Isolated event                |

---

## Key Event

The main event requiring investigation is the sequence of repeated failed authentication attempts from:

```text
192.168.100.50
```

targeting:

```text
admin
```

between:

```text
09:18:03 – 09:18:24
```

This sequence will be evaluated by the Python detection engine.

---

## Timeline Assessment

The timeline demonstrates why individual authentication events should be analyzed as a sequence rather than considered independently.

Repeated failures from the same source within a short period provide stronger evidence of suspicious activity than a single failed authentication attempt.

Final alert status will be updated after automated analysis.
