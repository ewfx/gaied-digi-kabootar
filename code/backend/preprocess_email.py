# Define patterns to remove (headers, footers, account info, greetings)
import re


removal_patterns = [
    r"(?i)Citizens Bank.*",        # Remove bank names
    r"(?i)Loan Agency Services.*",  # Remove agency references
    r"(?i)Date: \d{1,2}-\w{3}-\d{4}",  # Remove dates
    r"(?i)TO:.*",  # Remove TO headers
    r"(?i)FOR:.*",  # Remove FOR headers
    r"(?i)FROM:.*",  # Remove FROM headers
    r"(?i)ATTN:.*",  # Remove ATTN fields
    r"(?i)Fax:.*",  # Remove fax details
    r"(?i)Re:.*",  # Remove subject references
    r"(?i)Description:.*",  # Remove descriptions
    r"(?i)BORROWER:.*",  # Remove borrower details
    r"(?i)DEAL NAME:.*",  # Remove deal names
    r"(?i)Reference:.*",  # Remove references
    r"(?i)Bank Name:.*",  # Remove bank name mentions
    r"ABA # \d{9}",  # Remove ABA numbers
    r"Account #: \d+",  # Remove account numbers
    r"Account Name:.*",  # Remove account name
    r"(?i)Regards,.*",  # Remove signatures
    r"(?i)Telephone #:.*",  # Remove phone numbers
    r"(?i)Fax #:.*",  # Remove fax numbers
    r"\*{5,}",  # Remove separators (****)
    r"Citizens Commercial Banking.*",  # Remove disclaimers
    r"(?i)Regards:.*",  # Remove FROM headers
]

removedText = []
cleanedText = []
def clean_text(text):
    for pattern in removal_patterns:
        cleanedText.append(re.sub(pattern, "", text, flags=re.IGNORECASE))
        removedText.append(re.findall(pattern, text))
    return cleanedText

# Clean and Pre-process Email
def clean_email_text(raw_text):
    raw_text = re.sub(r"(?i)(From:|To:|CC:|Fax:|ATTN:|Re:|Date:|Subject:|Description:|For:|BORROWER:|DEAL NAME:|Reference:).*", "", raw_text)  # Remove email headers
    raw_text = re.sub(r"(?i)Regards,.*|Best regards,.*|Confidentiality Notice:.*|Bank Name:.*|Account #.*", "", raw_text, flags=re.DOTALL)
    raw_text = re.sub(r"\b\d{10,16}\b", "", raw_text)  # Remove possible account numbers
    raw_text = re.sub(r"\n{2,}", "\n", raw_text).strip()
    return raw_text