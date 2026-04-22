# Merge every traffic incident with that day's weather

import os
import pandas as pd

base = os.path.dirname(__file__)
cleanFolder = os.path.join(base, "CleanData")

traffic_path = os.path.join(cleanFolder, "traffic_cleaned.csv")
climate_path = os.path.join(cleanFolder, "climate_cleaned.csv")

traffic = pd.read_csv(traffic_path)
climate = pd.read_csv(climate_path)

print("Files Loaded")

# ---------------------------------------------------
# Clean column names
traffic.columns = traffic.columns.str.strip()
climate.columns = climate.columns.str.strip()

# ---------------------------------------------------
# Convert dates

traffic["date"] = pd.to_datetime(traffic["date"])
climate["Date/Time"] = pd.to_datetime(climate["Date/Time"])

# Rename climate column to match traffic
climate = climate.rename(columns={"Date/Time": "date"})
# Remove unnecessary climate location metadata
climate = climate.drop(columns=[
    "Longitude (x)",
    "Latitude (y)",
    "Station Name",
    "Climate ID",
], errors="ignore")
print("Dates Converted")

# ---------------------------------------------------
# Merge each incident with weather for that day

merged = pd.merge(
    traffic,
    climate,
    on="date",
    how="left"
)

print("Incident + Weather merge complete")

# ---------------------------------------------------
# Export merged dataset

output_path = os.path.join(cleanFolder, "reduced_incident_weather_merged.csv")
merged.to_csv(output_path, index=False)

print("\nMerged dataset exported")
print(output_path)

# ---------------------------------------------------
# Quick check

print("\nFinal dataset shape:", merged.shape)
print("\nSample:")
print(merged.head())