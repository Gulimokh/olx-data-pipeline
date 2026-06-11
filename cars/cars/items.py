import scrapy


class CarItem(scrapy.Item):
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

    # --- Car specific fields ---
    model = scrapy.Field()
    car_body = scrapy.Field()
    motor_year = scrapy.Field()
    motor_mileage = scrapy.Field()
    transmission_type = scrapy.Field()
    color = scrapy.Field()
    motor_engine_size = scrapy.Field()
    fuel_type = scrapy.Field()
    condition = scrapy.Field()
    owners = scrapy.Field()
    car_option = scrapy.Field()
