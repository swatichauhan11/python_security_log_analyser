# Investigation Notes

## Investigation Objective

The objective of this investigation was to analyze SSH authentication activity and identify suspicious login behavior that could indicate password-guessing or brute-force activity.

The analysis was performed using a controlled authentication log and a Python-based security log analyzer.

---

## Data Source

**Log file:** `sample_auth.log`

**Log type:** SSH authentication events

**Environment:** Kali Linux

The log contains both successful and failed authentication events so that normal activity can be compared with potentially suspicious behavior.

### Authentication Log Evidence

The sample log contains:

* Successful authentication
* Isolated failed authentication
* Multiple failed authentication attempts from the same source IP
* A failed login followed by a successful login

---

## Initial Observations

The following authentication activity was identified:

### 1. Normal Successful Authentication

A successful SSH login was observed from:

```text
Source IP: 192.168.100.10
User: swati
Time: 09:14:22
```

**Assessment:** Normal authentication activity within the controlled test environment.

---

### 2. Repeated Failed Authentication

Six failed authentication attempts were observed from:

```text
Source IP: 192.168.100.50
Target user: admin
Time range: 09:18:03 – 09:18:24
```

The attempts occurred within a short period and originated from the same source IP.

This pattern triggered the configured detection threshold.

**Assessment:** Potential brute-force or password-guessing activity requiring investigation.

---

### 3. Failed Login Followed by Successful Login

Authentication activity from:

```text
Source IP: 192.168.100.60
User: testuser
```

included a failed login followed by a successful login.

**Assessment:** Requires investigation and correlation with additional security telemetry. A successful login after a failure does not by itself establish malicious activity.

---

### 4. Isolated Failed Authentication

A single failed authentication attempt was observed from:

```text
Source IP: 192.168.100.70
User: root
Time: 09:22:18
```

**Assessment:** Isolated failed authentication. Insufficient evidence by itself to classify the activity as brute-force behavior.

---

## Detection Results

The Python Security Log Analyzer processed the authentication log and produced the following results:

```text
Failed authentication attempts: 8
Successful logins: 2
```

The failed-login distribution was:

```text
192.168.100.50: 6 failed attempts
192.168.100.60: 1 failed attempt
192.168.100.70: 1 failed attempt
```

The analyzer generated an alert for:

```text
[ALERT] Potential brute-force activity from 192.168.100.50
```

The detection was triggered because the source generated six failed authentication attempts, exceeding the configured threshold of five failures.

---

## Key Finding

The primary finding was repeated failed SSH authentication activity from:

```text
192.168.100.50
```

targeting:

```text
admin
```

The six failed attempts occurred between:

```text
09:18:03
09:18:07
09:18:11
09:18:15
09:18:19
09:18:24
```

The repeated failures from a single source within a short period form a pattern consistent with potential password-guessing or brute-force behavior.

Because the data is controlled test data, the activity is classified as **potential suspicious activity**, not confirmed malicious activity.

---

## Investigation Assessment

The analysis demonstrates why authentication events should be evaluated as a pattern rather than individually.

A single failed login does not necessarily indicate an attack. However, repeated failures from the same source targeting the same account provide a stronger reason for investigation.

The analyzer successfully differentiated between:

* Normal successful authentication
* Individual failed authentication
* Repeated authentication failures
* Failed authentication followed by successful authentication

This prevents every failed login from being automatically classified as an attack.

---

## Recommended SOC Investigation Actions

If the repeated authentication pattern were observed in a real environment, an analyst could perform additional investigation by:

1. Checking whether the source IP is known or trusted.
2. Reviewing additional SSH authentication logs.
3. Checking whether other usernames were targeted by the same source.
4. Looking for successful authentication from the suspicious source.
5. Correlating the source IP with firewall, endpoint, and network telemetry.
6. Reviewing the affected account for other unusual activity.
7. Applying appropriate account or network controls if malicious activity is confirmed.

---

## Limitations

This project uses controlled sample data rather than production security telemetry.

The current detection logic is based primarily on the number of failed authentication attempts associated with a source IP.

It does not yet provide:

* Production SIEM correlation
* Threat-intelligence enrichment
* Geographic IP analysis
* Advanced behavioral baselines
* Multi-stage attack correlation
* Automated response actions

These could be considered future enhancements.

---

## Conclusion

The investigation identified a clear repeated-authentication pattern from `192.168.100.50` and the Python analyzer correctly generated a potential brute-force alert after the configured threshold was exceeded.

The project demonstrates a basic SOC workflow:

```text
Authentication Logs
        ↓
Log Parsing
        ↓
Event Extraction
        ↓
Failed Login Analysis
        ↓
Source IP Aggregation
        ↓
Detection Threshold
        ↓
Security Alert
        ↓
Investigation
        ↓
Analyst Assessment
```

The results demonstrate the practical use of Python for basic security monitoring and detection engineering.


## Evidence

### Sample_auth.log


<img width="690" height="367" alt="image" src="https://github.com/user-attachments/assets/452eafd2-e737-422f-98d2-0941a6be9085" />


### Running Analyser


<img width="635" height="461" alt="image" src="https://github.com/user-attachments/assets/42290195-726d-4b77-8732-c6313fc265fc" />


### Detection Alert 


<img width="630" height="457" alt="image" src="https://github.com/user-attachments/assets/f5b1c608-4adc-4daa-a5ec-bd373ba6dee6" />

