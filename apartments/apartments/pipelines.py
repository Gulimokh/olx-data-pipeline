import os
import psycopg2
import psycopg2.extras
import logging
import json
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()  # loads .env from project root


class ApartmentsPipeline:
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

    # === DATA CLEANING HELPERS ===
    def clean_int(self, value: any) -> int | None:
        """Cleans and converts value to int"""
        try:
            return int(value.strip()) if isinstance(value, str) and value.strip().isdigit() else int(value)
        except (ValueError, TypeError):
            return None

    def clean_float(self, value: any) -> float | None:
        """Cleans and converts string to float (strips 'm²')"""
        try:
            if isinstance(value, str):
                return float(value.replace(" м²", "").replace(",", ".").strip())  # OLX area unit: "м²" = m²
            return float(value) if value else None
        except (ValueError, TypeError):
            return None

    def clean_bool(self, value: any) -> bool:
        """Converts 'Yes'/'No' and JSON True/False values to bool"""
        if value in ["Да", "да", "Yes", "yes", True]:  # OLX yes/no field values (Russian: "Да"=Yes, "Нет"=No)
            return True
        elif value in ["Нет", "нет", "No", "no", False]:  # OLX no field values
            return False
        return False  # default to False for None

    def clean_json(self, value: any) -> str:
        """Converts dict to JSON string"""
        return json.dumps(value) if isinstance(value, dict) else value

    def clean_year(self, value: any) -> int | None:
        """Extracts the first year from a year range string"""
        try:
            if isinstance(value, str) and "-" in value:
                return int(value.split("-")[0].strip())
            return int(value) if value else None
        except (ValueError, TypeError):
            return None

    def process_item(self, item: dict, spider) -> dict:
        try:
            values = (
                item.get('title'),
                self.clean_int(item.get('price')),
                item.get('currency'),
                item.get('description'),
                self.clean_int(item.get('content_id')),
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
                item.get('itemCondition'),
                self.clean_bool(item.get('negotiable')),
                item.get('cityName'),
                item.get('regionName'),
                item.get('districtName') or None,
                self.clean_json(item.get('user')),
                self.clean_int(item.get('number_of_rooms')),
                self.clean_int(item.get('floor')),
                self.clean_int(item.get('total_floors')),
                item.get('house_type'),
                item.get('layout'),
                self.clean_year(item.get('year_of_construction_sale')),
                item.get('wc'),
                item.get('furnished'),
                self.clean_float(item.get('ceiling_height')),
                item.get('repairs'),
                self.clean_bool(item.get('comission')),
                self.clean_float(item.get('total_area')),
                self.clean_float(item.get('total_living_area')),
            )

            query = """
            INSERT INTO public.apartments (
                title, price, currency, description, content_id, category, category_type, url,
                isbusiness, ishighlighted, ispromoted, promotion, delivery, createdtime, lastrefreshtime,
                pushuptime, validtotime, isactive, status, itemcondition, negotiable, cityname, regionname,
                districtname, olx_user, number_of_rooms, floor, total_floors, house_type, layout,
                year_of_construction_sale, wc, furnished, ceiling_height, repairs, comission, total_area, total_living_area
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
             ON CONFLICT (content_id) DO NOTHING;
            """



            self.cur.execute(query, values)
            self.conn.commit()

        except psycopg2.Error as e:
            self.conn.rollback()
            logger.error(f"❌ Database error: {e.pgcode} - {e.pgerror}, Item: {item}")
        except Exception as e:
            self.conn.rollback()
            logger.error(f"❌ Unexpected error: {e}, Item: {item}")

        return item
