import zipfile
import xml.etree.ElementTree as ET
import shutil
import os


def unlock_docx(docx_file):
    # Unzip the docx file
    temp_dir = "temp_docx"
    with zipfile.ZipFile(docx_file, "r") as zip_ref:
        zip_ref.extractall(temp_dir)

    # Modify settings.xml
    settings_path = os.path.join(temp_dir, "word", "settings.xml")

    tree = ET.parse(settings_path)
    root = tree.getroot()
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

    protec = root.find("w:documentProtection", ns)
    if protec is not None:
        root.remove(protec)
        tree.write(settings_path)

    # Zip files back into a new docx file
    new_docx_file = "unlocked_" + docx_file
    with zipfile.ZipFile(new_docx_file, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                zipf.write(
                    os.path.join(root, file),
                    os.path.relpath(os.path.join(root, file), temp_dir),
                )

    # Delete the temporary directory
    shutil.rmtree(temp_dir)
