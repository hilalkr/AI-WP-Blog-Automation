import requests
import base64
from requests.auth import HTTPBasicAuth


user_name = "username"
password = "password"
wordpress_url ="https://hilalkara.com"

def create_blog_post(title,content):
    credentials = user_name + ':' + password
    cred_token = base64.b64encode(credentials.encode())
    header = {
        'Authorization': 'Basic ' + cred_token.decode('utf-8'),
        "Content-type": "application/json",
        'User-Agent': "",
        }

    post = {
        "title":{title},
        "content":{content},
        "status":"draft",
        "categories": 22
    }
  
    response = requests.post(f'{wordpress_url}/wp-json/wp/v2/posts',headers=header,json=post)
    print(response.text)
    print(response.status_code)


title = "title"
content = "content"
create_blog_post(title,content)