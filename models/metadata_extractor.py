import os
import glob

from utils.file_handler import FileHandler
from utils.helpers import color_print
from utils.xml_extractor import XMLExtractor
from .extractor import Extractor


class DOCXMetadataExtractor(Extractor):
    def __init__(self, path):
        self.path = path

    def extract(self):
        if os.path.isdir(self.path):
            return self._extract_from_directory()
        elif os.path.isfile(self.path):
            return self._extract_from_file(self.path)

    def _extract_from_file(self, file_path):
        metadata = {}
        xml_data = FileHandler.read_zip_file(file_path, "docProps/core.xml")

        if xml_data is None:
            return metadata

        namespaces = {
            "ns0": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
            "dc": "http://purl.org/dc/elements/1.1/",
            "ns2": "http://purl.org/dc/terms/",
        }

        extractor = XMLExtractor(xml_data, namespaces)

        metadata["title"] = extractor.extract_value("dc:title")
        metadata["creator"] = extractor.extract_value("dc:creator")
        metadata["keywords"] = extractor.extract_value("ns0:keywords")
        metadata["description"] = extractor.extract_value("dc:description")
        metadata["lastModifiedBy"] = extractor.extract_value("ns0:lastModifiedBy")
        metadata["created"] = extractor.extract_value("ns2:created")
        metadata["modified"] = extractor.extract_value("ns2:modified")

        return metadata

    def _extract_from_directory(self):
        metadata = {}
        # Walks subdirectories -- for future use
        # for root, _, files in os.walk(self.path):
        #     for file in files:
        #         if file.endswith(".docx"):
        #             filepath = os.path.join(root, file)
        #             metadata[file] = self._extract_from_file(filepath)
        for filepath in glob.glob(f"{self.path}/*.docx"):
            file = os.path.basename(filepath)
            metadata[file] = self._extract_from_file(filepath)

        if not metadata:
            color_print(
                "red", "\nNo .docx files found in supplied directory. Try again."
            )
        return metadata
