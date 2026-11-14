import pandas as pd
from sqlalchemy import create_engine, text

def load_to_database(input_file="sensor_data_cleaned.csv"):
    """
    Loads cleaned vehicle sensor data into a SQLite database using SQLAlchemy.
    """
    # Load cleaned data
    df = pd.read_csv(input_file)
    print(f"✅ Loaded {len(df)} records from '{input_file}'")

    # Create database connection
    engine = create_engine("sqlite:///vehicle_sensors.db")
    print("✅ Database connection established")

    # Load data into database table
    df.to_sql(
        name="sensor_data",
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"✅ {len(df)} records loaded into table 'sensor_data'")

    # Quick verification query
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM sensor_data"))
        count = result.fetchone()[0]
        print(f"📊 Verification: {count} records found in database")

    return engine

if __name__ == "__main__":
    load_to_database()
