import email
from email import policy
from email.parser import BytesParser

def slice_email(raw_email):
    # Parse the raw email.
    msg = BytesParser(policy=policy.default).parsebytes(raw_email)
    
    # Extract different parts of the email.
    sender = msg['From']
    recipient = msg['To']
    subject = msg['Subject']
    date = msg['date']
    
    # Get the email body
    if msg.is_multipart():
        # If the email is multipart, get the payload and extract the text parts
        parts = msg.get_payload()
        body = ''
        for part in parts:
            if part.get_content_type() == 'text/plain':
                body += part.get_payload(decode=True).decode(part.get_content_charset())
                
    else:
        # If the email is not multipart, just get the payload
        body = msg.get_payload(decode=True).decode(msg.get_content_charset())
        
    # Return the extracted componets
    return {
        'sender': sender,
        'recipient': recipient,
        'subject': subject,
        'date': date,
        'body': body
    }
    
# Example usage
if __name__ == "__main__":
    # A sample raw email (normall you'd get this from reading an email file or stream)
    raw_email = b"Your raw email bytes here"
    
    sliced_email = slice_email(raw_email)
    print(slice_email)