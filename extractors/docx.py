import zipfile
import xml.etree.ElementTree as ET

def extract_docx_metadata(docx_path):
    metadata = {}

    with zipfile.ZipFile(docx_path, "r") as z:
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
            extract_data_item(root, "dc:title", ns, metadata)

            # creator
            extract_data_item(root, "dc:creator", ns, metadata)

            # keywords
            extract_data_item(root, "ns0:keywords", ns, metadata)

            # description
            extract_data_item(root, "dc:description", ns, metadata)

            # lastModifiedBy
            extract_data_item(root, "ns0:lastModifiedBy", ns, metadata)

            # created
            extract_data_item(root, "ns2:created", ns, metadata)

            # modified
            extract_data_item(root, "ns2:modified", ns, metadata)

    return metadata


def extract_data_item(root, item, ns, metadata):
    data_item = root.find(item, ns)
    name = item.split(":")[1]
    if data_item is not None and data_item.text is not None:
        metadata[name] = data_item.text
    else:
        metadata[name] = ""

    return metadata
