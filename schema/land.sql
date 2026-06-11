CREATE TABLE IF NOT EXISTS public.land (
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

    -- Land-specific fields
    land_type               VARCHAR(128),
    purpose                 VARCHAR(128),            -- residential / agricultural / commercial
    plot                    FLOAT,                   -- area in sotka
    total_area              FLOAT,
    in_city                 VARCHAR(128),
    location                TEXT,
    comission               BOOLEAN,
    phone                   VARCHAR(32),
    water                   TEXT,
    gas                     TEXT,
    electricity             TEXT,
    heating                 TEXT,
    internet                TEXT,
    canalization            TEXT,
    communications          TEXT,
    near_is                 TEXT,

    scraped_at              TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_land_content_id ON public.land (content_id);
CREATE INDEX IF NOT EXISTS idx_land_created    ON public.land (createdtime);
