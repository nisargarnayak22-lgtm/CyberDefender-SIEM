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

## Day 3

### Features
- Threat Detection Module
- Failed Login Detection
- Displayed Security Alerts

### Files Added

- src/detector.py

### Output

The SIEM now identifies failed login attempts from stored security logs and displays security alerts.

## Project Structure

CyberDefender-SIEM/
│
├── database/
│   └── siem.db
│
├── logs/
│   └── system.log
│
├── src/
│   ├── __pycache__/        (Ignored by Git using .gitignore)
│   ├── database.py
│   ├── detector.py
│   ├── log_collector.py
│   └── parser.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore