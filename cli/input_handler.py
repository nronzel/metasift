from utils.helpers import color_print, is_supported_filetype, is_valid_filename
from document.document import Document

import os


class InputHandler:
    @staticmethod
    def get_choice(options):
        choice = input("Make a selection: ")
        if choice.lower() in ["q", "exit", "quit"]:
            return None, True
        return options.get(choice, {}).get("action"), False

    def get_file(self, prompt):
        return input(prompt)

    @staticmethod
    def validate_and_create_document(path):
        is_file = is_valid_filename(path)
        is_valid_directory = os.path.isdir(path)

        if is_file and is_supported_filetype(path) or is_valid_directory:
            document = Document(path)
            return document

        color_print("red", "\nInvalid/unsupported file or path provided. Try again.\n")
        return None
