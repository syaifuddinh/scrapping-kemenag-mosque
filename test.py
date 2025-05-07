from usecases.GetDistricts import GetDistricts
from usecases.GetCities import GetCities
from concurrent.futures import ThreadPoolExecutor
from helpers.scrapper import SetupDriver
from entities.mosque import GetRegionMaxPage
import json
import os



def main():
    driver = SetupDriver()
    try:
        url = 'https://simas.kemenag.go.id/'
        driver.get(url)
        driver.implicitly_wait(10)
        city_id = 268
        city_name = "Kab. Jembrana"
        province_id = 17
        province_name = "Bali"
        GetDistricts(driver, province_id, province_name, city_id, city_name)
    except Exception as e:
        print(f"Error scraping : {str(e)}")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()