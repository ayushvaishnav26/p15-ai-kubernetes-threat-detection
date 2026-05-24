import random

ips = [
    "192.168.1.10",
    "192.168.1.20",
    "10.0.0.5",
    "172.16.0.2"
]

actions = [
    "LOGIN_SUCCESS",
    "LOGIN_FAILED",
    "FILE_ACCESS",
    "PASSWORD_CHANGE"
]

def generate_log():
    ip = random.choice(ips)
    action = random.choice(actions)

    return f"{ip} - {action}"