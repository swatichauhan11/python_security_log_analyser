# Investigation Notes

## Investigation Objective

Analyze authentication log activity and determine whether any events indicate suspicious or potentially malicious login behavior.

The investigation focuses on identifying repeated authentication failures, unusual source IP activity, and authentication sequences that may require further investigation.

---

## Data Source

**Log Type:** SSH authentication log

**Source:** `sample_auth.log`

**Environment:** Controlled test data created for this project

---

## Initial Observations

The sample contains both successful and failed authentication events.

Observed activity includes:

* Successful authentication from `192.168.100.10`
* Multiple failed authentication attempts from `192.168.100.50`
* Failed authentication followed by successful authentication from `192.168.100.60`
* An isolated failed authentication attempt from `192.168.100.70`

---

## Suspicious Activity

The repeated authentication failures originating from:

```text
192.168.100.50
```

are the primary event of interest.

Multiple attempts target the `admin` account within a short period.

This behavior is consistent with a potential password-guessing or brute-force pattern.

The activity should be investigated further rather than immediately treated as confirmed malicious activity.

---

## Investigation Questions

The following questions will be answered after the analyzer is implemented:

1. How many failed authentication attempts occurred?
2. Which source IP generated the highest number of failures?
3. Which usernames were targeted?
4. Did the failures occur within the configured detection window?
5. Did any successful login occur after repeated failures?
6. Which events triggered the detection rule?

---

## Analyst Assessment

At this stage, the log contains activity that warrants investigation.

The repeated failures from `192.168.100.50` represent the strongest suspicious pattern in the sample.

Final classification will be based on the results produced by the Python detection logic.

---

## Response / Recommended Investigation Actions

If this pattern were observed in a real environment, an analyst could:

* Review additional authentication logs.
* Determine whether the source IP is known or trusted.
* Check whether the targeted account is legitimate.
* Review successful logins from the same source.
* Correlate the activity with endpoint and network telemetry.
* Consider account protection measures if malicious activity is confirmed.

---

## Evidence

Detection output and screenshots will be added after the analyzer is implemented and tested.
