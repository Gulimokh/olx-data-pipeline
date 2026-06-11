CREATE TABLE IF NOT EXISTS public.commercial_premises (
    id                      SERIAL PRIMARY KEY,
    content_id              INTEGER UNIQUE,
    title                   VARCHAR(512),
    price                   FLOAT,
    currency                VARCHAR(10),
    description             TEXT,
    category                VARCHAR(128),
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
    negotiable              BOOLEAN,

    cityname                VARCHAR(128),
    regionname              VARCHAR(128),
    districtname            VARCHAR(128),
    olx_user                JSONB,

    -- Commercial-specific fields
    premise_type            VARCHAR(128),
    total_area              FLOAT,
    effective_area          FLOAT,
    land                    FLOAT,
    floor                   INTEGER,
    total_floors            INTEGER,
    ceiling_height          FLOAT,
    repairs                 VARCHAR(128),
    comission               BOOLEAN,
    parking_lot             VARCHAR(64),
    more_premises           TEXT,

    scraped_at              TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_commercial_content_id ON public.commercial_premises (content_id);
CREATE INDEX IF NOT EXISTS idx_commercial_created    ON public.commercial_premises (createdtime);
