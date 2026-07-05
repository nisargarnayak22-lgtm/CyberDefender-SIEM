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

## 🚨 Day 4 - Alert Engine

The Alert Engine analyzes security logs and generates alerts whenever suspicious activities such as multiple failed login attempts are detected.

### Alert Engine Screenshot

![Alert Engine](screenshot/alert_engine.png)

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

## 🚨 Day 6 - Brute Force Attack Detection

The SIEM system detects repeated failed login attempts from the same IP address and raises a **CRITICAL** brute force attack alert.

### Brute Force Detection

![Brute Force Detection](screenshot/brute_force_detection.png)

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


## 🚨 Day 7 - Log Severity Classification

The SIEM system classifies security events based on their severity level.

- 🟢 LOW – Successful login events
- 🔴 HIGH – Failed login events

### Log Severity Classification

![Log Severity Classification](screenshot/severity_classification.png)

---

## ✅ Day 8 - Email Alert Notification

### New Feature
- Sends email alerts automatically when HIGH severity events are detected.
- Uses Gmail SMTP with App Password authentication.
- Notifies the administrator instantly.


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


## 📸 Dashboard Screenshot

![CyberDefender-SIEM Dashboard](screenshot/dashboard.png)

---

## 📅 Day 10 - Recent Alerts Dashboard

### 🚀 Features Added

- Developed a dedicated **Recent Alerts Dashboard** using Flask.
- Displays only the latest failed login attempts in a separate web interface.
- Shows detailed information including **Timestamp, User, IP Address, and Event**.
- Improved dashboard readability by displaying only the most recent records.
- Enhanced the SIEM monitoring interface for quick analysis of suspicious login activities.

### 🛠 Tools & Technologies Used

- Python
- Flask
- SQLite
- HTML
- Jinja2 Templates
- Visual Studio Code

### 📸 Dashboard Overview

Displays an overview of the SIEM statistics including total logs, successful logins, failed logins, and recent log records.

![Dashboard Overview](screenshot/dashboard.png)

### 📸 Recent Alerts Dashboard

Displays the latest failed login attempts separately, making it easier to monitor suspicious activities in real time.

![Recent Alerts Dashboard](screenshot/recent_alerts_dashboard.png)

---

## 📅 Day 11 - Search & Filter Dashboard

### 🚀 Features Added

- Added search functionality to filter logs by username.
- Added event filtering for LOGIN_SUCCESS and LOGIN_FAILED.
- Improved dashboard usability with dynamic log filtering.
- Displays only relevant log records based on user input.

### 🛠 Tools & Technologies Used

- Python
- Flask
- SQLite
- HTML
- Jinja2 Templates
- Visual Studio Code

### 📸 Search & Filter Dashboard

![Search & Filter Dashboard](screenshot/search_filter_dashboard.png)

## Project Structure

CyberDefender-SIEM/
│
├── database/
│   └── siem.db
│
├── screenshot/
│
├── src/
│   ├── alert_engine.py
│   ├── brute_force.py
│   ├── database.py
│   ├── email_alert.py
│   ├── logger.py
│   ├── severity.py
│   └── web_dashboard.py
│
├── templates/
│   ├── dashboard.html
│   └── alerts.html      
│
├── main.py
├── requirements.txt
└── README.md