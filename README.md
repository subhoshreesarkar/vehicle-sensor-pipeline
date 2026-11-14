Vehicle Sensor Pipeline
An ETL Data Pipeline for simulated vehicle sensor data using Python, AWS S3, Pandas, SQLAlchemy and SQLite.

📋 Project Overview
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline for automotive sensor data:

Extract – Simulate and generate vehicle sensor data with Python
Transform – Clean and validate data with Pandas
Load – Store cleaned data in a SQLite database via SQLAlchemy
Cloud – Upload raw data to AWS S3
Analyze – Run SQL queries to extract insights
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Pandas	Data transformation and cleaning
SQLAlchemy	Database interface
SQLite	Local database
AWS S3	Cloud storage
boto3	AWS SDK for Python
Git & GitHub	Version control
📁 Project Structure
vehicle-sensor-pipeline/ │ ├── generate_sensor_data.py # Generate simulated vehicle sensor data ├── upload_to_s3.py # Upload raw data to AWS S3 ├── transform_data.py # Clean and transform data with Pandas ├── load_to_database.py # Load cleaned data into SQLite database ├── sql_analysis.py # SQL queries and data analysis ├── requirements.txt # Python dependencies ├── .env # AWS credentials (not uploaded to GitHub) ├── .gitignore # Files excluded from GitHub └── README.md # Project documentation

🚀 How to Run
1. Clone the repository
git clone https://github.com/tobias-hettmer-dev/vehicle-sensor-pipeline.git
2. Install dependencies
pip install -r requirements.txt
3. Configure AWS credentials
Create a .env file in the project root:

AWS_ACCESS_KEY_ID=your_access_key AWS_SECRET_ACCESS_KEY=your_secret_key AWS_REGION=eu-central-1

4. Run the pipeline
python generate_sensor_data.py
python upload_to_s3.py
python transform_data.py
python load_to_database.py
python sql_analysis.py
📊 Sample Output
Generated Sensor Data
100 simulated vehicle sensor records
10 unique vehicle IDs
Fields: timestamp, vehicle_id, speed_kmh, engine_temp_celsius, battery_voltage, fuel_level_percent, rpm, oil_pressure_bar
SQL Analysis Results
Average speed and temperature per vehicle
Anomaly detection (high temperature, high speed, low battery)
Overall fleet statistics
