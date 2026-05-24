def send_alert(threat):

    severity = threat["severity"]

    message = threat["message"]

    print(f"[{severity}] {message}")