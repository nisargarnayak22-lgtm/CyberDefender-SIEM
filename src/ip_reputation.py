# IP Reputation Engine
# Day 13 - CyberDefender SIEM

BLACKLISTED_IPS = {
    "192.168.1.20",
    "203.0.113.5",
    "185.220.101.1"
}

SUSPICIOUS_IPS = {
    "192.168.1.50",
    "198.51.100.10"
}

TRUSTED_IPS = {
    "192.168.1.10",
    "192.168.1.15",
    "127.0.0.1"
}


def check_ip_reputation(ip):

    if ip in BLACKLISTED_IPS:
        return "Blacklisted"

    elif ip in SUSPICIOUS_IPS:
        return "Suspicious"

    elif ip in TRUSTED_IPS:
        return "Trusted"

    else:
        return "Unknown"


# Test the reputation engine
if __name__ == "__main__":

    test_ips = [
        "192.168.1.10",
        "192.168.1.15",
        "192.168.1.20",
        "192.168.1.50",
        "10.10.10.10"
    ]

    print("========== IP REPUTATION REPORT ==========\n")

    for ip in test_ips:
        reputation = check_ip_reputation(ip)
        print(f"{ip}  -->  {reputation}")