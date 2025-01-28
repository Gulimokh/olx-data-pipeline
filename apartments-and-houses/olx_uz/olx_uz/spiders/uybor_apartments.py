import scrapy
import json

class ListingsSpider(scrapy.Spider):
    name = "listings"
    start_urls = [
        "https://api.uybor.uz/api/v1/listings/residential-complex?limit=10&isShowOnMainMenu__eq=true"
    ]

    def parse(self, response):
        data = json.loads(response.body)
        for listing in data['results']:
            yield {
                'id': listing.get('id'),
                'operation_type': listing.get('operationType'),
                'category_id': listing.get('categoryId'),
                'category_name': listing.get('category', {}).get('name', {}).get('en'),
                'description': listing.get('description'),
                'price': listing.get('price'),
                'price_currency': listing.get('priceCurrency'),
                'is_price_auction': listing.get('isPriceAuction'),
                'price_type': listing.get('priceType'),
                'address': listing.get('address'),
                'region_id': listing.get('regionId'),
                'region_name': listing.get('region', {}).get('name', {}).get('en'),
                'district_id': listing.get('districtId'),
                'district_name': listing.get('district', {}).get('name', {}).get('en'),
                'zone_id': listing.get('zoneId'),
                'zone_name': listing.get('zone', {}).get('name', {}).get('en'),
                'rooms': listing.get('room'),
                'latitude': listing.get('lat'),
                'longitude': listing.get('lng'),
                'square': listing.get('square'),
                'floor': listing.get('floor'),
                'floor_total': listing.get('floorTotal'),
                'is_new_building': listing.get('isNewBuilding'),
                'repair': listing.get('repair'),
                'foundation': listing.get('foundation'),
                'created_at': listing.get('createdAt'),
                'updated_at': listing.get('updatedAt'),
                'is_active': listing.get('isActive'),
                'up_at': listing.get('upAt'),
                'expired_at': listing.get('expiredAt'),
                'views': listing.get('views'),
                'clicks': listing.get('clicks'),
                'favorites': listing.get('favorites'),
                'is_favorite': listing.get('isFavorite'),
                'is_vip': listing.get('isVip'),
                'is_premium': listing.get('isPremium'),
                'is_urgent': listing.get('isUrgently'),
                'price_equivalent': listing.get('priceEquivalent')
            }

