import re

def extract_contacts(text):
    email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'
    phone_pattern = r'(?:\+91\s?)?[6-9]\d{9}'

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    return {
        "emails": emails,
        "phones": phones
    }


text = "Contact support at ravi.kumar@techcorp.in or admin@sales.co. Direct helpline: +91 9876543210 or call 8765432109."

print(extract_contacts(text))