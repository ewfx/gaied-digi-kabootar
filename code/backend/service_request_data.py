import re

def extract_email_headers(email_text):
    """
    Extract 'To', 'From', 'Date', 'Dear', and 'Sincerely'  fields from the email text.

    Args:
        email_text (str): The raw email text.

    Returns:
        dict: A dictionary containing the extracted fields.
    """
    headers = {}
    to_match = re.search(r"(?i)^To:\s*(.*)", email_text, re.MULTILINE)
    from_match = re.search(r"(?i)^From:\s*(.*)", email_text, re.MULTILINE)
    date_match = re.search(r"(?i)^Date:\s*(.*)", email_text, re.MULTILINE)
    dear_match = re.search(r"(?i)^Dear\s*(.*)", email_text, re.MULTILINE)
    sincerely_match = re.search(r"(?i)^Sincerely,\s*(.*)", email_text, re.MULTILINE)

    # Add fields to headers only if they are found
    if to_match and to_match.group(1).strip():
        headers["To"] = to_match.group(1).strip()
    if from_match and from_match.group(1).strip():
        headers["From"] = from_match.group(1).strip()
    if date_match and date_match.group(1).strip():
        headers["Date"] = date_match.group(1).strip()
    if dear_match and dear_match.group(1).strip():
        headers["Dear"] = dear_match.group(1).strip()
    if sincerely_match and sincerely_match.group(1).strip():
        headers["Sincerely"] = sincerely_match.group(1).strip()

    return headers