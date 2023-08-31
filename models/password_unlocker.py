import zipfile
import shutil
import os
import xml.etree.ElementTree as ET


class PasswordUnlocker:
    def __init__(self, doc):
        self.doc = doc

    def unlock(self):
        temp_dir = "temp_docx"
        docx_file = self.doc
        # extract just the filename, in case it includes directories
        new_docx_file = "unlocked_" + docx_file.split(os.path.sep)[-1]
        try:
            self._unzip_docx(docx_file, temp_dir)
            self._modify_settings(temp_dir)
            self._zip_new_docx(temp_dir, new_docx_file)
        finally:
            self._cleanup(temp_dir)

        print(f"Unlocked document can be found at ./unlocked-documents/{new_docx_file}")

    def _unzip_docx(self, docx_file, temp_dir):
        try:
            print(f"\nUnzipping {docx_file}...")
            with zipfile.ZipFile(docx_file, "r") as zip_ref:
                zip_ref.extractall(temp_dir)
            print("Unzipping complete.\n")
        except Exception as e:
            print(f"\nFailed to unzip {docx_file}. Error: {e}")
            return False
        return True

    def _modify_settings(self, temp_dir):
        try:
            print("Modifying settings...")
            settings_path = os.path.join(temp_dir, "word", "settings.xml")
            tree = ET.parse(settings_path)
            root = tree.getroot()
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

            # Find the documentProtection element
            doc_protection = root.find(".//w:documentProtection", ns)

            if doc_protection is not None:
                print("Found document protection. Removing...")
                root.remove(doc_protection)
                tree.write(settings_path)
                print("Document protection removed.\n")
            else:
                print("No document protection found.\n")
        except Exception as e:
            print(f"\nFailed to modify settings. Error: {e}")
            return False
        return True

    def _ensure_directory_exists(self, directory):
        if not os.path.exists(directory):
            try:
                os.mkdir(directory)
                print(f"'{directory}' directory created.")
            except Exception as e:
                print(f"\nFailed to create directory {directory}. Error: {e}")
                return False
        return True

    def _zip_new_docx(self, temp_dir, new_docx_file):
        # Ensure the '/unlocked-documents' directory exists
        if not self._ensure_directory_exists("unlocked-documents"):
            print("Failed to ensure directory exists.")
            return False

        # Update the path for the new_docx_file to be saved in new dir
        new_docx_file_path = os.path.join("unlocked-documents", new_docx_file)

        try:
            print(f"Creating New Document: {new_docx_file}...")
            with zipfile.ZipFile(new_docx_file_path, "w", zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, temp_dir)
                        zipf.write(file_path, arcname)
            print(f"New document {new_docx_file_path} created.\n")
        except Exception as e:
            print(f"\nFailed to create new document. Error: {e}")
            return False
        return True

    def _cleanup(self, temp_dir):
        try:
            print("Cleaning up...")
            shutil.rmtree(temp_dir)
            print("Cleanup Complete.\n")
        except Exception as e:
            print(f"\nFailed to clean up. Error {e}")
            return False
        return True
