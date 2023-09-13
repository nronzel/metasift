from utils.filecrawler import FileCrawler
from utils.helpers import color_print

import os


class InputHandler:
    def __init__(self):
        self.input_analyzer = InputAnalyzer()

    def get_choice(self, options):
        choice = input("Make a selection: ")
        if choice.lower() in ["q", "exit", "quit"]:
            return None, True
        return options.get(choice, {}).get("action"), False

    def get_path(self):
        path = input("Please provide a path or a filename: ")

        if path.lower() in ["exit", "quit", "q"]:
            return None

        return path

    def analyze(self, input):
        return self.input_analyzer.analyze(input)


class InputAnalyzer:
    def __init__(self):
        self.file_crawler = FileCrawler([".docx"])

    def analyze(self, user_input):
        if os.path.isdir(user_input):
            files = self.file_crawler.crawl(user_input)
            return files
        elif os.path.isfile(user_input):
            return [user_input]
        else:
            color_print("red", "\nInvalid input supplied. Try again.\n")
            return
