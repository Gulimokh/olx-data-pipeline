import scrapy


class CommercialPremisesItem(scrapy.Item):
    """OLX.uz listing item — common metadata fields."""

    # --- OLX common fields (present in all categories) ---
    title = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    description = scrapy.Field()
    content_id = scrapy.Field()
    category = scrapy.Field()
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
    negotiable = scrapy.Field()
    cityName = scrapy.Field()
    regionName = scrapy.Field()
    districtName = scrapy.Field()
    user = scrapy.Field()

    # --- CommercialPremises specific fields ---
    premise_type = scrapy.Field()
    total_area = scrapy.Field()
    effective_area = scrapy.Field()
    floor = scrapy.Field()
    total_floors = scrapy.Field()
    ceiling_height = scrapy.Field()
    repairs = scrapy.Field()
    comission = scrapy.Field()
    parking_lot = scrapy.Field()
    land = scrapy.Field()
    more_premises = scrapy.Field()
