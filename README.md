# Python Security Log Analyzer

A Python-based security log analysis tool that parses SSH authentication logs, identifies repeated failed login attempts, and detects potential brute-force activity.

## Project Overview

Security analysts regularly investigate authentication logs to identify suspicious login behavior.

This project demonstrates a lightweight detection workflow using Python to:

* Parse SSH authentication logs
* Identify successful and failed authentication events
* Extract usernames and source IP addresses
* Count failed authentication attempts
* Detect repeated failures from the same source
* Generate potential brute-force alerts
* Support basic SOC-style investigation and documentation

The project uses controlled authentication data to demonstrate the detection workflow.

---

## Detection Scenario

The primary detection scenario is repeated failed SSH authentication attempts originating from the same source IP.

```text
SSH Authentication Logs
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
```

The current detection threshold is **5 failed authentication attempts from the same source IP**.

---

## Example Detection

The sample log contains six failed authentication attempts from:

```text
192.168.100.50
```

targeting:

```text
admin
```

The analyzer identifies the repeated activity and generates:

```text
[ALERT] Potential brute-force activity from 192.168.100.50
```

The result is classified as **potential suspicious activity**, rather than confirmed malicious activity, because the project uses controlled test data.

---

## Project Structure

```text
python-security-log-analyzer/
│
├── README.md
├── analyzer.py
├── sample_auth.log
│
├── documentation/
│   ├── detection-logic.md
│   ├── investigation-notes.md
│   └── incident-timeline.md
│
└── tests/
    └── test-cases.md
```

---

## Technologies

* Python 3
* Regular expressions
* Linux authentication logs
* SSH log analysis
* File parsing
* Detection logic
* Git
* GitHub
* Kali Linux

---

## How to Run

Clone the repository and move into the project directory:

```bash
git clone https://github.com/YOUR-USERNAME/python-security-log-analyzer.git
cd python-security-log-analyzer
```

Run the analyzer against the sample authentication log:

```bash
python3 analyzer.py sample_auth.log
```

The analyzer will display:

* Total failed authentication attempts
* Total successful logins
* Failed attempts grouped by source IP
* Potential brute-force alerts
* Successful authentication events

---

## Investigation Workflow

The investigation follows a basic SOC analysis process:

### 1. Collect

Obtain authentication log data.

### 2. Parse

Extract timestamps, usernames, event types, and source IP addresses.

### 3. Analyze

Group failed authentication attempts by source IP.

### 4. Detect

Compare the number of failures against the configured threshold.

### 5. Investigate

Review suspicious activity and related authentication events.

### 6. Document

Record findings, timeline, assessment, and recommended investigation actions.

---

## Project Evidence

### Kali Project Environment

The project was developed and tested in a Kali Linux environment.

![Kali project environment](documentation/01-kali-project-setup.png)

### Project Structure

The project files and directories were organized into source code, authentication data, documentation, and test cases.

![Project structure](documentation/02-project-folder.png)

### Analyzer Implementation

The detection engine is implemented in `analyzer.py`.

![Analyzer implementation](documentation/03-analyzer-code.png)

### Analyzer Execution

The analyzer was executed against the sample authentication log.

![Analyzer execution](documentation/05-analyzer-execution.png)

### Detection Result

The analyzer identified repeated authentication failures from the same source IP and generated a potential brute-force alert.

![Detection alert](documentation/06-detection-alert.png)

---

## Learning Outcomes

This project provided practical experience with:

* Authentication log analysis
* Python-based security automation
* Regular-expression based log parsing
* Source IP aggregation
* Threshold-based detection
* Brute-force detection concepts
* SOC investigation workflows
* Security finding documentation
* Git and GitHub project management

---

## Limitations and Future Improvements

The current version is intentionally lightweight and uses controlled sample data.

Future improvements could include:

* Time-window based detection
* Multiple-account targeting detection
* Successful-login-after-failure correlation
* IP reputation enrichment
* Integration with a SIEM
* Alert severity classification
* CSV/JSON output
* Automated reporting

---

## Disclaimer

This project is intended for educational and defensive cybersecurity purposes. The authentication data used for analysis is controlled test data.

## Project Evidence

### Kali Project Setup

The project was developed and tested in a Kali Linux environment.

<img width="457" height="303" alt="image" src="https://github.com/user-attachments/assets/478448e4-382e-4dc5-97de-c6f93963c7f4" />

### Analyser.py Code 

<img width="477" height="342" alt="image" src="https://github.com/user-attachments/assets/656438da-8e06-432e-972a-ec216539cca8" />


