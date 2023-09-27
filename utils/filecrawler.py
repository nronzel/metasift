import os

from .helpers import color_print


class FileCrawler:
    def __init__(self, supported_types):
        self.supported_types = supported_types

    def crawl(self, directory):
        supported_files = []
        directory = os.path.abspath(directory)

        if not os.path.exists(directory):
            raise FileNotFoundError("The specified directory does not exist.")

        color_print("yellow", "\nSearching for supported files...")
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            _, extension = os.path.splitext(filename)
            if os.path.isfile(filepath) and extension in self.supported_types:
                supported_files.append(filepath)
                color_print("green", f"FOUND -> {filename}")

        if not supported_files:
            color_print("red", "\nNo supported files found. Try again.\n")

        return supported_files
