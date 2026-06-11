import scrapy


class TruckItem(scrapy.Item):
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
    isJob = scrapy.Field()
    itemCondition = scrapy.Field()
    negotiable = scrapy.Field()
    cityName = scrapy.Field()
    regionName = scrapy.Field()
    districtName = scrapy.Field()
    olx_user = scrapy.Field()

    # --- Truck specific fields ---
    truck_manufacturer = scrapy.Field()
    body_type = scrapy.Field()
