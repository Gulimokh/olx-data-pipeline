import scrapy
import json
import js2py


class LandOlxSpider(scrapy.Spider):
    name = "land_olx"
    allowed_domains = ["olx.uz"]
    start_urls = [
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=filter_float_price:desc',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=4',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=3',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=5&search%5Bfilter_enum_comission%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=5&search%5Bfilter_enum_location%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=5&search%5Bfilter_enum_location%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=5&search%5Bfilter_enum_location%5D%5B0%5D=3&search%5Bfilter_enum_location%5D%5B1%5D=4&search%5Bfilter_enum_location%5D%5B2%5D=5&search%5Bfilter_enum_location%5D%5B3%5D=6&search%5Bfilter_enum_location%5D%5B4%5D=7&search%5Bfilter_enum_location%5D%5B5%5D=8&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:to%5D=50&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=50&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=3&search%5Bfilter_enum_location%5D%5B1%5D=4&search%5Bfilter_enum_location%5D%5B2%5D=5&search%5Bfilter_enum_location%5D%5B3%5D=6&search%5Bfilter_enum_location%5D%5B4%5D=7&search%5Bfilter_enum_location%5D%5B5%5D=8&search%5Bfilter_enum_comission%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:to%5D=3&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=6&search%5Bfilter_float_land_area:to%5D=6&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=6&search%5Bfilter_float_land_area:to%5D=9&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=9&search%5Bfilter_float_land_area:to%5D=20&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=20&search%5Bfilter_float_land_area:to%5D=500&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=500&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:to%5D=3&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=6&search%5Bfilter_float_land_area:to%5D=6&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=9&search%5Bfilter_float_land_area:to%5D=30&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=30&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:to%5D=15&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=15&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:to%5D=20&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_land_area:from%5D=20&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=5&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/zemlja/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_purpose%5D%5B0%5D=1&search%5Bfilter_enum_location%5D%5B0%5D=6&search%5Bfilter_enum_location%5D%5B1%5D=7&search%5Bfilter_enum_location%5D%5B2%5D=8&search%5Bfilter_enum_comission%5D%5B0%5D=no',

    ]


    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "DOWNLOAD_TIMEOUT": 60,
        "COOKIES_ENABLED": True,
        "ROBOTSTXT_OBEY": True,
        "RETRY_TIMES": 2,
        "FEEDS": {
            "/Users/gulimoh/collateral-assessment/land/land/data/land.json": {
                "format": "json",
                "overwrite": True}
        }
    }

    def parse(self, response):
        # Extract links to listing detail pages
        for house in response.css('div[data-cy="l-card"]'):
            detail_page = house.css('div[data-cy="ad-card-title"]>a::attr(href)').get()
            if detail_page:
                yield response.follow(detail_page, self.parse_detail)

        # Follow to next page
        next_page = response.css('a[data-cy="pagination-forward"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_detail(self, response):
        js_content = self.extract_js_content(response)
        params_arr = js_content['ad']['ad']['params']
        params = {item['key']: item['value'] for item in params_arr}

        category_id = js_content['ad']['ad']['category']['id']
        category = js_content['categories']['list'][str(category_id)]['name']

        # Build extracted data dict
        land_data = {
            'title': js_content['ad']['ad']['title'],
            'price': js_content['ad']['ad']['price']['regularPrice']['value'],
            'currency': js_content['ad']['ad']['price']['regularPrice']['currencyCode'],
            'description': js_content['ad']['ad']['description'],
            'content_id': js_content['ad']['ad']['id'],
            'category': category,
            'category_type': js_content['ad']['ad']['category']['type'],
            'url': response.url,
            'isBusiness': js_content['ad']['ad']['isBusiness'],
            'isHighlighted': js_content['ad']['ad']['isHighlighted'],
            'isPromoted': js_content['ad']['ad']['isPromoted'],
            'promotion': json.dumps(js_content['ad']['ad']['promotion']),
            'delivery': json.dumps(js_content['ad']['ad']['delivery']),
            'createdTime': js_content['ad']['ad']['createdTime'],
            'lastRefreshTime': js_content['ad']['ad']['lastRefreshTime'],
            'pushupTime': js_content['ad']['ad'].get('pushupTime', None),
            'validToTime': js_content['ad']['ad']['validToTime'],
            'isActive': js_content['ad']['ad']['isActive'],
            'status': js_content['ad']['ad']['status'],
            'itemCondition': js_content['ad']['ad']['itemCondition'],
            'negotiable': js_content['ad']['ad']['price']['regularPrice']['negotiable'],
            'cityName': js_content['ad']['ad']['location']['cityName'],
            'regionName': js_content['ad']['ad']['location']['regionName'],
            'districtName': js_content['ad']['ad']['location'].get('districtName', None),
            'user': json.dumps(js_content['ad']['ad']['user']),

            # Land parameters

            "total_area": params.get("total_area"),
            "land_type": params.get("land_type"),  # e.g. "Indivisible"
            "purpose": params.get("purpose"),
            "in_city": params.get("location_place"),  # e.g. "in city", "in suburb", "in village"


            "comission": params.get("comission"),
            "water": params.get("water"),
            "heating": params.get("heating"),
            "gas": params.get("gas"),
            "electricity": params.get("electricity"),
            "internet": params.get("internet"),
            "phone": params.get("phone"),
            "canalization": params.get("canalization"),
            "communications": params.get("communications"),
            "location": params.get("location"),
            "near_is": params.get("near_is"),
        }

        self.logger.info(f"✅ [SUCCESS] Scraped listing: {land_data['title']}")
        yield land_data

    def extract_js_content(self, response):
        """Extract JavaScript content from OLX page."""
        script_content = response.xpath('//script[@id="olx-init-config"]/text()').get()
        if not script_content:
            self.logger.error("Error: script tag with id 'olx-init-config' not found")
            return None

        js = script_content + " window.__PRERENDERED_STATE__;"

        try:
            js_context = js2py.eval_js(js)
        except js2py.base.PyJsException:
            js_context = ""
            self.logger.error("Error: failed to execute JavaScript")

        js_content = json.loads(js_context)
        return js_content







