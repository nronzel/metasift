import os

from utils.cleanup_handler import CleanupHandler
from utils.directory_handler import DirectoryHandler
from utils.file_handler import FileHandler
from utils.settings_modifier import SettingsModifier


class PasswordUnlocker:
    """
    Removes password protection from .docx files.
    """

    def __init__(self, doc):
        self.doc = doc

    def unlock(self):
        temp_dir = "temp_docx"
        output_dir = "unlocked-documents"
        new_docx_file = "unlocked_" + self.doc.split(os.path.sep)[-1]
        new_docx_filepath = os.path.join(output_dir, new_docx_file)

        if not DirectoryHandler.ensure_directory_exists(output_dir):
            print("\nFailed to ensure directory exists.")
            return

        try:
            print("\n- Unzipping file(s)..")
            FileHandler.unzip_files(self.doc, temp_dir)
            print("- Removing found protections..")
            SettingsModifier.modify_settings(temp_dir)
            print("- Creating new unlocked file..")
            FileHandler.zip_file(temp_dir, new_docx_filepath)
        finally:
            print("- Cleaning up..")
            CleanupHandler.cleanup(temp_dir)
            print("- Cleanup complete.")

        print(f"\nUnlocked document can be found at {new_docx_filepath}")
