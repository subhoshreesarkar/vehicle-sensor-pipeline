import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()


def generate_sensor_data(num_records=100):
    """
    Simulates vehicle sensor data as it could occur in automotive production.
    """
    data = []

    vehicle_ids = [f"AU-{random.randint(1000, 9999)}" for _ in range(10)]

    for _ in range(num_records):
        record = {
            "timestamp": fake.date_time_between(start_date="-7d", end_date="now").strftime("%Y-%m-%d %H:%M:%S"),
            "vehicle_id": random.choice(vehicle_ids),
            "speed_kmh": round(random.uniform(0, 250), 2),
            "engine_temp_celsius": round(random.uniform(70, 120), 2),
            "battery_voltage": round(random.uniform(11.5, 14.8), 2),
            "fuel_level_percent": round(random.uniform(0, 100), 2),
            "rpm": random.randint(700, 7000),
            "oil_pressure_bar": round(random.uniform(1.0, 5.0), 2),
        }
        data.append(record)

    df = pd.DataFrame(data)
    df.to_csv("sensor_data_raw.csv", index=False)
    print(f"✅ {num_records} records successfully generated!")
    print(df.head())
    return df


if __name__ == "__main__":
    generate_sensor_data()
