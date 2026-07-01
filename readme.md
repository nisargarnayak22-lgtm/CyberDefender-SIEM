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

## Day 4 – Alert Engine

### Features
- Implemented Alert Engine
- Saved security alerts into a CSV file
- Generated alerts for failed login attempts

### Technologies
- Python
- CSV
- SQLite

## Day 5

Implemented a SIEM Dashboard that displays:

- Total Logs
- Successful Login Attempts
- Failed Login Attempts
- Real-time Log Statistics

## Day 6 – Brute Force Attack Detection

### Features

- Detects repeated failed login attempts.
- Identifies suspicious IP addresses.
- Generates CRITICAL alerts for brute-force attacks.
- Uses SQL GROUP BY and HAVING for attack detection.

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

## Project Structure

CyberDefender-SIEM
│
├── alert
│    └── alerts.csv
│
├── database
│    └── siem.db
│
├── logs
│    └── sample_logs.csv
│
├── src
│    ├── parser.py
│    ├── database.py
│    ├── detector.py
│    ├── alert_engine.py
│    ├── dashboard.py
│    └── brute_force.py      ← NEW
│
├── main.py
├── README.md
└── requirements.txt