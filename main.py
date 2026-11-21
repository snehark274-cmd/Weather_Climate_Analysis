
import os
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, count, round

# ==========================================
# 1. PROJECT CONFIGURATION
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "outputs"
WAREHOUSE_DIR = Path("C:/temp/spark-warehouse")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
WAREHOUSE_DIR.mkdir(parents=True, exist_ok=True)

# Hadoop configuration for Windows
os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["hadoop.home.dir"] = r"C:\hadoop"

# Use the same Python interpreter for Spark workers
python_path = os.path.abspath(os.sys.executable)
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

# ==========================================
# 2. CREATE SPARK SESSION
# ==========================================

spark = (
    SparkSession.builder
    .appName("Weather and Climate Analysis")
    .master("local[2]")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.sql.warehouse.dir", WAREHOUSE_DIR.as_uri())
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

try:

    print("\n==========================================")
    print(" REAL-TIME WEATHER AND CLIMATE ANALYSIS")
    print("==========================================")

    # ==========================================
    # 3. WEATHER DATASET
    # ==========================================

    weather_data = [
        ("Bengaluru", 28, 65, 12, 15, 1012),
        ("Mumbai", 32, 70, 25, 18, 1008),
        ("Delhi", 35, 45, 5, 12, 1005),
        ("Chennai", 33, 75, 30, 20, 1010),
        ("Hyderabad", 30, 60, 10, 14, 1011),
        ("Pune", 27, 55, 8, 11, 1013),
        ("Kolkata", 31, 80, 40, 22, 1007),
        ("Mysuru", 26, 68, 15, 10, 1014)
    ]

    columns = [
        "city",
        "temperature",
        "humidity",
        "rainfall",
        "wind_speed",
        "pressure"
    ]

    df = spark.createDataFrame(weather_data, columns)

    # ==========================================
    # 4. DISPLAY WEATHER DATA
    # ==========================================

    print("\n========== WEATHER DATA ==========")
    df.show(truncate=False)

    # ==========================================
    # 5. CREATE SPARK SQL TABLE
    # ==========================================

    df.createOrReplaceTempView("weather")

    # ==========================================
    # 6. AVERAGE TEMPERATURE
    # ==========================================

    print("\n========== AVERAGE TEMPERATURE ==========")

    spark.sql("""
        SELECT ROUND(AVG(temperature), 2)
        AS average_temperature
        FROM weather
    """).show()

    # ==========================================
    # 7. MAXIMUM AND MINIMUM TEMPERATURE
    # ==========================================

    print("\n========== MAXIMUM TEMPERATURE ==========")

    spark.sql("""
        SELECT city, temperature
        FROM weather
        ORDER BY temperature DESC
        LIMIT 1
    """).show()

    print("\n========== MINIMUM TEMPERATURE ==========")

    spark.sql("""
        SELECT city, temperature
        FROM weather
        ORDER BY temperature ASC
        LIMIT 1
    """).show()

    # ==========================================
    # 8. HUMIDITY ANALYSIS
    # ==========================================

    print("\n========== HUMIDITY ANALYSIS ==========")

    spark.sql("""
        SELECT
            ROUND(AVG(humidity), 2) AS average_humidity,
            MAX(humidity) AS maximum_humidity,
            MIN(humidity) AS minimum_humidity
        FROM weather
    """).show()

    # ==========================================
    # 9. RAINFALL ANALYSIS
    # ==========================================

    print("\n========== RAINFALL ANALYSIS ==========")

    spark.sql("""
        SELECT city, rainfall
        FROM weather
        ORDER BY rainfall DESC
    """).show()

    # ==========================================
    # 10. WIND SPEED ANALYSIS
    # ==========================================

    print("\n========== WIND SPEED ANALYSIS ==========")

    spark.sql("""
        SELECT city, wind_speed
        FROM weather
        ORDER BY wind_speed DESC
    """).show()

    # ==========================================
    # 11. ATMOSPHERIC PRESSURE ANALYSIS
    # ==========================================

    print("\n========== PRESSURE ANALYSIS ==========")

    spark.sql("""
        SELECT city, pressure
        FROM weather
        ORDER BY pressure DESC
    """).show()

    # ==========================================
    # 12. COMPLETE WEATHER SUMMARY
    # ==========================================

    print("\n========== COMPLETE WEATHER SUMMARY ==========")

    spark.sql("""
        SELECT
            COUNT(*) AS total_cities,
            ROUND(AVG(temperature), 2) AS avg_temperature,
            MAX(temperature) AS max_temperature,
            MIN(temperature) AS min_temperature,
            ROUND(AVG(humidity), 2) AS avg_humidity,
            ROUND(AVG(rainfall), 2) AS avg_rainfall,
            ROUND(AVG(wind_speed), 2) AS avg_wind_speed,
            ROUND(AVG(pressure), 2) AS avg_pressure
        FROM weather
    """).show()

    # ==========================================
    # 13. WEATHER CONDITION CLASSIFICATION
    # ==========================================

    print("\n========== WEATHER CONDITIONS ==========")

    spark.sql("""
        SELECT
            city,
            temperature,
            CASE
                WHEN temperature >= 35 THEN 'Very Hot'
                WHEN temperature >= 30 THEN 'Hot'
                WHEN temperature >= 25 THEN 'Moderate'
                ELSE 'Cold'
            END AS weather_condition
        FROM weather
        ORDER BY temperature DESC
    """).show()

    # ==========================================
    # 14. SAVE RESULTS
    # ==========================================

    output_path = OUTPUT_DIR / "weather_results"

    df.coalesce(1).write \
        .mode("overwrite") \
        .option("header", True) \
        .csv(str(output_path))

    print("\n==========================================")
    print(" WEATHER ANALYSIS COMPLETED SUCCESSFULLY")
    print("==========================================")

    print(f"Results saved in: {output_path}")

finally:

    # ==========================================
    # 15. STOP SPARK SESSION
    # ==========================================

    spark.stop()
    print("\nSpark session stopped.")

