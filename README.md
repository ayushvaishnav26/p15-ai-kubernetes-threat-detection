# 🛡 AI Kubernetes Threat Detection System on AWS EC2

An AI-powered cybersecurity monitoring platform designed to detect suspicious activities inside Kubernetes/cloud environments using real-time monitoring, anomaly detection, Docker, Kubernetes, and AWS EC2 deployment.

---

# 🚀 Project Overview

AI Kubernetes Threat Detection System is a cloud-native cybersecurity monitoring solution that simulates Security Operations Center (SOC) behavior for Kubernetes and cloud environments.

The system continuously monitors logs, system metrics, suspicious login attempts, and anomalous activities using rule-based detection and machine learning techniques.

The platform is containerized using Docker, orchestrated with Kubernetes, and deployed on AWS EC2 for real cloud infrastructure simulation.

---

# 🎯 Objectives

- Detect suspicious activities in Kubernetes/cloud systems
- Simulate real-world SOC monitoring workflows
- Perform AI-based anomaly detection
- Visualize threats using a real-time dashboard
- Deploy monitoring system using Docker + Kubernetes + AWS

---

# 🔥 Features

## Security Monitoring
- Real-time log monitoring
- Brute-force attack detection
- Failed login detection
- Suspicious activity alerts
- CPU spike detection
- System resource monitoring

## AI / Detection
- AI anomaly detection using Isolation Forest
- Rule-based threat detection
- Threat severity classification
- Behavioral analysis

## Dashboard
- Live SOC-style dashboard
- Threat analytics
- Pie charts & timeline graphs
- Top attacking IPs
- CPU & Memory monitoring
- Kubernetes pod monitoring
- Real-time alert feed

## DevOps / Cloud
- Docker containerization
- Kubernetes deployment
- AWS EC2 deployment
- Cloud-native architecture

---

# 🧠 AI Detection Logic

The project uses:
- Isolation Forest anomaly detection
- Rule-based monitoring
- Threshold analysis
- Behavioral anomaly detection

### Example Threat Rules

| Activity | Detection |
|---|---|
| CPU Usage > 80% | Possible Crypto Mining |
| Multiple Failed Logins | Brute Force Attack |
| Suspicious Activity Spike | Possible Intrusion |
| Anomalous Behavior Score | AI Alert Trigger |

---

# ☁️ Cloud Architecture

```text
AWS EC2
    ↓
Docker Container
    ↓
Kubernetes Deployment
    ↓
AI Threat Detection Engine
    ↓
SOC Dashboard
```

---

# 🏗 System Architecture

```text
Logs / Metrics
       ↓
Detection Engine
       ↓
AI Anomaly Detection
       ↓
Alert System
       ↓
Dashboard Visualization
       ↓
Docker
       ↓
Kubernetes
       ↓
AWS EC2
```

---

# 🛠 Tech Stack

## Languages
- Python

## Libraries
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit
- Psutil
- Kubernetes Python Client

## DevOps / Cloud
- Docker
- Kubernetes
- AWS EC2

## Tools
- VS Code
- GitHub
- Docker Desktop

---

# 📋 Requirements

## Software Requirements

- Python 3.10+
- Docker Desktop
- Kubernetes Enabled
- Git
- VS Code
- AWS Account
- EC2 Ubuntu Instance

## Python Libraries

Install using:

```bash
pip install -r requirements.txt
```

Required packages:

```text
streamlit
streamlit-autorefresh
pandas
numpy
scikit-learn
plotly
psutil
kubernetes
```

---

# 📂 Project Structure

```text
AI-Kubernetes-Threat-Detection/
│
├── dashboard/
│   └── app.py
│
├── detector/
│   ├── __init__.py
│   ├── anomaly_detector.py
│   ├── alert_system.py
│   └── rules_engine.py
│
├── simulator/
│   ├── __init__.py
│   ├── k8s_monitor.py
│   ├── log_generator.py
│   └── system_monitor.py
│
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
│
├── logs/
│   └── generated_logs.txt
│
├── screenshots/
│
├── requirements.txt
├── Dockerfile
├── start.sh
├── main.py
└── README.md
```

---

# ⚙️ Local Installation

## Clone Repository

```bash
git clone https://github.com/your-username/AI-Kubernetes-Threat-Detection.git
```

## Enter Project Folder

```bash
cd AI-Kubernetes-Threat-Detection
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Locally

## Start Detection Engine

```bash
python main.py
```

## Start Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build -t ai-threat-dashboard .
```

## Run Docker Container

```bash
docker run -p 8501:8501 ai-threat-dashboard
```

---

# ☸️ Kubernetes Deployment

## Apply Deployment

```bash
kubectl apply -f kubernetes/deployment.yaml
```

## Apply Service

```bash
kubectl apply -f kubernetes/service.yaml
```

## Check Pods

```bash
kubectl get pods
```

Dashboard URL:

```text
http://localhost:30007
```

---

# ☁️ AWS EC2 Deployment

## EC2 Setup
- Launch Ubuntu EC2 Instance
- Open Ports:
  - 22 (SSH)
  - 80 (HTTP)
  - 443 (HTTPS)
  - 8501 (Streamlit)

## SSH Into EC2

```bash
ssh -i ai-threat-key.pem ubuntu@YOUR_PUBLIC_IP
```

## Install Docker

```bash
sudo apt update
sudo apt install docker.io -y
```

## Clone Repository

```bash
git clone YOUR_REPOSITORY_URL
```

## Run Project

```bash
docker build -t ai-threat-dashboard .
docker run -p 8501:8501 ai-threat-dashboard
```

---

# 📊 Dashboard Features

- Live Threat Feed
- Threat Analytics
- Pie Chart Visualization
- Timeline Graphs
- Kubernetes Pod Monitoring
- CPU Usage Monitoring
- Memory Usage Monitoring
- Top Attacking IPs
- Threat Severity Alerts

---

# 🚨 Example Threat Scenarios

## Brute Force Attack
Repeated failed login attempts trigger HIGH/CRITICAL alerts.

## Crypto Mining Detection
High CPU usage triggers anomaly detection alerts.

## Suspicious Behavior
AI model identifies unusual activity scores.

---

# 📸 Screenshots

Add screenshots here:

- Dashboard UI
- Kubernetes Pod Monitoring
- Threat Analytics
- AWS EC2 Deployment
- Docker Containers

---

# 🔮 Future Improvements

- Prometheus Integration
- Grafana Dashboards
- Real Kubernetes Cluster Monitoring
- Email / Slack Alerts
- CI/CD Pipelines
- AWS EKS Deployment
- Threat Intelligence APIs
- SIEM Integration

---

# 🎓 Learning Outcomes

This project demonstrates:
- Kubernetes fundamentals
- Docker containerization
- Cloud deployment
- AWS EC2 management
- AI anomaly detection
- DevSecOps concepts
- SOC dashboard development
- Cybersecurity monitoring

---

# 🎤 Demo Flow

1. Start Monitoring System
2. Generate Suspicious Activity
3. Trigger Alerts
4. Show Dashboard Analytics
5. Demonstrate Kubernetes Monitoring
6. Explain AWS Cloud Deployment

---

# 📌 Conclusion

This project demonstrates how AI, cybersecurity, Docker, Kubernetes, and cloud computing can be combined to create an intelligent cloud-native threat detection platform for Kubernetes environments.

---

# 📄 License

This project is developed for educational, portfolio, and hackathon purposes.

---

# ⭐ Author

Ayush Kumar