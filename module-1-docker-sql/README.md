# Module 1 Homework: Docker & SQL

# Module 1 Homework: Docker, SQL & Terraform

## Q1: Docker Image

Run the Python 3.13 Docker image and check the pip version.

```bash
docker run -it --entrypoint bash python:3.13
pip --version
````

---

## Q2: Docker Container

Start a container interactively and open bash:

```bash
docker run -it python:3.13 bash
```

Inside the container, verify Python and pip versions:

```bash
python --version
pip --version
```

---

## Q3: Dockerfile (Optional)

You can build a custom Docker image:

```bash
docker build -t my-python-image .
docker run -it my-python-image
```

---

## Q4–Q6: SQL Tasks (PostgreSQL)

### Folder & Files

```
module-1-docker-sql/
├── clean_csv.py
├── clean_csv_v2.py
├── data/
│   ├── green_tripdata_2025-11.csv
│   ├── green_tripdata_2025-11_clean.csv
│   ├── taxi_zone_lookup.csv
│   └── taxi_zone_lookup_clean.csv
├── load_data.sql
└── queries.sql
```

---

### Step 1: Start PostgreSQL using Docker

```bash
docker run --name pg-docker \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -d postgres:15
```

Check it’s running:

```bash
docker ps
```

---

### Step 2: Connect to PostgreSQL

```bash
docker exec -it pg-docker psql -U postgres
```

---

### Step 3: Prepare the database

```sql
CREATE DATABASE ny_taxi;
\c ny_taxi
```

---

### Step 4: Load tables from CSV

1. Copy CSV files into the container:

```bash
docker cp data/green_tripdata_2025-11_clean.csv pg-docker:/green_tripdata_2025-11_clean.csv
docker cp data/taxi_zone_lookup_clean.csv pg-docker:/taxi_zone_lookup_clean.csv
```

2. Run the SQL script to create tables and load data:

```bash
psql -U postgres -d ny_taxi -f load_data.sql
```

---

### Step 5: Run SQL Queries

```sql
-- Run all queries from queries.sql
\i queries.sql
```

Verify table contents:

```sql
SELECT * FROM green_tripdata_2025_11 LIMIT 5;
\dt
```

---

### Step 6: Stop the container (optional)

```bash
docker stop pg-docker
docker rm pg-docker
```

---

## Q7: Terraform (GCP)

### Prerequisites

* GCP project ID (e.g., `data-eng-terraform-484916`)
* Service account JSON key (keep it **secure** — do NOT push to GitHub)

### Step 1: Configure provider

`main.tf` example:

```hcl
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = "data-eng-terraform-484916"
  region  = "us-central1"
}
```

### Step 2: Set credentials

Upload your JSON file to Codespaces (do not commit to git).
Then set the environment variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-key.json"
```

---

### Step 3: Initialize Terraform

```bash
terraform init
```

---

### Step 4: Plan

```bash
terraform plan
```

---

### Step 5: Apply (creates resources in GCP)

```bash
terraform apply -auto-approve
```

> Note: You must have billing enabled in your project to create Cloud Storage buckets. 

---

### Step 6: Cleanup (optional)

```bash
terraform destroy -auto-approve
```

---

## Notes

* Use **clean CSVs** to avoid formatting errors.
* Make sure Docker ports and GCP credentials are set correctly.
* Keep JSON service account keys **private**.
* Terraform will create **BigQuery dataset** and optionally **Cloud Storage bucket**.

```