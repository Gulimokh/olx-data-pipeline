CREATE TABLE IF NOT EXISTS public.houses (
    id                      SERIAL PRIMARY KEY,
    content_id              INTEGER UNIQUE,
    title                   VARCHAR(512),
    price                   FLOAT,
    currency                VARCHAR(10),
    description             TEXT,
    category                VARCHAR(128),
    category_type           VARCHAR(128),
    url                     TEXT,

    isbusiness              BOOLEAN,
    ishighlighted           BOOLEAN,
    ispromoted              BOOLEAN,
    promotion               JSONB,
    delivery                JSONB,
    createdtime             TIMESTAMP,
    lastrefreshtime         TIMESTAMP,
    pushuptime              TIMESTAMP,
    validtotime             TIMESTAMP,
    isactive                BOOLEAN,
    status                  VARCHAR(64),
    itemcondition           VARCHAR(64),
    negotiable              BOOLEAN,

    cityname                VARCHAR(128),
    regionname              VARCHAR(128),
    districtname            VARCHAR(128),
    olx_user                JSONB,

    -- House-specific fields
    number_of_rooms         INTEGER,
    floor                   INTEGER,
    total_floors            INTEGER,
    house_type              VARCHAR(128),
    house_subtype           VARCHAR(128),
    layout                  VARCHAR(128),
    year_of_construction_sale INTEGER,
    wc                      VARCHAR(64),
    furnished               VARCHAR(64),
    ceiling_height          FLOAT,
    repairs                 VARCHAR(128),
    comission               BOOLEAN,
    total_area              FLOAT,
    total_living_area       FLOAT,
    plot                    FLOAT,                   -- land plot area in sotka
    location                TEXT,                    -- urban/suburban/rural
    water                   TEXT,
    heating                 TEXT,
    gas                     TEXT,
    electricity             TEXT,
    more_house              TEXT,
    near_is                 TEXT,

    scraped_at              TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_houses_content_id ON public.houses (content_id);
CREATE INDEX IF NOT EXISTS idx_houses_created    ON public.houses (createdtime);
CREATE INDEX IF NOT EXISTS idx_houses_city       ON public.houses (cityname);
