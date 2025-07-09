import requests

def get_location(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    return {
        "IP": ip,
        "City": data.get("city"),
        "Region": data.get("region"),
        "Country": data.get("country"),
        "Location": data.get("loc"),
        "ISP": data.get("org")
    }

# Paste Phone A's IP here:
ip = "192.168.3.252"

print(get_location(ip))
