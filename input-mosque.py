from usecases.GetMosque import GetMosque
from concurrent.futures import ThreadPoolExecutor
from helpers.scrapper import SetupDriver
from helpers.storage import GetMosqueFiles
from helpers.collection import DivideCollection
from repositories.mosque import StoreMosque
import json
import os

max_workers = 10

def main():
    # mosque_files = GetMosqueFiles()
    # tree_files = DivideCollection(mosque_files, max_workers)
    StoreMosque('test1', 'test', 1, 1)

if __name__ == '__main__':
    main()