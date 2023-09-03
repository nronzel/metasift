import os
import xml.etree.ElementTree as ET


class SettingsModifier:
    @staticmethod
    def modify_settings(temp_dir):
        try:
            settings_path = os.path.join(temp_dir, "word", "settings.xml")
            tree = ET.parse(settings_path)
            root = tree.getroot()
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            doc_protection = root.find(".//w:documentProtection", ns)
            if doc_protection is not None:
                root.remove(doc_protection)
                tree.write(settings_path)
            return True
        except Exception as e:
            print(f"Failed to modify settings and remove password. Error: {e}")
            return False
