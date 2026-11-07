
import urllib.request
import json
import socket

def check_ip():
    url = "https://ipapi.co/json/"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())

        print("\n===== NETWORK INFORMATION =====")
        print(f"Public IP: {data.get('ip')}")
        print(f"Country:   {data.get('country_name')}")
        print(f"City:      {data.get('city')}")
        print(f"ISP:       {data.get('org')}")

    except Exception as error:
        print(f"Network check failed: {error}")

def check_dns():
    try:
        print("\n===== DNS RESOLUTION =====")
        print(socket.gethostbyname("example.com"))

    except socket.gaierror as error:
        print(f"DNS error: {error}")

if __name__ == "__main__":
    check_ip()
    check_dns()
