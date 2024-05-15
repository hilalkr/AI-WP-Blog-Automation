from ai_generate import choose_blog_title,ai_blog_generate
from wp_api import create_blog_post, create_tag
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


hashtag_list = [tag.strip('#') for tag in hashtag_list]

print(hashtag_list)
tag_ids=[]
for tag_name in hashtag_list:
    tag_id = create_tag(tag_name)
    if tag_id:
        tag_ids.append(tag_id)
        
html_content = markdown.markdown(blog_post)


create_blog_post(title,html_content, meta_description, tag_ids=tag_ids)