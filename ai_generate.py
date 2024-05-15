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
    "Here are five different trend titles: [{trend_titles[0]}], [{trend_titles[1]}], [{trend_titles[2]}], [{trend_titles[3]}], [{trend_titles[4]}]. Among these titles, select the one that is most related to technology and also the most interesting. Enhance the selected title to make it more suitable and appealing for a blog post. Return only the refined title. Do not return any other information or detail.""")
    return response.text


def ai_blog_generate(title):
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(f"""Title: {title}

    Prompt:
    "Based on the provided title, write a comprehensive and SEO-optimized blog post. While planning the content, select relevant keywords related to the topic and use them effectively throughout the article. The content should be detailed and informative, offering valuable insights to the readers. Include appropriate subheadings where necessary, and under each subheading, address different aspects of the topic. Additionally, use a fluid and consistent language style to engage the target audience. Aim for a minimum length of 1500 words. Enrich the content with the most up-to-date information specific to the topic to maximize reader engagement. End the blog post content with three dashes (---) to clearly separate the main body from the meta description and tags. Below the dashes, write 'Meta Description:' and provide a concise summary of the blog post. Then list the tags relevant to the post, each preceded by a hashtag.Also answer the title of the meta section like this: **Meta Description:** . In the same way, write like this for the tag: **Tags:** .""")
    return response.text

