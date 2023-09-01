import re
import os


def is_valid_filename(text):
    pattern = r".*\.[a-zA-Z]{3,4}$"
    file = bool(re.match(pattern, text))
    if file:
        is_supported = is_supported_filetype(text)
        if not is_supported:
            print("Filetype not supported, please try again.")
        else:
            return True
    else:
        return False


def is_supported_filetype(text):
    supported_extensions = [
        ".docx",
        ".pdf",
        ".jpg",
        ".png",
    ]
    _, extension = os.path.splitext(text.strip())
    if extension.lower() in supported_extensions:
        return True
    return False
