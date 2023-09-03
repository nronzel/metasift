![ascii-screenshot](./screenshot.png)

# Metasift

Metasift is a metadata extraction tool, and `.docx` password protection remover.

Soon to have support for cleaning metadata.

Python v3.10.7

> LIMITED FEATURES: This app currently has limited features and only supports
> `.docx` files at the moment. It will be expanded in the future to include
> more filetypes. My current focus is on implementing `.docx` metadata cleaning.

## Features

✅ - Extract metadata from `.docx` files <br />
✅ - Remove password protection from `.docx` files <br />
✅ - Batch processing <br />

#### Password Protection Removal

When removing passwords from `.docx` files, Metasift will not modify the original
file in order to prevent any potential for corruption. It will instead
create a new `/unlocked-documents` directory where it will store a separate
unlocked version.

## Quickstart

### Installation

Clone the repository:

```bash
git clone https://github.com/nronzel/metasift.git
```

Navigate to the project directory:

```bash
cd metasift
```

### Dependencies

None! Only utilizes Python's standard library. 😎

### Usage

Run Metasift by running the `main.py` file:

```bash
python main.py
```

or

```bash
python3 main.py
```

#### Input

Metasift accepts either a filename:

```bash
test.docx
```

or a directory path (relative or absolute):

```bash
.
./
/path/to/directory
```

If a directory path is supplied, it will crawl that directory only without going
into subfolders, and get all of the supported filetypes and attempt to extract the
metadata.

## Compatability

This program was built and tested on Linux. It should work on any POSIX based
systems such as Unix, Linux, MacOS, BSD, etc.

I have added some logic for checking for Windows filepaths, however I have not
tested it on a Windows machine to verify everything works. There may also be
issues with the ANSI color codes in your terminal on Windows as I believe ANSI
codes are disabled by default.

## Testing

You can run the provided unit tests with:

```bash
python tests.py -v
```

## Future Roadmap

- [x] ~~re-write to use classes for better maintainability~~
- [x] ~~password protection removal for `.docx` files~~
- [x] ~~directory support for batch processing~~
- [ ] `.docx` metadata cleaning
- [ ] `.pdf` file support
- [ ] Option to export metadata to CSV
- [ ] EXIF data support
- [ ] Metadata cleaning of other filetypes as implemented
