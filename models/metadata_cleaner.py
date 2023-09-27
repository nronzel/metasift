class Cleaner:
    def clean(self):
        raise NotImplementedError


class MetadataCleaner(Cleaner):
    def __init__(self, metadata):
        self.metadata = metadata
        self.docx_cleaner = DocxCleaner(self.metadata)

    def clean(self):
        # cleaning logic
        pass


class DocxCleaner(Cleaner):
    def __init__(self, metadata):
        self.metadata = metadata

    def clean(self):
        pass


class Editor:
    def __init__(self, data, namespaces):
        self.data = data
        self.namespaces = namespaces

    def edit(self, field, value):
        pass
