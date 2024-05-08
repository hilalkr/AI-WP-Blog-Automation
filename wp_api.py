import requests
import base64
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
import os

user_name = os.getenv("user_name")
password = os.getenv("password")
wordpress_url ="https://hilalkara.com"

def create_blog_post(title,content, meta, hashtag_list):
    credentials = user_name + ':' + password
    cred_token = base64.b64encode(credentials.encode())
    header = {
        'Authorization': 'Basic ' + cred_token.decode('utf-8'),
        "Content-type": "application/json",
        'User-Agent': "",
        }

    post = {
        "title":title,
        "content":content,
        "status":"draft",
        "categories": 22,
        "meta": {
            "description": meta
            } 
    }
  
    response = requests.post(f'{wordpress_url}/wp-json/wp/v2/posts',headers=header,json=post)
    return response




