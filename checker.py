import time
import smtplib
from email.message import EmailMessage
from selenium import webdriver


def search_website(url, target_string):
    while True:
        # Initialize the web driver
        driver = webdriver.Chrome()  # You'll need to have the Chrome WebDriver installed
        driver.get(url)

        # Search for the target string on the page
        page_content = driver.page_source
        if not target_string in page_content:
            print(f"Target string '{target_string}' not found on the page.")

            # Send email notification
            send_email_notification(url)

            # Close the browser
            break
        print(f"Target string '{target_string}' found on the page.")

        driver.quit()
        #
        # Wait for 30 seconds before the next search
        time.sleep(5)


def send_email_notification(website_url):
    # Set up the email parameters
    sender = "PUT EMAIL HERE"  # Replace with your email address
    recipient = "PUT EMAIL HERE"  # Replace with the recipient's email address
    subject = "Site up"
    body = f"Site is up {website_url}"

    # Create the email message
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient
    message.set_content(body)

    # Send the email
    # If you dont want to use E-Mail, just place a # before each E-Mail line.
    smtp_server = "PUT SMTP HERE"  # Replace with your SMTP server
    smtp_port = 587  # Replace with the SMTP server port
    smtp_username = "PUT EMAIL HERE"  # Replace with your SMTP server username
    smtp_password = "PUT YOUR PASSWORD HERE"  # Replace with your SMTP server password

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)


# Example usage
website_url = "https://anmelden.deutsch-franzoesischer-interrail-pass.de/"  # Replace with your desired website URL
string_to_search = "Der deutsch-französischen Freundschaftspass ist Opfer seines Erfolgs geworden. Wir haben viele Anträge erhalten, die im Moment bearbeitet werden. Sobald alle Anträge eingegangen sind, wird die Plattform wieder geöffnet, um neue Anträge aufzunehmen. Vielen Dank für deine Geduld."
search_website(website_url, string_to_search)
