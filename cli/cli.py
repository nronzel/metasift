from document.document import Document
from enum import Enum, auto
from utils.helpers import is_supported_filetype, is_valid_filename
from .menu_drawer import MenuDrawer
from .input_handler import InputHandler
from .document_action import DocumentAction

import os


# ANSI colors for console output
class Color(Enum):
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    RESET = "\033[0m"


# State machine pattern used for future expansion of menu system.
# To expand:
# Add new value to State enum
# Add new method to handle that state
# Add entry to self.state_handlers that maps state to method
class State(Enum):
    MAIN_MENU = auto()


class CLI:
    def __init__(self):
        self.document = None
        self.state = State.MAIN_MENU
        self.state_handlers = {
            State.MAIN_MENU: self._handle_main_menu_state,
        }
        self.menu_drawer = MenuDrawer()
        self.input_handler = InputHandler()
        self.document_action = None

    def _handle_main_menu_state(self):
        self.state = State.MAIN_MENU
        options = {
            "1": {"text": "Extract metadata", "action": self._extract_metadata},
            "2": {
                "text": "Clean metadata *coming soon",
                "action": self._clean_metadata,
            },
            "3": {
                "text": "Remove password protection (.docx only)",
                "action": self._unlock_docx,
            },
        }
        self.menu_drawer.draw_menu("Main Menu", options)
        action, should_quit = self.input_handler.get_choice(options)
        if should_quit:
            self._quit()
        elif action:
            action()
        else:
            print("\nInvalid option, try again.")

    def _extract_metadata(self):
        self._get_and_check_input()
        self.document_action = DocumentAction(self.document)
        data = self.document_action.extract_metadata()
        self._print_metadata(data)

    def _clean_metadata(self):
        pass

    def _unlock_docx(self):
        self._get_and_check_input()
        self.document_action = DocumentAction(self.document)
        self.document_action.remove_password()

    def _print_metadata(self, data):
        if data is None:
            print("\nNo data supplied to metadata printer.")
            return
        print("\n")
        for key, val in data.items():
            color = Color.GREEN.value if val else Color.RED.value

            if isinstance(val, dict):
                print(f"{color}{key}{Color.RESET.value}:")
                for subkey, subval in val.items():
                    color = Color.GREEN.value if subval else Color.RED.value
                    print(f"    {color}{subkey}{Color.RESET.value}: {subval}")
                print("\n")
            else:
                print(f"{color}{key}{Color.RESET.value}: {val}")

    def _get_and_check_input(self):
        while True:
            path = input("Please provide a path or a filename: ")
            if path.lower() in ["exit", "quit", "q"]:
                self._quit()

            is_file = is_valid_filename(path)
            is_valid_directory = os.path.isdir(path)

            if is_file and is_supported_filetype(path):
                self.document = Document(path)
                self.document.set_type("filename")
                break
            elif is_valid_directory:
                self.document = Document(path)
                self.document.set_type("directory")
                break
            else:
                print("\nInvalid or unsupported file provided. Try again.\n")

    def _quit(self):
        self._clear_console()
        print("\nThanks for using")
        self._ascii_logo()
        print("\nGoodbye!")
        exit(0)

    def run(self):
        self._ascii_logo(True)
        while True:
            state_handler = self.state_handlers.get(self.state)
            if state_handler:
                state_handler()
            else:
                print("Invalid state")
                self._quit()

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
            f"""{Color.YELLOW.value}
                   _                      ___  _
    /'\\_/`\\       ( )_               _  /'___)( )_
    |     |   __  | ,_)   _ _   ___ (_)| (__  | ,_)
    | (_) | /'__`\\| |   /'_` )/',__)| || ,__) | |
    | | | |(  ___/| |_ ( (_| |\\__, \\| || |    | |_
    (_) (_)`\\____)`\\__)`\\__,_)(____/(_)(_)    `\\__)
    {Color.RESET.value}
    {additional_text}
    """
        )
