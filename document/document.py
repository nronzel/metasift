from models.metadata_extractor import MetadataExtractor
from models.password_unlocker import PasswordUnlocker
from utils.helpers import is_supported_filetype, is_valid_filename

import os


class Document:
    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.set_path()

        self.type = None

    def extract_metadata(self):
        metadata_extractor = MetadataExtractor(self.path)
        data = metadata_extractor.extract()
        return data

    def clean_metadata(self):
        # CleanMetadata here
        pass

    def remove_password(self):
        password_unlocker = PasswordUnlocker(self.path)
        return password_unlocker.unlock()

    def set_path(self):
        while True:
            path = input("Please provide a path or filename: ")
            is_file = is_valid_filename(path)
            is_valid_directory = os.path.isdir(path)

            if is_file and is_supported_filetype(path):
                self.type = "filename"
                self.path = path
                break
            else:
                print("Invalid filename provided. Try again.")

            if is_valid_directory:
                self.type = "directory"
                self.path = path
                break
