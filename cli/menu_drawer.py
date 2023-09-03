class MenuDrawer:
    @staticmethod
    def draw_menu(title, options):
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
