from helpers.mouse import ClickBySelector
from helpers.keyboard import PressAndEnter
from helpers.selector import GetElements
from helpers.string import GetFormalName
from entities.mosque import SetupDriver

import time
import json
import os

def GetDistricts(driver, province_id, province_name, city_id, city_name):
    # Wait for the selectize-control element to be clickable and click it
    ClickBySelector(driver, ".selectize-control")
    
    PressAndEnter(driver, province_name)
    
    ClickBySelector(driver, "#wKota")
    time.sleep(3)

    PressAndEnter(driver, city_name)
    time.sleep(3)

    ClickBySelector(driver, "#wKecamatan")
    time.sleep(1)
    district_elements = GetElements(driver, "#wKecamatan .selectize-dropdown-content .option")
    district_id = int(element.get_attribute('data-value'))
    # Extract city names and create array of objects with id and name
    districts = [{'id': district_id, 'name': element.get_attribute('innerText'), 'city_id': city_id, 'city_name': city_name, 'province_id': province_id, 'province_name': province_name} for idx, element in enumerate(district_elements)]
    # # Create storage/files directory if it doesn't exist
    os.makedirs('storage/districts', exist_ok=True)
    filename = GetFormalName(city_name)
    # # Save cities data to JSON file
    file_path = f'storage/districts/{filename}.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(districts, f, ensure_ascii=False, indent=2)
    
    # return cities