import re


def is_valid_filename(text):
    pattern = r".*\.[a-zA-Z]{3,4}$"
    return bool(re.match(pattern, text.strip()))


def is_supported_filetype(text):
    supported_filetypes = {
        ".docx",
        ".pdf",
        ".jpg",
        ".png",
    }
    text = text.strip().lower()
    return any(text.endswith(ext) for ext in supported_filetypes)
