import pandas as pd
from sqlalchemy import create_engine, text

def run_analysis():
    """
    Runs SQL queries to analyze vehicle sensor data.
    """
    # Connect to database
    engine = create_engine("sqlite:///vehicle_sensors.db")
    print("✅ Connected to database")
    print("=" * 50)

    # Query 1: Average values per vehicle
    query1 = text("""
        SELECT 
            vehicle_id,
            ROUND(AVG(speed_kmh), 2) AS avg_speed,
            ROUND(AVG(engine_temp_celsius), 2) AS avg_engine_temp,
            ROUND(AVG(fuel_level_percent), 2) AS avg_fuel_level,
            COUNT(*) AS total_records
        FROM sensor_data
        GROUP BY vehicle_id
        ORDER BY avg_speed DESC
    """)

    # Query 2: Count anomalies per vehicle
    query2 = text("""
        SELECT 
            vehicle_id,
            SUM(anomaly_high_temp) AS high_temp_count,
            SUM(anomaly_high_speed) AS high_speed_count,
            SUM(anomaly_low_battery) AS low_battery_count
        FROM sensor_data
        GROUP BY vehicle_id
        ORDER BY high_temp_count DESC
    """)

    # Query 3: Overall statistics
    query3 = text("""
        SELECT
            COUNT(*) AS total_records,
            ROUND(AVG(speed_kmh), 2) AS avg_speed,
            ROUND(MAX(speed_kmh), 2) AS max_speed,
            ROUND(AVG(engine_temp_celsius), 2) AS avg_temp,
            ROUND(MAX(engine_temp_celsius), 2) AS max_temp
        FROM sensor_data
    """)

    # Run and print results
    with engine.connect() as conn:
        print("📊 Query 1: Average values per vehicle")
        print("-" * 50)
        df1 = pd.read_sql(query1, conn)
        print(df1.to_string(index=False))

        print("\n📊 Query 2: Anomalies per vehicle")
        print("-" * 50)
        df2 = pd.read_sql(query2, conn)
        print(df2.to_string(index=False))

        print("\n📊 Query 3: Overall statistics")
        print("-" * 50)
        df3 = pd.read_sql(query3, conn)
        print(df3.to_string(index=False))

if __name__ == "__main__":
    run_analysis()
