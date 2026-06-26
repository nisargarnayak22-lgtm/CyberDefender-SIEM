# CyberShield-SIEM

A Mini Security Information and Event Management (SIEM) Tool developed using Python.

## Project Overview

CyberShield-SIEM collects security logs, parses them, stores them in a SQLite database, detects suspicious activities, and generates security alerts.

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

## Project Structure

CyberShield-SIEM/

├── database/

│ └── siem.db

├── logs/

│ └── system.log

├── src/

│ ├── database.py

│ ├── log_collector.py

│ └── parser.py

├── main.py

├── README.md

├── requirements.txt

└── .gitignore