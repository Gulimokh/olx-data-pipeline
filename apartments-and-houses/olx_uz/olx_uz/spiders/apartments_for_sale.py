import scrapy
import scrapy
import json  # Импортируем модуль json
from olx_uz.items import ApartmentItem
import js2py


class OLXApartmentSpider(scrapy.Spider):
    name = "olx_apartments"
    allowed_domains = ["olx.uz"]
    start_urls = [
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/tashkent/?currency=UYE&search%5Border%5D=created_at%3Adesc',
    ]
    custom_settings = {
        'FEEDS': {
            'olx_uz_apartments.json': {'format': 'json', 'overwrite': True}
        }
    }

    def parse(self, response):
        for item in response.css('div[data-cy="l-card"]'):
            detail_page = item.css('a::attr(href)').get()
            if detail_page:
                yield response.follow(detail_page, self.parse_detail)

        next_page = response.css('a[data-cy="pagination-forward"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_detail(self, response):

        apartment_item = ApartmentItem()

        js_content = self.extract_js_content(response)

        apartment_item['title'] = response.css('div[data-cy="ad_title"] h4::text').get()
        apartment_item['price'] = response.css('div[data-testid="ad-price-container"] h3::text').get()
        apartment_item['url'] = response.url
        apartment_item['is_business'] = js_content['ad']['ad']['isBusiness']
        apartment_item['type_of_market'] = response.css('li:contains("Тип жилья") p::text').get()
        apartment_item['rooms'] = response.css('li:contains("Количество комнат") p::text').get()
        apartment_item['living_area'] = response.css('li:contains("Жилая площадь") p::text').get()
        apartment_item['total_area'] = response.css('li:contains("Общая площадь") p::text').get()
        apartment_item['kitchen_area'] = response.css('li:contains("Площадь кухни") p::text').get()
        apartment_item['floor'] = response.css('li:contains("Этаж") p::text').get()
        apartment_item['total_floors'] = response.css('li:contains("Этажность дома") p::text').get()
        apartment_item['house_type'] = response.css('li:contains("Тип строения") p::text').get()
        apartment_item['layout'] = response.css('li:contains("Планировка") p::text').get()
        apartment_item['year_built'] = response.css('li:contains("Год постройки/сдачи") p::text').get()
        apartment_item['bathroom'] = response.css('li:contains("Санузел") p::text').get()
        apartment_item['furnished'] = response.css('li:contains("Меблирована") p::text').get()
        apartment_item['ceiling_height'] = response.css('li:contains("Высота потолков") p::text').get()
        apartment_item['features'] = response.css('li:contains("В квартире есть") p::text').get()
        apartment_item['nearby'] = response.css('li:contains("Рядом есть") p::text').get()
        apartment_item['renovation'] = response.css('li:contains("Ремонт") p::text').get()
        apartment_item['commission'] = response.css('li:contains("Комиссионные") p::text').get()
        apartment_item['description'] = js_content['ad']['ad']['description']
        apartment_item['content_id'] = js_content['ad']['ad']['id']
        apartment_item['created_time'] = js_content['ad']['ad']['createdTime']
        apartment_item['updated_time'] = js_content['ad']['ad']['lastRefreshTime']
        apartment_item['city_id'] = js_content['ad']['ad']['location']['cityId']
        apartment_item['city_name'] = js_content['ad']['ad']['location']['cityName']
        apartment_item['city_normalized_name'] = js_content['ad']['ad']['location']['cityNormalizedName']
        apartment_item['district_id'] = js_content['ad']['ad']['location']['districtId']
        apartment_item['district_name'] = js_content['ad']['ad']['location']['districtName']
        apartment_item['region_id'] = js_content['ad']['ad']['location']['regionId']
        apartment_item['region_name'] = js_content['ad']['ad']['location']['regionName']
        apartment_item['region_normalized_name'] = js_content['ad']['ad']['location']['regionNormalizedName']
        apartment_item['longitude'] = js_content['ad']['ad']['map']['lon']
        apartment_item['latitude'] = js_content['ad']['ad']['map']['lat']
        apartment_item['negotiable'] = js_content['ad']['ad']['price']['regularPrice']['negotiable']

        yield apartment_item

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
        return js_content


class OlxSpider(scrapy.Spider):
    name = "olx"
    start_urls = [
        'https://www.olx.uz/d/obyavlenie/chilonzor-novostroyka-3xona-70m-2-ID3JLia.html',
    ]

    def parse(self, response):
        js_content = self.extract_js_content(response)
        print(response.css('li:contains("Этаж") p::text').get())
        if js_content:
            # Extract the necessary fields from the JavaScript content
            location, top_ad, lon, lat, refresh_time = self.extract_data_from_js(js_content)
        yield {
            'title': response.css('h1.css-rj6ybf-Text.eu5v0x0::text').get(),
            'price': response.css('span.css-8kqr5l-Text.eu5v0x0::text').get(),
            'location': response.css('span.css-17y7clw-Text.eu5v0x0::text').get(),
            'description': response.css('div.css-g5mtbi-Text.eu5v0x0::text').getall(),
            'attributes': response.css('ul.css-sfcl1s-Text.eu5v0x0 li::text').getall(),
            'contact_name': response.css('h3.css-1lcz6o7-Text.eu5v0x0::text').get(),
            'contact_phone': response.css('div.css-1wvg8dw-Text.eu5v0x0::text').re_first(r'Тел\.\s*(.*)'),
        }

        # To run the spider, you would typically use the following command in your terminal:
        # scrapy runspider olx_spider.py -o output.json

        script_content = response.xpath('//script[@id="olx-init-config"]/text()').get()

    def extract_js_content(self, response):
        """Extract and evaluate the JavaScript content."""
        script_content = response.xpath('//script[@id="olx-init-config"]/text()').get()
        if not script_content:
            self.logger.error("Script tag with id 'olx-init-config' not found")
            return None

        # Combine script content with the variable assignment for window.__PRERENDERED_STATE__
        js = script_content + " window.__PRERENDERED_STATE__;"

        try:
            js_context = js2py.eval_js(js)
            return js_context
        except js2py.base.PyJsException:
            self.logger.error("Failed to evaluate JavaScript content")
            return None

    def extract_data_from_js(self, js_content):
        """Extract data from the evaluated JavaScript content."""
        try:
            location = js_content['ad']['ad']['location']['pathName']
        except (KeyError, TypeError):
            location = None
        # str to json js_content
        js_content = json.loads(js_content)
        try:
            top_ad = js_content['ad']['ad']['promotion']['top_ad']
            lon = js_content['ad']['ad']['map']['lon']
            lat = js_content['ad']['ad']['map']['lat']
            refresh_time = js_content['ad']['ad']['lastRefreshTime']
        except (KeyError, TypeError):
            top_ad = None
            lon = None
            lat = None
            refresh_time = None

        return location, top_ad, lon, lat, refresh_time
