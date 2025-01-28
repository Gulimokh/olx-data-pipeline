# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ApartmentItem(scrapy.Item):
    content_id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
    is_business = scrapy.Field()
    rooms = scrapy.Field()
    total_area = scrapy.Field()
    living_area = scrapy.Field()
    kitchen_area = scrapy.Field()
    floor = scrapy.Field()
    total_floors = scrapy.Field()
    house_type = scrapy.Field()
    layout = scrapy.Field()
    year_built = scrapy.Field()
    bathroom = scrapy.Field()
    furnished = scrapy.Field()
    ceiling_height = scrapy.Field()
    nearby = scrapy.Field()
    features = scrapy.Field()
    renovation = scrapy.Field()
    commission = scrapy.Field()
    description = scrapy.Field()
    created_time = scrapy.Field()
    updated_time = scrapy.Field()
    city_id = scrapy.Field()
    city_name = scrapy.Field()
    city_normalized_name = scrapy.Field()
    district_id = scrapy.Field()
    district_name = scrapy.Field()
    region_id = scrapy.Field()
    region_name = scrapy.Field()
    region_normalized_name = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    negotiable = scrapy.Field()
    type_of_market = scrapy.Field()
