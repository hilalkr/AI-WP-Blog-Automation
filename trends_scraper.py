import requests
from bs4 import BeautifulSoup
import time
import json


cookies = {}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'SEARCH_SAMESITE=CgQI15oB; OGPC=19037049-1:; SID=g.a000iAgE1xK8ojaz27d7oMXbx0BZ9gm5uzgBp2AFIpE80jHbM6CO7hB3l4vSSfLM5N1aUv9OUAACgYKAZISAQASFQHGX2MiUkWYjyaeVRGdtQEmLvotexoVAUF8yKoXhgf-u_GvYby-Ibr3gVq_0076; __Secure-1PSID=g.a000iAgE1xK8ojaz27d7oMXbx0BZ9gm5uzgBp2AFIpE80jHbM6CONpxb2jt9UqQn3CYDfIDj6gACgYKAegSAQASFQHGX2MiMxTAj-Zxij4pIJqT3XDMjxoVAUF8yKrOhsCi0r_fVozKWISUYs200076; __Secure-3PSID=g.a000iAgE1xK8ojaz27d7oMXbx0BZ9gm5uzgBp2AFIpE80jHbM6COaxryfFRv3ihRFzXiWXfkPQACgYKAQ8SAQASFQHGX2MiMUte8-TGqjVvfyuFxBL8sRoVAUF8yKrcHq1ogKosqgANyPLSHTby0076; HSID=AtMbIoRY9T3fEWp6O; SSID=AbBXPpikR12wABMsM; APISID=S9tiaGbQDiHNViwy/A7dHdM96qTuTWFEqR; SAPISID=3jBshnN1deEqWLJO/AcrvfRnXFh17dXPV-; __Secure-1PAPISID=3jBshnN1deEqWLJO/AcrvfRnXFh17dXPV-; __Secure-3PAPISID=3jBshnN1deEqWLJO/AcrvfRnXFh17dXPV-; OTZ=7494949_44_48_123900_44_436380; AEC=AQTF6HwpewCc0Cb08CV-wWLi4aGwpx0S6z7szXebfztAUq1wfJTgzvJWvg; NID=513=LzHOnO1nntBWbm5Q06iUGZMa-zOUgeuJQgXdDIbhTTE8KOkL1XWefIfrpHU9C0NYIDW6uDr9v0bAVRITY4nFXgZ7dscTA6Ac2kDEj0F27wqrWzYm1TDM_Xyp5_vEH_57Vb7mVNqPagLaqAy9J-bhBL3myfkADXFxbnZ96HvYdAtKJ1wsPmoDIGKIwVxQVuy1y12e5PzcEyWaS_SuOmoZ5DFkFECts0lDWxH7NB03V8NweJZGwAKjKxYITweHkI6GiTUZVDuQSHovH8kYqBzFUifAJvM9J9mpfHBohvyyfoIjY-CxqKOAM_T0nBPLiyCMcdFdo1z64GDmYQ_JEA7eFTvolZnpbP0IVrhyYmFqfVF6ArS3c-h4ya2Z-lHkfbYe; __Secure-1PSIDTS=sidts-CjIB7F1E_LgCRdXTZkCqR85VcR9JbMgTyr-_MYnvP5_du-wsd0aAdknd5n4bRCriTSQcbRAA; __Secure-3PSIDTS=sidts-CjIB7F1E_LgCRdXTZkCqR85VcR9JbMgTyr-_MYnvP5_du-wsd0aAdknd5n4bRCriTSQcbRAA; SIDCC=AKEyXzXrBcmCC5lHLb92lCnwFiidPhqFOA8Wgf37G0vMCFcAiO3MiJ_I6x4rz38iIpxeI8t5Tzg; __Secure-1PSIDCC=AKEyXzUkghcd8faTzONql4w0gsdvJmSOLjTmoDUIBtOp1CDoo4MPEPpPpiLectyjXJOGOZzAZA; __Secure-3PSIDCC=AKEyXzV5nog2zsVFJiVNRme37cg5pmQ4ar7KmC2tzqfRNW1jRSnl4JWv8Jqy6vzbjrJFr4wXrpwY',
    'referer': 'https://trends.google.com/trends/explore?cat=733&geo=US&hl=tr',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"123.0.6312.124"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.124", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-client-data': 'CJO2yQEIprbJAQipncoBCJ/kygEIlKHLAQjvmM0BCIWgzQEI4uzNAQji+s0BCPj+zQEIhtXMIhizqcoBGJj1zQEY2IbOAQ==',
}

def get_trend_topic():
    response = requests.get(
        'https://trends.google.com/trends/api/widgetdata/relatedsearches?hl=tr&tz=-180&req=%7B%22restriction%22:%7B%22geo%22:%7B%22country%22:%22US%22%7D,%22time%22:%222023-04-22+2024-04-22%22,%22originalTimeRangeForExploreUrl%22:%22today+12-m%22%7D,%22keywordType%22:%22QUERY%22,%22metric%22:%5B%22TOP%22,%22RISING%22%5D,%22trendinessSettings%22:%7B%22compareTime%22:%222022-04-20+2023-04-21%22%7D,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22IZG%22,%22category%22:733%7D,%22language%22:%22tr%22,%22userCountryCode%22:%22TR%22,%22userConfig%22:%7B%22userType%22:%22USER_TYPE_LEGIT_USER%22%7D%7D&token=APP6_UEAAAAAZif-uDWvn6Gg_RFqpdKmS5A2ZMwc5GSP',
        cookies=cookies,
        headers=headers,
    )
    response_str = response.text[5:]
    response_json = json.loads(response_str)
    ranked_keyword =response_json["default"]["rankedList"][1]["rankedKeyword"]
    ranked_list= ranked_keyword[0:5]
    title_list = []
    
    for rank in ranked_list:
        title_list.append(rank["query"])
        
    return title_list






















