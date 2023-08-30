import zipfile
from lxml import etree as ET
import shutil
import os
import logging

logging.basicConfig(level=logging.INFO)


def unzip_docx(docx_file, temp_dir):
    logging.info("Unzipping .docx file...")
    with zipfile.ZipFile(docx_file, "r") as zip_ref:
        zip_ref.extractall(temp_dir)


def modify_settings(temp_dir):
    logging.info("Parsing settings.xml...")
    settings_path = os.path.join(temp_dir, "word", "settings.xml")
    tree = ET.parse(settings_path)
    root = tree.getroot()
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

    protections = root.findall(".//w:documentProtection", ns)
    if protections:
        logging.info("Found document protection. Removing...")
        for protec in protections:
            protec.getparent().remove(protec)
        tree.write(settings_path)
    else:
        logging.info("No document protection found.")


def zip_new_docx(temp_dir, new_docx_file):
    logging.info("Zipping new .docx file...")
    with zipfile.ZipFile(new_docx_file, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(temp_dir):
            for file in files:
                zipf.write(
                    os.path.join(root, file),
                    os.path.relpath(os.path.join(root, file), temp_dir),
                )


def cleanup(temp_dir):
    logging.info("Cleaning up...")
    shutil.rmtree(temp_dir)


def unlock_docx(docx_file):
    temp_dir = "temp_docx"
    new_docx_file = "unlocked_" + docx_file

    try:
        unzip_docx(docx_file, temp_dir)
        modify_settings(temp_dir)
        zip_new_docx(temp_dir, new_docx_file)
    finally:
        cleanup(temp_dir)

    logging.info(f"Unlocked document can be found at {new_docx_file}")
