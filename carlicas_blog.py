import scrapy

class carlicasSpider(scrapy.Spider):
    name="carlicas_posts"
    start_urls = [
        "https://carlicas.com/blog/",
    ]

    
    def parse(self, response):
        
        for post in response.css("div.elementor-post__card"):
            yield { 
                "title" : post.css(".elementor-post__title a::text").get(),
                "date" : post.css(".elementor-post-date::text").get(),
                "url" : post.css(".elementor-post__title a::attr(href)").get()
                }
        
        current_page_num = response.css("span.page-numbers.current::text").get()
        
        if int(current_page_num) < 4:
            next_page_ref = int(current_page_num) -1
        else:
            next_page_ref = 3
        
        """ yield {"CCCCCCCCURRENT_PAGE" : current_page_num,
            "UUUUUUUURL_REFF" : next_page_ref
            } """

        try:
            next_page = response.css(".page-numbers::attr(href)")[next_page_ref].get()
        except:
            print("--- END OF CRAWLING ---")
        else:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
