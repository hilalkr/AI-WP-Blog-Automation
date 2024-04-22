import google.generativeai as genai
import os
from trends_scraper import get_trend_topic
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

my_api_key = os.getenv("genai_api_key")

genai.configure(api_key=my_api_key)

def choose_blog_title():
    model = genai.GenerativeModel('gemini-pro')
    trend_titles = get_trend_topic()
    
    response = model.generate_content(f"""
    Prompt:
    "Here are five different trend titles: [{trend_titles[0]}], [{trend_titles[1]}], [{trend_titles[2]}], [{trend_titles[3]}], [{trend_titles[4]}]. Among these titles, select the one that is most related to technology and also the most interesting. Return only that title. Do not return any other information or detail.""")
    print(response.text)
    return response.text


def ai_blog_generate(title):
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(f"""Title: {title}

    Prompt:
    "Based on the provided title, write a comprehensive and SEO-optimized blog post. While planning the content, select relevant keywords related to the topic and use them effectively throughout the article. The content should be detailed and informative, offering valuable insights to the readers. Include appropriate subheadings where necessary, and under each subheading, address different aspects of the topic. Additionally, use a fluid and consistent language style to engage the target audience. Aim for a minimum length of 1500 words. Enrich the content with the most up-to-date information specific to the topic to maximize reader engagement.""")
    return response.text

title = choose_blog_title()
blog = ai_blog_generate(title=title)
print(blog)