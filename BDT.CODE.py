
from pyspark.sql import SparkSession

# ==========================================
# WEATHER DATASET
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

# ==========================================
# COLUMN NAMES
# ==========================================

columns = [
    "city",
    "temperature",
    "humidity",
    "rainfall",
    "wind_speed",
    "pressure"
]

# ==========================================
# CREATE WEATHER DATAFRAME
# ==========================================

def load_weather_data(spark):

    df = spark.createDataFrame(weather_data, columns)

    return df


# ==========================================
# DISPLAY WEATHER DATA
# ==========================================

def display_weather_data(spark):

    df = load_weather_data(spark)

    print("\n========== WEATHER DATA ==========")

    df.show(truncate=False)

    return df


# ==========================================
# MAIN FUNCTION FOR TESTING
# ==========================================

if __name__ == "__main__":

    spark = (
        SparkSession.builder
        .appName("Weather Data")
        .master("local[2]")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    try:
        display_weather_data(spark)

    finally:
        spark.stop()
