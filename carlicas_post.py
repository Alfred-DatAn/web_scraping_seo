import scrapy
import json

with open("carlicas_posts.json") as blog_data:
    posts = json.load(blog_data)

articles_urls = []
for post in posts:
    articles_urls.append(post["url"])

class carPostSpider(scrapy.Spider):
    name = "carlicas_blog_post"
    start_urls = articles_urls

    def parse(self, response):
        yield {
            "h1" : response.css("h1::text").getall(),
            "h2" : response.css("h2::text").getall(),
            "h3" : response.css("h3::text").getall(),
            "h4" : response.css("h4::text").getall(),
            "text_body" : response.css("p::text").getall(),
            "em" : response.css("em::text").getall(),
            "strong" : response.css("strong::text").getall(),
            "li" : response.css("li::text").getall(),
            "a" : response.css("p a::text").getall()
        }