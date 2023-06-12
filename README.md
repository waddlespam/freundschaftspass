# Sadly, the Freundschaftspass is already over and this project is no longer in use.

# Website String Scanner and Email Notifier

This Python bot scans a website and sends an email notification when a specific string is found on the webpage. It utilizes the `requests` library for making HTTP requests and the `smtplib` library for sending emails via SMTP.

## Requirements

- Python 3.x
- `requests` library: Install using `pip install requests`
- `smtplib` library (comes pre-installed with Python)

## Usage

1. Clone the repository or download the source code.

2. Open the Python script file `checker.py` in a text editor.

3. Replace the following placeholders with your desired values:

    - `website_url`: Replace with the URL of the website you want to scan.
    - `string_to_search`: Replace with the specific string you want to search for on the website.
    - Email notification details in the `send_email_notification` function:
        - `sender`: Replace with your email address.
        - `recipient`: Replace with the recipient's email address.
        - `smtp_server`: Replace with the address of your SMTP server.
        - `smtp_port`: Replace with the port number of your SMTP server.
        - `smtp_username`: Replace with your SMTP server username.
        - `smtp_password`: Replace with your SMTP server password.

4. Save the changes to the `checker.py` file.

5. Open a terminal or command prompt and navigate to the directory where the `checker.py` file is located.

6. Run the following command to execute the Python script:

    ```
    python checker.py
    ```

7. The script will start scanning the website every 30 seconds. If the target string is found, it will print a success message and send an email notification to the specified recipient. The scanning process will continue until the target string is found.

## License

This project is dedicated to the public domain under the [Creative Commons Zero v1.0 Universal (CC0 1.0) license](https://creativecommons.org/publicdomain/zero/1.0/). You can use, modify, and distribute the code without any restrictions. Attribution is not required.

## Disclaimer

This code is provided as-is without any warranty. The author shall not be held liable for any damages or losses arising from the use of this code.
