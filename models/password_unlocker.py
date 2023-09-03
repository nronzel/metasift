import os

from utils.cleanup_handler import CleanupHandler
from utils.directory_handler import DirectoryHandler
from utils.file_handler import FileHandler
from utils.helpers import color_print
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
            FileHandler.unzip_files(self.doc, temp_dir)
            if not SettingsModifier.modify_settings(temp_dir):
                color_print("cyan", "No protection found! No action required.")
                return
            FileHandler.zip_file(temp_dir, new_docx_filepath)
        finally:
            CleanupHandler.cleanup(temp_dir)

        color_print("cyan", f"\nUnlocked documents can be found at {new_docx_filepath}")
