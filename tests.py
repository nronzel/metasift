import unittest
from utils.helpers import filename_or_directory


# Helpers
class TestHelpers(unittest.TestCase):
    def test_filename_or_directory(self):
        values = [
            "test.docx",
            "test.doc",
            "test.jpg",
            "test.png",
        ]

        for value in values:
            result = filename_or_directory(value)
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
            result = filename_or_directory(value)
            self.assertFalse(result, f"Expected {value} to be False")


if __name__ == "__main__":
    unittest.main()
