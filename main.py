import time
import random

from simulator.log_generator import generate_log
from simulator.system_monitor import get_system_metrics

from detector.rules_engine import detect_threat
from detector.alert_system import send_alert
from detector.anomaly_detector import detect_anomaly

LOG_FILE = "logs/generated_logs.txt"

while True:

    # Generate log
    log = generate_log()

    print(f"[LOG] {log}")

    with open(LOG_FILE, "a") as file:
        file.write(log + "\n")

    # Rule-based detection
    threat = detect_threat(log)

    if threat:

        send_alert(threat)

    # AI anomaly detection
    activity_score = random.randint(1, 10)

    if detect_anomaly(activity_score):

        send_alert({
            "severity": "HIGH",
            "message": f"AI detected anomalous behavior score: {activity_score}"
        })

    # System Metrics
    metrics = get_system_metrics()

    cpu = metrics["cpu"]

    memory = metrics["memory"]

    print(f"[CPU] {cpu}%")

    print(f"[MEMORY] {memory}%")

    # CPU Threat Detection
    if cpu > 80:

        send_alert({
            "severity": "CRITICAL",
            "message": f"High CPU Usage Detected: {cpu}%"
        })

    time.sleep(2)