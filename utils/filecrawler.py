import os

from .helpers import color_print, is_supported_filetype


# To be used at a future point when more filetypes are supported
class FileCrawler:
    @staticmethod
    def crawl_for_supported_files(directory):
        supported_files = []
        directory = os.path.abspath(directory)

        if not os.path.exists(directory):
            raise FileNotFoundError("The specified directory does not exist.")

        color_print("yellow", "\nSearching for supported files...")
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath) and is_supported_filetype(filename):
                supported_files.append(filepath)
                color_print("green", f"FOUND -> {filename}")

        return supported_files
