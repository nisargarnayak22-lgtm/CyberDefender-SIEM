🛡 CyberDefender-SIEM

Python • Flask • SQLite • HTML • CSS • Jinja2

Security Information and Event Management (SIEM) Platform for Real-Time Threat Detection & Security Monitoring

CyberDefender-SIEM is a lightweight Security Information and Event Management (SIEM) platform developed to collect, analyze, and monitor authentication logs through an interactive Flask dashboard. The system detects suspicious activities, generates security alerts, and provides multiple dashboards for threat investigation, user activity monitoring, and incident reporting.

---

# ✨ Features

- Centralized Log Collection
- Log Parsing & Analysis
- SQLite Database Integration
- Brute Force Detection
- Security Alert Generation
- Security Analytics Dashboard
- User Activity Monitoring
- Login Timeline Analysis
- Incident Reporting
- System Health Monitoring
- CSV Report Export
- User & IP Search

---

# 🔄 SIEM Workflow

```text
Start Application
        │       
        ▼
Collect Security Logs
        │
        ▼
Parse & Process Logs
        │
        ▼
Store Events in SQLite Database
        │
        ▼
Threat Detection Engine
        │
        ▼
Generate Security Alerts
        │
        ▼
Update Security Dashboards
 │
        ├──────────────► Security Analytics
        │
        ├──────────────► Incident Reports
        │
        ├──────────────► User Activity Monitoring
        │
        ├──────────────► Login Timeline
        │
        └──────────────► System Health Dashboard

---

# 📸 Dashboard Preview

## 🔐 Professional Dashboard

![Professional Dashboard](screenshots/dashboard.png)

---

## 📊 Security Analytics

![Security Analytics](screenshots/security_analytics_dashboard.png)

---

## 👥 User Activity Report

![User Activity Report](screenshots/user_activity_report.png)

---

## 📈 Login Timeline

![Login Timeline](screenshots/login_activity_timeline.png)

---

## 🚨 Security Incident Report

![Security Incident Report](screenshots/incident_report_dashboard.png)

---

## 💚 System Health Dashboard

![System Health Dashboard](screenshots/system_health_dashboard.png)

---

#  project structure

               CyberDefender-SIEM

             Flask Web Dashboard
                     │
                     ▼
              Log Collection
                     │
                     ▼
                Log Parser
                     │
                     ▼
              SQLite Database
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
 Threat Engine   Alert Engine   Analytics
        │            │            │
        └────────────┼────────────┘
                     ▼
          Security Monitoring Reports

---

# 📁 Project Structure

CyberDefender-SIEM/
│
├── alerts/           Security alerts
├── database/         SQLite database
├── logs/             Authentication logs
├── screenshots/      Dashboard screenshots
├── src/              Backend source code
├── static/           CSS & static assets
├── templates/        HTML templates
│
├── main.py           Application entry point
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore

---

# 🛠 Technology Stack
 __ __ __ __ __ __ __ __ __ __ __ __ __ __
| Component        | Technology          |
| ---------------- | ------------------- |
| Language         | Python 3            |
| Backend          | Flask               |
| Database         | SQLite              |
| Frontend         | HTML5, CSS3, Jinja2 |
| Threat Detection | Python              |
| Reporting        | CSV Export          |
| Version Control  | Git & GitHub        | 
__ __ __ __ __ __ __ __ __ __ __ __ __ __ 
---

# 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/nisargarnayak22-lgtm/CyberDefender-SIEM.git
```

```bash
cd CyberDefender-SIEM
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```
---

# ▶ Running the Project

### Start the Flask Application

```bash
python src/web_dashboard.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 📄 Documentation

The project includes comprehensive documentation covering the core modules and architecture of the SIEM platform.

- 📌 System Architecture
- 📌 Threat Detection Engine
- 📌 Security Dashboard
- 📌 Database Design
- 📌 Incident Reporting
- 📌 User Activity Monitoring
- 📌 System Health Dashboard

---

### 👨‍💻 Author

Nisarga Nayak

B.Tech – Computer Science & Engineering (Networks)

Presidency University

GitHub

https://github.com/nisargarnayak22-lgtm
