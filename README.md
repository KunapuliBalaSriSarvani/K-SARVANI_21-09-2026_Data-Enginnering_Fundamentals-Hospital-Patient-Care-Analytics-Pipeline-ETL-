# 🏥 Hospital Patient Care Analytics Pipeline

> **End-to-End Data Engineering ETL Pipeline using Python, Pandas and MySQL**

## 📌 Project Overview

A multi-specialty hospital generates data from multiple operational systems such as **patient registration, appointments, laboratory reports, wearable devices, and doctor consultations**.

This project demonstrates an end-to-end **Data Engineering pipeline** that integrates these heterogeneous data sources, cleans and transforms the data, performs data-quality validation, and loads the processed dataset into **MySQL** for patient-care analytics.

The pipeline is designed to support analysis of:

- Patient waiting times
- Department-level operational performance
- Patient risk indicators
- Long-wait cases
- Healthcare-related analytical KPIs

---

## 🎯 Objectives

The main objectives of this project are:

1. **Integrate data from multiple hospital source systems**
2. **Clean and transform raw healthcare-related data**
3. **Calculate patient waiting-time metrics**
4. **Create analytical risk indicators from available patient attributes**
5. **Validate data quality before loading**
6. **Store the processed dataset in MySQL**
7. **Enable SQL-based analytics for patient-care insights**

---

# 🏗️ Data Engineering Architecture

<img width="1145" height="1374" alt="image" src="https://github.com/user-attachments/assets/c814dcd6-06b1-47b2-b800-37202b317499" />
---

# 📊 SQL Analytics

After loading the validated dataset into MySQL, SQL queries are used to generate patient-care and operational insights.

### Key Analytics

- **Patient Volume:** Total number of patient records in the analytical table.
- **Waiting-Time Analysis:** Average and maximum waiting time across departments.
- **Risk Distribution:** Distribution of Low, Medium, and High analytical risk categories.
- **Long-Wait Cases:** Identification of patients with long waiting times.
- **Department KPIs:** Patient count, average waiting time, long-wait cases, and high-risk analytical cases.

### Example SQL Query

```sql
SELECT
    department_x,
    COUNT(*) AS patients,
    ROUND(AVG(waiting_minutes), 2) AS avg_wait_minutes,
    SUM(CASE WHEN waiting_category = 'Long' THEN 1 ELSE 0 END) AS long_wait_cases,
    SUM(CASE WHEN risk_flag = 'High' THEN 1 ELSE 0 END) AS high_risk_cases
FROM patient_care_analytics
GROUP BY department_x
ORDER BY avg_wait_minutes DESC;
<img width="959" height="473" alt="image" src="https://github.com/user-attachments/assets/dd1757e4-de72-4ed9-a711-2ee55fcfb183" />

Figure: Integrated patient-care analytics dataset successfully loaded into the patient_care_analytics MySQL table.
SELECT * FROM patient_care_analytics;
<img width="1918" height="994" alt="image" src="https://github.com/user-attachments/assets/e78f03b2-bc58-46a1-9391-70c266ea1317" />

Figure: MySQL table schema showing the structure and data types of the patient_care_analytics table.
USE hospital_db;
DESCRIBE patient_care_analytics;
<img width="959" height="500" alt="image" src="https://github.com/user-attachments/assets/1e48a0fc-e30b-46f4-9aa3-613246351cec" />

