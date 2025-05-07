from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def GetFormalName(keyword):
   res = keyword.lower().replace(" ", "")

   return res

def GetCoordinatesFromURL(url):
    if "query=" in url:
        # Extract coordinates from Google Maps URL
        query_params = url.split("query=")[1]
        coordinates = query_params.split(",")
    else:
        # Handle original URL format
        coordinates = url.split("/")[-1].split(",")
    
    latitude = float(coordinates[0])
    longitude = float(coordinates[1])
    return latitude, longitude