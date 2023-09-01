import re


def filename_or_directory(text):
    """
    True -> filename
    False -> directory
    """
    pattern = r"\.[a-zA-Z]{3,4}$"  # does the text end in . with 3 letters
    return re.search(pattern, text)
