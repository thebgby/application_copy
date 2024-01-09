# Application Name and Content Updater

This Python package provides a set of scripts to automate the process of updating application names in various files and directories. The primary use case is to facilitate the rebranding or renaming of an application by changing occurrences of the old application name to the new one. The package includes functionality to update file and folder names, file contents, and XML configuration files.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/thebgby/application_copy.git
```

2. Navigate to the project directory:

```bash
cd copy_file_structure
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Create an input file (`input.txt`) with the following format:

```plaintext
source_path = /path/to/source
destination_dir = /path/to/destination
old_app_name = OldAppName
app_name = NewAppName
```
Replace `/path/to/source`, `/path/to/destination`, `OldAppName`, and `NewAppName` with your actual values.

2. Run the main script (`main.py`):

```bash
python main.py
```

3. The script will read the input file, copy the contents from the source to the destination directory, update file and folder names, and modify file contents and XML configurations.

## File Descriptions

- `main.py`: The main script that orchestrates the renaming process based on the input file.

- `change_file_content.py`: Contains a function to replace occurrences of the old application name with the new one in file contents.

- `change_file_folder_name.py`: Defines a function to update file and folder names by replacing the old application name with the new one.

- `change_xml_content.py`: Provides a function to modify XML configuration files by updating occurrences of the old application name with the new one.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

