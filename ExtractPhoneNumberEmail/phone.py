import re

def extract_phone_numbers(email_body):
    # Regular expression pattern for phone numbers
    phone_number_pattern = re.compile(r'''
        # Don't match beginning of string
        (?<!\d)
        (
            # Match country code
            (\+?\d{1,3}[\s.-]?)?
            # Match area code
            (\(?\d{3}\)?[\s.-]?)
            # Match first 3 digits
            \d{3}
            # Match separator
            [\s.-]?
            # Match last 4 digits
            \d{4}
            # Extension
            (\s?(ext|x|ext.)\s?\d{2,5})?
        )
        # Don't match end of string
        (?!\d)
    ''', re.VERBOSE)

    # Find all matches in the email body
    phone_numbers = phone_number_pattern.findall(email_body)
    # Extract the matched phone numbers
    extracted_phone_numbers = [match[0] for match in phone_numbers]
    return extracted_phone_numbers

# Example usage
if __name__ == "__main__":
    email_body = """
    Hello,

    You can reach me at (123) 456-7890 or 987-654-3210. Alternatively, my office number is 123.456.7890 ext. 1234. 
    If you need any assistance, please call +1-800-555-1234.

    Best regards,
    John Doe
    """
    phone_numbers = extract_phone_numbers(email_body)
    print("Extracted phone numbers:", phone_numbers)