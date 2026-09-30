# Python Security Log Analyzer

A Python-based security log analysis project designed to identify suspicious authentication activity and potential brute-force attacks from Linux authentication logs.

## Project Overview

Security teams regularly analyze authentication logs to identify abnormal login activity, repeated authentication failures, suspicious source addresses, and possible brute-force attempts.

This project implements a lightweight Python-based detection tool that processes authentication logs and highlights suspicious login behavior.

The project focuses on understanding the fundamentals of:

* Security log analysis
* Authentication monitoring
* Failed-login detection
* Brute-force detection
* Source IP analysis
* Detection rules
* Security alert generation
* Basic Python automation

## Objectives

The main objectives of this project are:

1. Parse authentication log entries.
2. Identify failed authentication attempts.
3. Group authentication failures by source IP and user.
4. Detect repeated failures within a defined threshold.
5. Generate alerts for potentially suspicious activity.
6. Test the detection logic using controlled log data.
7. Document the investigation process and findings.

## Detection Scenario

The primary detection scenario investigated in this project is repeated failed authentication attempts that may indicate a brute-force or password-guessing attack.

Example:

```text
Multiple failed login attempts
        ↓
Same source IP
        ↓
Repeated attempts against a user
        ↓
Threshold exceeded
        ↓
Potential brute-force activity
        ↓
Security alert
```

## Project Structure

```text
python-security-log-analyzer/
│
├── analyzer.py
├── sample_auth.log
├── README.md
│
├── documentation/
│   ├── detection-logic.md
│   ├── investigation-notes.md
│   └── incident-timeline.md
│
└── tests/
    └── test-cases.md
```

## Technologies

* Python 3
* Linux authentication logs
* Regular expressions
* File parsing
* Basic security detection logic
* Git & GitHub

## Project Evidence

### Kali Project Setup

The project was developed and tested in a Kali Linux environment.

![Kali project setup](documentation/01-kali-project-setup.png)


## Current Status

🚧 Project under development.

The repository structure and documentation framework have been created. Detection logic, testing, and investigation evidence will be added as the project progresses.

## Learning Outcomes

By completing this project, I aim to develop practical understanding of:

* How authentication logs are structured
* How security analysts identify suspicious login patterns
* How simple detection rules can be implemented using Python
* How security findings are documented
* How detection logic can be tested against known scenarios


