from models.metadata_extractor import MetadataExtractor
from models.password_unlocker import PasswordUnlocker
from utils.helpers import is_supported_filetype

import os


class Document:
    def __init__(self, path):
        self.path = path
        self.type = None

    def extract_metadata(self):
        metadata_extractor = MetadataExtractor(self.path)
        if self.type == "filepath":
            return metadata_extractor.extract()
        elif self.type == "directory":
            return self._extract_directory_metadata()

    def _extract_directory_metadata(self):
        metadata = {}
        supported_files = self._crawl_for_supported_files()
        if supported_files is not None:
            for file in supported_files:
                title = file.split("/")[-1]
                filename, extension = os.path.splitext(title)

                # until other formats are supported, leave this in.
                if extension != ".docx":
                    print(f"\n'{extension}' not yet supported for metadata extraction.")
                    continue

                extractor = MetadataExtractor(file)
                data = extractor.extract()
                metadata[filename] = data
        return metadata

    def clean_metadata(self):
        # CleanMetadata here
        pass

    def remove_password(self):
        password_unlocker = PasswordUnlocker(self.path)
        return password_unlocker.unlock()

    def set_type(self, type):
        self.type = type

    def _crawl_for_supported_files(self):
        supported_files = []
        directory = os.path.abspath(self.path)

        if not os.path.exists(directory):
            print("\nThe specified directory does not exist.")
            return

        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            if os.path.isfile(filepath):
                if is_supported_filetype(filename):
                    supported_files.append(filepath)

        return supported_files
