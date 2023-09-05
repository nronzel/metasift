from models.metadata_cleaner import MetadataCleaner
from models.metadata_extractor import DOCXMetadataExtractor
from models.password_unlocker import PasswordUnlocker
from utils.helpers import check_path_type, color_print


class Document:
    def __init__(self, path):
        self.path = path
        self.type = check_path_type(self.path)
        self.metadata_extractor = DOCXMetadataExtractor(self.path)
        self.password_unlocker = PasswordUnlocker(self.path)
        self.metadata_cleaner = MetadataCleaner(self.path)

    def extract_metadata(self):
        if self.type == "directory":
            return self.metadata_extractor.batch_extract()
        if self.type == "file":
            return self.metadata_extractor.extract(self.path)
        color_print(
            "red",
            f"\n'{self.path}' not found. Try again.\n",
        )

    def clean_metadata(self):
        # return self.metadata_cleaner.clean()
        pass

    def remove_password(self):
        return self.password_unlocker.unlock()
