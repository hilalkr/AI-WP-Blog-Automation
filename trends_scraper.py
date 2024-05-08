from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import undetected_chromedriver as uc
from contextlib import contextmanager

class Chrome(uc.Chrome):
    def init(self):
        options = uc.ChromeOptions()
    
        options.add_argument('--blink-settings=imagesEnabled=false')  # image loading disable.

        super().init(options=options)

    def no_timings_detection_get(self, url, wait=0):
        self.execute_script(f"location='{url}'; alert();")
        self.switch_to.alert.accept()
        self.reconnect(wait)


@contextmanager
def get_driver():
    driver = Chrome()
    try:
        yield driver
    finally:
        driver.quit()






def get_trend_topic():
    # Google Trends URL'sine git
    url = "https://trends.google.com/trends/explore?cat=733&geo=TR"
    with get_driver() as driver:
        response = driver.get(url)
        time.sleep(4)
        driver.no_timings_detection_get(url, wait=5)

        # Yapılacak istek için gerekli URL
    
        time.sleep(10)  # Yeterli süre vermek için

        # Sayfanın içeriğini al
        page_source = driver.page_source

        # BeautifulSoup ile içeriği parse etmek yerine Selenium ile doğrudan işlem yap
        response_str = driver.find_elements(By.CLASS_NAME, 'fe-atoms-generic-content-container')[2]
        labels_text= response_str.find_elements(By.CLASS_NAME, 'label-text')
        title_list = []
        for label in labels_text:
            title_list.append(label.text)


    return title_list





















# import requests
# from bs4 import BeautifulSoup
# import json

# with open('cookies.json', 'r') as file:
#     cookies = json.load(file)


# headers = {
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
#     # 'cookie': 'SEARCH_SAMESITE=CgQI15oB; HSID=Aecx19GPN3WpdaAFT; SSID=ABg-T08Ko5SYUdqVR; APISID=obdo-XW6Gznm3FOO/AzWMXtqDhHz9Ukr8N; SAPISID=ZVhToSXb3fiGmops/AV6Ry3HmaI0DgXeT1; __Secure-1PAPISID=ZVhToSXb3fiGmops/AV6Ry3HmaI0DgXeT1; __Secure-3PAPISID=ZVhToSXb3fiGmops/AV6Ry3HmaI0DgXeT1; SID=g.a000jAgE1wZQdJN15PrnyN4XUJsdb6G9DDHYC_QGzMTFXm_a4HoCEERRfnoMVo_9VzCMDsXCxAACgYKAZoSAQASFQHGX2MizESrCt1gZoGAxFFpcnXAORoVAUF8yKpsbMS7FWYHVZcq6UMVCNzV0076; __Secure-1PSID=g.a000jAgE1wZQdJN15PrnyN4XUJsdb6G9DDHYC_QGzMTFXm_a4HoCNoQ9yNv3K9sWoAPhRIKycQACgYKAb8SAQASFQHGX2MiBJbHQ40Qtx0Xl-H2I0rE4RoVAUF8yKqCsJwswqaUpW_mXvvkDYWi0076; __Secure-3PSID=g.a000jAgE1wZQdJN15PrnyN4XUJsdb6G9DDHYC_QGzMTFXm_a4HoCbbXdeXHBYm8hpXbIjaE1vQACgYKAcsSAQASFQHGX2MicTCVjX4K2qtyapi4t1zVpRoVAUF8yKpqs27Oi78bipbb1OXlYyhS0076; AEC=AQTF6HyoTES5_E-9w3nbB_VpNpIPsfFbg8g_oBFhX7gusS3BZD-qG-eUpg; __Secure-1PSIDTS=sidts-CjIBLwcBXOtE_JVS2YcIPBUZIybqKB1_5W1lX2THkcLP1XQ4l-JP6PW2IFztX0mGtZ_TphAA; __Secure-3PSIDTS=sidts-CjIBLwcBXOtE_JVS2YcIPBUZIybqKB1_5W1lX2THkcLP1XQ4l-JP6PW2IFztX0mGtZ_TphAA; NID=514=Xq5V4hV5EW8RYrcwiQWa4CFgMCZtUbLd-c8ZcMlk3fbFtWLi6q2sIAOwkDa6_8kJ18cBzmvx5LQSZvOMNEZ6VkDVKNd4uUKMDSnp_booy-BnxdOivnz3b7mQaon0txxAy7KYZZfnjjKMV0hsjRYTfSZq8tPkF_XPpjb7ng0y1Bk4N5hC4u87fPg_VYpjoLiOWky1yFhLJlYjFd5CC9WYQlE49wIcwl-AeWR7Fuv-h2c7YJ-ikqt4Bwjh60sbnpd5mg3b4e3RZRU0i-xMl1r5Kccph_KMOMssnUXUCq895rHLAIYxj3HEVOROs_LmF8IR6P_7H4CObt1NDSOLQ4POY64rCw1fSWog5SX8bY5AbHmvd2XfRQVqqk2qbyWsl3OXrjn-vk9Yhtru; OTZ=7548003_44_48_123900_44_436380; SIDCC=AKEyXzWl-QPwT8A2PPqvTQZzPDqoel4QIEwnXWv6vdJ3LrkS5lttWfWQ1Ye4bi4ctPVr-IMUoNk; __Secure-1PSIDCC=AKEyXzWrXKMYN9iFpUIfIf9x4h7C3x0iSN66e7-vyqPD9jDHo27k2XMPbBsLIlhyWz8rZnFhfw; __Secure-3PSIDCC=AKEyXzXr35YGFMT-pfqiopAYs82sgOutGxh5xieRDLivnkYaT9ddHFWgFr9twZ_Aoa5Y4SDNIMRr',
#     'priority': 'u=1, i',
#     'referer': 'https://trends.google.com/trends/explore?cat=733&geo=TR',
#     'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
#     'sec-ch-ua-arch': '"x86"',
#     'sec-ch-ua-bitness': '"64"',
#     'sec-ch-ua-full-version': '"124.0.6367.119"',
#     'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.119", "Google Chrome";v="124.0.6367.119", "Not-A.Brand";v="99.0.0.0"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-model': '""',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-ch-ua-platform-version': '"15.0.0"',
#     'sec-ch-ua-wow64': '?0',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
#     'x-client-data': 'CJO2yQEIprbJAQipncoBCJ/kygEIlqHLAQjvmM0BCIWgzQEI4uzNAQji+s0BCPj+zQE=',
# }

# def get_trend_topic():
#     response = requests.get(
#     'https://trends.google.com/trends/api/widgetdata/relatedsearches?hl=tr&tz=-180&req=%7B%22restriction%22:%7B%22geo%22:%7B%22country%22:%22US%22%7D,%22time%22:%222023-04-24+2024-04-24%22,%22originalTimeRangeForExploreUrl%22:%22today+12-m%22%7D,%22keywordType%22:%22QUERY%22,%22metric%22:%5B%22TOP%22,%22RISING%22%5D,%22trendinessSettings%22:%7B%22compareTime%22:%222022-04-22+2023-04-23%22%7D,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22IZG%22,%22category%22:733%7D,%22language%22:%22tr%22,%22userCountryCode%22:%22TR%22,%22userConfig%22:%7B%22userType%22:%22USER_TYPE_LEGIT_USER%22%7D%7D&token=APP6_UEAAAAAZiqsgtIeavhASuzfDQdrlqaCU5NPFP7Y',
#     cookies=cookies,
#     headers=headers,
# )
#     response_str = response.text[5:]
#     response_json = json.loads(response_str)
#     ranked_keyword =response_json["default"]["rankedList"][1]["rankedKeyword"]
#     ranked_list= ranked_keyword[0:5]
#     title_list = []
    
#     for rank in ranked_list:
#         title_list.append(rank["query"])
        
#     return title_list






















