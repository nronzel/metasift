import unittest
from utils.helpers import is_valid_filename, is_supported_filetype


# Helpers
class TestHelpers(unittest.TestCase):
    def test_filename_or_directory(self):
        values = [
            "test.docx",
            "test.pdf",
            "test.jpg",
            "test.png",
        ]

        for value in values:
            result = is_valid_filename(value)
            self.assertTrue(result, f"Expected {value} to be True")

    def test_bad_filename_or_directory(self):
        values = [
            "test.py",
            "test.js",
            "test.asdfl",
            "",
            "12315",
        ]
        for value in values:
            result = is_valid_filename(value)
            self.assertFalse(result, f"Expected {value} to be False")

    def test_supported_extensions(self):
        values = ["test.docx", "test.pdf", "test.jpg", "test.png"]
        for value in values:
            result = is_supported_filetype(value)
            self.assertTrue(result, f"Expected {value} to be True")

    def test_unsupported_extensions(self):
        values = ["test.doc", "test.gif", "test.avi"]
        for value in values:
            result = is_supported_filetype(value)
            self.assertFalse(result, f"Expected {value} to be False")


if __name__ == "__main__":
    unittest.main()
