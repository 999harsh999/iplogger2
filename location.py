import requests

IPINFO_TOKEN = "6c278dc38194d9"  # Your token

def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json?token={IPINFO_TOKEN}")
        data = response.json()
        return {
            "IP": ip,
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": data.get("loc"),
            "ISP": data.get("org")
        }
    except Exception as e:
        return {"error": str(e)}

# Test with a public IP (e.g., from your logs)
ip = "157.38.244.46"  # This is a public IP from your log
print(get_location(ip))
