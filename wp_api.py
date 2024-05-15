import requests
import base64
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
import os

user_name = os.getenv("user_name")
password = os.getenv("password")
wordpress_url ="https://hilalkara.com"

def create_tag(tag_name):
    tag_data = {
        "name": tag_name,
        "description":tag_name,
        "slug":tag_name.lower()
    }
    credentials = user_name + ':' + password
    cred_token = base64.b64encode(credentials.encode())
    header = {
        'Authorization': 'Basic ' + cred_token.decode('utf-8'),
        "Content-type": "application/json",
        'User-Agent': "",
        }
    response = requests.post(f"{wordpress_url}/wp-json/wp/v2/tags", headers=header, json= tag_data)
    if response.status_code == 201:
        tag_id = response.json()['id']
        print(f"Tag '{tag_name}' created with ID: {tag_id}")
        return tag_id
    else:
        print(f"Failed to create tag '{tag_name}': {response.status_code}")
        print(response.json())
        return None
    
def create_blog_post(title,content, meta, tag_ids):
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
            },
        "tags": tag_ids 
    }
  
    response = requests.post(f'{wordpress_url}/wp-json/wp/v2/posts',headers=header,json=post)
    return response




