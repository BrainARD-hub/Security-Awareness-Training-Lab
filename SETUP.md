# ⚙️ Security Awareness Training Lab - Setup Guide

This guide explains how to install and run all required components for the Security Awareness Training Lab on Kali Linux.

---

## ⚠️ Prerequisites

Ensure your system has:

- Kali Linux (or any Debian-based Linux)
- Python 3
- Git
- Internet connection
- Sudo privileges

---

## 📁 1. Clone the Repository

```bash
git clone https://github.com/BrainARD-hub/Security-Awareness-Training-Lab.git
cd Security-Awareness-Training-Lab
🐍 2. Install Python Dependencies

If required, install Flask:

pip3 install flask
📧 3. Install Go (Required for MailHog)

MailHog is used for capturing test emails locally.

sudo apt update
sudo apt install golang-go -y

Verify installation:

go version
📬 4. Install MailHog

Install MailHog using Go:

go install github.com/mailhog/MailHog@latest

Run MailHog:

~/go/bin/MailHog

Access dashboard:

http://localhost:8025
🎯 5. Install GoPhish

Download GoPhish:

wget https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip

Extract it:

unzip gophish-v0.12.1-linux-64bit.zip
cd gophish

Run GoPhish:

sudo ./gophish
🌐 6. Access GoPhish Dashboard

After starting GoPhish:

Admin Panel: https://127.0.0.1:3333
User Panel: http://127.0.0.1:80

Default credentials are displayed in the terminal.

🚀 7. Run the Flask OTP Server

Go back to project folder:

python3 otp_server.py "for Google" or python3 m365_server.py "for Microsoft"
