terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = "data-eng-terraform-484916"   #  GCP project ID
  region  = "us-central1"
}


# Create a BigQuery dataset
resource "google_bigquery_dataset" "ny_taxi_dataset" {
  dataset_id = "ny_taxi_dataset"   # dataset name
  project    = "data-eng-terraform-484916"
  location   = "US"
  
}
