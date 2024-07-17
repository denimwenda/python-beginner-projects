import imaplib
import email
from email.header import decode_header

def check_mail(username, password, imap_server='imap.gmail.com', imap_port=993):
    # Connect to the server
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)

    try:
        # Login to your account
        mail.login(username, password)

        # Select the mailbox you want to check (default is 'inbox')
        mail.select("inbox")

        # Search for all unseen emails
        status, messages = mail.search(None, 'UNSEEN')

        # Convert messages to a list of email IDs
        mail_ids = messages[0].split()

        for mail_id in mail_ids:
            # Fetch the email by ID
            status, msg_data = mail.fetch(mail_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Parse the email content
                    msg = email.message_from_bytes(response_part[1])

                    # Decode email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else 'utf-8')

                    # Decode email sender
                    from_ = msg.get("From")

                    print(f"Subject: {subject}")
                    print(f"From: {from_}")

                    # If the email message is multipart
                    if msg.is_multipart():
                        for part in msg.walk():
                            # Extract content type of the email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            try:
                                # Get the email body
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass

                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                # Print text/plain emails and skip attachments
                                print(body)
                            elif "attachment" in content_disposition:
                                # Download attachment
                                filename = part.get_filename()
                                if filename:
                                    with open(filename, "wb") as f:
                                        f.write(part.get_payload(decode=True))

                    else:
                        # Extract content type of the email
                        content_type = msg.get_content_type()

                        # Get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            # Print only text email parts
                            print(body)

                    print("="*50)

        # Close the connection and logout
        mail.close()
        mail.logout()

    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")

if __name__ == "__main__":
    # Replace with your email and password
    EMAIL = "your_email@example.com"
    PASSWORD = "your_password"
    check_mail(EMAIL, PASSWORD)
