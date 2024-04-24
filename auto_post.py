from ai_generate import choose_blog_title,ai_blog_generate
from wp_api import create_blog_post
import markdown


title = choose_blog_title()
blog = ai_blog_generate(title=title)

print(title)
html_content = markdown.markdown(blog)
print(html_content)

create_blog_post(title,html_content)