from usecases.GetDistricts import GetDistricts
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
        max_page = GetRegionMaxPage(driver, 1, 1, 24)
        print("max page: ", max_page)
    except Exception as e:
        print(f"Error scraping : {str(e)}")
    finally:
        driver.quit()

if __name__ == '__main__':
    main()