from document.document import Document
from enum import Enum, auto


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
        self.document = Document()
        data = self.document.extract_metadata()
        self.print_metadata(data)
        return data

    def clean_metadata(self):
        pass

    def unlock_docx(self):
        self.document = Document()
        self.document.remove_password()

    def print_metadata(self, data):
        if data is None:
            print("data was None")
            return
        print("\n")
        for key, val in data.items():
            print(f"{key}: {val}")

    def quit(self):
        print("\nThanks for using Metasift. Goodbye!")
        exit(0)

    def run(self):
        self.intro()
        while True:
            self.draw_main_menu()

    def intro(self):
        print(
            """
                   _                      ___  _
    /'\\_/`\\       ( )_               _  /'___)( )_
    |     |   __  | ,_)   _ _   ___ (_)| (__  | ,_)
    | (_) | /'__`\\| |   /'_` )/',__)| || ,__) | |
    | | | |(  ___/| |_ ( (_| |\\__, \\| || |    | |_
    (_) (_)`\\____)`\\__)`\\__,_)(____/(_)(_)    `\\__)

        by: nronzel

        If you run into any issues, bugs, or have a feature request, please
        submit an issue at https://github.com/nronzel/metasift/issues and I
        will take a look.
             """
        )
