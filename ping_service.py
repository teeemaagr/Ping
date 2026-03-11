
import time
import json
import subprocess
statuses = {}
def ping(ip):
            
            result=subprocess.run(
            ["ping", "-c", "1", ip],
            stdout=subprocess.DEVNULL
        )
            return result.returncode == 0

def ping_loop():
    while True:
        with open("ips.json", "r") as file:
            ips = json.load(file)

        for ip in ips:
            statuses[ip] = ping(ip)

        time.sleep(5)