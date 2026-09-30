# Detection Logic

## Objective

The purpose of the detection logic is to identify repeated failed SSH authentication attempts that may indicate password-guessing or brute-force activity.

The detector is designed as a simple rule-based security detection mechanism.

---

## Authentication Events

The analyzer currently recognizes two SSH authentication event types:

### Failed Authentication

Example:

```text
Failed password for invalid user admin from 192.168.100.50
```

The analyzer extracts:

* Timestamp
* Username
* Source IP
* Event type

The event is classified as:

```text
FAILED_LOGIN
```

### Successful Authentication

Example:

```text
Accepted password for testuser from 192.168.100.60
```

The analyzer extracts the same basic fields and classifies the event as:

```text
SUCCESSFUL_LOGIN
```

---

## Detection Rule

The current threshold is:

```python
FAILURE_THRESHOLD = 5
```

The analyzer counts failed authentication attempts originating from each source IP.

If the number of failures from one source reaches or exceeds five:

```text
Failed attempts >= 5
```

the analyzer generates:

```text
[ALERT] Potential brute-force activity
```

---

## Detection Flow

```text
Authentication Log
        ↓
Read Log Entry
        ↓
Identify Authentication Event
        ↓
Extract Username + Source IP
        ↓
Store Failed/Successful Event
        ↓
Count Failed Attempts by IP
        ↓
Compare Count With Threshold
        ↓
Generate Alert
```

---

## Why Source IP Is Used

Grouping failures by source IP allows repeated authentication attempts from the same origin to be identified.

For example:

```text
192.168.100.50 → 6 failures
192.168.100.60 → 1 failure
192.168.100.70 → 1 failure
```

Only the first source exceeds the configured threshold.

---

## Detection Interpretation

A triggered alert does **not** automatically prove that an attack occurred.

Repeated authentication failures can have legitimate explanations, such as:

* Incorrect password
* Misconfigured automation
* Forgotten credentials
* Administrative activity
* Password guessing

Therefore, the alert should be treated as:

```text
Potential suspicious activity
```

and investigated using additional evidence.

---

## Current Limitations

The current implementation does not yet use a time-window calculation.

Therefore, the detector primarily identifies repeated failures by source IP rather than determining whether the attempts occurred within a specific rolling time period.

It also does not currently perform:

* Threat-intelligence lookups
* Geographic analysis
* Account-risk scoring
* SIEM correlation
* Automated response

---

## Future Detection Enhancements

Possible improvements include:

1. Rolling time-window detection
2. Detection of multiple targeted accounts
3. Successful login after repeated failures
4. IP reputation enrichment
5. Detection severity levels
6. SIEM integration
7. JSON/CSV alert output
8. Automated investigation reports

