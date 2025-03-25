import hashlib

def is_duplicate_email(email_text, seen_hashes, seen_files):
    """
    Check if the email content is a duplicate based on its hash.

    Args:
        email_text (str): The content of the email.
        seen_hashes (dict): A dictionary mapping hashes to file names.
        seen_files (dict): A dictionary mapping hashes to file names.

    Returns:
        tuple: (bool, str) - True if the email is a duplicate, and the file name of the original email.
    """
    email_hash = hashlib.md5(email_text.encode('utf-8')).hexdigest()
    if email_hash in seen_hashes:
        return True, seen_hashes[email_hash]
    seen_hashes[email_hash] = seen_files
    return False, None