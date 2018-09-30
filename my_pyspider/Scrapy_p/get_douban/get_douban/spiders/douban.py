# -*- coding: utf-8 -*-
import scrapy
from ..items import GetDoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']//li")
        for item in movie_list:
            movieitem = GetDoubanItem()
            movieitem['serial_number'] = item.xpath(".//div[@class='item']//div[@class='pic']//em//text()").extract_first()
            movieitem['film_name']=item.xpath(".//div[@class='info']//div[@class='hd']//a//span[1]//text()").extract_first()
            content=item.xpath(".//div[@class='bd']//p[1]/text()").extract()
            for i_content in content:
                content_s="".join(i_content.split())
                movieitem['film_intro']=content_s
            movieitem['film_star']=item.xpath(".//span[@class='rating_num']/text()").extract_first()
            movieitem['film_eval']=item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            movieitem['film_describe']=item.xpath(".//p[@class='quote']//span[1]/text()").extract_first()
            yield movieitem
            next_link=response.xpath("//span[@class='next']/link/@href").extract()
        if  next_link:
            next_link=next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)