
from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "cakespri23@gmail.com"  
EMAIL_PASSWORD = "ignj rvbd akga lhqf"  
DESTINATION_EMAIL = "cakespri23@gmail.com"

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        email = request.form.get("email")
        if email:
            send_email(email)
            message = "Successfully joined the waitlist!"
        else:
            message = "Please enter a valid email address."

    return render_template("index.html", message=message)

def send_email(user_email):
    subject = "New Waitlist Request"
    body = f"The following email wants to join the waitlist: {user_email}"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = DESTINATION_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, DESTINATION_EMAIL, msg.as_string())
            print("Email sent successfully")
    except smtplib.SMTPAuthenticationError:
        print("Error: SMTP Authentication failed. Check email/password.")
    except smtplib.SMTPConnectError:
        print("Error: Could not connect to SMTP server.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    app.run(debug=True)
