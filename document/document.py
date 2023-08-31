from models.metadata_extractor import MetadataExtractor
from models.password_unlocker import PasswordUnlocker


class Document:
    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.set_path()

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
        path = input("Please provide a path or filename: ")
        self.path = path
