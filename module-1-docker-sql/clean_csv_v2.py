# clean_csv_v2.py
import pandas as pd

tripdata_path = "data/green_tripdata_2025-11.csv"
clean_path = "data/green_tripdata_2025-11_clean.csv"

# Load CSV
df = pd.read_csv(tripdata_path)

# Expected columns
expected_columns = [
    "lpep_pickup_datetime","lpep_dropoff_datetime","store_and_fwd_flag",
    "ratecodeid","pulocationid","dolocationid","passenger_count",
    "trip_distance","fare_amount","extra","mta_tax","tip_amount",
    "tolls_amount","ehail_fee","improvement_surcharge","total_amount",
    "payment_type","trip_type","congestion_surcharge","cbd_congestion_fee"
]

# Add missing columns if any
for col in expected_columns:
    if col not in df.columns:
        df[col] = 0

# Keep only expected columns, in order
df = df[expected_columns]

# Ensure numeric columns are numeric and fill NaNs
numeric_cols = [
    "ratecodeid","pulocationid","dolocationid","passenger_count",
    "trip_distance","fare_amount","extra","mta_tax","tip_amount","tolls_amount",
    "ehail_fee","improvement_surcharge","total_amount","payment_type",
    "trip_type","congestion_surcharge","cbd_congestion_fee"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Fill datetime missing values with some placeholder (won’t affect homework queries)
df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"], errors='coerce')
df["lpep_dropoff_datetime"] = pd.to_datetime(df["lpep_dropoff_datetime"], errors='coerce')

# Fill text columns
df["store_and_fwd_flag"] = df["store_and_fwd_flag"].fillna('N')

# Save clean CSV
df.to_csv(clean_path, index=False)

print("Cleaned CSV saved, exactly 20 columns now!")
