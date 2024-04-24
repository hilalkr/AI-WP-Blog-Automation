import requests
from bs4 import BeautifulSoup
import json

with open('cookies.json', 'r') as file:
    cookies = json.load(file)


headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://trends.google.com/trends/explore?cat=733&geo=US',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"124.0.6367.61"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.61", "Google Chrome";v="124.0.6367.61", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-client-data': 'CJO2yQEIprbJAQipncoBCJ/kygEIlaHLAQjvmM0BCIWgzQEI4uzNAQji+s0BCPj+zQEIhtXMIhizqcoBGNiGzgE=',
}

def get_trend_topic():
    response = requests.get(
    'https://trends.google.com/trends/api/widgetdata/relatedsearches?hl=tr&tz=-180&req=%7B%22restriction%22:%7B%22geo%22:%7B%22country%22:%22US%22%7D,%22time%22:%222023-04-24+2024-04-24%22,%22originalTimeRangeForExploreUrl%22:%22today+12-m%22%7D,%22keywordType%22:%22QUERY%22,%22metric%22:%5B%22TOP%22,%22RISING%22%5D,%22trendinessSettings%22:%7B%22compareTime%22:%222022-04-22+2023-04-23%22%7D,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22IZG%22,%22category%22:733%7D,%22language%22:%22tr%22,%22userCountryCode%22:%22TR%22,%22userConfig%22:%7B%22userType%22:%22USER_TYPE_LEGIT_USER%22%7D%7D&token=APP6_UEAAAAAZiqsgtIeavhASuzfDQdrlqaCU5NPFP7Y',
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






















