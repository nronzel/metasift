import os

from utils.helpers import color_print


class DirectoryHandler:
    @staticmethod
    def ensure_directory_exists(directory):
        if not os.path.exists(directory):
            try:
                color_print("yellow", "\nCreating directory...")
                os.mkdir(directory)
                color_print("green", f"'{directory}' created -- SUCCESS!")
                return True

            except Exception as e:
                color_print("red", f"\n'{directory}' created -- FAILED!\nError: {e}")
                return False
        return True
