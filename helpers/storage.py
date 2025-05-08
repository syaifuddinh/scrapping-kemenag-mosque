import os
import json

def GetMosqueFiles():
    storage_dir = 'storage/mosque-stage-1'
    
    # Ensure directory exists
    if not os.path.exists(storage_dir):
        return []
    
    # Get all JSON files from the directory
    mosque_files = []
    for file in os.listdir(storage_dir):
        if file.endswith('.json'):
            mosque_files.append(file)
    
    return mosque_files

def LoadMosque(filename):
    storage_dir ='storage/mosque-stage-1'
    file_path = os.path.join(storage_dir, filename)

    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as file:
        data = json.load(file)
    return data