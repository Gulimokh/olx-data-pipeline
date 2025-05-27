
# 🏘 Collateral Assessment: OLX Real Estate Scraper

This project is designed for automatic parsing, filtering, and analysis of real estate listings from [OLX.uz](https://www.olx.uz/). The system covers:

- Apartments
- Houses
- Commercial properties

---

## 🧱 Project Structure

```
collateral-assessment/
├── apartments/                  # Apartment parser
│   └── apartments/
│       ├── spiders/apartments_olx.py
│       ├── pipelines.py
│       ├── settings.py
├── commercial_premises/        # Commercial real estate parser
│   └── commercial_premises/
│       ├── spiders/commercial_premises_olx.py
│       ├── pipelines.py
│       ├── settings.py
├── houses/                     # House parser
│   └── houses/
│       ├── spiders/houses_olx.py
│       ├── pipelines.py
│       ├── settings.py
├── ydata_profiling/           # Jupyter notebooks for analysis
│   ├── apartments_report/
│   └── houses_reports/
├── requirements.txt
├── README.md
```

---

## ⚡ Run Parsers

### Apartments
```bash
cd apartments
scrapy crawl apartments_olx
```

### Houses
```bash
cd houses
scrapy crawl houses
```

### Commercial Real Estate
```bash
cd commercial_premises
scrapy crawl commercial_premises_olx
```

---

## 📅 Filtering by Date and Area

📆 Listings are filtered by date:
```python
createdtime >= '2024-02-01'
```

🏢 Apartments are filtered by number of rooms and area:
```python
filters = {
    1: (18, 70),
    2: (25, 100),
    3: (30, 150),
    4: (50, 150),
    5: (80, 400)
}
```

---

## 📊 Data Profiling with `ydata_profiling`

Jupyter notebooks for data analysis:
- `ydata_profiling/apartments_report/ydataprofiling_for_apartments.ipynb`
- `ydata_profiling/houses_reports/ydataprofiling_for_houses.ipynb`

They perform:
- Outlier removal
- Filtering by region and area
- Generation of profiling reports: distributions, missing values, correlations

---

## 🗃 Data Storage

- Data is stored directly into PostgreSQL using `psycopg2`.
- `pipelines.py` handles the DB connection and inserts into tables `apartments`, `houses`, and `commercial_premises`.

---


## Environment Setup
Tested on **Python 3.10**.

```bash
pip install -r requirements.txt
```


