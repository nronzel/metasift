from models.metadata_cleaner import MetadataCleaner
from models.metadata_extractors import MetadataExtractor
from models.password_unlocker import PasswordUnlocker


class Document:
    def __init__(self, files):
        self.files = files
        self.metadata_extractor = MetadataExtractor(files)
        self.password_unlocker = PasswordUnlocker(files)
        self.metadata_cleaner = MetadataCleaner(files)

    def extract_metadata(self):
        return self.metadata_extractor.extract()

    def clean_metadata(self):
        # return self.metadata_cleaner.clean()
        pass

    def remove_password(self):
        return self.password_unlocker.unlock()
