import shutil
from utils.helpers import color_print


class CleanupHandler:
    @staticmethod
    def cleanup(temp_dir):
        try:
            color_print("yellow", "\nBeginning cleanup...")
            shutil.rmtree(temp_dir)
            color_print("green", f"Cleanup -- SUCCESS!")
        except Exception as e:
            color_print("red", f"\nCleanup -- FAILED!\nError: {e}")
