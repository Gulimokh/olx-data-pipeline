
import scrapy
import js2py
import json

class CarsSpiders(scrapy.Spider):
    name ='carsspider'
    allowed_domains = ["olx.uz"]

    start_urls = ['https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_model%5D%5B0%5D=arcadia&search%5Bfilter_enum_model%5D%5B1%5D=damas&search%5Bfilter_enum_model%5D%5B2%5D=espero', 
                  'https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_model%5D%5B0%5D=evanda&search%5Bfilter_enum_model%5D%5B1%5D=kalos&search%5Bfilter_enum_model%5D%5B2%5D=korando&search%5Bfilter_enum_model%5D%5B3%5D=lacetti&search%5Bfilter_enum_model%5D%5B4%5D=lanos&search%5Bfilter_enum_model%5D%5B5%5D=leganza', 
                  'https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_owners%5D%5B0%5D=1&search%5Bfilter_enum_model%5D%5B0%5D=matiz', 
                  'https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_owners%5D%5B0%5D=2&search%5Bfilter_enum_owners%5D%5B1%5D=3&search%5Bfilter_enum_owners%5D%5B2%5D=4&search%5Bfilter_enum_model%5D%5B0%5D=matiz', 
                  'https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_condition%5D%5B0%5D=perfect&search%5Bfilter_enum_model%5D%5B0%5D=nexia', 
                  'https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_condition%5D%5B0%5D=good&search%5Bfilter_enum_owners%5D%5B0%5D=1&search%5Bfilter_enum_model%5D%5B0%5D=nexia', 
                  'https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_condition%5D%5B0%5D=good&search%5Bfilter_enum_owners%5D%5B0%5D=2&search%5Bfilter_enum_owners%5D%5B1%5D=3&search%5Bfilter_enum_owners%5D%5B2%5D=4&search%5Bfilter_enum_model%5D%5B0%5D=nexia', 
                  'https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_condition%5D%5B0%5D=mediocre&search%5Bfilter_enum_condition%5D%5B1%5D=needs_repairs&search%5Bfilter_enum_model%5D%5B0%5D=nexia',
                  'https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_model%5D%5B0%5D=magnus&search%5Bfilter_enum_model%5D%5B1%5D=musso&search%5Bfilter_enum_model%5D%5B2%5D=nubira&search%5Bfilter_enum_model%5D%5B3%5D=prince&search%5Bfilter_enum_model%5D%5B4%5D=racer&search%5Bfilter_enum_model%5D%5B5%5D=sens',
                  'https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_model%5D%5B0%5D=tico',
                  'https://www.olx.uz/transport/legkovye-avtomobili/daewoo/?currency=UYE&search%5Bfilter_enum_model%5D%5B0%5D=winstorm&search%5Bfilter_enum_model%5D%5B1%5D=charman&search%5Bfilter_enum_model%5D%5B2%5D=g2x&search%5Bfilter_enum_model%5D%5B3%5D=gentra&search%5Bfilter_enum_model%5D%5B4%5D=le-mans&search%5Bfilter_enum_model%5D%5B5%5D=rezzo&search%5Bfilter_enum_model%5D%5B6%5D=tacuma&search%5Bfilter_enum_model%5D%5B7%5D=tosca&search%5Bfilter_enum_model%5D%5B8%5D=condor',












                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_fuel_type%5D%5B0%5D=547&search%5Bfilter_enum_fuel_type%5D%5B1%5D=543&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=cabriolet&search%5Bfilter_enum_car_body%5D%5B1%5D=pickup&search%5Bfilter_enum_car_body%5D%5B2%5D=coupe&search%5Bfilter_enum_car_body%5D%5B3%5D=estate-car&search%5Bfilter_enum_car_body%5D%5B4%5D=hatchback&search%5Bfilter_enum_car_body%5D%5B5%5D=minibus&search%5Bfilter_enum_fuel_type%5D%5B0%5D=546&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=off-road-vehicle&search%5Bfilter_enum_fuel_type%5D%5B0%5D=546&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=other&search%5Bfilter_enum_fuel_type%5D%5B0%5D=546&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_fuel_type%5D%5B0%5D=546&search%5Bfilter_enum_condition%5D%5B0%5D=perfect&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_fuel_type%5D%5B0%5D=546&search%5Bfilter_enum_condition%5D%5B0%5D=good&search%5Bfilter_enum_condition%5D%5B1%5D=mediocre&search%5Bfilter_enum_condition%5D%5B2%5D=needs_repairs&search%5Bfilter_enum_condition%5D%5B3%5D=new&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=cabriolet&search%5Bfilter_enum_car_body%5D%5B1%5D=coupe&search%5Bfilter_enum_car_body%5D%5B2%5D=pickup&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=minibus&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=off-road-vehicle&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=estate-car&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=estate-car&search%5Bfilter_enum_color%5D%5B0%5D=2&search%5Bfilter_enum_color%5D%5B1%5D=7&search%5Bfilter_enum_color%5D%5B2%5D=8&search%5Bfilter_enum_color%5D%5B3%5D=23&search%5Bfilter_enum_color%5D%5B4%5D=9&search%5Bfilter_enum_color%5D%5B5%5D=14&search%5Bfilter_enum_color%5D%5B6%5D=17&search%5Bfilter_enum_color%5D%5B7%5D=18&search%5Bfilter_enum_color%5D%5B8%5D=10&search%5Bfilter_enum_color%5D%5B9%5D=11&search%5Bfilter_enum_color%5D%5B10%5D=15&search%5Bfilter_enum_color%5D%5B11%5D=22&search%5Bfilter_enum_color%5D%5B12%5D=21&search%5Bfilter_enum_color%5D%5B13%5D=12&search%5Bfilter_enum_color%5D%5B14%5D=13&search%5Bfilter_enum_color%5D%5B15%5D=3&search%5Bfilter_enum_color%5D%5B16%5D=4&search%5Bfilter_enum_color%5D%5B17%5D=5&search%5Bfilter_enum_color%5D%5B18%5D=6&search%5Bfilter_enum_color%5D%5B19%5D=19&search%5Bfilter_enum_color%5D%5B20%5D=20&search%5Bfilter_enum_color%5D%5B21%5D=25&search%5Bfilter_enum_color%5D%5B22%5D=24&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=hatchback&search%5Bfilter_float_motor_mileage:to%5D=225000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=hatchback&search%5Bfilter_float_motor_mileage:from%5D=250000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=hatchback&search%5Bfilter_enum_color%5D%5B0%5D=2&search%5Bfilter_enum_color%5D%5B1%5D=3&search%5Bfilter_enum_color%5D%5B2%5D=4&search%5Bfilter_enum_color%5D%5B3%5D=5&search%5Bfilter_enum_color%5D%5B4%5D=6&search%5Bfilter_enum_color%5D%5B5%5D=7&search%5Bfilter_enum_color%5D%5B6%5D=8&search%5Bfilter_enum_color%5D%5B7%5D=9&search%5Bfilter_enum_color%5D%5B8%5D=10&search%5Bfilter_enum_color%5D%5B9%5D=11&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=hatchback&search%5Bfilter_enum_color%5D%5B0%5D=12&search%5Bfilter_enum_color%5D%5B1%5D=13&search%5Bfilter_enum_color%5D%5B2%5D=14&search%5Bfilter_enum_color%5D%5B3%5D=15&search%5Bfilter_enum_color%5D%5B4%5D=17&search%5Bfilter_enum_color%5D%5B5%5D=18&search%5Bfilter_enum_color%5D%5B6%5D=19&search%5Bfilter_enum_color%5D%5B7%5D=20&search%5Bfilter_enum_color%5D%5B8%5D=21&search%5Bfilter_enum_color%5D%5B9%5D=22&search%5Bfilter_enum_color%5D%5B10%5D=23&search%5Bfilter_enum_color%5D%5B11%5D=24&search%5Bfilter_enum_color%5D%5B12%5D=25&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',



                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:to%5D=30000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:from%5D=50000&search%5Bfilter_float_motor_mileage:to%5D=100000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:from%5D=125000&search%5Bfilter_float_motor_mileage:to%5D=200000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:from%5D=225000&search%5Bfilter_float_motor_mileage:to%5D=300000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:from%5D=300000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',


                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_color%5D%5B0%5D=2&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_color%5D%5B0%5D=3&search%5Bfilter_enum_color%5D%5B1%5D=4&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_color%5D%5B0%5D=5&search%5Bfilter_enum_color%5D%5B1%5D=6&search%5Bfilter_enum_color%5D%5B2%5D=7&search%5Bfilter_enum_color%5D%5B3%5D=8&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_color%5D%5B0%5D=9&search%5Bfilter_enum_color%5D%5B1%5D=12&search%5Bfilter_enum_color%5D%5B2%5D=10&search%5Bfilter_enum_color%5D%5B3%5D=11&search%5Bfilter_enum_color%5D%5B4%5D=13&search%5Bfilter_enum_color%5D%5B5%5D=14&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_color%5D%5B0%5D=15&search%5Bfilter_enum_color%5D%5B1%5D=17&search%5Bfilter_enum_color%5D%5B2%5D=19&search%5Bfilter_enum_color%5D%5B3%5D=18&search%5Bfilter_enum_color%5D%5B4%5D=20&search%5Bfilter_enum_color%5D%5B5%5D=21&search%5Bfilter_enum_color%5D%5B6%5D=24&search%5Bfilter_enum_color%5D%5B7%5D=22&search%5Bfilter_enum_color%5D%5B8%5D=23&search%5Bfilter_enum_color%5D%5B9%5D=25&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=other&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=other&search%5Bfilter_enum_color%5D%5B0%5D=2&search%5Bfilter_enum_color%5D%5B1%5D=12&search%5Bfilter_enum_color%5D%5B2%5D=13&search%5Bfilter_enum_color%5D%5B3%5D=14&search%5Bfilter_enum_color%5D%5B4%5D=15&search%5Bfilter_enum_color%5D%5B5%5D=3&search%5Bfilter_enum_color%5D%5B6%5D=4&search%5Bfilter_enum_color%5D%5B7%5D=5&search%5Bfilter_enum_color%5D%5B8%5D=6&search%5Bfilter_enum_color%5D%5B9%5D=7&search%5Bfilter_enum_color%5D%5B10%5D=18&search%5Bfilter_enum_color%5D%5B11%5D=8&search%5Bfilter_enum_color%5D%5B12%5D=9&search%5Bfilter_enum_color%5D%5B13%5D=10&search%5Bfilter_enum_color%5D%5B14%5D=11&search%5Bfilter_enum_color%5D%5B15%5D=17&search%5Bfilter_enum_color%5D%5B16%5D=19&search%5Bfilter_enum_color%5D%5B17%5D=20&search%5Bfilter_enum_color%5D%5B18%5D=21&search%5Bfilter_enum_color%5D%5B19%5D=22&search%5Bfilter_enum_color%5D%5B20%5D=23&search%5Bfilter_enum_color%5D%5B21%5D=25&search%5Bfilter_enum_color%5D%5B22%5D=24&search%5Bfilter_enum_fuel_type%5D%5B0%5D=545&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=cabriolet&search%5Bfilter_enum_car_body%5D%5B1%5D=pickup&search%5Bfilter_enum_car_body%5D%5B2%5D=estate-car&search%5Bfilter_enum_car_body%5D%5B3%5D=coupe&search%5Bfilter_enum_car_body%5D%5B4%5D=hatchback&search%5Bfilter_enum_car_body%5D%5B5%5D=minibus&search%5Bfilter_enum_car_body%5D%5B6%5D=sedan&search%5Bfilter_enum_fuel_type%5D%5B0%5D=544&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=off-road-vehicle&search%5Bfilter_enum_fuel_type%5D%5B0%5D=544&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=other&search%5Bfilter_enum_fuel_type%5D%5B0%5D=544&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',



                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=cabriolet&search%5Bfilter_enum_car_body%5D%5B1%5D=pickup&search%5Bfilter_enum_car_body%5D%5B2%5D=coupe&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=estate-car&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=minibus&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=hatchback&search%5Bfilter_float_motor_mileage:to%5D=125000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=hatchback&search%5Bfilter_float_motor_mileage:from%5D=125000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=hatchback&search%5Bfilter_enum_color%5D%5B0%5D=2&search%5Bfilter_enum_color%5D%5B1%5D=3&search%5Bfilter_enum_color%5D%5B2%5D=4&search%5Bfilter_enum_color%5D%5B3%5D=5&search%5Bfilter_enum_color%5D%5B4%5D=6&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=hatchback&search%5Bfilter_enum_color%5D%5B0%5D=7&search%5Bfilter_enum_color%5D%5B1%5D=14&search%5Bfilter_enum_color%5D%5B2%5D=15&search%5Bfilter_enum_color%5D%5B3%5D=17&search%5Bfilter_enum_color%5D%5B4%5D=23&search%5Bfilter_enum_color%5D%5B5%5D=18&search%5Bfilter_enum_color%5D%5B6%5D=19&search%5Bfilter_enum_color%5D%5B7%5D=20&search%5Bfilter_enum_color%5D%5B8%5D=8&search%5Bfilter_enum_color%5D%5B9%5D=9&search%5Bfilter_enum_color%5D%5B10%5D=10&search%5Bfilter_enum_color%5D%5B11%5D=11&search%5Bfilter_enum_color%5D%5B12%5D=12&search%5Bfilter_enum_color%5D%5B13%5D=13&search%5Bfilter_enum_color%5D%5B14%5D=21&search%5Bfilter_enum_color%5D%5B15%5D=22&search%5Bfilter_enum_color%5D%5B16%5D=24&search%5Bfilter_enum_color%5D%5B17%5D=25&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=off-road-vehicle&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_color%5D%5B1%5D=3&search%5Bfilter_enum_color%5D%5B2%5D=4&search%5Bfilter_enum_color%5D%5B3%5D=5&search%5Bfilter_enum_color%5D%5B4%5D=6&search%5Bfilter_enum_color%5D%5B5%5D=7&search%5Bfilter_enum_color%5D%5B6%5D=8&search%5Bfilter_enum_color%5D%5B7%5D=9&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=off-road-vehicle&search%5Bfilter_enum_color%5D%5B0%5D=2&search%5Bfilter_enum_color%5D%5B1%5D=20&search%5Bfilter_enum_color%5D%5B2%5D=21&search%5Bfilter_enum_color%5D%5B3%5D=22&search%5Bfilter_enum_color%5D%5B4%5D=10&search%5Bfilter_enum_color%5D%5B5%5D=11&search%5Bfilter_enum_color%5D%5B6%5D=12&search%5Bfilter_enum_color%5D%5B7%5D=13&search%5Bfilter_enum_color%5D%5B8%5D=14&search%5Bfilter_enum_color%5D%5B9%5D=15&search%5Bfilter_enum_color%5D%5B10%5D=17&search%5Bfilter_enum_color%5D%5B11%5D=18&search%5Bfilter_enum_color%5D%5B12%5D=19&search%5Bfilter_enum_color%5D%5B13%5D=23&search%5Bfilter_enum_color%5D%5B14%5D=24&search%5Bfilter_enum_color%5D%5B15%5D=25&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:to%5D=10000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',



                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:to%5D=10000&search%5Bfilter_enum_transmission_type%5D%5B0%5D=546&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:to%5D=10000&search%5Bfilter_enum_transmission_type%5D%5B0%5D=547&search%5Bfilter_enum_transmission_type%5D%5B1%5D=545&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=business&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:from%5D=20000&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:from%5D=20000&search%5Bfilter_enum_transmission_type%5D%5B0%5D=546&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bprivate_business%5D=private&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:from%5D=20000&search%5Bfilter_enum_transmission_type%5D%5B0%5D=545&search%5Bfilter_enum_transmission_type%5D%5B1%5D=547&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:to%5D=30000&search%5Bfilter_enum_color%5D%5B0%5D=2&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_float_motor_mileage:from%5D=50000&search%5Bfilter_enum_color%5D%5B0%5D=2&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_color%5D%5B0%5D=3&search%5Bfilter_enum_color%5D%5B1%5D=4&search%5Bfilter_enum_color%5D%5B2%5D=7&search%5Bfilter_enum_color%5D%5B3%5D=8&search%5Bfilter_enum_color%5D%5B4%5D=5&search%5Bfilter_enum_color%5D%5B5%5D=6&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_color%5D%5B0%5D=9&search%5Bfilter_enum_color%5D%5B1%5D=10&search%5Bfilter_enum_color%5D%5B2%5D=11&search%5Bfilter_enum_color%5D%5B3%5D=12&search%5Bfilter_enum_color%5D%5B4%5D=13&search%5Bfilter_enum_color%5D%5B5%5D=14&search%5Bfilter_enum_color%5D%5B6%5D=15&search%5Bfilter_enum_color%5D%5B7%5D=17&search%5Bfilter_enum_color%5D%5B8%5D=18&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=sedan&search%5Bfilter_enum_color%5D%5B0%5D=19&search%5Bfilter_enum_color%5D%5B1%5D=21&search%5Bfilter_enum_color%5D%5B2%5D=20&search%5Bfilter_enum_color%5D%5B3%5D=22&search%5Bfilter_enum_color%5D%5B4%5D=23&search%5Bfilter_enum_color%5D%5B5%5D=24&search%5Bfilter_enum_color%5D%5B6%5D=25&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=other&search%5Bfilter_enum_color%5D%5B0%5D=1&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish',
                  'https://www.olx.uz/transport/legkovye-avtomobili/?currency=UZS&search%5Bfilter_enum_car_body%5D%5B0%5D=other&search%5Bfilter_enum_color%5D%5B0%5D=2&search%5Bfilter_enum_color%5D%5B1%5D=7&search%5Bfilter_enum_color%5D%5B2%5D=8&search%5Bfilter_enum_color%5D%5B3%5D=9&search%5Bfilter_enum_color%5D%5B4%5D=10&search%5Bfilter_enum_color%5D%5B5%5D=11&search%5Bfilter_enum_color%5D%5B6%5D=19&search%5Bfilter_enum_color%5D%5B7%5D=12&search%5Bfilter_enum_color%5D%5B8%5D=13&search%5Bfilter_enum_color%5D%5B9%5D=14&search%5Bfilter_enum_color%5D%5B10%5D=22&search%5Bfilter_enum_color%5D%5B11%5D=15&search%5Bfilter_enum_color%5D%5B12%5D=23&search%5Bfilter_enum_color%5D%5B13%5D=24&search%5Bfilter_enum_color%5D%5B14%5D=17&search%5Bfilter_enum_color%5D%5B15%5D=3&search%5Bfilter_enum_color%5D%5B16%5D=6&search%5Bfilter_enum_color%5D%5B17%5D=4&search%5Bfilter_enum_color%5D%5B18%5D=5&search%5Bfilter_enum_color%5D%5B19%5D=18&search%5Bfilter_enum_color%5D%5B20%5D=20&search%5Bfilter_enum_color%5D%5B21%5D=21&search%5Bfilter_enum_color%5D%5B22%5D=25&search%5Bfilter_enum_fuel_type%5D%5B0%5D=542&search%5Bfilter_enum_terms_of_sale%5D%5B0%5D=oddiy_sotish'
                  ]


    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'DOWNLOAD_TIMEOUT': 60,  # Increase timeout to 30 seconds
        'COOKIES_ENABLED': True,
        'ROBOTSTXT_OBEY': True,
        'RETRY_TIMES': 2,  # Increase the number of retries
    
    }
    
    def parse(self, response):
        for car in response.css('div[data-cy="l-card"]'):
            detail_page = car.css('div[data-cy="ad-card-title"]>a::attr(href)').get()
            if detail_page:
                yield response.follow(detail_page, self.parse_detail)

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
            'price':js_content['ad']['ad']['price']['regularPrice']['value'],
            'currency':js_content['ad']['ad']['price']['regularPrice']['currencyCode'],
            'description':js_content['ad']['ad']['description'],
            'content_id':js_content['ad']['ad']['id'],
            'category':category,
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
            'user':json.dumps(js_content['ad']['ad']['user']), #json
            #'test':js_content,
        }
        itemValues.update(params)

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
        return js_content



# {
#                 'title': response.css('div[data-cy="ad_title"]>h4::text').get(),
#                 'price': response.css('div[data-testid="ad-price-container"]>h3::text').get(),
#                 'description': response.css('div[data-cy="ad_description"]>div::text').getall(),
#                 'content_id': response.css('div[data-cy="ad-footer-bar-section"]>span::text').getall()[1],
#                 'url': response.url,
#                 'test':js_content,
#             }



#
# CREATE TABLE public.cars
# (
#     id integer NOT NULL,
#     title character varying(256),
#     description character varying(8000),
#     content_id integer,
#     price integer,
#     currency character varying(256),
#     category character varying(256),
#     category_type character varying(256),
#     url character varying(8000),
#     "isBusiness" boolean,
#     "isHighlighted" boolean,
#     "isPromoted" boolean,
#     promotion json,
#     delivery json,
#     "createdTime" date,
#     "lastRefreshTime" date,
#     "pushupTime" date,
#     "validToTime" date,
#     "isActive" boolean,
#     status character varying(100),
#     "isJob" boolean,
#     "itemCondition" character varying(256),
#     negotiable boolean,
#     "cityName" character varying(100),
#     "regionName" character varying(256),
#     "districtName" character varying(256),
#     "user" json,
#     model character varying(100),
#     car_body character varying(100),
#     motor_year character varying(100),
#     motor_mileage character varying(256),
#     transmission_type character varying(100),
#     color character varying(100),
#     motor_engine_size character varying(100),
#     fuel_type character varying(100),
#     condition character varying(100),
#     owners character varying(100),
#     car_option character varying(256),
#     PRIMARY KEY (id)
# );

# ALTER TABLE IF EXISTS public.cars
#     OWNER to postgres;




# CREATE TABLE public.cars
# (
#     id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
#     title character varying(256),
#     description character varying(8000),
#     content_id INTEGER NOT NULL,
#     price integer,
#     currency character varying(256),
#     category character varying(256),
#     category_type character varying(256),
#     url character varying(8000),
#     isBusiness boolean,
#     isHighlighted boolean,
#     isPromoted boolean,
#     promotion json,
#     delivery json,
#     createdTime TIMESTAMP NOT NULL,
#     lastRefreshTime TIMESTAMP,
#     pushupTime TIMESTAMP,
#     validToTime TIMESTAMP,
#     isActive boolean,
#     status character varying(100),
#     isJob boolean,
#     itemCondition character varying(256),
#     negotiable boolean,
#     cityName character varying(100),
#     regionName character varying(256),
#     districtName character varying(256),
#     olx_user json,
#     model character varying(100),
#     car_body character varying(100),
#     motor_year character varying(100),
#     motor_mileage character varying(256),
#     transmission_type character varying(100),
#     color character varying(100),
#     motor_engine_size character varying(100),
#     fuel_type character varying(100),
#     car_condition character varying(100),
#     owners character varying(100),
#     car_option character varying(256),
#     PRIMARY KEY (id)
# 	UNIQUE (content_id, createdTime)
# );

# ALTER TABLE IF EXISTS public.cars
#     OWNER to postgres;



# https://www.olx.uz/d/obyavlenie/harasho-mashina-sipartivni-ID3xxQo.html

# CREATE TABLE public.users
# (
#     id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 ),
#     name character varying(255),
#     uuid character varying(255),
#     "sellerType" character varying(255),
#     created timestamp with time zone,
#     company_name character varying(255),
#     logo_ad_page character varying(1000),
#     "bannerDesktopURL" character varying,
#     about character varying(1000),
#     "lastSeen" timestamp with time zone,
#     "isOnline" boolean,
#     "socialNetworkAccountType" character varying(255),
#     "otherAdsEnabled" boolean,
#     logo character varying(1000),
#     photo character varying(1000),
#     olx_id integer,
#     PRIMARY KEY (id)
# );

# ALTER TABLE IF EXISTS public.users
#     OWNER to postgres;


# CREATE TABLE public.cars
# (
#     id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 ),
#     user_id integer,
#     category character varying(255),
#     model character varying(255),
#     PRIMARY KEY (id)
# );

# ALTER TABLE IF EXISTS public.cars
#     OWNER to postgres;



# DROP TABLE IF EXISTS public.users;
# DROP TABLE IF EXISTS public.cars;

# CREATE TABLE public.users (
#     id INT NOT NULL,
#     name VARCHAR(100),
#     email VARCHAR(100),
# 	PRIMARY KEY (id)
# );

# CREATE TABLE public.promotions
# (
#     id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
#     user_id INT,
#     category character varying(255),
#     model character varying(255),
#     PRIMARY KEY (id),
# 	FOREIGN KEY (user_id) REFERENCES users(id)
# );

# ALTER TABLE IF EXISTS public.cars
#     OWNER to postgres;