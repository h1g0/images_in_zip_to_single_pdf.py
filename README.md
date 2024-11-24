# images_in_zip_to_single_pdf.py

This Python script processes all `.zip` files in a selected folder, converts the contained `.jpg`, `.jpeg`, `.bmp`, `.png`, or `.webp` images into a single PDF file for each `.zip`, and organizes the output and processed files systematically.

## Features

- **Batch Processing**: Automatically processes all `.zip` files in the specified folder.
- **Folder Organization**:
  - Saves the generated PDF files in a `pdf` folder within the specified folder.
  - Moves processed `.zip` files to a `zip` folder.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `Pillow` (for handling images)
  - `tkinter` (built-in with most Python distributions)

### Install Required Libraries

Install `Pillow` using pip if it is not already installed:

```bash
pip install pillow
```

## Usage

1. Run the script using Python:
```
python images_in_zip_to_single_pdf.py
```
1. A folder selection dialog will appear. Select the folder containing `.zip` files with images.
1. The script will:
   - Convert each `.zip` file's images into a PDF and save it in a `pdf` folder.
   - Move processed `.zip` files to a `zip` folder.
1. Progress updates, including the currently processed file count and `.zip` file, will be displayed in the terminal.

## File Structure After Execution

Suppose the selected folder is `/path/to/folder`. After execution, the structure will look like this:

```plain
/path/to/folder/
├── pdf/
│   ├── file1.pdf
│   ├── file2.pdf
│   └── ...
├── zip/
│   ├── file1.zip
│   ├── file2.zip
│   └── ...
├── file3.zip
├── ...
```

## Example Output

```bash
Processing ZIP file: sample1.zip
  - Image file in process: 100/100
  -> PDF created: /path/to/folder/pdf/sample1.pdf
  -> ZIP file moved to: /path/to/folder/zip/sample1.zip
```

## Notes

- The `.zip` files must contain images named sequentially (e.g., `000.jpg`, `001.jpg`, ...).
- The generated PDFs will have the same base name as the `.zip` files.
