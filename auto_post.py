from ai_generate import choose_blog_title,ai_blog_generate
from wp_api import create_blog_post
import markdown


title = choose_blog_title()
blog = ai_blog_generate(title=title)

print(title)
print(blog)
blog_post = blog.split("---")[0]
meta_tags = blog.split("---")[1]
meta_description= meta_tags.split("**Meta Description:**")[1].split("**Tags:**")[0]
tags = meta_tags.split("**Tags:**")[1]

hashtag_list = tags.split()

# Listenin başındaki '#' karakterini temizle
hashtag_list = [tag.strip('#') for tag in hashtag_list]

# Sonucu yazdır
print(hashtag_list)

html_content = markdown.markdown(blog_post)


create_blog_post(title,html_content, meta_description, hashtag_list)