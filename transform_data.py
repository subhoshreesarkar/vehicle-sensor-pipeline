import pandas as pd

def transform_data(input_file="sensor_data_raw.csv"):
    """
    Transforms and cleans raw vehicle sensor data.
    """
    # Load raw data
    df = pd.read_csv(input_file)
    print(f"✅ Loaded {len(df)} records from '{input_file}'")
    print(f"📊 Columns: {list(df.columns)}")

    # Convert timestamp to datetime format
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Remove duplicate records
    before = len(df)
    df = df.drop_duplicates()
    print(f"🔍 Removed {before - len(df)} duplicate records")

    # Remove records with missing values
    before = len(df)
    df = df.dropna()
    print(f"🔍 Removed {before - len(df)} records with missing values")

    # Flag anomalies without removing them
    df["anomaly_high_temp"] = df["engine_temp_celsius"] > 110
    df["anomaly_high_speed"] = df["speed_kmh"] > 230
    df["anomaly_low_battery"] = df["battery_voltage"] < 12.0

    # Save cleaned data
    output_file = "sensor_data_cleaned.csv"
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to '{output_file}'")
    print(f"📊 Final dataset: {len(df)} records")
    print(df.head())

    return df

if __name__ == "__main__":
    transform_data()
