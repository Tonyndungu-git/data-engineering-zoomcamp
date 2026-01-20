# clean_csv.py
import pandas as pd

# ---------- GREEN TRIPDATA ----------
tripdata_input = "data/green_tripdata_2025-11.csv"
tripdata_clean = "data/green_tripdata_2025-11_clean.csv"

# Load CSV
df_trip = pd.read_csv(tripdata_input)

# Columns expected in the table
expected_columns = [
    "lpep_pickup_datetime","lpep_dropoff_datetime","store_and_fwd_flag",
    "RatecodeID","PULocationID","DOLocationID","passenger_count",
    "trip_distance","fare_amount","extra","mta_tax","tip_amount",
    "tolls_amount","ehail_fee","improvement_surcharge","total_amount",
    "payment_type","trip_type","congestion_surcharge","cbd_congestion_fee"
]

# Keep only expected columns
df_trip = df_trip[expected_columns]

# Columns that should be integers
int_cols = ["RatecodeID","PULocationID","DOLocationID","passenger_count","payment_type","trip_type"]
for col in int_cols:
    df_trip[col] = pd.to_numeric(df_trip[col], errors='coerce').fillna(0).astype(int)

# Columns that should be floats
float_cols = ["trip_distance","fare_amount","extra","mta_tax","tip_amount",
              "tolls_amount","ehail_fee","improvement_surcharge","total_amount",
              "congestion_surcharge","cbd_congestion_fee"]
for col in float_cols:
    df_trip[col] = pd.to_numeric(df_trip[col], errors='coerce').fillna(0.0)

# Datetime columns
df_trip["lpep_pickup_datetime"] = pd.to_datetime(df_trip["lpep_pickup_datetime"], errors='coerce')
df_trip["lpep_dropoff_datetime"] = pd.to_datetime(df_trip["lpep_dropoff_datetime"], errors='coerce')

# Text column
df_trip["store_and_fwd_flag"] = df_trip["store_and_fwd_flag"].fillna("N")

# Save cleaned CSV
df_trip.to_csv(tripdata_clean, index=False)
print("✅ green_tripdata cleaned!")

# ---------- TAXI ZONE LOOKUP ----------
zone_input = "data/taxi_zone_lookup.csv"
zone_clean = "data/taxi_zone_lookup_clean.csv"

df_zone = pd.read_csv(zone_input)

# Keep only expected columns
zone_columns = ["LocationID","Borough","Zone","service_zone"]
df_zone = df_zone[zone_columns]

# LocationID must be integer
df_zone["LocationID"] = pd.to_numeric(df_zone["LocationID"], errors='coerce').fillna(0).astype(int)

# Text columns fill missing values
for col in ["Borough","Zone","service_zone"]:
    df_zone[col] = df_zone[col].fillna("Unknown")

# Save cleaned CSV
df_zone.to_csv(zone_clean, index=False)
print("✅ taxi_zone_lookup cleaned!")
