import zipfile
import os

from utils.helpers import color_print


class FileHandler:
    @staticmethod
    def unzip_files(src, dest):
        try:
            color_print("yellow", "\nUnzipping file...")
            with zipfile.ZipFile(src, "r") as zip_ref:
                zip_ref.extractall(dest)
            color_print("green", "Unzip file -- SUCCESS!")
        except Exception as e:
            color_print("red", f"\nUnzip file -- FAILED!\nError: {e}")

    @staticmethod
    def zip_file(src, dest):
        try:
            color_print("yellow", "\nCreating new file...")
            with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(src):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, src)
                        zipf.write(file_path, arcname)
            color_print("green", "Created new file -- SUCCESS!")
        except Exception as e:
            color_print("red", f"\nCreated new file -- FAILED!\nError: {e}")

    @staticmethod
    def read_zip_file(src, filename):
        try:
            with zipfile.ZipFile(src, "r") as z:
                if filename not in z.namelist():
                    raise Exception(f"{filename} not found.")
                with z.open(filename) as f:
                    return f.read()
        except Exception as e:
            color_print("red", f"\nFailed to read {filename} from {src}.\nError: {e}")
            return None
