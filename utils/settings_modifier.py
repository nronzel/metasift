import os
import xml.etree.ElementTree as ET

from utils.helpers import color_print


class SettingsModifier:
    @staticmethod
    def modify_settings(temp_dir):
        try:
            color_print("yellow", "\nChecking for file protection...")
            settings_path = os.path.join(temp_dir, "word", "settings.xml")
            tree = ET.parse(settings_path)
            root = tree.getroot()
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            doc_protection = root.find(".//w:documentProtection", ns)
            if doc_protection is not None:
                color_print("red", "Protection found -> REMOVING")
                root.remove(doc_protection)
                tree.write(settings_path)
                color_print("green", "Protection removal -- SUCCESS!")
                return True
            else:
                return False
        except Exception as e:
            color_print("red", f"Protection removal -- FAILED!.\nError: {e}")
            return False
