import os

logger = logging.getLogger(__name__)

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import logging
import psycopg2.extras
from dotenv import load_dotenv
load_dotenv()  # loads .env from project root


class CarsPipeline:
    def process_item(self, item: dict, spider) -> dict:
        return item



class PostgresqlPipeline:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST', '127.0.0.1'),
            database=os.getenv('POSTGRES_DB', 'postgres'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'your_password'),
            port=os.getenv('POSTGRES_PORT', '5432')
        )
        self.cur = self.conn.cursor()

    def close_spider(self, spider) -> None:
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    def process_item(self, item: dict, spider) -> dict:
        try:
            # Prepare the query and values
            query = """
               insert into public.cars(title, description, content_id, price, currency, category, category_type, url, isBusiness, isHighlighted, isPromoted, promotion, delivery, createdTime, lastRefreshTime, pushupTime, validToTime, isActive, status, isJob, itemCondition, negotiable, cityName, regionName, districtName, olx_user, model, car_body, motor_year, motor_mileage, transmission_type, color, motor_engine_size, fuel_type, car_condition, owners, car_option)
               values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                item.get('title'),
                item.get('description'),
                item.get('content_id'),
                item.get('price'),
                item.get('currency'),
                item.get('category'),
                item.get('category_type'),
                item.get('url'),
                item.get('isBusiness'),
                item.get('isHighlighted'),
                item.get('isPromoted'),
                item.get('promotion'),
                item.get('delivery'),
                item.get('createdTime'),
                item.get('lastRefreshTime'),
                item.get('pushupTime'),
                item.get('validToTime'),
                item.get('isActive'),
                item.get('status'),
                item.get('isJob'),
                item.get('itemCondition'),
                item.get('negotiable'),
                item.get('cityName'),
                item.get('regionName'),
                item.get('districtName'),
                item.get('olx_user'),
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
            self.cur.execute(query, values)
            self.conn.commit()
        except psycopg2.IntegrityError as e:
            self.conn.rollback()
            logger.warning(
                f"Duplicate entry found for content_id {item.get('content_id')}: {e.pgcode} - {e.pgerror}")
        except psycopg2.Error as e:
            self.conn.rollback()
            logger.error(f"Error processing item: {e.pgcode} - {e.pgerror}, Item: {item}")
        except Exception as e:
            self.conn.rollback()
            logger.error(f"Error processing item: {e}, Item: {item}")
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


