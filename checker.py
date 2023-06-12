import time
import smtplib
from email.message import EmailMessage
import requests


def search_website(url, target_string):
    while True:
        r = requests.get(url)

        if not target_string in r.text:
            # Since we navigate to the /1 Endpoint, we should automatically land on the first step of the registration
            # If so, then "Überprüfung" should be part of the websites content
            # If not the maintenance page will be shown and we skip this check.
            if "Überprüfung" in r.text:
                print(time.strftime("%d.%m.%Y %H:%M:%S") + ": " + f"INFO: Register seems up")
                send_email_notification(url, "Registration seems up", f"Registration for {url} seems to be up.")
                break

            print(time.strftime("%d.%m.%Y %H:%M:%S") + ": " + f"Target string '{target_string}' not found on the page.")

            # Send email notification
            send_email_notification(url, "Site Content Changed", f"Site {url} has changed its content")
            break

        print(time.strftime("%d.%m.%Y %H:%M:%S") + ": " + f"Target string '{target_string}' found on the page.")

        # Wait for 5 seconds before the next search
        time.sleep(5)


def send_email_notification(website_url, title, body_msg):
    # Set up the email parameters
    sender = "PUT EMAIL HERE"  # Replace with your email address
    recipient = "PUT EMAIL HERE"  # Replace with the recipient's email address
    subject = title
    body = body_msg

    # Create the email message
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient
    message.set_content(body)

    # Send the email
    # If you don't want to use E-Mail, just place a # before each E-Mail line.
    smtp_server = "PUT SMTP SERVER HERE"  # Replace with your SMTP server
    smtp_port = 587  # Replace with the SMTP server port
    smtp_username = "PUT EMAIL HERE"  # Replace with your SMTP server username
    smtp_password = "PUT PASSWORD HERE"  # Replace with your SMTP server password

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)


# Example usage
website_url = "https://anmelden.deutsch-franzoesischer-interrail-pass.de/1"  # Replace with your desired website URL
string_to_search = "Liebe Interessenten, wir haben viele Anträge erhalten, die im Moment bearbeitet werden. Sobald alle Anträge bearbeitet wurden, wird die Plattform wieder geöffnet, um neue Anträge aufzunehmen. Vielen Dank für deine Geduld."
search_website(website_url, string_to_search)
