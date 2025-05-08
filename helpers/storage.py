import os

"""
Function : GetMosqueFiles
Author : AI Assistant
Created : 2024-01-09
Description : Returns an array of mosque JSON files from the mosque-stage-1 storage directory
"""
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