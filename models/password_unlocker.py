import os
import glob

from utils.cleanup_handler import CleanupHandler
from utils.directory_handler import DirectoryHandler
from utils.file_handler import FileHandler
from utils.helpers import color_print
from utils.settings_modifier import SettingsModifier


class PasswordUnlocker:
    """
    Removes password protection from .docx files.
    """

    def __init__(self, path):
        self.path = path

    def unlock(self):
        if os.path.isdir(self.path):
            return self._batch_unlock()
        elif os.path.isfile(self.path):
            return self._unlock_file()
        else:
            color_print("red", "\nInvalid path or filename provided. Try again.")

    def _unlock_file(self):
        temp_dir = "temp_docx"
        output_dir = "unlocked-documents"
        new_docx_file = "unlocked_" + self.path.split(os.path.sep)[-1]
        new_docx_filepath = os.path.join(output_dir, new_docx_file)

        if not DirectoryHandler.ensure_directory_exists(output_dir):
            print("\nFailed to ensure directory exists.")
            return

        try:
            color_print("yellow", f"{('-') * 40}")
            FileHandler.unzip_files(self.path, temp_dir)
            if not SettingsModifier.modify_settings(temp_dir):
                color_print("cyan", "No protection found! No action required.")
                return
            FileHandler.zip_file(temp_dir, new_docx_filepath)
        finally:
            CleanupHandler.cleanup(temp_dir)

        color_print(
            "cyan", f"\nUnlocked documents can be found at {new_docx_filepath}\n"
        )

    def _batch_unlock(self):
        # find all .docx files and add to list
        docx_files = glob.glob(os.path.join(self.path, "*.docx"))

        if not docx_files:
            color_print("red", "\nNo .docx files found in the directory. Try again.\n")
            return

        for docx_file in docx_files:
            self.path = docx_file
            self.unlock()
