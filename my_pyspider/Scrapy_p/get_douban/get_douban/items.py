# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetDoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serial_number = scrapy.Field()
    film_name = scrapy.Field()
    film_intro = scrapy.Field()
    film_star = scrapy.Field()
    film_eval = scrapy.Field()
    film_describe = scrapy.Field()