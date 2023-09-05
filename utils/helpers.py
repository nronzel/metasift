import re
import os

from utils.ansi_colors import Color


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


def check_path_type(path):
    is_file = os.path.isfile(path) and is_supported_filetype(path)
    is_directory = os.path.isdir(path)
    if is_file:
        return "file"
    if is_directory:
        return "directory"
    return "invalid"


def color_print(color, *args, **kwargs):
    color = color.upper()
    if color in Color._member_names_:
        color_code = Color[color].value
        reset_code = Color.RESET.value
        formatted_text = " ".join(str(arg) for arg in args)
        print(f"{color_code}{formatted_text}{reset_code}", **kwargs)
    else:
        print(
            f"Invalid color specified. Available colors are {', '.join(Color._member_names_)}."
        )
