import zipfile
from lxml import etree as ET
import shutil
import os
import logging

logging.basicConfig(level=logging.INFO)


def print_status(message, is_error=False):
    marker = "!" if is_error else "="
    print(f"{marker*5} {message} {marker*5}")


def unzip_docx(docx_file, temp_dir):
    try:
        print_status(f"Unzipping {docx_file}...")
        with zipfile.ZipFile(docx_file, "r") as zip_ref:
            zip_ref.extractall(temp_dir)
        print("Unzipping complete.\n")
    except Exception as e:
        print_status(f"Failed to unzip {docx_file}. Error: {e}", True)
        return False
    return True


def modify_settings(temp_dir):
    try:
        print_status("Modifying settings...")
        settings_path = os.path.join(temp_dir, "word", "settings.xml")
        tree = ET.parse(settings_path)
        root = tree.getroot()
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

        protections = root.findall(".//w:documentProtection", ns)
        if protections:
            print("Found document protection. Removing...")
            for protec in protections:
                protec.getparent().remove(protec)
            tree.write(settings_path)
            print("Document protection removed.\n")
        else:
            print("No document protection found.\n")
    except Exception as e:
        print_status(f"Failed to modify settings. Error: {e}", True)
        return False
    return True


def zip_new_docx(temp_dir, new_docx_file):
    try:
        print_status(f"Creating New Document: {new_docx_file}...")
        with zipfile.ZipFile(new_docx_file, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    zipf.write(
                        os.path.join(root, file),
                        os.path.relpath(os.path.join(root, file), temp_dir),
                    )
        print(f"New document {new_docx_file} created.\n")
    except Exception as e:
        print_status(f"Failed to create new document. Error: {e}", True)
        return False
    return True


def cleanup(temp_dir):
    try:
        print_status("Cleaning Up...")
        shutil.rmtree(temp_dir)
        print("Cleanup complete.\n")
    except Exception as e:
        print_status(f"Failed to clean up. Error: {e}", True)
        return False
    return True


def unlock_docx(docx_file):
    temp_dir = "temp_docx"
    new_docx_file = "unlocked_" + docx_file

    try:
        if not unzip_docx(docx_file, temp_dir):
            return
        if not modify_settings(temp_dir):
            return
        if not zip_new_docx(temp_dir, new_docx_file):
            return
    finally:
        if not cleanup(temp_dir):
            return

    print_status(f"Success! Unlocked document can be found at {new_docx_file}")
