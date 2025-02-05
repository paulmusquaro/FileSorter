# FileSorter

`FileSorter` is a Python utility that organizes files in a given folder by categorizing them into subfolders based on their extensions (e.g., images, videos, documents, music, archives). It also normalizes file names by transliterating characters from the Cyrillic alphabet to Latin and replacing non-alphanumeric characters with underscores.

## Features

- **File Renaming**: Transliterates Cyrillic characters into Latin and replaces non-alphanumeric characters with underscores.
- **File Sorting**: Sorts files into respective folders based on their extensions (images, videos, documents, music, archives).
- **Archive Handling**: Unpacks `.zip`, `.tar`, `.gz` archives into dedicated subfolders and removes the original archive file.
- **File Extension Detection**: Identifies known file types (images, videos, documents, music, and archives) and moves them into corresponding folders.
- **Unknown Extensions**: Lists any files with extensions that are not categorized.

## Requirements

- Python 3.x

## Installation

Clone this repository or download the files:

```bash
git clone https://github.com/paulmusquaro/FileSorter.git
```

## Usage

To use `FileSorter`, run the script with the path to the folder you want to organize:

```bash
python main.py /path/to/folder
```

If no path is provided, the script will prompt you to input the folder path manually.

### Example:

```bash
python main.py ~/Downloads
```

## How it Works

1. **Normalization**: The script renames files by normalizing their names—transliterating Cyrillic characters to Latin letters and replacing spaces and special characters with underscores.
2. **Sorting**: Based on file extensions, files are moved into one of the following folders:
   - `images`: For image files (e.g., `.jpeg`, `.png`, `.jpg`)
   - `videos`: For video files (e.g., `.mp4`, `.avi`, `.mkv`)
   - `documents`: For document files (e.g., `.docx`, `.pdf`, `.txt`)
   - `music`: For audio files (e.g., `.mp3`, `.wav`, `.ogg`)
   - `archives`: For archive files (e.g., `.zip`, `.tar`, `.gz`)
3. **Archiving**: If the script encounters an archive file, it extracts its contents into a subfolder named after the archive and deletes the original archive file.

## Known Limitations

- The script only recognizes a predefined list of file extensions. Files with unrecognized extensions will be reported under "Unknown extensions".
- Archives are extracted into subfolders, but the original archive file is deleted after extraction.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!