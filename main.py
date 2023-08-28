import sys
from extractors.docx import extract_docx_metadata


def main():
    if len(sys.argv) != 2:
        raise Exception("Not enough or too many arguments provided.")

    args = sys.argv[1:]
    file_path = args[0]

    metadata = extract_docx_metadata(file_path)

    if metadata is not None:
        for key, value in metadata.items():
            print(f"{key}: {value}")


main()
