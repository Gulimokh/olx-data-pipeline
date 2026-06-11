import scrapy
import js2py
import json

class HeavyVehiclesSpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_item_count = {}
    name = "specialvehiclesspiders"
    allowed_domains = ["www.olx.uz"]
    start_urls = [
        'https://www.olx.uz/transport/spetstehnika/commercial/?currency=UZS&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/transport/spetstehnika/commercial/?currency=UZS&search%5Bprivate_business%5D=private',
        'https://www.olx.uz/transport/spetstehnika/avtocrane/?currency=UZS&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/transport/spetstehnika/avtocrane/?currency=UZS&search%5Bprivate_business%5D=private',
        'https://www.olx.uz/transport/spetstehnika/loaders/?currency=UZS&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/transport/spetstehnika/loaders/?currency=UZS&search%5Bprivate_business%5D=private',
        'https://www.olx.uz/transport/spetstehnika/excavators/?currency=UZS&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/transport/spetstehnika/excavators/?currency=UZS&search%5Bprivate_business%5D=private',
        'https://www.olx.uz/transport/spetstehnika/concrete_mixer/?currency=UZS&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/transport/spetstehnika/concrete_mixer/?currency=UZS&search%5Bprivate_business%5D=private',
        'https://www.olx.uz/transport/spetstehnika/graders/?currency=UZS&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/transport/spetstehnika/graders/?currency=UZS&search%5Bprivate_business%5D=private',
        'https://www.olx.uz/transport/spetstehnika/hauler/?currency=UZS&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/transport/spetstehnika/hauler/?currency=UZS&search%5Bprivate_business%5D=private',
        'https://www.olx.uz/transport/spetstehnika/vehicle_others/?currency=UZS&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/transport/spetstehnika/vehicle_others/?currency=UZS&search%5Bprivate_business%5D=private',
        'https://www.olx.uz/transport/spetstehnika/commercial/?currency=UZS&search%5Bprivate_business%5D=business',
    
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'DOWNLOAD_TIMEOUT': 60,  # Increase timeout to 30 seconds
        'COOKIES_ENABLED': True,
        'ROBOTSTXT_OBEY': True,
        'RETRY_TIMES': 2,  # Increase the number of retries
        "FEEDS": {
            "olx_uz.json": {"format": "json", "overwrite": True}
        }

    }

    def parse(self, response):
        # Extract links to listing detail pages
        for heavy in response.css('div[data-cy="l-card"]'):
            detail_page = heavy.css('div[data-cy="ad-card-title"]>a::attr(href)').get()
            if detail_page:
                yield response.follow(detail_page, self.parse_detail)

        # Follow to next page if available
        next_page = response.css('a[data-cy="pagination-forward"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        # Track item count per page
        #current_url = response.meta.get('start_url', response.url)
        #self.page_item_count.setdefault(current_url, 0)

        #for specialvehicles in response.css('div[data-cy="l-card"]'):
            #if self.page_item_count[current_url] >= 5:
                #break

        #detail_page = specialvehicles.css('div[data-cy="ad-card-title"]>a::attr(href)').get()
        #if detail_page:
            #self.page_item_count[current_url] += 1
            #yield response.follow(detail_page, self.parse_detail, meta={'start_url': current_url})

    def parse_detail(self, response):

        js_content = self.extract_js_content(response)

        params_arr = js_content['ad']['ad']['params']
        params = {item['key']: item['value'] for item in params_arr}

        #categoryId = js_content['ad']['ad']['category']['id']
        #category = js_content['categories']['list'][str(categoryId)]['name']
        
        # remove if not working
        category_id = js_content['ad']['ad']['category']['id']
        category_data = js_content['categories']['list'].get(str(category_id), {})

        category_name = category_data.get('name')  # Current category name
        parent_id = category_data.get('parentId') or category_data.get('parent_id')

        # Start with None
        main_category = None
        category = None
        parent_data = None

        if parent_id == 273:
            main_category = "Спецтехника"  # OLX category: "Special vehicles / Heavy equipment"
            category = category_name  # store subcategory (e.g. "Loader")
        elif not parent_id:
            main_category = category_name  # fallback
        else:
            parent_data = js_content['categories']['list'].get(str(parent_id))
        if parent_data:
            main_category = parent_data.get('name')



        #print("CATEGORY:", category)
        #print("PARENT ID:", parent_id)
        #print("MAIN CATEGORY:", main_category)

        itemValues = {
            'title':  js_content['ad']['ad']['title'],
            'price': js_content['ad']['ad']['price']['regularPrice']['value'],
            'currency': js_content['ad']['ad']['price']['regularPrice']['currencyCode'],
            'description': js_content['ad']['ad']['description'],
            'content_id': js_content['ad']['ad']['id'],
            'main_category': main_category,
            'category': category,
            'category_type': js_content['ad']['ad']['category']['type'],
            'url': response.url,
            'isBusiness': js_content['ad']['ad']['isBusiness'],
            'isHighlighted': js_content['ad']['ad']['isHighlighted'],
            'isPromoted': js_content['ad']['ad']['isPromoted'],
            'promotion': json.dumps(js_content['ad']['ad']['promotion']),  #json
            'delivery': json.dumps(js_content['ad']['ad']['delivery']),  #json
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