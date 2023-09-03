import shutil


class CleanupHandler:
    @staticmethod
    def cleanup(temp_dir):
        try:
            shutil.rmtree(temp_dir)
            return True
        except Exception as e:
            print(f"Failed to clean up. Error {e}")
            return False
