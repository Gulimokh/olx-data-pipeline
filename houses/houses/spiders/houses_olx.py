import scrapy
import json
import js2py

class OLXHousesSpider(scrapy.Spider):
    name = "houses"
    allowed_domains = ["www.olx.uz"]
    start_urls =  [
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=created_at:desc',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=filter_float_price:asc',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=filter_float_price:desc',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Border%5D=relevance:desc',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Border%5D=relevance:desc',




        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_enum_private_house_type%5D%5B0%5D=2&search%5Bfilter_enum_private_house_type%5D%5B1%5D=3&search%5Bfilter_enum_private_house_type%5D%5B2%5D=5&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_enum_private_house_type%5D%5B0%5D=6&search%5Bfilter_enum_private_house_type%5D%5B1%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:to%5D=150&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_enum_private_house_type%5D%5B0%5D=6&search%5Bfilter_enum_private_house_type%5D%5B1%5D=5&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_enum_private_house_type%5D%5B0%5D=4&search%5Bfilter_enum_private_house_type%5D%5B1%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_enum_private_house_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_enum_private_house_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_float_total_area:to%5D=125&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_float_total_area:from%5D=150&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:to%5D=80&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=90&search%5Bfilter_float_total_area:to%5D=150&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes&search%5Bfilter_enum_location%5D%5B0%5D=2&search%5Bfilter_enum_location%5D%5B1%5D=3&search%5Bfilter_enum_location%5D%5B2%5D=4&search%5Bfilter_enum_location%5D%5B3%5D=5&search%5Bfilter_enum_location%5D%5B4%5D=6&search%5Bfilter_enum_location%5D%5B5%5D=7&search%5Bfilter_enum_location%5D%5B6%5D=8',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_float_total_floors:to%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes&search%5Bfilter_enum_location%5D%5B0%5D=2&search%5Bfilter_enum_location%5D%5B1%5D=3&search%5Bfilter_enum_location%5D%5B2%5D=4&search%5Bfilter_enum_location%5D%5B3%5D=5&search%5Bfilter_enum_location%5D%5B4%5D=7&search%5Bfilter_enum_location%5D%5B5%5D=8&search%5Bfilter_enum_location%5D%5B6%5D=6',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_float_total_floors:to%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_float_total_floors:to%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=3&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=yes',


        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_private_house_type%5D%5B0%5D=6&search%5Bfilter_enum_private_house_type%5D%5B1%5D=5&search%5Bfilter_enum_private_house_type%5D%5B2%5D=4&search%5Bfilter_enum_private_house_type%5D%5B3%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_private_house_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:to%5D=150&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=yes&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_private_house_type%5D%5B0%5D=6&search%5Bfilter_enum_private_house_type%5D%5B1%5D=2&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_enum_private_house_type%5D%5B0%5D=5&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_enum_private_house_type%5D%5B0%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_enum_private_house_type%5D%5B0%5D=4&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_enum_private_house_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_enum_private_house_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:to%5D=150&search%5Bfilter_enum_private_house_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=3&search%5Bfilter_enum_private_house_type%5D%5B0%5D=3&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=2&search%5Bfilter_float_number_of_rooms:to%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_total_area:to%5D=90&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=3&search%5Bfilter_float_number_of_rooms:to%5D=3&search%5Bfilter_float_total_area:from%5D=100&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',


        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_float_total_area:to%5D=90&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_float_total_area:from%5D=100&search%5Bfilter_float_total_area:to%5D=150&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=4&search%5Bfilter_float_number_of_rooms:to%5D=4&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:to%5D=20&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=8&search%5Bfilter_enum_location%5D%5B1%5D=7&search%5Bfilter_enum_location%5D%5B2%5D=6&search%5Bfilter_enum_location%5D%5B3%5D=5&search%5Bfilter_enum_location%5D%5B4%5D=4&search%5Bfilter_enum_location%5D%5B5%5D=3&search%5Bfilter_enum_location%5D%5B6%5D=2',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:to%5D=20&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:to%5D=20&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=25&search%5Bfilter_float_total_area:to%5D=150&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=8&search%5Bfilter_enum_location%5D%5B1%5D=6&search%5Bfilter_enum_location%5D%5B2%5D=7&search%5Bfilter_enum_location%5D%5B3%5D=5&search%5Bfilter_enum_location%5D%5B4%5D=4&search%5Bfilter_enum_location%5D%5B5%5D=3',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=2',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:to%5D=1&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_float_total_floors:to%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=8&search%5Bfilter_enum_location%5D%5B1%5D=7&search%5Bfilter_enum_location%5D%5B2%5D=6&search%5Bfilter_enum_location%5D%5B3%5D=5&search%5Bfilter_enum_location%5D%5B4%5D=4&search%5Bfilter_enum_location%5D%5B5%5D=3&search%5Bfilter_enum_location%5D%5B6%5D=2',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_float_total_floors:to%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=2&search%5Bfilter_float_total_floors:to%5D=2&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=3&search%5Bfilter_float_total_floors:to%5D=3&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=7&search%5Bfilter_enum_location%5D%5B1%5D=8&search%5Bfilter_enum_location%5D%5B2%5D=5&search%5Bfilter_enum_location%5D%5B3%5D=6&search%5Bfilter_enum_location%5D%5B4%5D=4&search%5Bfilter_enum_location%5D%5B5%5D=3&search%5Bfilter_enum_location%5D%5B6%5D=2',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=business&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=3&search%5Bfilter_float_total_floors:to%5D=3&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Bprivate_business%5D=private&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=3&search%5Bfilter_float_total_floors:to%5D=3&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no&search%5Bfilter_enum_location%5D%5B0%5D=1',
        'https://www.olx.uz/nedvizhimost/doma/prodazha/?currency=UZS&search%5Border%5D=relevance:desc&search%5Bfilter_float_number_of_rooms:from%5D=5&search%5Bfilter_float_total_area:from%5D=175&search%5Bfilter_float_total_floors:from%5D=4&search%5Bfilter_enum_private_house_type%5D%5B0%5D=1&search%5Bfilter_enum_comission%5D%5B0%5D=no&search%5Bfilter_enum_furnished_house%5D%5B0%5D=no'

    ]

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "DOWNLOAD_TIMEOUT": 60,
        "COOKIES_ENABLED": True,
        "ROBOTSTXT_OBEY": True,
        "RETRY_TIMES": 2,
        "FEEDS": {
            "/Users/gulimoh/collateral-assessment/houses/houses/data/houses.json": {
                "format": "json",
                "overwrite": True}
        }
    }

    def parse(self, response):
        # Извлекаем ссылки на детальные страницы объявлений
        for house in response.css('div[data-cy="l-card"]'):
            detail_page = house.css('div[data-cy="ad-card-title"]>a::attr(href)').get()
            if detail_page:
                yield response.follow(detail_page, self.parse_detail)

        # Переход на следующую страницу
        next_page = response.css('a[data-cy="pagination-forward"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_detail(self, response):
        js_content = self.extract_js_content(response)
        params_arr = js_content['ad']['ad']['params']
        params = {item['key']: item['value'] for item in params_arr}

        category_id = js_content['ad']['ad']['category']['id']
        category = js_content['categories']['list'][str(category_id)]['name']

        # Формирование извлекаемых данных
        house_data = {
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

            # **Параметры дома из JSON**
            "number_of_rooms": params.get("number_of_rooms"),
            "total_area": params.get("total_area"),
            "total_living_area": params.get("total_living_area"),
            "floor": params.get("floor"),
            "total_floors": params.get("total_floors"),
            "house_type": params.get("house_type"),
            "layout": params.get("layout"),
            "year_of_construction_sale": params.get("year_of_construction_sale"),
            "wc": params.get("wc") or params.get("wc_house"),
            "furnished": params.get("furnished") or params.get("furnished_house"),
            "ceiling_height": params.get("ceiling_height"),
            "repairs": params.get("repairs") or params.get("house_repairs"),
            "comission": params.get("comission"),
            "water": params.get("water"),
            "heating": params.get("heating"),
            "gas": params.get("gas"),
            "electricity": params.get("electricity"),
            "plot": params.get("plot"),
            "location": params.get("location"),
            "more_house": params.get("more_house"),
            "near_is": params.get("near_is"),
        }

        self.logger.info(f"✅ [SUCCESS] Спарсено объявление: {house_data['title']}")
        yield house_data

    def extract_js_content(self, response):
        """Извлечение JavaScript-контента с OLX."""
        script_content = response.xpath('//script[@id="olx-init-config"]/text()').get()
        if not script_content:
            self.logger.error("Ошибка: тег script с id 'olx-init-config' не найден")
            return None

        js = script_content + " window.__PRERENDERED_STATE__;"

        try:
            js_context = js2py.eval_js(js)
        except js2py.base.PyJsException:
            js_context = ""
            self.logger.error("Ошибка: Не удалось выполнить JavaScript")

        js_content = json.loads(js_context)
        return js_content