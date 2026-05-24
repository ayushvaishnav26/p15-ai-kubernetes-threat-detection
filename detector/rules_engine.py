failed_attempts = {}

THRESHOLD = 3

def detect_threat(log):

    if "LOGIN_FAILED" in log:

        ip = log.split(" - ")[0]

        if ip not in failed_attempts:
            failed_attempts[ip] = 0

        failed_attempts[ip] += 1

        count = failed_attempts[ip]

        if count >= 10:
            return {
                "message": f"CRITICAL Brute Force Attack from {ip}",
                "severity": "CRITICAL"
            }

        elif count >= 6:
            return {
                "message": f"HIGH Threat Activity from {ip}",
                "severity": "HIGH"
            }

        elif count >= 3:
            return {
                "message": f"MEDIUM Suspicious Login Attempts from {ip}",
                "severity": "MEDIUM"
            }

    return None