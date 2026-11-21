
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, round, count

from weather_data import load_weather_data


# ==========================================
# 1. CREATE SPARK SESSION
# ==========================================

def create_spark_session():

    spark = (
        SparkSession.builder
        .appName("Weather Climate Analysis")
        .master("local[2]")
        .config("spark.driver.host", "127.0.0.1")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark


# ==========================================
# 2. TEMPERATURE ANALYSIS
# ==========================================

def temperature_analysis(spark):

    print("\n========== TEMPERATURE ANALYSIS ==========")

    spark.sql("""
        SELECT
            ROUND(AVG(temperature), 2) AS average_temperature,
            MAX(temperature) AS maximum_temperature,
            MIN(temperature) AS minimum_temperature
        FROM weather
    """).show()


# ==========================================
# 3. HUMIDITY ANALYSIS
# ==========================================

def humidity_analysis(spark):

    print("\n========== HUMIDITY ANALYSIS ==========")

    spark.sql("""
        SELECT
            ROUND(AVG(humidity), 2) AS average_humidity,
            MAX(humidity) AS maximum_humidity,
            MIN(humidity) AS minimum_humidity
        FROM weather
    """).show()


# ==========================================
# 4. RAINFALL ANALYSIS
# ==========================================

def rainfall_analysis(spark):

    print("\n========== RAINFALL ANALYSIS ==========")

    spark.sql("""
        SELECT city, rainfall
        FROM weather
        ORDER BY rainfall DESC
    """).show()


# ==========================================
# 5. WIND SPEED ANALYSIS
# ==========================================

def wind_analysis(spark):

    print("\n========== WIND SPEED ANALYSIS ==========")

    spark.sql("""
        SELECT city, wind_speed
        FROM weather
        ORDER BY wind_speed DESC
    """).show()


# ==========================================
# 6. ATMOSPHERIC PRESSURE ANALYSIS
# ==========================================

def pressure_analysis(spark):

    print("\n========== PRESSURE ANALYSIS ==========")

    spark.sql("""
        SELECT city, pressure
        FROM weather
        ORDER BY pressure DESC
    """).show()


# ==========================================
# 7. CITY-WISE WEATHER ANALYSIS
# ==========================================

def city_weather_analysis(spark):

    print("\n========== CITY-WISE WEATHER ==========")

    spark.sql("""
        SELECT
            city,
            temperature,
            humidity,
            rainfall,
            wind_speed,
            pressure
        FROM weather
        ORDER BY temperature DESC
    """).show(truncate=False)


# ==========================================
# 8. WEATHER CONDITION ANALYSIS
# ==========================================

def weather_condition_analysis(spark):

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
# 9. COMPLETE WEATHER SUMMARY
# ==========================================

def weather_summary(spark):

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
# 10. RUN ALL ANALYSIS
# ==========================================

def run_analysis():

    spark = create_spark_session()

    try:

        print("\n==========================================")
        print(" WEATHER AND CLIMATE ANALYSIS SYSTEM")
        print("==========================================")

        # Load weather dataset
        df = load_weather_data(spark)

        # Create Spark SQL temporary table
        df.createOrReplaceTempView("weather")

        # Display original data
        print("\n========== WEATHER DATA ==========")
        df.show(truncate=False)

        # Execute all analysis functions
        temperature_analysis(spark)
        humidity_analysis(spark)
        rainfall_analysis(spark)
        wind_analysis(spark)
        pressure_analysis(spark)
        city_weather_analysis(spark)
        weather_condition_analysis(spark)
        weather_summary(spark)

        print("\n==========================================")
        print(" ANALYSIS COMPLETED SUCCESSFULLY")
        print("==========================================")

    finally:

        spark.stop()


# ==========================================
# 11. MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    run_analysis()
