import os


class DirectoryHandler:
    @staticmethod
    def ensure_directory_exists(directory):
        if not os.path.exists(directory):
            try:
                os.mkdir(directory)
                print(f"'{directory}' directory successfully created.")
                return True
            except Exception as e:
                print(f"\nFailed to create directory {directory}. Error: {e}")
                return False
        return True
