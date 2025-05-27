import scrapy
import json
from commercial_premises.items import CommercialPremisesItem
import js2py
import scrapy
import json

class CommercialPremisesOlxSpider(scrapy.Spider):
    name = "commercial_premises_olx"
    allowed_domains = ["www.olx.uz"]
    start_urls = [
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=18',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Border%5D=created_at:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=16&search%5Border%5D=created_at%3Adesc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Border%5D=filter_float_price:asc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=18&search%5Border%5D=filter_float_price%3Aasc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Border%5D=filter_float_price:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=19&search%5Border%5D=filter_float_price%3Adesc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Border%5D=filter_float_price:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Border%5D=filter_float_price:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Border%5D=relevance:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&page=19&search%5Border%5D=relevance%3Adesc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Bprivate_business%5D=business&search%5Border%5D=relevance:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Bprivate_business%5D=private&search%5Border%5D=relevance:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Border%5D=created_at:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&page=20&search%5Border%5D=created_at%3Adesc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Bprivate_business%5D=business&search%5Border%5D=created_at:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Bprivate_business%5D=private&search%5Border%5D=created_at:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Bprivate_business%5D=private&search%5Border%5D=filter_float_price:asc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Bprivate_business%5D=business&search%5Border%5D=filter_float_price:asc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Border%5D=filter_float_price:asc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Border%5D=filter_float_price:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Bprivate_business%5D=business&search%5Border%5D=filter_float_price:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Bprivate_business%5D=private&search%5Border%5D=filter_float_price:desc',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UYE&search%5Border%5D=relevance:desc',







        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=1&search%5Bfilter_enum_premise_type%5D%5B1%5D=2&search%5Bfilter_enum_premise_type%5D%5B2%5D=3&search%5Bfilter_enum_premise_type%5D%5B3%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=5&search%5Bfilter_enum_premise_type%5D%5B1%5D=7&search%5Bfilter_enum_premise_type%5D%5B2%5D=6&search%5Bfilter_enum_premise_type%5D%5B3%5D=8&search%5Bfilter_enum_premise_type%5D%5B4%5D=9&search%5Bfilter_enum_premise_type%5D%5B5%5D=10&search%5Bfilter_enum_comission%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=12&search%5Bfilter_enum_premise_type%5D%5B1%5D=11&search%5Bfilter_enum_comission%5D%5B0%5D=yes',


        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:to%5D=60',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=70&search%5Bfilter_float_total_area:to%5D=90',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=100&search%5Bfilter_float_total_area:to%5D=150',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_premise_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=15&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_premise_type%5D%5B0%5D=1&search%5Bfilter_float_total_area%3Afrom%5D=175&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:to%5D=70',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=80&search%5Bfilter_float_total_area:to%5D=100',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=125&search%5Bfilter_float_total_area:to%5D=150',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_premise_type%5D%5B0%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=19&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_premise_type%5D%5B0%5D=2&search%5Bfilter_float_total_area%3Afrom%5D=175&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_premise_type%5D%5B0%5D=2&search%5Bfilter_float_total_area%3Afrom%5D=175&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:to%5D=90',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=100&search%5Bfilter_float_total_area:to%5D=150',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=24&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_premise_type%5D%5B0%5D=3&search%5Bfilter_float_total_area%3Afrom%5D=175&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_premise_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_premise_type%5D%5B0%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:to%5D=70',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=80&search%5Bfilter_float_total_area:to%5D=100',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=125&search%5Bfilter_float_total_area:to%5D=150',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',



        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=14&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_premise_type%5D%5B0%5D=4&search%5Bfilter_float_total_area%3Afrom%5D=175&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_premise_type%5D%5B0%5D=5&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=5&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:to%5D=150',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=5&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=25&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_premise_type%5D%5B0%5D=5&search%5Bfilter_float_total_area%3Afrom%5D=175&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_premise_type%5D%5B0%5D=6&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=6&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:to%5D=150',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=6&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=23&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_premise_type%5D%5B0%5D=6&search%5Bfilter_float_total_area%3Afrom%5D=175&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=7&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=8&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:to%5D=150',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_premise_type%5D%5B0%5D=8&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=8&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_premise_type%5D%5B0%5D=9&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=9&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:to%5D=150',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=9&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_premise_type%5D%5B0%5D=10&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_premise_type%5D%5B0%5D=11&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=11&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:to%5D=150',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=11&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=175',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_premise_type%5D%5B0%5D=12&search%5Bfilter_enum_comission%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=12&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:to%5D=90',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_premise_type%5D%5B0%5D=12&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_float_total_area:from%5D=100&search%5Bfilter_float_total_area:to%5D=150',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&page=16&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_premise_type%5D%5B0%5D=12&search%5Bfilter_float_total_area%3Afrom%5D=175&search%5Bprivate_business%5D=business',
        'https://www.olx.uz/nedvizhimost/kommercheskie-pomeshcheniya/prodazha/?currency=UZS&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_premise_type%5D%5B0%5D=12&search%5Bfilter_float_total_area%3Afrom%5D=175&search%5Bprivate_business%5D=business',


    ]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "DOWNLOAD_TIMEOUT": 60,
        "COOKIES_ENABLED": True,
        "ROBOTSTXT_OBEY": True,
        "RETRY_TIMES": 2,
        "FEEDS": {
            "/Users/gulimoh/collateral-assessment/commercial_premises/commercial_premises/data/commercial_premises_olx.json": {
                "format": "json",
                "overwrite": True}
        }
    }

    def parse(self, response):
        # Извлекаем ссылки на детальные страницы
        for apartment in response.css('div[data-cy="l-card"]'):
            detail_page = apartment.css('div[data-cy="ad-card-title"]>a::attr(href)').get()
            if detail_page:
                yield response.follow(detail_page, self.parse_detail)

        # Переход на следующую страницу, если есть
        next_page = response.css('a[data-cy="pagination-forward"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_detail(self, response):
        js_content = self.extract_js_content(response)

        params_arr = js_content['ad']['ad']['params']
        params = {item['key']: item['value'] for item in params_arr}

        categoryId = js_content['ad']['ad']['category']['id']
        category = js_content['categories']['list'][str(categoryId)]['name']
        # print(type(js_content), js_content)

        item_values = {
            'title': js_content['ad']['ad']['title'],
            'description': js_content['ad']['ad']['description'],
            'content_id':js_content['ad']['ad']['id'],
            'category': category,
            'url': response.url,
            'isBusiness': js_content['ad']['ad']['isBusiness'],
            'isHighlighted': js_content['ad']['ad']['isHighlighted'],
            'isPromoted': js_content['ad']['ad']['isPromoted'],
            'promotion': json.dumps(js_content['ad']['ad']['promotion']),  #json
            'delivery': json.dumps(js_content['ad']['ad']['delivery']),
            'createdTime': js_content['ad']['ad']['createdTime'],
            'lastRefreshTime': js_content['ad']['ad']['lastRefreshTime'],
            'pushupTime': js_content['ad']['ad'].get('pushupTime', None),
            'validToTime': js_content['ad']['ad']['validToTime'],
            'isActive': js_content['ad']['ad']['isActive'],
            'status': js_content['ad']['ad']['status'],
            'price': js_content['ad']['ad']['price']['regularPrice']['value'],
            'currency': js_content['ad']['ad']['price']['regularPrice']['currencyCode'],
            'negotiable': js_content['ad']['ad']['price']['regularPrice']['negotiable'],
            'cityName': js_content['ad']['ad']['location']['cityName'],
            'regionName': js_content['ad']['ad']['location']['regionName'],
            'districtName': js_content['ad']['ad']['location']['districtName'],
            'user': json.dumps(js_content['ad']['ad']['user']), #json

            # Параметры коммерческой недвижимости
            "premise_type": params.get("premise_type"),
            "total_area": params.get("total_area"),
            "effective_area": params.get("effective_area"),
            "land": params.get("land"),
            "floor": params.get("floor"),
            "total_floors": params.get("total_floors"),
            "ceiling_height": params.get("ceiling_height"),
            "repairs": params.get("repairs"),
            "more_premises": params.get("more_premises"),
            "parking_lot": params.get("parking_lot"),
            "comission": params.get("comission"),
            # 'test':js_content,
        }
        for key, value in params.items():
            if key not in item_values:
                item_values[key] = value

        self.logger.info(f"✅ [SUCCESS] Спарсено объявление: {item_values['title']}")
        yield item_values

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