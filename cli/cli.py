from document.document import Document
from enum import Enum, auto
from utils.helpers import is_supported_filetype, is_valid_filename

import os


class State(Enum):
    MAIN_MENU = auto()
    FILETYPE_SELECTION = auto()


class CLI:
    def __init__(self):
        self.document = None
        self.state = State.MAIN_MENU
        self.action = None

    def draw_menu(self, title, options):
        max_len = max(
            len(f"{key}. {val['text']}") for key, val in options.items()
        )  # Calculate max length based on key and value
        border_line = "+" + "-" * (max_len + 4) + "+"

        print("\n" + border_line)
        print(f"|  {title.center(max_len)}  |")
        print("|" + " " * (max_len + 4) + "|")

        for key, val in options.items():
            menu_item = f"{key}. {val['text']}"
            print(f"|  {menu_item.ljust(max_len)}  |")

        print("|" + " " * (max_len + 4) + "|")
        print(f"|  {'q. Quit'.ljust(max_len)}  |")
        print(border_line + "\n")

    def handle_choice(self, options):
        choice = input("Make a selection: ")
        action = options.get(choice, {}).get("action")
        if action:
            action()
        elif choice == "q":
            self.quit()
        else:
            print(f"\n{choice} is not a valid option")

    def draw_main_menu(self):
        self.state = State.MAIN_MENU
        options = {
            "1": {"text": "Extract metadata", "action": self.extract_metadata},
            "2": {"text": "Clean metadata *coming soon", "action": self.clean_metadata},
            "3": {
                "text": "Remove password protection (.docx only)",
                "action": self.unlock_docx,
            },
        }
        self.draw_menu("Main Menu", options)
        self.handle_choice(options)

    def extract_metadata(self):
        self._clear_console()
        self.get_and_check_input()
        if self.document is not None:
            data = self.document.extract_metadata()
            self.print_metadata(data)
            return data
        else:
            print("\nError: document is None")

    def clean_metadata(self):
        pass

    def unlock_docx(self):
        self._clear_console()
        self.get_and_check_input()
        if self.document is not None:
            self.document.remove_password()
        else:
            print("\nError: document is None")

    def print_metadata(self, data):
        if data is None:
            print("\nNo data supplied to metadata printer.")
            return
        print("\n")
        for key, val in data.items():
            print(f"{key}: {val}")

    def get_and_check_input(self):
        while True:
            path = input("Please provide a path or a filename: ")
            if path.lower() in ["exit", "quit", "q"]:
                self.quit()

            is_file = is_valid_filename(path)
            is_valid_directory = os.path.isdir(path)

            if is_file and is_supported_filetype(path):
                self.document = Document(path)
                self.document.set_type("filename")
                break
            else:
                print("\nInvalid or unsupported file provided. Try again.\n")

            if is_valid_directory:
                self.document = Document(path)
                self.document.set_type("directory")
                break

    def quit(self):
        self._clear_console()
        print("\nThanks for using")
        self._ascii_logo()
        print("\nGoodbye!")
        exit(0)

    def run(self):
        self._ascii_logo(True)
        while True:
            self.draw_main_menu()

    def _clear_console(self):
        if os.name == "posix":
            # Unix/Linux/MacOs/BSD/etc..
            os.system("clear")
        elif os.name in ("nt", "dos", "ce"):
            # DOS/Windows
            os.system("cls")

    def _ascii_logo(self, intro=False):
        additional_text = (
            """
        by: nronzel

        Please submit any bugs, issues, or feature requests to:
        https://github.com/nronzel/metasift/issues
            """
            if intro
            else ""
        )
        print(
            f"""
                   _                      ___  _
    /'\\_/`\\       ( )_               _  /'___)( )_
    |     |   __  | ,_)   _ _   ___ (_)| (__  | ,_)
    | (_) | /'__`\\| |   /'_` )/',__)| || ,__) | |
    | | | |(  ___/| |_ ( (_| |\\__, \\| || |    | |_
    (_) (_)`\\____)`\\__)`\\__,_)(____/(_)(_)    `\\__)
    {additional_text}
    """
        )
