def change_file_content(file_path, app_name, old_app_name): # Declare change_file_content function
    with open(file_path, 'r') as f:
        content = f.read()
        content = content.replace(old_app_name, app_name) # Replace old_app_name with app_name in content
    
    with open(file_path, 'w') as f:     # Open file_path in write mode
        f.write(content) # Write content to file_path