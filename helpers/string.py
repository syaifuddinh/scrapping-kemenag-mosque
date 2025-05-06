from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def GetFormalName(keyword):
   res = keyword.lower().replace(" ", "")

   return res