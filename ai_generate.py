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
    "Write an SEO-optimized blog post based on the provided title. The title should start with the main keyword and be 45-60 characters long, with 3-6 words. Limit the meta description to 145 characters. Highlight important parts with bold, italic, or colored text. Ensure sentences are up to 20 words and use transition words in at least 30% of sentences for better flow. The content should be at least 1500 words, using relevant keywords throughout. Provide detailed, informative content with simple language, enriched with up-to-date information, and use subheadings to cover different aspects. Maintain a fluid and engaging language style. End the main body of the blog post with three dashes (---) to clearly separate the main body from the meta description and tags.Below the dashes, write 'Meta Description:' and provide a concise summary of the blog post. Then list the tags relevant to the post, each preceded by a hashtag.Also answer the title of the meta section like this: **Meta Description:** . In the same way, write like this for the tag: **Tags:** .""")
    return response.text

