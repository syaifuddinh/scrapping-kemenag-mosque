from helpers.mouse import ClickBySelector
from helpers.keyboard import PressAndEnter
from helpers.selector import GetElements
from helpers.string import GetFormalName
from helpers.string import GetCoordinatesFromURL
from entities.mosque import SetupDriver
from selenium.webdriver.common.by import By

import time
import json
import os

def GetMosque(driver, page):
    # Wait for the selectize-control element to be clickable and click it
    mosques = []
    mosque_elements = GetElements(driver, ".container .search-result-wrapper", 20)
    for mosque_element in mosque_elements:
        mosque = {}
        mosque['name'] = mosque_element.find_element(By.CSS_SELECTOR, "h4").text
        mosque['address'] = mosque_element.find_element(By.CSS_SELECTOR, "p").text
        gmap_url = mosque_element.find_element(By.CSS_SELECTOR, "a:last-child").get_attribute("href")
        coordinates = GetCoordinatesFromURL(gmap_url)
        mosque['latitude'] = coordinates[0]
        mosque['longitude'] = coordinates[1]
        mosque['detail_url'] = mosque_element.find_element(By.CSS_SELECTOR, "a:first-child").get_attribute("href")
        mosques.append(mosque)

    os.makedirs('storage/mosque-stage-1', exist_ok=True)
    filename = "mosque" + str(page)
    file_path = f'storage/mosque-stage-1/{filename}.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(mosques, f, ensure_ascii=False, indent=2)
    
