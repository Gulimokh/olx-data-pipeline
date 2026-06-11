CREATE TABLE IF NOT EXISTS public.cars (
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

    -- Car-specific fields
    model                   VARCHAR(128),
    car_body                VARCHAR(64),
    motor_year              INTEGER,
    motor_mileage           INTEGER,
    transmission_type       VARCHAR(64),
    color                   VARCHAR(64),
    motor_engine_size       FLOAT,
    fuel_type               VARCHAR(64),
    car_condition           VARCHAR(64),
    owners                  INTEGER,
    car_option              TEXT,

    scraped_at              TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_cars_content_id ON public.cars (content_id);
CREATE INDEX IF NOT EXISTS idx_cars_created    ON public.cars (createdtime);
CREATE INDEX IF NOT EXISTS idx_cars_model      ON public.cars (model);
