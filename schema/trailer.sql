CREATE TABLE IF NOT EXISTS public.trailer (
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
    isjob                   BOOLEAN,
    itemcondition           VARCHAR(64),
    negotiable              BOOLEAN,

    cityname                VARCHAR(128),
    regionname              VARCHAR(128),
    districtname            VARCHAR(128),
    olx_user                JSONB,

    scraped_at              TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_trailer_content_id ON public.trailer (content_id);
CREATE INDEX IF NOT EXISTS idx_trailer_created    ON public.trailer (createdtime);
