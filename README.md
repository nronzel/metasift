# Metasift

Metasift is a metadata extraction tool.


Python 3.10.7

> LIMITED FEATURES: This app currently has limited features and only supports
> `.docx` files at the moment. It will be expanded in the future to include
> more filetypes. My current focus is on getting batch processing implemented,
> and then working on cleaning metadata for `.docx` files before moving onto
> other filetypes.

## Features

✅ - Extract metadata from `.docx` files <br />
✅ - Remove password protection from `.docx` files <br />
✅ - _Coming Soon_ Batch processing <br />

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

## Future Roadmap

- [x] ~~re-write to use classes for better maintainability~~
- [x] ~~password protection removal for `.docx` files~~
- [ ] directory support for batch processing _coming soon_
- [ ] `.pdf` file support
- [ ] Option to export metadata to CSV
- [ ] EXIF data support
- [ ] Metadata cleaning feature
