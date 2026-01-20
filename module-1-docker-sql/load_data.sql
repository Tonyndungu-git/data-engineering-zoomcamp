-- ---------- 1. Create green_tripdata table ----------
DROP TABLE IF EXISTS green_tripdata;
CREATE TABLE green_tripdata (
    lpep_pickup_datetime TIMESTAMP,
    lpep_dropoff_datetime TIMESTAMP,
    store_and_fwd_flag TEXT,
    ratecodeid INT,
    pulocationid INT,
    dolocationid INT,
    passenger_count INT,
    trip_distance FLOAT,
    fare_amount FLOAT,
    extra FLOAT,
    mta_tax FLOAT,
    tip_amount FLOAT,
    tolls_amount FLOAT,
    ehail_fee FLOAT,
    improvement_surcharge FLOAT,
    total_amount FLOAT,
    payment_type INT,
    trip_type INT,
    congestion_surcharge FLOAT,
    cbd_congestion_fee FLOAT
);

-- ---------- 2. Load green_tripdata CSV ----------
\copy green_tripdata FROM '/data/green_tripdata_2025-11_clean.csv' DELIMITER ',' CSV HEADER NULL AS '';

-- ---------- 3. Create taxi_zone_lookup table ----------
DROP TABLE IF EXISTS taxi_zone_lookup;
CREATE TABLE taxi_zone_lookup (
    "LocationID" INT,
    "Borough" TEXT,
    "Zone" TEXT,
    "service_zone" TEXT
);

-- ---------- 4. Load taxi_zone_lookup CSV ----------
\copy taxi_zone_lookup FROM '/data/taxi_zone_lookup_clean.csv' DELIMITER ',' CSV HEADER NULL AS '';
