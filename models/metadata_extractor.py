import zipfile
import os
import xml.etree.ElementTree as ET

from .extractor import Extractor


class MetadataExtractor(Extractor):
    def __init__(self, path):
        self.path = path

    def extract(self):
        if os.path.isdir(self.path):
            return self._extract_from_directory()
        elif os.path.isfile(self.path):
            return self._extract_from_file(self.path)

    def _extract_from_file(self, file_path):
        metadata = {}

        with zipfile.ZipFile(file_path, "r") as z:
            if "docProps/core.xml" not in z.namelist():
                raise Exception("core.xml not found")

            with z.open("docProps/core.xml") as f:
                tree = ET.parse(f)
                root = tree.getroot()

            ns = {
                "ns0": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
                "dc": "http://purl.org/dc/elements/1.1/",
                "ns2": "http://purl.org/dc/terms/",
            }

            title = root.find("dc:title", ns)
            self._add_data_to_obj(title, "title", metadata)

            creator = root.find("dc:creator", ns)
            self._add_data_to_obj(creator, "creator", metadata)

            keywords = root.find("ns0:keywords", ns)
            self._add_data_to_obj(keywords, "keywords", metadata)

            description = root.find("dc:description", ns)
            self._add_data_to_obj(description, "description", metadata)

            last_modified_by = root.find("ns0:lastModifiedBy", ns)
            self._add_data_to_obj(last_modified_by, "lastModifiedBy", metadata)

            created = root.find("ns2:created", ns)
            self._add_data_to_obj(created, "created", metadata)

            modified = root.find("ns2:modified", ns)
            self._add_data_to_obj(modified, "modified", metadata)

        return metadata

    def _extract_from_directory(self):
        metadata = {}
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".docx"):
                    filepath = os.path.join(root, file)
                    metadata[file] = self._extract_from_file(filepath)
        return metadata

    @staticmethod
    def _add_data_to_obj(item, name, metadata):
        if item is not None and item.text is not None:
            metadata[name] = item.text
        else:
            metadata[name] = ""

        return metadata
