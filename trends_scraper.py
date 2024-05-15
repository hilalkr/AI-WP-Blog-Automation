from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import undetected_chromedriver as uc
from contextlib import contextmanager

class Chrome(uc.Chrome):
    def __init__(self):
        options = uc.ChromeOptions()
    
        options.add_argument('--blink-settings=imagesEnabled=false')  # image loading disable.

        super().__init__(options=options)
    def __del__(self):
        try:
            self.quit()
        except Exception as e:
            pass 

    def no_timings_detection_get(self, url, wait=0):
        self.execute_script(f"location='{url}'; alert();")
        self.switch_to.alert.accept()
        self.reconnect(wait)


@contextmanager         #used for resource management
def get_driver():       #The get_driver() function is defined as a context manager.    
    driver = Chrome()   #This function was used to manage web driver operations with Selenium.
    try:
        yield driver
    finally:
        driver.quit()






def get_trend_topic():

    url = "https://trends.google.com/trends/explore?cat=733&geo=TR"
    with get_driver() as driver:
        response = driver.get(url)
        time.sleep(4)
        driver.no_timings_detection_get(url, wait=5)

       
    
        time.sleep(10)  

        page_source = driver.page_source


        response_str = driver.find_elements(By.CLASS_NAME, 'fe-atoms-generic-content-container')[2]
        labels_text= response_str.find_elements(By.CLASS_NAME, 'label-text')
        title_list = []
        for label in labels_text:
            title_list.append(label.text)


    return title_list






















