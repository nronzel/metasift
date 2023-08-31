import zipfile
import xml.etree.ElementTree as ET


class MetadataExtractor:
    def __init__(self, doc):
        self.doc = doc

    def extract(self):
        # extraction logic here
        metadata = {}

        with zipfile.ZipFile(self.doc, "r") as z:
            if "docProps/core.xml" not in z.namelist():
                raise Exception("core.xml not found")

            with z.open("docProps/core.xml") as f:
                tree = ET.parse(f)
                root = tree.getroot()

            # define namespaces for .docx filetype
                ns = {
                    "ns0": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
                    "dc": "http://purl.org/dc/elements/1.1/",
                    "ns2": "http://purl.org/dc/terms/",
                }

                # title
                title = root.find("dc:title", ns)
                self.add_data_to_obj(title, "title", metadata)

                # creator
                creator = root.find("dc:creator", ns)
                self.add_data_to_obj(creator, "creator", metadata)

                # keywords
                keywords = root.find("ns0:keywords", ns)
                self.add_data_to_obj(keywords, "keywords", metadata)

                # description
                description = root.find("dc:description", ns)
                self.add_data_to_obj(description, "description", metadata)

                # lastModifiedBy
                last_modified_by = root.find("ns0:lastModifiedBy", ns)
                self.add_data_to_obj(last_modified_by, "lastModifiedBy", metadata)

                # created
                created = root.find("ns2:created", ns)
                self.add_data_to_obj(created, "created", metadata)

                # modified
                modified = root.find("ns2:modified", ns)
                self.add_data_to_obj(modified, "modified", metadata)

        return metadata

    @staticmethod
    def add_data_to_obj(item, name, metadata):
        if item is not None and item.text is not None:
            metadata[name] = item.text
        else:
            metadata[name] = ""

        return metadata
