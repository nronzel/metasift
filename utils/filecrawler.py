import os

from utils.helpers import is_supported_filetype


class FileCrawler:
    @staticmethod
    def crawl_for_supported_files(directory):
        supported_files = []
        directory = os.path.abspath(directory)

        if not os.path.exists(directory):
            raise FileNotFoundError("The specified directory does not exist.")

        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath) and is_supported_filetype(filename):
                supported_files.append(filepath)

        return supported_files
