from usecases.GetMosque import GetMosque
from concurrent.futures import ThreadPoolExecutor
from helpers.scrapper import SetupDriver
from helpers.storage import GetMosqueFiles
from helpers.storage import LoadMosque
from helpers.collection import DivideCollection
from repositories.mosque import StoreMosque
import json
import os

max_workers = 5
mosque_files = GetMosqueFiles()
tree_files = DivideCollection(mosque_files, max_workers)

def scrap_mosque(index):
    row = tree_files[index]
    for filename in row:
        raw_mosques = None
        try:
            raw_mosques = LoadMosque(filename)
        except Exception as e:
            print(f"Error loading {filename}: {str(e)}")
            return None
            
        if raw_mosques is None:
            return None

        for raw_mosque in raw_mosques:
            mosque = raw_mosque['name']
            address = raw_mosque['address']
            latitude = raw_mosque['latitude']
            longitude = raw_mosque['longitude']
            StoreMosque(mosque, address, latitude, longitude)


def main():
    for index in range(len(tree_files)):
        scrap_mosque(index)
        print(f"Scraped {index} of {len(tree_files)}")



if __name__ == '__main__':
    main()