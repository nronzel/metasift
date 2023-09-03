import zipfile
import os


class FileHandler:
    @staticmethod
    def unzip_files(src, dest):
        try:
            with zipfile.ZipFile(src, "r") as zip_ref:
                zip_ref.extractall(dest)
            return True
        except Exception as e:
            print(f"Failed to unzip {src}. Error: {e}")
            return False

    @staticmethod
    def zip_file(src, dest):
        try:
            with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(src):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, src)
                        zipf.write(file_path, arcname)
            return True
        except Exception as e:
            print(f"Failed to create new document. Error: {e}")
            return False

    @staticmethod
    def read_zip_file(src, filename):
        try:
            with zipfile.ZipFile(src, "r") as z:
                if filename not in z.namelist():
                    raise Exception(f"\n{filename} not found")
                with z.open(filename) as f:
                    return f.read()
        except Exception as e:
            print(f"\nFailed to read {filename} from {src}. Error: {e}")
            return None
