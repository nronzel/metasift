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
        print(f"\n=== {title} ===\n")
        for key, val in options.items():
            if val["text"] == "Main Menu":
                print(f"\n{key}. {val['text']}")
            else:
                print(f"{key}. {val['text']}")
        print("\nq. Quit\n")

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
            "1": {
                "text": "Extract metadata",
                "action": self.set_action_and_goto_file_selection("extract_metadata"),
            },
            "2": {
                "text": "Clean metadata *coming soon",
                "action": self.set_action_and_goto_file_selection("clean_metadata"),
            },
            "3": {
                "text": "Remove password protection (.docx only)",
                "action": self.perform_unlock_docx,
            },
        }
        self.draw_menu("Main Menu", options)
        self.handle_choice(options)

    def set_action_and_goto_file_selection(self, action):
        def wrapper():
            self.action = action
            self.goto_filetype_selection()

        return wrapper

    def perform_unlock_docx(self):
        self.action = "remove_password"
        self.perform_action()

    def goto_filetype_selection(self):
        self.state = State.FILETYPE_SELECTION
        self.draw_filetype_selection_menu()

    def draw_filetype_selection_menu(self):
        options = {
            "1": {"text": ".docx", "action": self.perform_action},
            "2": {"text": ".pdf (*coming soon)", "action": None},
            "3": {"text": ".jpg or .png (*coming soon)", "action": None},
            "4": {"text": "Main Menu", "action": self.draw_main_menu},
        }
        self.draw_menu("Filetype", options)
        self.handle_choice(options)

    def perform_action(self):
        if self.action == "extract_metadata":
            self.extract_metadata()
        elif self.action == "clean_metadata":
            self.clean_metadata()
        elif self.action == "remove_password":
            self.unlock_docx()

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
            match self.state:
                case State.MAIN_MENU:
                    self.draw_main_menu()
                case State.FILETYPE_SELECTION:
                    self.draw_filetype_selection_menu()

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
