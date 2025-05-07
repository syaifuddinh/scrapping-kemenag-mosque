from usecases.GetMosque import GetMosque
from concurrent.futures import ThreadPoolExecutor
from helpers.scrapper import SetupDriver
import json
import os

max_workers = 18
start = 6941
end = 15605

def scrape_mosque(page):
    driver = SetupDriver()
    try:
        url = 'https://simas.kemenag.go.id/page/profilmasjid/11/0/0/0/0?page=' + str(page)
        driver.get(url)
        driver.implicitly_wait(10)
        GetMosque(driver, page)
    except Exception as e:
        print(f"Error scraping {str(e)}")
    finally:
        driver.quit()

def main():
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        pages = range(start, end + 1)
        futures = [executor.submit(scrape_mosque, page) for page in pages]
        
        for future in futures:
            try:
                future.result()
            except Exception as e:
                print(f"Task failed with error: {str(e)}")


if __name__ == '__main__':
    main()