from helpers.mouse import ClickBySelector
from helpers.keyboard import PressAndEnter
from helpers.selector import GetElements
from helpers.string import GetFormalName
import time
import json
import os

def GetCities(driver, province_id, province_name):
    # Wait for the selectize-control element to be clickable and click it
    ClickBySelector(driver, ".selectize-control")
    
    PressAndEnter(driver, province_name)
    
    ClickBySelector(driver, "#wKota")
    time.sleep(3)
    
    city_elements = GetElements(driver, "#wKota .selectize-dropdown-content .option")    
    # Extract city names and create array of objects with id and name
    cities = [{'id': int(element.get_attribute('data-value')), 'name': element.get_attribute('innerText'), 'province_id': province_id, 'province_name': province_name} for idx, element in enumerate(city_elements)]
    # Create storage/files directory if it doesn't exist
    os.makedirs('storage/cities', exist_ok=True)
    filename = GetFormalName(province_name)
    # Save cities data to JSON file
    file_path = f'storage/cities/{filename}.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(cities, f, ensure_ascii=False, indent=2)
    
    return cities