import PyPDF2
import re

def extract_text_from_pdf(pdf_file):

    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)   
    text = re.sub(r'[^a-zA-Z0-9\s\.\,\+\#\-]', '', text)
    text = text.lower()    
    return text.strip()

def extract_email(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails[0] if emails else "Not found"


def extract_phone(text):
    phone_pattern = r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'
    phones = re.findall(phone_pattern, text)
    return phones[0] if phones else "Not found"