# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import psycopg2.extras
import logging
import json


class CarsPipeline:
    def process_item(self, item, spider):
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

    def clean_int(self, value):
        """Очищает и конвертирует значение в int"""
        try:
            return int(value.strip()) if isinstance(value, str) and value.strip().isdigit() else int(value)
        except:
            return None

    def clean_json(self, value):
        """Конвертирует словарь в JSON-строку"""
        return json.dumps(value) if isinstance(value, dict) else value

    def clean_bool(self, value):
        """Конвертирует 'Да'/'Нет' и JSON-значения True/False в Boolean"""
        if value in ["Да", "да", "Yes", "yes", True]:
            return True
        elif value in ["Нет", "нет", "No", "no", False]:
            return False
        return False  # Если None, ставим False

    def process_item(self, item, spider):
        try:
            # Prepare the query and values
            query = """
               insert into public.cars(title, description, content_id, price, currency, category, category_type, url, isBusiness, isHighlighted, isPromoted, promotion, delivery, createdTime, lastRefreshTime, pushupTime, validToTime, isActive, status, isJob, itemCondition, negotiable, cityName, regionName, districtName, olx_user, model, car_body, motor_year, motor_mileage, transmission_type, color, motor_engine_size, fuel_type, car_condition, owners, car_option)
               values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               ON CONFLICT (content_id) DO NOTHING
            """
            values = (
                item.get('title'),
                item.get('description'),
                self.clean_int(item.get('content_id')),
                self.clean_int(item.get('price')),
                item.get('currency'),
                item.get('category'),
                item.get('category_type'),
                item.get('url'),
                self.clean_bool(item.get('isBusiness')),
                self.clean_bool(item.get('isHighlighted')),
                self.clean_bool(item.get('isPromoted')),
                self.clean_json(item.get('promotion')),
                self.clean_json(item.get('delivery')),
                item.get('createdTime'),
                item.get('lastRefreshTime'),
                item.get('pushupTime'),
                item.get('validToTime'),
                self.clean_bool(item.get('isActive')),
                item.get('status'),
                item.get('isJob'),
                item.get('itemCondition'),
                self.clean_bool(item.get('negotiable')),
                item.get('cityName'),
                item.get('regionName'),
                item.get('districtName'),
                self.clean_json(item.get('olx_user')),
                item.get('model'),
                item.get('car_body'),
                item.get('motor_year'),
                item.get('motor_mileage'),
                item.get('transmission_type'),
                item.get('color'),
                item.get('motor_engine_size'),
                item.get('fuel_type'),
                item.get('condition'),
                item.get('owners'),
                item.get('car_option'),
            )

            # Execute the query
            self.logger.info(f"VALUES COUNT: {len(values)}")
            self.logger.info(f"PLACEHOLDERS COUNT: {query.count('%s')}")
            self.logger.info(f"Executing SQL with values: {values}")

            self.logger.info(f"Executing SQL with values: {values}")

            self.cur.execute(query, values)
            self.conn.commit()

        except psycopg2.Error as e:
            self.conn.rollback()
            self.logger.error(f"❌ Ошибка базы данных: {e.pgcode} - {e.pgerror}, Item: {item}")
        except Exception as e:
            self.conn.rollback()
            self.logger.error(f"❌ Неожиданная ошибка: {e}, Item: {item}")

        return item

# CREATE TABLE public.cars
# (
#     id integer NOT NULL,
#     title character varying(256),
#     price character varying(100),
#     PRIMARY KEY (id)
# );

# ALTER TABLE IF EXISTS public.cars
#     OWNER to postgres;


# CREATE TABLE public.cars
# (
#     id INT GENERATED ALWAYS AS IDENTITY NOT NULL,
#     title character varying(256),
#     price character varying(100),
#     PRIMARY KEY (id)
# );

# ALTER TABLE IF EXISTS public.cars
#     OWNER to postgres;


