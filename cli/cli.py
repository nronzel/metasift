from document.document import Document
from enum import Enum, auto
from utils.helpers import color_print
from .menu_drawer import MenuDrawer
from .input_handler import InputHandler

import os


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

    def _handle_main_menu_state(self):
        self.state = State.MAIN_MENU
        options = {
            "1": {"text": "Extract metadata", "action": self._extract_metadata},
            "2": {
                "text": "Clean metadata *coming soon",
                "action": self._clean_metadata,
            },
            "3": {
                "text": "Remove password protection(.docx)",
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
        self._get_input()
        if self.document is not None:
            data = self.document.extract_metadata()
            self._print_metadata(data)

    def _clean_metadata(self):
        pass

    def _unlock_docx(self):
        self._get_input()
        if self.document is not None:
            self.document.remove_password()

    def _print_metadata(self, data):
        if data is None:
            return

        print("\n")

        for dict in data:
            for key, val in dict.items():
                if key == "file":
                    color_print("yellow", f"\n{val}\n")
                    continue
                color = "green" if val else "red"
                color_print(color, f"{key}: {val}")
            print("-" * 40)  # Print a separator between dictionaries

    def _get_input(self):
        while True:
            path = self.input_handler.get_path()

            if path is None:
                self._quit()

            files = self.input_handler.analyze(path)

            document = Document(files)

            if document:
                self.document = document
                break

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
        ascii_art = f"""
                   _                      ___  _
    /'\\_/`\\       ( )_               _  /'___)( )_
    |     |   __  | ,_)   _ _   ___ (_)| (__  | ,_)
    | (_) | /'__`\\| |   /'_` )/',__)| || ,__) | |
    | | | |(  ___/| |_ ( (_| |\\__, \\| || |    | |_
    (_) (_)`\\____)`\\__)`\\__,_)(____/(_)(_)    `\\__)
    """
        complete_text = ascii_art + additional_text
        color_print("yellow", complete_text)
