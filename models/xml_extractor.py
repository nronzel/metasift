import xml.etree.ElementTree as ET


class XMLExtractor:
    def __init__(self, xml_data, namespaces):
        self.root = ET.fromstring(xml_data)
        self.namespaces = namespaces

    def extract_value(self, query):
        element = self.root.find(query, self.namespaces)
        return element.text if element is not None and element.text is not None else ""
