import psycopg2
import psycopg2.extras
import logging
import json

class CommercialPremisesPipeline:
    def process_item(self, item, spider):
        return item

class PostgresqlPipeline:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='127.0.0.1',
            database='postgres',
            user='postgres',
            password='5837',
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

    # === ФУНКЦИИ ОЧИСТКИ ДАННЫХ ===
    def clean_int(self, value):
        """Очищает и конвертирует значение в int"""
        try:
            return int(value.strip()) if isinstance(value, str) and value.strip().isdigit() else int(value)
        except:
            return None

    def clean_float(self, value):
        """Очищает и конвертирует строки в float (убирает 'м²')"""
        try:
            if isinstance(value, str):
                return float(value.replace(" м²", "").replace(",", ".").strip())
            return float(value) if value else None
        except:
            return None

    def clean_bool(self, value):
        """Конвертирует 'Да'/'Нет' и JSON-значения True/False в Boolean"""
        if value in ["Да", "да", "Yes", "yes", True]:
            return True
        elif value in ["Нет", "нет", "No", "no", False]:
            return False
        return False  # Если None, ставим False

    def clean_json(self, value):
        """Конвертирует словарь в JSON-строку"""
        return json.dumps(value) if isinstance(value, dict) else value

    def clean_year(self, value):
        """Выбирает первый год из диапазона"""
        try:
            if isinstance(value, str) and "-" in value:
                return int(value.split("-")[0].strip())
            return int(value) if value else None
        except:
            return None

    def process_item(self, item, spider):
        try:
            values = (
                item.get('title'),
                self.clean_int(item.get('content_id')),
                item.get('description'),
                item.get('category'),
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
                self.clean_int(item.get('price')),
                item.get('currency'),
                self.clean_bool(item.get('negotiable')),
                item.get('cityName'),
                item.get('regionName'),
                item.get('districtName') or None,
                self.clean_json(item.get('user')),

                item.get('premise_type'),
                self.clean_float(item.get('total_area')),
                self.clean_float(item.get('effective_area')),
                self.clean_float(item.get('land')),
                self.clean_int(item.get('floor')),
                self.clean_int(item.get('total_floors')),
                self.clean_float(item.get('ceiling_height')),
                item.get('repairs'),
                item.get('more_premises'),
                self.clean_bool(item.get('parking_lot')),
                self.clean_bool(item.get('comission')),
            )

            query = """
        INSERT INTO public.commercial_premises (
            title, content_id, description, category, url, isbusiness, ishighlighted, ispromoted,
            promotion, delivery, createdtime, lastrefreshtime, pushuptime, validtotime, isactive, status,
            price, currency, negotiable, cityname, regionname, districtname, olx_user,
            premise_type, total_area, effective_area, land, floor, total_floors, ceiling_height, repairs,
             more_premises, parking_lot, comission
             ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (content_id) DO NOTHING;
"""

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


