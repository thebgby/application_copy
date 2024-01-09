# imports
import os

def change_file_folder_name(path, old_name, new_name): 
    for root, dirs, files in os.walk(path): # Loop through all files and folders in path
        for dir in dirs:
            if old_name in dir:             # If old_name in dir
                old_dir_path = os.path.join(root, dir)      # Declare old_dir_path variable
                new_dir_path = os.path.join(root, dir.replace(old_name, new_name)) # Declare new_dir_path variable
                os.rename(old_dir_path, new_dir_path)       # Rename old_dir_path to new_dir_path
                
        for file in files:
            if old_name in file:
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file.replace(old_name, new_name))
                os.rename(old_file_path, new_file_path)