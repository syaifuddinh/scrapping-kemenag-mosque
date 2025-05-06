from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def PressAndEnter(driver, keyword):
    ActionChains(driver).send_keys(keyword).send_keys(Keys.RETURN).perform()