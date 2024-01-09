# imports
import xml.etree.ElementTree as ET
import os

def change_xml_content(destination_path, app_name, old_app_name): # Declare change_xml_content function
    # dedclare xml_file_path variable
    xml_file_path = os.path.join(destination_path, "config", "application-config", "data-model-config", f"{app_name}-sql-db.xml")
    tree = ET.parse(xml_file_path) # Parse xml_file_path
    root = tree.getroot()          # Get root of xml_file_path

    for element in root.iter():
        if old_app_name in element.text: 
            element.text = element.text.replace(old_app_name, app_name) # Replace old_app_name with app_name in element.text

    tree.write(xml_file_path)
    
    