from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from usecases.GetCities import GetCities
from concurrent.futures import ThreadPoolExecutor
import json
import os

max_workers = 3

def setup_driver():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    
    # Initialize the Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_cities(province_id, province_name):
    driver = setup_driver()
    try:
        url = 'https://simas.kemenag.go.id/'
        driver.get(url)
        driver.implicitly_wait(10)
        GetCities(driver, province_id, province_name)
    except Exception as e:
        print(f"Error scraping {province_name}: {str(e)}")
    finally:
        driver.quit()

def load_provinces():
    json_path = os.path.join(os.path.dirname(__file__), 'storage', 'materials', 'provinces.json')
    try:
        with open(json_path, 'r') as file:
            provinces_data = json.load(file)
            return [(p['id'], p['provinceName'].lower()) for p in provinces_data]
    except Exception as e:
        print(f"Error loading provinces: {str(e)}")
        return []

def main():
    # Load provinces from JSON file
    provinces = load_provinces()
    if not provinces:
        print("No provinces loaded. Exiting...")
        return
    
    try:
        # Use ThreadPoolExecutor for concurrent execution
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all scraping tasks
            futures = [executor.submit(scrape_cities, pid, pname) for pid, pname in provinces]
            
            # Wait for all tasks to complete
            for future in futures:
                future.result()
                
    except Exception as e:
        print(f"An error occurred in main: {str(e)}")

if __name__ == '__main__':
    main()