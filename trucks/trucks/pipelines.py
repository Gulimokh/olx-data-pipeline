import os

logger = logging.getLogger(__name__)

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2
import psycopg2.extras
import logging
import json
from dotenv import load_dotenv
load_dotenv()  # loads .env from project root


class TrucksPipeline:
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

    def clean_int(self, value: any) -> int | None:
        """Cleans and converts value to int"""
        try:
            return int(value.strip()) if isinstance(value, str) and value.strip().isdigit() else int(value)
        except (ValueError, TypeError):
            return None

    def clean_json(self, value: any) -> str:
        """Converts dict to JSON string"""
        return json.dumps(value) if isinstance(value, dict) else value

    def clean_bool(self, value: any) -> bool:
        """Converts 'Yes'/'No' and JSON True/False values to bool"""
        if value in ["Да", "да", "Yes", "yes", True]:  # OLX yes/no field values (Russian: "Да"=Yes, "Нет"=No)
            return True
        elif value in ["Нет", "нет", "No", "no", False]:  # OLX no field values
            return False
        return False  # default to False for None

    def process_item(self, item: dict, spider) -> dict:
        try:
            # Check if content_id already exists in the database
            check_query = "SELECT EXISTS (SELECT 1 FROM trucks_olx WHERE content_id = %s)"
            self.cur.execute(check_query, (item.get('content_id'),))
            result = self.cur.fetchone()

            if result[0]:
                logger.info(f"Item with content_id {item.get('content_id')} already exists. Skipping insertion.")
                return None  # Skip inserting the item
            # Prepare the query and values
            query = """
               insert into trucks_olx(title, description, content_id, price, currency, category, category_type, url, isBusiness, isHighlighted, isPromoted, promotion, delivery, createdTime, lastRefreshTime, pushupTime, validToTime, isActive, status, isJob, itemCondition, negotiable, cityName, regionName, districtName, olx_user, truck_manufacturer, body_type)
               values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               
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
                item.get('truck_manufacturer'),
                item.get('body_type')
            )


            self.cur.execute(query, values)
            self.conn.commit()

        except psycopg2.Error as e:
            self.conn.rollback()
            logger.error(f"❌ Database error: {e.pgcode} - {e.pgerror}, Item: {item}")
        except Exception as e:
            self.conn.rollback()
            logger.error(f"❌ Unexpected error: {e}, Item: {item}")

        return item