import scrapy
import js2py
import json

class trucksSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_item_count = {}
    name = "trucksspiders"
    allowed_domains = ["www.olx.uz"]
    start_urls = [
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=562',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=562',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=563',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=563',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=564',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=564',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=565',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=565',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=566',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=566',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=567',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=567',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=568',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=568',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=569',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=569',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=570',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=570',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=571',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=571',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=572',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=572',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=573',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=573',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=574',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=574',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_body_type%5D%5B0%5D=575',
        'https://www.olx.uz/transport/gruzovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_body_type%5D%5B0%5D=575',
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'DOWNLOAD_TIMEOUT': 60, # Increase timeout to 30 seconds
        'COOKIES_ENABLED': True,
        'ROBOTSTXT_OBEY': True,
        'RETRY_TIMES': 2, # Increase the number of retries
        "FEEDS": {
            "trucks_olx.json": {"format": "json", "overwrite": True}
        }

    }

    def parse(self, response):
    # Extract links to listing detail pages
        for trucks in response.css('div[data-cy="l-card"]'):
            detail_page = trucks.css('div[data-cy="ad-card-title"]>a::attr(href)').get()
            if detail_page:
                yield response.follow(detail_page, self.parse_detail)

        # Follow to next page if available
        next_page = response.css('a[data-cy="pagination-forward"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_detail(self, response):

        js_content = self.extract_js_content(response)

        params_arr = js_content['ad']['ad']['params']
        params = {item['key']: item['value'] for item in params_arr}

        categoryId = js_content['ad']['ad']['category']['id']
        category = js_content['categories']['list'][str(categoryId)]['name']
        #print("CATEGORY:", category)
        #print("PARENT ID:", parent_id)
        #print("MAIN CATEGORY:", main_category)

        itemValues = {
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
            'promotion': json.dumps(js_content['ad']['ad']['promotion']), #json
            'delivery': json.dumps(js_content['ad']['ad']['delivery']), #json
            'createdTime': js_content['ad']['ad']['createdTime'],
            'lastRefreshTime': js_content['ad']['ad']['lastRefreshTime'],
            'pushupTime': js_content['ad']['ad'].get('pushupTime', None),
            'validToTime': js_content['ad']['ad']['validToTime'],
            'isActive': js_content['ad']['ad']['isActive'],
            'status': js_content['ad']['ad']['status'],
            'isJob': js_content['ad']['ad']['isJob'],
            'itemCondition': js_content['ad']['ad']['itemCondition'],
            'negotiable': js_content['ad']['ad']['price']['regularPrice']['negotiable'],
            'cityName': js_content['ad']['ad']['location']['cityName'],
            'regionName': js_content['ad']['ad']['location']['regionName'],
            'districtName': js_content['ad']['ad']['location']['districtName'],
            'olx_user': json.dumps(js_content['ad']['ad']['user']), #json

        }
        for key, value in params.items():
            if key not in itemValues:
                itemValues[key] = value


        self.logger.info(f"✅ [SUCCESS] Scraped listing: {itemValues['title']}")
        yield itemValues

    def extract_js_content(self, response):
        """Extract and evaluate the JavaScript content."""
        script_content = response.xpath('//script[@id="olx-init-config"]/text()').get()
        if not script_content:
            self.logger.error("Script tag with id 'olx-init-config' not found")
            return None

        js = script_content + " window.__PRERENDERED_STATE__;"

        try:
            js_context = js2py.eval_js(js)
        except js2py.base.PyJsException:
            js_context = ""
            self.logger.error("Failed to evaluate JavaScript content")

        js_content = json.loads(js_context)
        # print(js_content)
        return js_content