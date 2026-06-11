import os

logger = logging.getLogger(__name__)

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class KupidomApartmentsPipeline:
    def process_item(self, item: dict, spider) -> dict:
        return item




import psycopg2
import json
import logging
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()  # loads .env from project root



class PostgresqlPipeline:
    def __init__(self):
        # substitute your actual DB credentials here
        self.conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "127.0.0.1"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            database=os.getenv("POSTGRES_DB", "postgres"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv('POSTGRES_PASSWORD', 'your_password'),
        )
        self.cur = self.conn.cursor()

    def close_spider(self, spider) -> None:
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

    # ---- helper methods (same as OLX pipeline) ----

    def clean_int(self, value: any) -> int | None:
        try:
            if isinstance(value, str):
                v = value.strip()
                return int(v) if v else None
            return int(value) if value is not None else None
        except Exception:
            return None

    def clean_float(self, value: any) -> float | None:
        try:
            if isinstance(value, str):
                v = value.replace("м²", "").replace(" ", "").replace(",", ".").strip()  # OLX area unit: "м²" = m²
                return float(v) if v else None
            return float(value) if value is not None else None
        except Exception:
            return None

    def clean_date(self, value):
        # value is already a string like '2025-06-23' or '23.06.2025'
        if not value:
            return None
        if isinstance(value, datetime):
            return value.date()
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                try:
                    return datetime.strptime(value, "%d.%m.%Y").date()
                except ValueError:
                    return None
        return None

    def clean_json(self, value: any) -> str:
        if value is None:
            return None
        # store both dict and list as JSON string
        if isinstance(value, (dict, list)):
            return json.dumps(value, ensure_ascii=False)
        return str(value)

    # ---- main insert logic ----

    def process_item(self, item: dict, spider) -> dict:
        try:
            features_json = self.clean_json(item.get("features"))
            images_json = self.clean_json(item.get("image_urls"))

            values = (
                self.clean_int(item.get("property_id")),
                item.get("url"),

                item.get("page_title"),
                item.get("meta_description"),
                item.get("meta_keywords"),
                item.get("h1_title"),

                item.get("category"),
                item.get("deal_type"),

                item.get("price_uzs"),
                item.get("price_usd"),
                self.clean_date(item.get("publish_date")),

                self.clean_int(item.get("rooms")),
                self.clean_float(item.get("total_space")),

                item.get("address"),
                item.get("district"),

                features_json,
                item.get("description"),
                item.get("phone"),

                item.get("lat"),
                item.get("lng"),

                images_json,
            )

            query = """
            INSERT INTO public.kupidom_apartments (
                property_id,
                url,
                page_title, meta_description, meta_keywords, h1_title,
                category, deal_type,
                price_uzs, price_usd, publish_date,
                rooms, total_space,
                address, district,
                features, description, phone,
                lat, lng,
                image_urls
            )
            VALUES (
                %s, %s,
                %s, %s, %s, %s,
                %s, %s,
                %s, %s, %s,
                %s, %s,
                %s, %s,
                %s, %s, %s,
                %s, %s,
                %s
            )
            ON CONFLICT (property_id) DO NOTHING;
            """

            self.cur.execute(query, values)
            self.conn.commit()

        except psycopg2.Error as e:
            self.conn.rollback()
            logger.error(
                f"❌ Database error: {e.pgcode} - {e.pgerror}, Item: {item}"
            )
        except Exception as e:
            self.conn.rollback()
            logger.error(f"❌ Unexpected error: {e}, Item: {item}")

        return item