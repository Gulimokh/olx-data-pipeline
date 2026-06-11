import scrapy
import re
import datetime as dt


class ApartmentsKupiDomSpider(scrapy.Spider):
    name = "apartments_kupidom"
    allowed_domains = ["kupi-dom.uz"]
    start_urls = [
        # apartment listings
        "https://kupi-dom.uz/prodazha/t-kvartiry/",
    ]

    # ---------- LISTINGS ----------

    def parse(self, response):
        """
        Apartment listings page.
        Cards look like <div id="property-XXXX" class="property">...</div>.
        We collect all such blocks and extract links to detail pages.
        """

        # listing cards
        for card in response.css('div[id^="property-"].property'):
            detail_url = card.css("a::attr(href)").get()
            if detail_url:
                yield response.follow(detail_url, callback=self.parse_detail)

        # ---------- PAGINATION ----------

        # Pagination HTML structure on this page:
        # <div class="pagination">
        #   <li class="active"><a href=".../t-kvartiry/">1</a></li>
        #   <li><a href=".../t-kvartiry/page/2/">2</a></li>
        #   ...
        #   <li><a href=".../t-kvartiry/page/2/">Next</a></li>
        # </div>
        #
        # Grab the "Next" link from .pagination block
        next_page = response.xpath(
            '//div[contains(@class, "pagination")]'
            '//a[contains(normalize-space(.), "Следующие")]/@href'  # OLX pagination button: "Следующие" = "Next"
        ).get()

        if next_page:
            # log next page for visibility
            self.logger.info(f"Next page: {next_page}")
            yield response.follow(next_page, callback=self.parse)

    # ---------- LISTING DETAIL PAGE ----------

    def parse_detail(self, response):
        item = {}

        def clean_text(x):
            return x.strip() if isinstance(x, str) else x

        # URL
        item["url"] = response.url

        # <title>...</title>
        page_title = response.xpath("//title/text()").get()
        item["page_title"] = clean_text(page_title)

        # meta description / keywords
        meta_desc = response.xpath('//meta[@name="description"]/@content').get()
        meta_kw = response.xpath('//meta[@name="keywords"]/@content').get()
        item["meta_description"] = clean_text(meta_desc)
        item["meta_keywords"] = clean_text(meta_kw)

        # H1 title
        h1 = response.css("section#property-detail header.property-title h1::text").get()
        item["h1_title"] = clean_text(h1)

        # Category + deal type: "Apartments, Sale"
        tag_text = response.css("section.property-gallery figure.tag.status::text").get()
        if tag_text:
            parts = [p.strip() for p in tag_text.split(",")]
            item["category"] = parts[0] if len(parts) > 0 else None
            item["deal_type"] = parts[1] if len(parts) > 1 else None
        else:
            item["category"] = None
            item["deal_type"] = None

        # Listing ID
        property_id = response.css("a.print-page::attr(data-propertyid)").get()
        if property_id and property_id.isdigit():
            item["property_id"] = int(property_id)
        else:
            gallery_id = response.css('section[id^="property-gallery-"]::attr(id)').get()
            if gallery_id and "-" in gallery_id:
                try:
                    item["property_id"] = int(gallery_id.split("-")[-1])
                except ValueError:
                    item["property_id"] = None
            else:
                item["property_id"] = None

        # ---------- "Property Description" block ----------

        desc_html = response.xpath('//section[@id="description"]').get() or ""

        # Price in UZS (sums)
        m_uzs = re.search(
            r'([\d\s]+)&nbsp;<span class="wpcs_price_symbol">сум', desc_html  # OLX currency label: "сум" = UZS (sum)
        )
        if not m_uzs:
            m_uzs = re.search(r'([\d\s]+)\s*сум', desc_html)  # OLX currency: "сум" = UZS (sum)

        if m_uzs:
            uzs_digits = re.sub(r"[^\d]", "", m_uzs.group(1))
            item["price_uzs"] = int(uzs_digits) if uzs_digits else None
        else:
            item["price_uzs"] = None

        # Price in USD – from data-amount or "(85 000$)" as fallback
        m_usd = re.search(r'data-amount\s*=\s*"?([\d\.]+)"?', desc_html)
        if m_usd:
            try:
                item["price_usd"] = int(float(m_usd.group(1)))
            except ValueError:
                item["price_usd"] = None
        else:
            price_usd_raw = response.xpath(
                '//section[@id="description"]//p[contains(@class, "property-price")]'
                '//span[contains(@class, "price-secondary")]/text()'
            ).get()
            if price_usd_raw:
                usd_digits = re.sub(r"[^\d]", "", price_usd_raw)
                item["price_usd"] = int(usd_digits) if usd_digits else None
            else:
                item["price_usd"] = None

        # Publication date
        date_raw = response.xpath(
            '//section[@id="description"]//p[span[contains(text(), "Дата публикации")]]/text()'  # OLX label: "Дата публикации" = "Publication date"
        ).get()
        if date_raw:
            date_raw = date_raw.strip()
            try:
                dt_obj = dt.datetime.strptime(date_raw, "%d.%m.%Y")
                item["publish_date"] = dt_obj.date().isoformat()
            except ValueError:
                item["publish_date"] = date_raw
        else:
            item["publish_date"] = None

        # Number of rooms
        rooms_raw = response.xpath(
            '//section[@id="description"]//p[span[contains(text(), "Количество комнат")]]/text()'  # OLX label: "Количество комнат" = "Number of rooms"
        ).get()
        if rooms_raw:
            rooms_digits = re.sub(r"[^\d]", "", rooms_raw)
            item["rooms"] = int(rooms_digits) if rooms_digits else None
        else:
            item["rooms"] = None

        # Total area
        space_raw = response.xpath(
            '//section[@id="description"]//p[span[contains(text(), "Площадь")]]/text()'  # OLX label: "Площадь" = "Total area"
        ).get()
        if space_raw:
            m_space = re.search(r"([\d\.]+)", space_raw.replace(",", "."))
            item["total_space"] = float(m_space.group(1)) if m_space else None
        else:
            item["total_space"] = None

        # Address
        address = response.css("section#description p.property-address a::text").get()
        item["address"] = clean_text(address)

        # Property attributes
        features = response.css(
            "section#property_features ul.property_features-list li::text"
        ).getall()
        item["features"] = [clean_text(f) for f in features if clean_text(f)]

        # District (if "район" exists in features)
        district = None
        for f in item["features"]:
            if "район" in f:  # OLX word for "district"
                district = f
                break
        item["district"] = district

        # Description
        description_paragraphs = response.xpath(
            '//section[@id="description"]'
            '//p[preceding-sibling::p[@class="property-description"]'
            ' and not(@class="property-phones")]/text()'
        ).getall()
        description_paragraphs = [
            clean_text(p) for p in description_paragraphs if clean_text(p)
        ]
        item["description"] = "\n".join(description_paragraphs) if description_paragraphs else None

        # Phone
        phone_href = response.css("p.property-phones a::attr(href)").get()
        if phone_href and phone_href.startswith("tel:"):
            phone = phone_href[4:]
        else:
            phone = None
        item["phone"] = phone

        # Images
        image_urls = response.css(
            "section.property-gallery a.image-popup::attr(href)"
        ).getall()
        item["image_urls"] = [u for u in image_urls if u]

        # Coordinates from initMap("lat","lng",...)
        script_text = "".join(
            response.xpath('//script[contains(text(), "initMap")]/text()').getall()
        )

        lat = lng = None
        if script_text:
            m_coord = re.search(
                r'initMap\(\s*"([-0-9\.]+)"\s*,\s*"([-0-9\.]+)"',
                script_text
            )
            if m_coord:
                lat = float(m_coord.group(1))
                lng = float(m_coord.group(2))

        item["lat"] = lat
        item["lng"] = lng

        yield item