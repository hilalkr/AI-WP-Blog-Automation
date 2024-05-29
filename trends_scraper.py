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
        driver.close()
        driver.quit()






def get_trend_topic():
    url_home="https://trends.google.com"
    url = "https://trends.google.com/trends/explore?cat=733&geo=US&hl=en"
    with get_driver() as driver:
        driver.get(url_home)
        time.sleep(3)
        driver.get(url)
        time.sleep(3)
        driver.no_timings_detection_get(url, wait=5)
        time.sleep(10)  
        
        try:

            content_containers = driver.find_elements(By.CLASS_NAME, 'fe-atoms-generic-content-container')
                    
            # Ensure there is at least three elements before accessing
            if len(content_containers) > 2:
                    response_str = content_containers[2]
                    labels_text = response_str.find_elements(By.CLASS_NAME, 'label-text')
                    title_list = [label.text for label in labels_text]
                    return title_list
            else:
                    print("Not enough elements found.")
                    return []
            
        except Exception as e:
                    print(f"An error occurred: {str(e)}")
                    return []






















