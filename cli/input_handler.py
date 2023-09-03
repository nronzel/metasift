class InputHandler:
    @staticmethod
    def get_choice(options):
        choice = input("Make a selection: ")
        if choice.lower() in ["q", "exit", "quit"]:
            return None, True
        return options.get(choice, {}).get("action"), False
