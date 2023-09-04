from models.metadata_extractor import DOCXMetadataExtractor
from models.password_unlocker import PasswordUnlocker


class Document:
    def __init__(self, path):
        self.path = path
        self.metadata_extractor = DOCXMetadataExtractor(self.path)
        self.password_unlocker = PasswordUnlocker(self.path)

    def extract_metadata(self):
        return self.metadata_extractor.extract()

    def clean_metadata(self):
        pass

    def remove_password(self):
        return self.password_unlocker.unlock()
