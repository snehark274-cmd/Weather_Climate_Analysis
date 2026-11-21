
import os
import sys
from pathlib import Path

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from pyspark.sql import SparkSession
from weather_data import load_weather_data


# ==========================================
# 1. PROJECT CONFIGURATION
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parent

os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["hadoop.home.dir"] = r"C:\hadoop"

python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path


# ==========================================
# 2. STREAMLIT PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Weather and Climate Analysis",
    page_icon="🌦️",
    layout="wide"
)


# ==========================================
# 3. DASHBOARD TITLE
# ==========================================

st.title("🌦️ Weather and Climate Analysis System")

st.markdown(
    """
    ### A Spark SQL-Based Weather Data Analysis Dashboard

    This dashboard analyzes temperature, humidity, rainfall,
    wind speed and atmospheric pressure across different cities.
    """
)

st.info("Dataset: Sample weather records for demonstration. Not live weather data.")


# ==========================================
# 4. LOAD WEATHER DATA USING SPARK
# ==========================================

@st.cache_data
def get_weather_data():

    spark = (
        SparkSession.builder
        .appName("Weather Dashboard")
        .master("local[2]")
        .config("spark.driver.host", "127.0.0.1")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    try:

        df = load_weather_data(spark)

        pandas_df = df.toPandas()

        return pandas_df

    finally:

        spark.stop()


try:

    data = get_weather_data()

except Exception as error:

    st.error("Unable to load weather data. Please check your Spark and Java configuration.")

    st.exception(error)

    st.stop()


# ==========================================
# 5. WEATHER DATA TABLE
# ==========================================

st.header("📋 Weather Data")

st.dataframe(data, use_container_width=True)


# ==========================================
# 6. WEATHER SUMMARY
# ==========================================

st.header("📊 Weather Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Cities",
    len(data)
)

col2.metric(
    "Average Temperature",
    f"{data['temperature'].mean():.2f} °C"
)

col3.metric(
    "Average Humidity",
    f"{data['humidity'].mean():.2f} %"
)

col4.metric(
    "Average Rainfall",
    f"{data['rainfall'].mean():.2f} mm"
)


# ==========================================
# 7. TEMPERATURE ANALYSIS
# ==========================================

st.header("🌡️ Temperature Analysis")

fig1, ax1 = plt.subplots()

ax1.bar(
    data["city"],
    data["temperature"]
)

ax1.set_xlabel("City")
ax1.set_ylabel("Temperature (°C)")
ax1.set_title("City-wise Temperature Comparison")

plt.xticks(rotation=45)

st.pyplot(fig1)
plt.close(fig1)


# ==========================================
# 8. HUMIDITY ANALYSIS
# ==========================================

st.header("💧 Humidity Analysis")

fig2, ax2 = plt.subplots()

ax2.bar(
    data["city"],
    data["humidity"]
)

ax2.set_xlabel("City")
ax2.set_ylabel("Humidity (%)")
ax2.set_title("City-wise Humidity Comparison")

plt.xticks(rotation=45)

st.pyplot(fig2)
plt.close(fig2)


# ==========================================
# 9. RAINFALL ANALYSIS
# ==========================================

st.header("🌧️ Rainfall Analysis")

fig3, ax3 = plt.subplots()

ax3.bar(
    data["city"],
    data["rainfall"]
)

ax3.set_xlabel("City")
ax3.set_ylabel("Rainfall (mm)")
ax3.set_title("City-wise Rainfall Comparison")

plt.xticks(rotation=45)

st.pyplot(fig3)
plt.close(fig3)


# ==========================================
# 10. WIND SPEED ANALYSIS
# ==========================================

st.header("💨 Wind Speed Analysis")

fig4, ax4 = plt.subplots()

ax4.bar(
    data["city"],
    data["wind_speed"]
)

ax4.set_xlabel("City")
ax4.set_ylabel("Wind Speed (km/h)")
ax4.set_title("City-wise Wind Speed Comparison")

plt.xticks(rotation=45)

st.pyplot(fig4)
plt.close(fig4)


# ==========================================
# 11. ATMOSPHERIC PRESSURE ANALYSIS
# ==========================================

st.header("🌍 Atmospheric Pressure Analysis")

fig5, ax5 = plt.subplots()

ax5.plot(
    data["city"],
    data["pressure"],
    marker="o"
)

ax5.set_xlabel("City")
ax5.set_ylabel("Pressure (hPa)")
ax5.set_title("City-wise Atmospheric Pressure")

plt.xticks(rotation=45)

st.pyplot(fig5)
plt.close(fig5)


# ==========================================
# 12. CITY FILTER
# ==========================================

st.header("🔍 City-wise Weather Details")

selected_city = st.selectbox(
    "Select a City",
    data["city"].tolist()
)

city_data = data[data["city"] == selected_city]

st.dataframe(city_data, use_container_width=True)


# ==========================================
# 13. DOWNLOAD WEATHER DATA
# ==========================================

st.header("📥 Download Weather Data")

csv_data = data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Weather Data CSV",
    data=csv_data,
    file_name="weather_analysis.csv",
    mime="text/csv"
)


# ==========================================
# 14. FOOTER
# ==========================================

st.divider()

st.markdown(
    """
    **Weather and Climate Analysis System**

    Developed using Python, Apache Spark, Spark SQL,
    Streamlit, Pandas and Matplotlib.
    """
)

st.success("Weather dashboard loaded successfully!")
