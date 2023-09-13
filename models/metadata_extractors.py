import os
import glob

from utils.file_handler import FileHandler
from utils.helpers import color_print
from .xml_extractor import XMLExtractor


class MetadataExtractor:
    def __init__(self, files):
        self.files = files
        self.docx_extractor = DOCXMetadataExtractor()

    def extract(self):
        metadata = []

        if self.files is None:
            color_print("red", "\nNo files for extractor to parse.\n")

        for file in self.files:
            _, extension = os.path.splitext(file)
            match extension:
                case ".docx":
                    metadata.append(self.docx_extractor.extract(file))
                case _:
                    color_print("red", "\nNo supported files found to extract.\n")

        return metadata


class DOCXMetadataExtractor(MetadataExtractor):
    def __init__(self):
        self.file_handler = FileHandler()

    def extract(self, file_path):
        metadata = {}
        xml_data = self.file_handler.read_zip_file(file_path, "docProps/core.xml")

        if xml_data is None:
            return metadata

        namespaces = {
            "ns0": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
            "dc": "http://purl.org/dc/elements/1.1/",
            "ns2": "http://purl.org/dc/terms/",
        }

        extractor = XMLExtractor(xml_data, namespaces)

        metadata["file"] = file_path.split("/")[-1]
        metadata["title"] = extractor.extract_value("dc:title")
        metadata["creator"] = extractor.extract_value("dc:creator")
        metadata["keywords"] = extractor.extract_value("ns0:keywords")
        metadata["description"] = extractor.extract_value("dc:description")
        metadata["lastModifiedBy"] = extractor.extract_value("ns0:lastModifiedBy")
        metadata["created"] = extractor.extract_value("ns2:created")
        metadata["modified"] = extractor.extract_value("ns2:modified")

        return metadata
