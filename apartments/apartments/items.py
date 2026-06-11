import scrapy


class ApartmentItem(scrapy.Item):
    """OLX.uz listing item — common metadata fields."""

    # --- OLX common fields (present in all categories) ---
    title = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    description = scrapy.Field()
    content_id = scrapy.Field()
    category = scrapy.Field()
    category_type = scrapy.Field()
    url = scrapy.Field()
    isBusiness = scrapy.Field()
    isHighlighted = scrapy.Field()
    isPromoted = scrapy.Field()
    promotion = scrapy.Field()
    delivery = scrapy.Field()
    createdTime = scrapy.Field()
    lastRefreshTime = scrapy.Field()
    pushupTime = scrapy.Field()
    validToTime = scrapy.Field()
    isActive = scrapy.Field()
    status = scrapy.Field()
    itemCondition = scrapy.Field()
    negotiable = scrapy.Field()
    cityName = scrapy.Field()
    regionName = scrapy.Field()
    districtName = scrapy.Field()
    user = scrapy.Field()

    # --- Apartment specific fields ---
    number_of_rooms = scrapy.Field()
    floor = scrapy.Field()
    total_floors = scrapy.Field()
    house_type = scrapy.Field()
    layout = scrapy.Field()
    year_of_construction_sale = scrapy.Field()
    wc = scrapy.Field()
    furnished = scrapy.Field()
    ceiling_height = scrapy.Field()
    repairs = scrapy.Field()
    comission = scrapy.Field()
    total_area = scrapy.Field()
    total_living_area = scrapy.Field()
