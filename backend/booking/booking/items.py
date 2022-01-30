# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    image_url = scrapy.Field()
    score = scrapy.Field()
    description = scrapy.Field()