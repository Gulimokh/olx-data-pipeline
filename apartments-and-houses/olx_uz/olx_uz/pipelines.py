# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
# import cx_Oracle
import json
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import psycopg2.extras
import logging


class OlxUzPipeline:
    def process_item(self, item, spider):
        return item


class ApartmentPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        price = item.get('price', '')
        if price:
            numeric_value = re.findall(r'\d+[\s\d]*', price)
            if numeric_value:
                numeric_value = int(''.join(numeric_value[0].split()))
                item['price'] = numeric_value

            if 'у.е.' in price:
                item['currency'] = 'USD'
            elif 'сум' in price:
                item['currency'] = 'SUM'
            else:
                item['currency'] = 'Unknown'

        bathroom = item.get('bathroom', '')
        if bathroom:
            item['bathroom'] = bathroom.replace('Санузел: ', '')

        furnished = item.get('furnished', '')
        if furnished:
            item['furnished'] = furnished.replace('Меблирована: ', '')
            if item['furnished'] == 'Да':
                item['furnished'] = 1
            else:
                item['furnished'] = 0

        ceiling_height = item.get('ceiling_height', '')
        if ceiling_height:
            ceiling_height = ceiling_height.replace('Высота потолков: ', '').replace(" ", "")
            if len(ceiling_height) > 1 and ceiling_height[1] != '.':
                ceiling_height = ceiling_height[0] + '.' + ceiling_height[1:]
            item['ceiling_height'] = float(ceiling_height)

        features = item.get('features', '')
        if features:
            item['features'] = features.replace('В квартире есть: ', '')

        nearby = item.get('nearby', '')
        if nearby:
            item['nearby'] = nearby.replace('Рядом есть: ', '')

        renovation = item.get('renovation', '')
        if renovation:
            item['renovation'] = renovation.replace('Ремонт: ', '')

        commission = item.get('commission', '')
        if commission:
            item['commission'] = commission.replace('Комиссионные: ', '')
            if item['commission'] == 'Да':
                item['commission'] = 1
            else:
                item['commission'] = 0

        layout = item.get('layout', '')
        if layout:
            item['layout'] = layout.replace('Планировка: ', '')

        year_built = item.get('year_built', '')
        if year_built:
            item['year_built'] = year_built.replace('Год постройки/сдачи: ', '')

        total_floors = item.get('total_floors', '')
        if total_floors:
            item['total_floors'] = int(total_floors.replace('Этажность дома: ', ''))

        floor = item.get('floor', '')
        if floor:
            item['floor'] = floor.replace('Этаж: ', '')

        total_area = item.get('total_area', '')
        if total_area:
            item['total_area'] = float(total_area.replace('Общая площадь: ', ''))

        living_area = item.get('living_area', '')
        if living_area:
            living_area = float(living_area.replace('Жилая площадь: ', '').replace('м²', '').replace(" ", ""))
            item['living_area'] = living_area

        kitchen_area = item.get('kitchen_area', '')
        if kitchen_area:
            kitchen_area = float(kitchen_area.replace('Площадь кухни: ', '').replace('м²', '').replace(" ", ""))
            item['kitchen_area'] = kitchen_area

        rooms = item.get('rooms', '')
        if rooms:
            item['rooms'] = int(rooms.replace('Количество комнат: ', ''))

        type_of_market = item.get('type_of_market', '')
        if type_of_market:
            item['type_of_market'] = type_of_market.replace('Тип жилья: ', '')

        house_type = item.get('house_type', '')
        if house_type:
            item['house_type'] = house_type.replace('Тип строения: ', '')

        description = item.get('description', '')
        if description:
            description = description.replace('<br />', '')
            item['description'] = description

        return item


class PostgresqlPipeline:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='127.0.0.1',
            database='postgres',
            user='gulimoh',
            password='postgres',
            port='5432'
        )
        self.cur = self.conn.cursor()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def close_spider(self, spider):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        try:
            # Prepare the query and values
            query = """
                INSERT INTO olx_apartments (
                    content_id, title, price, currency, url, is_business, type_of_market, rooms, total_area, living_area, kitchen_area, floor, total_floors, house_type, layout, year_built, bathroom, furnished, ceiling_height, nearby, features, renovation, commission, description, created_time, updated_time, city_id, city_name, city_normalized_name, district_id, district_name, region_id, region_name, region_normalized_name, longitude, latitude, negotiable
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
                ON CONFLICT (content_id) DO NOTHING
            """
            values = (
                item.get('content_id'),
                item.get('title'),
                item.get('price'),
                item.get('currency'),
                item.get('url'),
                item.get('is_business'),
                item.get('type_of_market'),
                item.get('rooms'),
                item.get('total_area'),
                item.get('living_area'),
                item.get('kitchen_area'),
                int(item.get('floor').strip()) if item.get('floor') else None,
                item.get('total_floors'),
                item.get('house_type'),
                item.get('layout'),
                item.get('year_built'),
                item.get('bathroom'),
                bool(item.get('furnished')) if item.get('furnished') is not None else None,
                item.get('ceiling_height'),
                item.get('nearby'),
                item.get('features'),
                item.get('renovation'),
                item.get('commission'),
                item.get('description'),
                item.get('created_time'),
                item.get('updated_time'),
                item.get('city_id'),
                item.get('city_name'),
                item.get('city_normalized_name'),
                item.get('district_id'),
                item.get('district_name'),
                item.get('region_id'),
                item.get('region_name'),
                item.get('region_normalized_name'),
                item.get('longitude'),
                item.get('latitude'),
                item.get('negotiable')
            )

            # Execute the query
            self.cur.execute(query, values)
            self.conn.commit()
        except psycopg2.IntegrityError as e:
            self.conn.rollback()
            self.logger.warning(
                f"Duplicate entry found for content_id {item.get('content_id')}: {e.pgcode} - {e.pgerror}")
        except psycopg2.Error as e:
            self.conn.rollback()
            self.logger.error(f"Error processing item: {e.pgcode} - {e.pgerror}, Item: {item}")
        except Exception as e:
            self.conn.rollback()
            self.logger.error(f"Error processing item: {e}, Item: {item}")
        return item
