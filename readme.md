#  CyberDefender-SIEM

A Mini Security Information and Event Management (SIEM) Tool developed using Python.

## Project Overview

Mini Security Information and Event Management (SIEM) Tool

A Python-based cybersecurity project that collects security logs, stores them in a SQLite database, detects suspicious activities, and generates alerts. This project is being developed over 30 days as an internship portfolio project.

## Technologies Used

- Python
- SQLite
- VS Code
- Git
- GitHub

---

# Day 1

## Features
- Project Setup
- Log Collection
- Log Parsing

## Files
- main.py
- src/log_collector.py
- src/parser.py
- logs/system.log

---

# Day 2

## Features
- SQLite Database Integration
- Automatic Table Creation
- Log Storage
- Persistent Security Logs

## Files Added
- src/database.py
- database/siem.db

---

## Day 3

### Features
- Threat Detection Module
- Failed Login Detection
- Displayed Security Alerts

### Files Added

- src/detector.py

---

## Day 4 – Alert Engine

### Features
- Implemented Alert Engine
- Saved security alerts into a CSV file
- Generated alerts for failed login attempts

### Technologies
- Python
- CSV
- SQLite

---

## Day 5

Implemented a SIEM Dashboard that displays:

- Total Logs
- Successful Login Attempts
- Failed Login Attempts
- Real-time Log Statistics

---

## Day 6 – Brute Force Attack Detection

### Features

- Detects repeated failed login attempts.
- Identifies suspicious IP addresses.
- Generates CRITICAL alerts for brute-force attacks.
- Uses SQL GROUP BY and HAVING for attack detection.

---

## Day 7 – Log Severity Classification

### Features
- Detects failed login attempts.
- Identifies brute-force attacks.
- Classifies logs based on severity.
- Displays a security dashboard.
- Stores alerts in CSV format.

### Technologies
- Python
- SQLite
- CSV
- Git
- GitHub

---

## ✅ Day 8 - Email Alert Notification

### New Feature
- Sends email alerts automatically when HIGH severity events are detected.
- Uses Gmail SMTP with App Password authentication.
- Notifies the administrator instantly.

---

## 📧 Day 8 - Email Alert Notification

### Terminal Output

![Email Alert Terminal](screenshot/email_alert_terminal.png)

### Email Received

![Gmail Alert](screenshot/gmail_alert.png)

---

## ✅ Day 9 - Flask Web Dashboard

### New Features
- Developed a web-based SIEM dashboard using Flask.
- Connected the dashboard with the SQLite database.
- Displays:
  - Total Logs
  - Successful Login Attempts
  - Failed Login Attempts
  - Recent Security Logs
- Dynamic dashboard that updates using data stored in the database.
- Simple and user-friendly web interface.

### Technologies Used
- Python
- Flask
- SQLite
- HTML
- CSS

---

## 📸 Dashboard Screenshot

![CyberDefender-SIEM Dashboard](screenshot/dashboard.png)

---

## Project Structure

CyberDefender-SIEM/
│
├── alert/
│   └── alerts.csv
│
├── database/
│   └── siem.db
│
├── logs/
│   └── sample_logs.csv
│
├── screenshots/
│   └── dashboard.png
│
├── src/
│   ├── parser.py
│   ├── database.py
│   ├── detector.py
│   ├── alert_engine.py
│   ├── dashboard.py
│   ├── brute_force.py
│   ├── severity.py
│   ├── email_alert.py
│   └── web_dashboard.py
│
├── templates/
│   └── dashboard.html
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore