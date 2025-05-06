from helpers.scrapper import SetupDriver
from helpers.selector import GetElement
import time


def OpenListMosque(driver, province_id, city_id, district_id):
    url = "https://simas.kemenag.go.id/page/profilmasjid/{province_id}/{city_id}/{district_id}/0/0"
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url.format(province_id=province_id, city_id=city_id, district_id=district_id))
    
def GetRegionMaxPage(driver, province_id, city_id, district_id):
    selector = ".page-item:nth-last-child(2) a"
    OpenListMosque(driver, province_id, city_id, district_id)
    time.sleep(4)
    max_page_el = GetElement(driver, selector)
    max_page = max_page_el.get_attribute("innerText")
    tabs = driver.window_handles
    driver.switch_to.window(tabs[0])

    return int(max_page)
