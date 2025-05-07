from usecases.GetDistricts import GetDistricts
from concurrent.futures import ThreadPoolExecutor
from helpers.scrapper import SetupDriver
import json
import os

max_workers = 7



def scrape_districts(province_id, province_name, city_id, city_name):
    driver = SetupDriver()
    try:
        url = 'https://simas.kemenag.go.id/'
        driver.get(url)
        driver.implicitly_wait(10)
        GetDistricts(driver, province_id, province_name, city_id, city_name)
    except Exception as e:
        print(f"Error scraping {province_name}: {str(e)}")
    finally:
        driver.quit()

def load_cities():
    cities_dir = os.path.join(os.path.dirname(__file__), 'storage', 'cities')
    cities = []
    
    try:
        # Iterate through all JSON files in the cities directory
        for filename in os.listdir(cities_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(cities_dir, filename)
                with open(file_path, 'r') as file:
                    city_data = json.load(file)
                    # Transform each city entry into the required format
                    for city in city_data:
                        cities.append((city['province_id'], 
                                     city['province_name'], 
                                     city['id'], 
                                     city['name'].lower()))
    except Exception as e:
        print(f"Error loading cities: {str(e)}")
    return cities

def main():
    # Load and merge cities from all JSON files
    cities = load_cities()
    
    if not cities:
        print("No cities loaded. Exiting...")
        return
    
    try:
        # Use ThreadPoolExecutor for concurrent execution
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all scraping tasks
            futures = [executor.submit(scrape_districts, province_id, province_name, city_id, city_name) 
                      for province_id, province_name, city_id, city_name in cities]
            
            # Wait for all tasks to complete
            for future in futures:
                future.result()
                
    except Exception as e:
        print(f"An error occurred in main: {str(e)}")

if __name__ == '__main__':
    main()