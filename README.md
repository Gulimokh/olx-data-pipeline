# collateral-assessment

A production-grade data collection pipeline for real estate and vehicle market analysis in Uzbekistan. Scrapes structured listing data from [OLX.uz](https://www.olx.uz/) and [kupi-dom.uz](https://kupi-dom.uz/) across 10 asset categories, storing normalized records in PostgreSQL for downstream pricing and collateral valuation models.

---

## Asset Categories

| Category | Spider | Source | Table |
|----------|--------|--------|-------|
| Apartments | `apartments_olx` | OLX.uz | `public.apartments` |
| Houses | `houses` | OLX.uz | `public.houses` |
| Commercial premises | `commercial_premises_olx` | OLX.uz | `public.commercial_premises` |
| Land plots | `land_olx` | OLX.uz | `public.land` |
| Apartments (alt) | `apartments_kupidom` | kupi-dom.uz | `public.kupidom_apartments` |
| Cars | `carsspider` | OLX.uz | `public.cars` |
| Trucks | `trucksspiders` | OLX.uz | `public.trucks` |
| Trailers | `trailerspiders` | OLX.uz | `public.trailer` |
| Special vehicles | `specialvehiclesspiders` | OLX.uz | `public.specialvehicles` |
| Agricultural machinery | `agromachinespiders` | OLX.uz | `public.agromachine` |

---

## Architecture

```
OLX.uz / kupi-dom.uz
        │
        │  HTTP (Scrapy + js2py for OLX JSON extraction)
        ▼
┌──────────────────────────────────┐
│         Scrapy Spider            │
│  - Segments search space into    │
│    multiple start_urls to bypass │
│    OLX 25-page pagination limit  │
│  - Extracts listing data from    │
│    embedded JS (js2py)           │
│  - Follows pagination            │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│         Pipeline                 │
│  - Type-safe field cleaning      │
│    (int, float, bool, JSON, year)│
│  - ON CONFLICT DO NOTHING        │
│    (deduplication by content_id) │
│  - psycopg2 → PostgreSQL         │
└──────────────┬───────────────────┘
               │
               ▼
         PostgreSQL
```

---

## Setup

### 1. Clone and install dependencies

```bash
git clone https://github.com/Gulimokh/collateral-assessment.git
cd collateral-assessment
pip install -r requirements.txt
```

### 2. Configure environment

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

```env
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
```

### 3. Create PostgreSQL tables

Each spider expects its table to exist. Schema examples are provided as comments at the bottom of each `pipelines.py` file.

---

## Running Spiders

Each spider is a standalone Scrapy project. Run from the corresponding subdirectory:

```bash
# Apartments
cd apartments && scrapy crawl apartments_olx

# Houses
cd houses && scrapy crawl houses

# Commercial premises
cd commercial_premises && scrapy crawl commercial_premises_olx

# Land
cd land && scrapy crawl land_olx

# Cars
cd cars && scrapy crawl carsspider

# Trucks
cd trucks && scrapy crawl trucksspiders

# Trailers
cd trailer && scrapy crawl trailerspiders

# Special vehicles
cd specialvehicles && scrapy crawl specialvehiclesspiders

# Agricultural machinery
cd agromachine && scrapy crawl agromachinespiders

# Apartments from kupi-dom.uz
cd kupidom && scrapy crawl apartments_kupidom
```

---

## URL Segmentation Strategy

OLX pagination is capped at 25 pages × 40 items = 1,000 results per search. To maximize coverage, each spider splits the search space into multiple `start_urls` using OLX filter parameters (room count, area range, floor, condition, fuel type, body type, etc.). This ensures full market coverage without hitting the pagination ceiling.

---

## Data Filtering

Listings are filtered before insertion to ensure quality:

```python
# Date filter — only recent listings
createdtime >= '2024-02-01'

# Area filter by room count (apartments)
filters = {
    1: (18, 70),    # 1-room: 18–70 m²
    2: (25, 100),   # 2-room: 25–100 m²
    3: (30, 150),   # 3-room: 30–150 m²
    4: (50, 150),   # 4-room: 50–150 m²
    5: (80, 400),   # 5+ rooms: 80–400 m²
}
```

---

## Data Profiling

Jupyter notebooks for EDA are in `ydata_profiling/`:

```bash
# Apartments analysis
jupyter notebook ydata_profiling/apartments_report/ydataprofiling_for_apartments.ipynb

# Houses analysis
jupyter notebook ydata_profiling/houses_reports/ydataprofiling_houses.ipynb
```

Reports include: distributions, missing values, outlier detection, correlations, and region-level segmentation.

---

## Project Structure

```
collateral-assessment/
├── apartments/                  # Apartment spider (OLX.uz)
├── houses/                      # House spider (OLX.uz)
├── commercial_premises/         # Commercial property spider (OLX.uz)
├── land/                        # Land plot spider (OLX.uz)
├── kupidom/                     # Apartment spider (kupi-dom.uz)
├── cars/                        # Car spider (OLX.uz)
├── trucks/                      # Truck spider (OLX.uz)
├── trailer/                     # Trailer spider (OLX.uz)
├── specialvehicles/             # Special vehicle spider (OLX.uz)
├── agromachine/                 # Agricultural machinery spider (OLX.uz)
├── ydata_profiling/             # EDA notebooks (apartments, houses)
├── requirements.txt
├── .env.example                 # Environment variable template
└── README.md
```

Each spider subdirectory follows the standard Scrapy layout:
```
<category>/
├── <category>/
│   ├── spiders/
│   │   └── <spider>.py      # Spider — URL segmentation + data extraction
│   ├── pipelines.py         # DB pipeline — field cleaning + PostgreSQL insert
│   ├── items.py             # Item schema
│   └── settings.py          # Scrapy settings + pipeline config
└── scrapy.cfg
```

---

## Tech Stack

`Python 3.10` · `Scrapy` · `js2py` · `psycopg2` · `PostgreSQL` · `ydata-profiling` · `pandas` · `python-dotenv`
