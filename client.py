import delta_sharing
import pandas as pd
import os

# Path to the Delta Sharing profile (JSON format)
profile_file = os.path.abspath("config/delta-sharing-profile.json")

# Check if the file exists
if not os.path.isfile(profile_file):
    raise FileNotFoundError(f"Delta Sharing profile not found: {profile_file}")

# Create a Delta Sharing client
try:
    client = delta_sharing.SharingClient(profile_file)
except Exception as e:
    print(f"Error creating Delta Sharing client: {e}")
    raise

# Define the URL to access the shared Parquet files
table_url = "shares/kamal_parquets/schemas/default/tables/all_parquets"

# Load the table as a Pandas DataFrame
try:
    print("Reading data from Delta Sharing...")
    table = delta_sharing.load_as_pandas(table_url, client)
except Exception as e:
    print(f"Error loading data from Delta Sharing: {e}")
    raise

# Display the data
print("Data from shared Parquet files:")
print(table.head())

# Save the data to a local CSV file for verification
table.to_csv("shared_parquets_data.csv", index=False)
print("Data saved to 'shared_parquets_data.csv'")
