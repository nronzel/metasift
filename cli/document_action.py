class DocumentAction:
    def __init__(self, document):
        self.document = document

    def extract_metadata(self):
        if self.document is not None:
            return self.document.extract_metadata()

    def clean_metadata(self):
        pass

    def remove_password(self):
        if self.document is not None:
            return self.document.remove_password()
