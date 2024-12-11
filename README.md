# ExeExtractor - EXE Unpacker

ExeExtractor is a simple GUI-based tool designed to unpack self-extracting executable files. This tool is useful for extracting the contents of EXE files that function as self-contained archives.

## Features

- **User-Friendly Interface**: Intuitive GUI for selecting files and output directories.
- **Supports Multiple Formats**: Utilizes `pyunpack` to handle a wide range of self-extracting EXE files.
- **Safe and Reliable**: Ensures files are unpacked securely to the desired directory.

## How It Works

1. Browse and select an `.exe` file you want to unpack.
2. Choose an output directory for the extracted files.
3. Click the "Unpack EXE" button to extract the contents.

## Requirements

- Python 3.x
- Required Python libraries:
  - `pyunpack`
  - `patool`
  - `tkinter`

## Screenshots

*Coming Soon*

## Troubleshooting

- Ensure the selected EXE file is a valid self-extracting archive.
- Verify the output directory exists and is writable.
- If errors occur, check the detailed error message in the application dialog.

## License

This project is licensed under the MIT License. Feel free to modify and distribute it as needed.

