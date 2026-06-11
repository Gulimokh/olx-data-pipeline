import scrapy
import js2py
import json

class ApartmentsOlxSpider(scrapy.Spider):
    name = "apartments_olx"
    allowed_domains = ["www.olx.uz"]
    start_urls = [
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_repairs%5D%5B1%5D=3&search%5Bfilter_enum_repairs%5D%5B2%5D=6&search%5Bfilter_enum_repairs%5D%5B3%5D=4&search%5Bfilter_enum_repairs%5D%5B4%5D=5&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=1&search%5Bfilter_float_floor:to%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=6&search%5Bfilter_float_floor:to%5D=16&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=1&search%5Bfilter_float_floor:to%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=6&search%5Bfilter_float_floor:to%5D=16&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=1&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_float_floor:to%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=1&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_float_floor:from%5D=6&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=3&search%5Bfilter_float_floor:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=5&search%5Bfilter_float_floor:to%5D=6&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=7&search%5Bfilter_float_floor:to%5D=8&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=9&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=3&search%5Bfilter_float_floor:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=5&search%5Bfilter_float_floor:to%5D=6&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=7&search%5Bfilter_float_floor:to%5D=8&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=9&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_float_floor:to%5D=6&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_float_floor:from%5D=7&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_repairs%5D%5B1%5D=3&search%5Bfilter_enum_repairs%5D%5B2%5D=4&search%5Bfilter_enum_repairs%5D%5B3%5D=5&search%5Bfilter_enum_repairs%5D%5B4%5D=6&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=4&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=4&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=5&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=5&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=5&search%5Bfilter_float_floor:to%5D=8&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=5&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=9&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=5&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:to%5D=6&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=5&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=7&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=5&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=5&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=6&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=6&search%5Bfilter_enum_type_of_market%5D%5B0%5D=primary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_repairs%5D%5B1%5D=4&search%5Bfilter_enum_repairs%5D%5B2%5D=5&search%5Bfilter_enum_repairs%5D%5B3%5D=6&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=4&search%5Bfilter_enum_repairs%5D%5B1%5D=5&search%5Bfilter_enum_repairs%5D%5B2%5D=6&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_float_floor:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_float_floor:from%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:to%5D=1&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=2&search%5Bfilter_float_floor:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_total_area:to%5D=50&search%5Bfilter_float_floor:from%5D=3&search%5Bfilter_float_floor:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_total_area:from%5D=55&search%5Bfilter_float_floor:from%5D=3&search%5Bfilter_float_floor:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=4&search%5Bfilter_float_floor:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=3&search%5Bfilter_float_floor:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=4&search%5Bfilter_float_floor:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=3&search%5Bfilter_float_floor:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=4&search%5Bfilter_float_floor:to%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=6&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=3&search%5Bfilter_float_floor:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=yes&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_repairs%5D%5B1%5D=4&search%5Bfilter_enum_repairs%5D%5B2%5D=5&search%5Bfilter_enum_repairs%5D%5B3%5D=6&search%5Bfilter_enum_repairs%5D%5B4%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=1&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=6&search%5Bfilter_enum_repairs%5D%5B1%5D=5&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=2&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_float_floor:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_float_floor:from%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:to%5D=1&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=2&search%5Bfilter_float_floor:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=3&search%5Bfilter_float_floor:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=4&search%5Bfilter_float_floor:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_float_floor:from%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=3&search%5Bfilter_float_floor:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_floor:from%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=3&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=4&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=4&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=4&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary',
        'https://www.olx.uz/nedvizhimost/kvartiry/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_enum_furnished%5D%5B0%5D=no&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_repairs%5D%5B0%5D=4&search%5Bfilter_enum_type_of_market%5D%5B0%5D=secondary'

    ]

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "DOWNLOAD_TIMEOUT": 60,
        "COOKIES_ENABLED": True,
        "ROBOTSTXT_OBEY": True,
        "RETRY_TIMES": 2,
        "FEEDS": {
            "/Users/gulimoh/collateral-assessment/apartments/data/olx_ux.json": {
                "format": "json",
                "overwrite": True
            }
        }
    }

    def parse(self, response):
        # Extract links to listing detail pages
        for apartment in response.css('div[data-cy="l-card"]'):
            detail_page = apartment.css('div[data-cy="ad-card-title"]>a::attr(href)').get()
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

        itemValues = {
            'title':  js_content['ad']['ad']['title'],
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
            'user': json.dumps(js_content['ad']['ad']['user']), #json

            # Apartment parameters
            "number_of_rooms": params.get("number_of_rooms"),
            "floor": params.get("floor"),
            "total_floors": params.get("total_floors"),
            "house_type": params.get("house_type"),
            "layout": params.get("layout"),
            "year_of_construction_sale": params.get("year_of_construction_sale"),
            "wc": params.get("wc"),
            "furnished": params.get("furnished"),
            "ceiling_height": params.get("ceiling_height"),
            "repairs": params.get("repairs"),
            "comission": params.get("comission"),
            "total_area": params.get("total_area"),
            "total_living_area": params.get("total_living_area"),
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