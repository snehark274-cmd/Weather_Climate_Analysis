
# 🌦️ A Spark SQL-Based Real-Time Data Analysis System for Weather and Climate

## 1. Project Overview

The Weather and Climate Analysis System is a data analysis project developed using Python, Apache Spark, and Spark SQL.

The system analyzes weather parameters such as temperature, humidity, rainfall, wind speed, and atmospheric pressure across different cities.

Apache Spark is used to process weather datasets, while Spark SQL performs data querying, filtering, sorting, and aggregation. Streamlit provides an interactive dashboard to visualize the analysis results.

**Note:** The current version uses sample weather data. Real-time API integration is planned as a future enhancement.

---

## 2. Objectives

- To collect and organize weather data from different cities.
- To analyze temperature and humidity variations.
- To examine rainfall and wind speed patterns.
- To analyze atmospheric pressure.
- To perform data processing using Apache Spark.
- To execute analytical queries using Spark SQL.
- To visualize weather information through charts and graphs.
- To provide an interactive weather analysis dashboard.

---

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Apache Spark | Distributed data processing |
| PySpark | Python interface for Spark |
| Spark SQL | Weather data analysis |
| Pandas | Data handling |
| Matplotlib | Data visualization |
| Streamlit | Interactive dashboard |
| Java 17 | Spark execution environment |
| VS Code | Development environment |

---

## 4. Project Structure

```text
Weather_Climate_Analysis/
│
├── main.py
├── weather_data.py
├── analysis.py
├── dashboard.py
├── README.md
│
├── outputs/
│   └── weather_results/
│
└── .venv/
```

---

## 5. Weather Parameters

The project analyzes the following weather parameters:

1. Temperature – Measures the atmospheric temperature in Celsius.
2. Humidity – Measures the amount of moisture in the air.
3. Rainfall – Measures the amount of rainfall in millimetres.
4. Wind Speed – Measures the speed of wind in km/h.
5. Atmospheric Pressure – Measures atmospheric pressure in hPa.

---

## 6. System Features

- Weather dataset creation.
- City-wise weather analysis.
- Average temperature calculation.
- Maximum and minimum temperature identification.
- Humidity analysis.
- Rainfall comparison.
- Wind speed analysis.
- Atmospheric pressure analysis.
- Weather condition classification.
- Interactive charts and graphs.
- CSV data download.

---

## 7. Installation and Setup

### Step 1: Install Python

Install Python and verify the installation:

```bash
python --version
```

### Step 2: Install Java

Install Java JDK 17 and verify:

```bash
java -version
```

### Step 3: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install Required Packages

```bash
pip install pyspark pandas matplotlib streamlit
```

---

## 8. How to Execute the Project

### Run the Main Program

```powershell
.\.venv\Scripts\python.exe main.py
```

### Run Weather Analysis

```powershell
.\.venv\Scripts\python.exe analysis.py
```

### Run the Dashboard

```powershell
.\.venv\Scripts\python.exe -m streamlit run dashboard.py
```

Open the following address in your browser:

```text
http://localhost:8501
```

---

## 9. Expected Results

The project processes sample weather records from eight cities.

| Parameter | Expected Result |
|---|---:|
| Total Cities | 8 |
| Average Temperature | 30.25 °C |
| Maximum Temperature | 35 °C |
| Minimum Temperature | 26 °C |
| Average Humidity | 64.75% |
| Average Rainfall | 18.125 mm |

---

## 10. Output and Visualization

The system generates:

- Weather dataset tables.
- Temperature comparison charts.
- Humidity comparison charts.
- Rainfall analysis charts.
- Wind speed comparison charts.
- Atmospheric pressure graphs.
- Weather summary results.
- Downloadable CSV files.

---

## 11. Future Enhancements

- Integration with real-time weather APIs.
- Live weather monitoring.
- Weather forecasting using machine learning.
- Historical weather data analysis.
- Advanced interactive visualizations.
- Automatic weather alerts.
- Cloud-based data processing.
- Support for more cities and locations.

---

## 12. Conclusion

The Weather and Climate Analysis System demonstrates how Apache Spark and Spark SQL can be used to process and analyze weather datasets efficiently.

The project provides useful information about temperature, humidity, rainfall, wind speed, and atmospheric pressure. The interactive Streamlit dashboard makes the analysis easier to understand through tables, charts, and graphs.

The system provides a foundation for future development, including real-time weather data integration, predictive analysis, and advanced climate monitoring.

---

## 13. Developed Using

**Python | Apache Spark | PySpark | Spark SQL | Pandas | Matplotlib | Streamlit | Java 17**

**Project Domain:** Big Data Technologies (BDT)
