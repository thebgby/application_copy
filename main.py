#imports
import os
import shutil
from change_xml_content import change_xml_content
from change_file_content import change_file_content
from change_file_folder_name import change_file_folder_name

input_file = 'input.txt' # Declare input file

#Declare variables from input file
with open(input_file, 'r') as f:
    data = f.readlines()                # Read the file
    for line in data:                   # Loop through all lines in the file
        if line.startswith('source_path'):              # If the line starts with 'source_path'
            source_path = line.split('=')[1].strip()    # Split the line by '=' and get the second element
        elif line.startswith('destination_dir'):       # If the line starts with 'destination_path'
            destination_dir = line.split('=')[1].strip()      # declare destination_path variable
        elif line.startswith('old_app_name'):           # If the line starts with 'old_app_name'
            old_app_name = line.split('=')[1].strip()   # declare old_app_name variable
        elif line.startswith('app_name'):               # If the line starts with 'app_name'
            app_name = line.split('=')[1].strip()

def main(app_name, source_path, destination_dir, old_app_name): # Declare main function
    destination_path = os.path.join(destination_dir, app_name) # Declare destination_path variable
    shutil.copytree(source_path, destination_path, dirs_exist_ok=True)  # Copy source_path to destination_path
    change_file_folder_name(destination_path, old_app_name, app_name)   # Change file and folder names

    for root, dirs, files in os.walk(destination_path): # Loop through all files and folders in destination_path
        for file in files:                              # Loop through all files in destination_path
            file_path = os.path.join(root, file)        # Declare file_path variable
            if file.endswith('.iashell') or file.endswith('.properties') or file.endswith('.yml'): # If file ends with '.iashell' or '.properties' or '.yml'
                change_file_content(file_path, app_name, old_app_name)                             # Change file content

    change_xml_content(destination_path, app_name, old_app_name) # Change xml content

if __name__ == '__main__':
    main(app_name, source_path, destination_dir, old_app_name)
